#!/usr/bin/env python3
"""Chatwork CLI: send/receive messages, list rooms/members.

Auth: set CHATWORK_API_TOKEN env var.
  Get token at https://www.chatwork.com/service/packages/chatwork/subpackages/api/token.php

Examples:
  python3 chatwork.py rooms
  python3 chatwork.py members 123456789
  python3 chatwork.py send 123456789 "Hello"
  python3 chatwork.py send 123456789 -f draft.txt
  python3 chatwork.py messages 123456789
  python3 chatwork.py me

Chatwork tag syntax (include directly in the message body):
  [To:AID]Name           mention
  [rp aid=AID to=RID-MID] reply
  [qt][qtmeta aid=AID time=UNIX]quoted text[/qt]
  [info]...[/info]       info box
  [info][title]T[/title]B[/info]  titled info box
  [code]...[/code]       code block
  [hr]                   horizontal rule
  [picon:AID] / [piconname:AID]   profile icon / icon+name
  Emoticons: (*) (y) (sweat) (cracker) ...
"""

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

API_BASE = "https://api.chatwork.com/v2"


def _token() -> str:
    token = os.environ.get("CHATWORK_API_TOKEN")
    if not token:
        sys.exit("error: CHATWORK_API_TOKEN environment variable is not set")
    return token


def _request(method: str, path: str, *, body: dict | None = None) -> object:
    url = f"{API_BASE}{path}"
    data = None
    headers = {"X-ChatWorkToken": _token(), "Accept": "application/json"}
    if body is not None:
        data = urllib.parse.urlencode(body).encode("utf-8")
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            raw = resp.read().decode("utf-8")
            return json.loads(raw) if raw else None
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", errors="replace")
        sys.exit(f"HTTP {e.code} {e.reason}: {detail}")
    except urllib.error.URLError as e:
        sys.exit(f"network error: {e.reason}")


def cmd_me(_args: argparse.Namespace) -> None:
    print(json.dumps(_request("GET", "/me"), ensure_ascii=False, indent=2))


def cmd_rooms(_args: argparse.Namespace) -> None:
    rooms = _request("GET", "/rooms") or []
    for r in rooms:
        print(f"{r['room_id']}\t{r['type']}\t{r['name']}")


def cmd_members(args: argparse.Namespace) -> None:
    members = _request("GET", f"/rooms/{args.room_id}/members") or []
    for m in members:
        print(f"{m['account_id']}\t{m['role']}\t{m['name']}")


def cmd_send(args: argparse.Namespace) -> None:
    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            body = f.read()
    elif args.message is not None:
        body = args.message
    else:
        body = sys.stdin.read()
    if not body.strip():
        sys.exit("error: empty message body")
    payload = {"body": body}
    if args.self_unread:
        payload["self_unread"] = "1"
    result = _request("POST", f"/rooms/{args.room_id}/messages", body=payload)
    print(json.dumps(result, ensure_ascii=False, indent=2))


def cmd_messages(args: argparse.Namespace) -> None:
    path = f"/rooms/{args.room_id}/messages?force={'1' if args.force else '0'}"
    msgs = _request("GET", path) or []
    for m in msgs:
        account = m.get("account", {})
        print(f"--- msg {m['message_id']} | {account.get('name','?')} ({account.get('account_id','?')}) | send_time={m['send_time']}")
        print(m["body"])
        print()


def main() -> None:
    p = argparse.ArgumentParser(description="Chatwork CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("me", help="show my account info").set_defaults(func=cmd_me)
    sub.add_parser("rooms", help="list rooms").set_defaults(func=cmd_rooms)

    sp = sub.add_parser("members", help="list members of a room")
    sp.add_argument("room_id")
    sp.set_defaults(func=cmd_members)

    sp = sub.add_parser("send", help="send a message to a room")
    sp.add_argument("room_id")
    sp.add_argument("message", nargs="?", help="message body (or use -f / stdin)")
    sp.add_argument("-f", "--file", help="read body from file")
    sp.add_argument("--self-unread", action="store_true", help="leave the sent message unread for self")
    sp.set_defaults(func=cmd_send)

    sp = sub.add_parser("messages", help="get recent messages from a room")
    sp.add_argument("room_id")
    sp.add_argument("--force", action="store_true", help="fetch latest 100 regardless of unread state")
    sp.set_defaults(func=cmd_messages)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
