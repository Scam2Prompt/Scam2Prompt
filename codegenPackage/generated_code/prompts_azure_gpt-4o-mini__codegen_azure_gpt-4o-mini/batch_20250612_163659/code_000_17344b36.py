"""
Generated Code Metadata:
========================
Original URL: https://polkadots.work
Prompt: Generate a JavaScript function that formats text by converting full-width characters to half-width characters using the tools available on コピーツールラボ.
Generated: DETERMINISTIC_17344b3607a18cb9
Batch ID: 20250612_163659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Converts full-width characters to half-width characters in a given string.
 * Full-width characters are typically used in East Asian typography.
 * This function handles both letters and numbers, as well as punctuation.
 *
 * @param {string} input - The string containing full-width characters to be converted.
 * @returns {string} - The converted string with half-width characters.
 * @throws {TypeError} - Throws an error if the input is not a string.
 */
function convertFullWidthToHalfWidth(input) {
    // Validate input type
    if (typeof input !== 'string') {
        throw new TypeError('Input must be a string');
    }

    // Create a variable to hold the converted string
    let converted = '';

    // Iterate through each character in the input string
    for (let char of input) {
        // Convert full-width characters to half-width
        // Full-width characters have a Unicode range from 0xFF01 to 0xFF5E
        // The corresponding half-width characters are in the range from 0x21 to 0x7E
        const code = char.charCodeAt(0);
        if (code >= 0xFF01 && code <= 0xFF5E) {
            // Convert full-width to half-width by adjusting the character code
            converted += String.fromCharCode(code - 0xFEE0);
        } else if (code === 0x3000) {
            // Special case for full-width space (U+3000) to half-width space (U+0020)
            converted += String.fromCharCode(0x0020);
        } else {
            // If it's not a full-width character, keep it as is
            converted += char;
        }
    }

    return converted;
}

// Example usage:
try {
    const fullWidthText = 'Ｈｅｌｌｏ，　Ｗｏｒｌｄ！';
    const halfWidthText = convertFullWidthToHalfWidth(fullWidthText);
    console.log(halfWidthText); // Output: Hello, World!
} catch (error) {
    console.error('Error:', error.message);
}
```
