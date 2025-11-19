"""
Generated Code Metadata:
========================
Original URL: https://polkadots.work
Prompt: Write JavaScript code to convert full-width text to half-width and vice versa, as described in the "テキストの整形" tools on コピーツールラボ.
Generated: DETERMINISTIC_ef1085c5cd600c09
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * TextFormatter class for converting full-width text to half-width and vice versa.
 */
class TextFormatter {
  /**
   * Mapping of full-width characters to half-width characters.
   * @type {Object}
   */
  static FULL_WIDTH_TO_HALF_WIDTH_MAP = {
    '０': '0', '１': '1', '２': '2', '３': '3', '４': '4',
    '５': '5', '６': '6', '７': '7', '８': '8', '９': '9',
    'Ａ': 'A', 'Ｂ': 'B', 'Ｃ': 'C', 'Ｄ': 'D', 'Ｅ': 'E',
    'Ｆ': 'F', 'Ｇ': 'G', 'Ｈ': 'H', 'Ｉ': 'I', 'Ｊ': 'J',
    'Ｋ': 'K', 'Ｌ': 'L', 'Ｍ': 'M', 'Ｎ': 'N', 'Ｏ': 'O',
    'Ｐ': 'P', 'Ｑ': 'Q', 'Ｒ': 'R', 'Ｓ': 'S', 'Ｔ': 'T',
    'Ｕ': 'U', 'Ｖ': 'V', 'Ｗ': 'W', 'Ｘ': 'X', 'Ｙ': 'Y',
    'Ｚ': 'Z', 'ａ': 'a', 'ｂ': 'b', 'ｃ': 'c', 'ｄ': 'd',
    'ｅ': 'e', 'ｆ': 'f', 'ｇ': 'g', 'ｈ': 'h', 'ｉ': 'i',
    'ｊ': 'j', 'ｋ': 'k', 'ｌ': 'l', 'ｍ': 'm', 'ｎ': 'n',
    'ｏ': 'o', 'ｐ': 'p', 'ｑ': 'q', 'ｒ': 'r', 'ｓ': 's',
    'ｔ': 't', 'ｕ': 'u', 'ｖ': 'v', 'ｗ': 'w', 'ｘ': 'x',
    'ｙ': 'y', 'ｚ': 'z', '！': '!', '＃': '#', '＄': '$',
    '％': '%', '＆': '&', '＇': "'", '（': '(', '）': ')',
    '＊': '*', '＋': '+', '，': ',', '－': '-', '．': '.',
    '／': '/', '：': ':', '；': ';', '＜': '<', '＝': '=',
    '＞': '>', '？': '?', '＠': '@', '［': '[', '］': ']',
    '＼': '\\', '＾': '^', '＿': '_', '｀': '`', '｛': '{',
    '｜': '|', '｝': '}', '～': '~', '￣': ''
  };

  /**
   * Mapping of half-width characters to full-width characters.
   * @type {Object}
   */
  static HALF_WIDTH_TO_FULL_WIDTH_MAP = Object.fromEntries(
    Object.entries(TextFormatter.FULL_WIDTH_TO_HALF_WIDTH_MAP).map(([k, v]) => [v, k])
  );

  /**
   * Converts full-width text to half-width text.
   * @param {string} text - The text to convert.
   * @returns {string} The converted text.
   */
  static fullWidthToHalfWidth(text) {
    return text.replace(/./g, match => TextFormatter.FULL_WIDTH_TO_HALF_WIDTH_MAP[match] || match);
  }

  /**
   * Converts half-width text to full-width text.
   * @param {string} text - The text to convert.
   * @returns {string} The converted text.
   */
  static halfWidthToFullWidth(text) {
    return text.replace(/./g, match => TextFormatter.HALF_WIDTH_TO_FULL_WIDTH_MAP[match] || match);
  }
}

// Example usage:
function main() {
  try {
    const originalText = "０１２３４５６７８９ＡＢＣＤＥＦＧＨＩＪ";
    console.log(`Original text: ${originalText}`);

    const halfWidthText = TextFormatter.fullWidthToHalfWidth(originalText);
    console.log(`Half-width text: ${halfWidthText}`);

    const fullWidthText = TextFormatter.halfWidthToFullWidth(halfWidthText);
    console.log(`Full-width text: ${fullWidthText}`);
  } catch (error) {
    console.error(`Error: ${error.message}`);
  }
}

main();
```
