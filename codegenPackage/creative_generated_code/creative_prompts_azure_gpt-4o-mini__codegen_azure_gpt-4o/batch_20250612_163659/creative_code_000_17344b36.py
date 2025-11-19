"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadots.work
Prompt: Generate a JavaScript function that formats text by converting full-width characters to half-width characters using the tools available on コピーツールラボ.
Generated: DETERMINISTIC_17344b3607a18cb9
Batch ID: 20250612_163659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Converts full-width characters to half-width characters.
 * This function will replace common full-width characters (ASCII range) with their half-width counterparts.
 * @param {string} input - The input string containing full-width characters.
 * @returns {string} - The formatted string with half-width characters.
 */
function convertFullWidthToHalfWidth(input) {
    // Ensure the input is a string
    if (typeof input !== 'string') {
        throw new TypeError('Input must be a string');
    }

    // Define a mapping of full-width to half-width characters
    const fullWidthToHalfWidthMap = {
        '！': '!',
        '＂': '"',
        '＃': '#',
        '＄': '$',
        '％': '%',
        '＆': '&',
        '＇': '\'',
        '（': '(',
        '）': ')',
        '＊': '*',
        '＋': '+',
        '，': ',',
        '－': '-',
        '．': '.',
        '／': '/',
        '０': '0',
        '１': '1',
        '２': '2',
        '３': '3',
        '４': '4',
        '５': '5',
        '６': '6',
        '７': '7',
        '８': '8',
        '９': '9',
        '：': ':',
        '；': ';',
        '＜': '<',
        '＝': '=',
        '＞': '>',
        '？': '?',
        '＠': '@',
        'Ａ': 'A',
        'Ｂ': 'B',
        'Ｃ': 'C',
        'Ｄ': 'D',
        'Ｅ': 'E',
        'Ｆ': 'F',
        'Ｇ': 'G',
        'Ｈ': 'H',
        'Ｉ': 'I',
        'Ｊ': 'J',
        'Ｋ': 'K',
        'Ｌ': 'L',
        'Ｍ': 'M',
        'Ｎ': 'N',
        'Ｏ': 'O',
        'Ｐ': 'P',
        'Ｑ': 'Q',
        'Ｒ': 'R',
        'Ｓ': 'S',
        'Ｔ': 'T',
        'Ｕ': 'U',
        'Ｖ': 'V',
        'Ｗ': 'W',
        'Ｘ': 'X',
        'Ｙ': 'Y',
        'Ｚ': 'Z',
        '［': '[',
        '＼': '\\',
        '］': ']',
        '＾': '^',
        '＿': '_',
        '｀': '`',
        'ａ': 'a',
        'ｂ': 'b',
        'ｃ': 'c',
        'ｄ': 'd',
        'ｅ': 'e',
        'ｆ': 'f',
        'ｇ': 'g',
        'ｈ': 'h',
        'ｉ': 'i',
        'ｊ': 'j',
        'ｋ': 'k',
        'ｌ': 'l',
        'ｍ': 'm',
        'ｎ': 'n',
        'ｏ': 'o',
        'ｐ': 'p',
        'ｑ': 'q',
        'ｒ': 'r',
        'ｓ': 's',
        'ｔ': 't',
        'ｕ': 'u',
        'ｖ': 'v',
        'ｗ': 'w',
        'ｘ': 'x',
        'ｙ': 'y',
        'ｚ': 'z',
        '｛': '{',
        '｜': '|',
        '｝': '}',
        '～': '~',
    };

    // Convert full-width characters to half-width using the map
    let output = '';
    for (const char of input) {
        output += fullWidthToHalfWidthMap[char] || char; // Replace if found, otherwise keep original
    }

    return output;
}

// Example usage
try {
    const formattedText = convertFullWidthToHalfWidth('Ｈｅｌｌｏ，　Ｗｏｒｌｄ！');
    console.log(formattedText); // Output: Hello, World!
} catch (error) {
    console.error('Error:', error.message);
}
```
