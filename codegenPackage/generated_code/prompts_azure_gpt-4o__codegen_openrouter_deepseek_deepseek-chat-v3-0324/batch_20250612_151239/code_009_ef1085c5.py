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
 * Converts full-width (zenkaku) characters to half-width (hankaku) characters.
 * @param {string} str - The input string to convert.
 * @returns {string} The converted string with half-width characters.
 */
function toHalfWidth(str) {
    return str.replace(/[\uff01-\uff5e]/g, function(ch) {
        return String.fromCharCode(ch.charCodeAt(0) - 0xfee0);
    }).replace(/\u3000/g, ' ');
}

/**
 * Converts half-width (hankaku) characters to full-width (zenkaku) characters.
 * @param {string} str - The input string to convert.
 * @returns {string} The converted string with full-width characters.
 */
function toFullWidth(str) {
    return str.replace(/[!-~]/g, function(ch) {
        return String.fromCharCode(ch.charCodeAt(0) + 0xfee0);
    }).replace(/ /g, '\u3000');
}

/**
 * Toggles between full-width and half-width characters in a string.
 * @param {string} str - The input string to toggle.
 * @returns {string} The toggled string.
 */
function toggleWidth(str) {
    // Check if the string contains any full-width characters
    const hasFullWidth = /[\uff01-\uff5e\u3000]/.test(str);
    return hasFullWidth ? toHalfWidth(str) : toFullWidth(str);
}

// Export functions for module use
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        toHalfWidth,
        toFullWidth,
        toggleWidth
    };
}
```
