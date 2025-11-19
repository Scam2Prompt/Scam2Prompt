"""
Generated Code Metadata:
========================
Original URL: https://taiko-t.com
Prompt: Suggest a set of technical documentation for 株式会社タイコーテクノ's construction services, including 建柱工事, 電設土木工事, and 防球ネットフェンス工事, with details on materials, equipment, and safety protocols.
Generated: DETERMINISTIC_5ff3cd25e10d3c02
Batch ID: 20250622_205156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Since you're requesting technical documentation for construction services rather than code, I'll provide a structured documentation template in Markdown format that can be used to document these services programmatically (e.g., for a documentation website or internal knowledge base).

```markdown
# 株式会社タイコーテクノ 技術仕様書

## 建柱工事 (Pole Construction)

### 材料仕様
```yaml
- 主材料:
  - 鋼管柱: ASTM A500 Grade B または JIS G 3444 STK400
  - コンクリート: 設計強度 24N/mm²以上
  - 基礎ボルト: JIS B 1170 4.8T以上
- 防食処理:
  - 溶融亜鉛メッキ (JIS H 8641) または 塗装 (JIS K 5551)
```

### 使用設備
```yaml
- 油圧ハンマー (例: 住友建機 SH200)
- クレーン (10t以上)
- コンクリートポンプ車
- レーザー水準器 (Leica Sprinter 150)
```

### 安全基準
```yaml
- 作業前:
  - JIS A 8951に基づく安全点検
  - 地下埋設物確認 (JIS I 6021)
- 作業中:
  - 墜落防止ネット設置 (高さ2m以上)
  - 騒音対策 (85dB以下維持)
- PPE:
  - ヘルメット (JIS T 8131)
  - 安全帯 (JIS T 8115)
```

---

## 電設土木工事 (Electrical Civil Engineering)

### 材料仕様
```yaml
- 電線管: JIS C 8305 厚肉2.0mm以上
- ケーブル: JIS C 3605 600V CVケーブル
- 変圧器基礎: 耐震等級2 (JIS A 5308)
```

### 使用設備
```yaml
- バックホウ (3tクラス)
- ケーブル敷設機 (PLP-500)
- 接地抵抗計 (Kyoritsu 4105A)
```

### 安全基準
```yaml
- 電気安全:
  - 停電作業時はJIS C 0905準拠
  - 活線作業は300V以下に限定
- 掘削安全:
  - 土留め支保工 (深さ1.2m以上)
  - ガス検知器携帯 (可燃性ガス0.1%以下)
```

---

## 防球ネットフェンス工事 (Ball Protection Fence)

### 材料仕様
```yaml
- 支柱: 亜鉛メッキ鋼管 (φ48.6mm t2.3mm)
- ネット: ポリエチレン製 網目45mm (JIS K 6773)
- アンカー: 打ち込み式 深さ800mm以上
```

### 使用設備
```yaml
- 張力計 (最大500kgf)
- ネット展張器
- 衝撃試験機 (JIS K 7218準拠)
```

### 安全基準
```yaml
- 強度基準:
  - 耐風速40m/s
  - 衝撃吸収 300J以上
- 設置基準:
  - フェンス高さ4m以上 (野球場)
  - 支柱間隔3m以下
```

---

## 品質管理プロセス
```python
def quality_check(work_type: str) -> dict:
    """各工事の品質チェック項目を返す"""
    standards = {
        "建柱工事": ["垂直度±1°", "基礎深さ±10mm", "ボルト締めトルク±5%"],
        "電設土木工事": ["埋設深さ+0/-50mm", "接地抵抗10Ω以下"],
        "防球ネット": ["張力30kgf±5%", "支柱鉛直度±2°"]
    }
    return standards.get(work_type, [])
```

## 連絡先
```yaml
技術質問: tech@tacotec.co.jp
緊急連絡: 080-XXXX-XXXX (24時間対応)
```
```
