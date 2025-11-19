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
 * Converts full-width characters to half-width and vice versa.
 * Full-width characters are typically used in East Asian languages,
 * while half-width characters are more common in Western languages.
 * 
 * @param {string} input - The string to be converted.
 * @param {boolean} toHalfWidth - If true, converts to half-width; if false, converts to full-width.
 * @returns {string} - The converted string.
 * @throws {TypeError} - Throws an error if the input is not a string.
 */
function convertWidth(input, toHalfWidth) {
    // Validate input type
    if (typeof input !== 'string') {
        throw new TypeError('Input must be a string');
    }

    // Define conversion functions
    const fullWidthToHalfWidth = (str) => {
        return str.replace(/[\uFF01-\uFF5E]/g, (char) => {
            return String.fromCharCode(char.charCodeAt(0) - 0xFEE0);
        }).replace(/\u3000/g, ' '); // Convert full-width space to half-width space
    };

    const halfWidthToFullWidth = (str) => {
        return str.replace(/[!-~]/g, (char) => {
            return String.fromCharCode(char.charCodeAt(0) + 0xFEE0);
        }).replace(/ /g, '\u3000'); // Convert half-width space to full-width space
    };

    // Perform conversion based on the flag
    return toHalfWidth ? fullWidthToHalfWidth(input) : halfWidthToFullWidth(input);
}

// Example usage:
try {
    const fullWidthText = 'Ｈｅｌｌｏ，　世界！'; // Full-width text
    const halfWidthText = convertWidth(fullWidthText, true);
    console.log('Half-width:', halfWidthText); // Output: Hello, 世界!

    const backToFullWidth = convertWidth(halfWidthText, false);
    console.log('Full-width:', backToFullWidth); // Output: Ｈｅｌｌｏ，　世界！
} catch (error) {
    console.error('Error:', error.message);
}
```
