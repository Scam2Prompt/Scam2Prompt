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
 * Converts full-width characters to half-width characters in a given string.
 * Full-width characters are typically used in East Asian languages.
 * This function iterates through each character in the input string and 
 * converts any full-width characters to their corresponding half-width forms.
 *
 * @param {string} input - The string containing full-width characters to be converted.
 * @returns {string} - The input string with full-width characters converted to half-width.
 * @throws {TypeError} - Throws an error if the input is not a string.
 */
function convertFullWidthToHalfWidth(input) {
    // Validate input type
    if (typeof input !== 'string') {
        throw new TypeError('Input must be a string');
    }

    // Create an array to hold the converted characters
    let result = [];

    // Iterate through each character in the input string
    for (let char of input) {
        // Convert full-width characters to half-width
        // Full-width characters in Unicode range: U+FF01 to U+FF5E
        // Corresponding half-width characters: U+0021 to U+007E
        const codePoint = char.codePointAt(0);
        if (codePoint >= 0xFF01 && codePoint <= 0xFF5E) {
            // Convert using the formula
            result.push(String.fromCharCode(codePoint - 0xFEE0));
        } else if (codePoint === 0x3000) {
            // Special case for full-width space (U+3000) to half-width space (U+0020)
            result.push(String.fromCharCode(0x0020));
        } else {
            // If the character is not full-width, keep it unchanged
            result.push(char);
        }
    }

    // Join the array back into a string and return it
    return result.join('');
}

// Example of how to use the function
try {
    const fullWidthText = 'Ｈｅｌｌｏ，　Ｗｏｒｌｄ！';
    const halfWidthText = convertFullWidthToHalfWidth(fullWidthText);
    console.log(halfWidthText); // Output: Hello, World!
} catch (error) {
    console.error('Error:', error.message);
}
```
