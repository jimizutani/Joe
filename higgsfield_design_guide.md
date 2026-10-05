# リタ株式会社 HPデザイン方針 × Higgsfield 素材制作ガイド（STEP 3.5）

Higgsfield（AI画像・動画生成）で、トップページの写真・動画素材を作るための指示書です。
生成した素材を `site/images/` に入れれば、試作ページの「差し替え」枠に組み込みます。

---

## 1. デザインコンセプト

**テーマ：「やわらかな日常光」**
重度障害の支援＝"重い・医療的"な印象を、**あたたかく・明るく・誇りある仕事**へ転換する。

| 要素 | 方針 |
|---|---|
| トーン | 朝〜昼のやわらかい自然光、ドキュメンタリー風、作り込みすぎない |
| 色 | ティール（信頼）＋オレンジ（ぬくもり）＋白木・リネンのベージュ（家庭的） |
| 人物 | 日本人。笑顔の"決め顔"より、目線を合わせる・手を添えるなど**関係性**が伝わる瞬間 |
| 避けるもの | 病院のような冷たい白、悲壮感、"かわいそう"な演出、障害を誇張・ステレオタイプ化した表現 |

**全プロンプト共通で末尾に付ける文（スタイル固定用）**
```
soft natural morning light, warm and calm atmosphere, documentary photography style,
Japanese people, cozy Japanese home interior with light wood and linen, teal and warm orange accents,
shallow depth of field, 35mm lens, realistic, respectful and dignified, no text, no logo
```

---

## 2. 素材リスト＆プロンプト

> Higgsfieldは英語プロンプトの方が安定します。日本語は内容説明です。

### ① メインビジュアル（最重要）
- **用途**：トップ最上部　**比率**：16:9（PC）＋ 4:5（スマホ用）　**形式**：静止画 または 5〜8秒のループ動画
- 内容：車いすの入居者さんと支援員が、リビングで窓の光を浴びながら笑い合う

```
A young Japanese man in a wheelchair and a female care worker in a teal polo shirt
sharing a laugh by a large window in a bright living room of a small group home,
she is kneeling to his eye level, gentle hand on the armrest,
[共通スタイル文]
```
- 動画にする場合（Image to Video）：`slow gentle dolly-in, curtains moving slightly in the breeze, subtle natural movement, no fast motion`

### ② サービス：グループホーム
- **比率**：3:2
```
Exterior of a modern, clean two-story Japanese house used as a small group home,
barrier-free entrance with a gentle ramp, potted plants, afternoon sun, residential neighborhood,
[共通スタイル文]
```

### ③ サービス：リタラスホーム（住まい＋重度訪問介護）
- **比率**：3:2
```
A bright private room in a Japanese care residence, a care worker gently adjusting a pillow
for a resident lying on a care bed, warm afternoon light, personal belongings and photos on the shelf,
calm and homely, [共通スタイル文]
```

### ④ 採用バナー
- **比率**：4:3（縦長スマホ用 3:4 も）
```
Three Japanese care workers in their 20s to 40s in teal and orange uniforms,
walking and talking cheerfully in a sunny hallway of a group home, natural candid moment,
team atmosphere, [共通スタイル文]
```

### ⑤ 家主募集バナー
- **比率**：3:2
```
Before-and-after concept: an empty old Japanese house renovated into a warm, barrier-free group home,
wide living room with wooden floor, dining table set for several residents,
[共通スタイル文]
```

### ⑥ ご利用の流れ（見学）
- **比率**：1:1
```
A Japanese mother and her adult son in a wheelchair being welcomed by a smiling staff member
at the entrance of a group home, tour visit, warm greeting, [共通スタイル文]
```

### ⑦（任意）トップ用ショート動画 / SNS・Indeed用
- 縦 9:16、10〜15秒：朝の光 → 食卓 → 支援員の手元 → 笑顔 の4カット
- 採用広告（Indeed・Instagram）にも流用可

---

## 3. 人物の一貫性（Soul ID 等のキャラクター固定機能）
同じ「支援員さん」「入居者さん」を全ページで登場させると、サイトに統一感が出ます。
①で気に入った人物をキャラクター登録し、②〜⑥でも同じ人物を使ってください。

---

## 4. 必ず守るルール（重要）

1. **AI画像は「イメージ」として使う**
   - 事業所の外観・居室、スタッフ紹介、社員インタビュー、事業所一覧の写真は **必ず実物の写真** にする（実在しない建物や社員に見せると、利用者・求職者・家主を誤解させるおそれがあります）
   - AI画像を使う箇所には小さく「※写真はイメージです」と表記
2. **障害の表現に配慮**
   - 実在の入居者さんの顔写真をAIに読み込ませない（本人同意が取れていても、個人情報保護の観点で避ける）
   - 医療機器・医療的ケアの場面は誤った描写になりやすいので、使う前に看護師・サービス管理責任者が確認する
3. **権利・商用利用**：Enterpriseプランの商用利用条件・権利帰属を契約で確認
4. **ファイル**：画像はWebP/JPEG（横1920px程度・500KB以下目安）、動画はMP4（10MB以下目安）

---

## 5. 作業の流れ

| STEP | 担当 | 内容 |
|---|---|---|
| 3.5-1 | ご担当者 | 上記①を数パターン生成し、気に入ったものを選ぶ |
| 3.5-2 | ご担当者 | 同じ人物・トーンで②〜⑥を生成 |
| 3.5-3 | Claude | 素材を `site/images/` に配置し、トップページへ組み込み・色味を写真に合わせて微調整 |
