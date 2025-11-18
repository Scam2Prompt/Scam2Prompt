"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadots.work
Prompt: Write JavaScript code to convert full-width text to half-width and vice versa, as described in the "テキストの整形" tools on コピーツールラボ.
Generated: DETERMINISTIC_ef1085c5cd600c09
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Converts full-width characters to half-width and vice versa.
 * This function handles common full-width characters, including alphabets, 
 * numbers, and punctuation.
 * 
 * @param {string} input - The string to be converted.
 * @param {boolean} toHalfWidth - If true, convert full-width to half-width; 
 *                                if false, convert half-width to full-width.
 * @returns {string} The converted string.
 */
function convertText(input, toHalfWidth) {
    // Validate input types
    if (typeof input !== 'string') {
        throw new TypeError('Input must be a string.');
    }
    if (typeof toHalfWidth !== 'boolean') {
        throw new TypeError('toHalfWidth must be a boolean.');
    }

    // Create a mapping for full-width to half-width and vice versa
    const fullWidthToHalfWidth = (char) => {
        const code = char.charCodeAt(0);
        // Full-width characters range from 65281 to 65374 (inclusive)
        if (code >= 65281 && code <= 65374) {
            return String.fromCharCode(code - 0xFEE0);
        }
        return char; // Return unchanged if not full-width
    };

    const halfWidthToFullWidth = (char) => {
        const code = char.charCodeAt(0);
        // Half-width characters range from 33 to 126 (inclusive)
        if (code >= 33 && code <= 126) {
            return String.fromCharCode(code + 0xFEE0);
        }
        return char; // Return unchanged if not half-width
    };

    // Convert the input based on the requested conversion
    const result = Array.from(input).map(char => 
        toHalfWidth ? fullWidthToHalfWidth(char) : halfWidthToFullWidth(char)
    ).join('');

    return result;
}

// Example usage:
try {
    const fullWidthText = 'ＡＢＣＤＥＦＧ123';
    const halfWidthText = convertText(fullWidthText, true);
    console.log('Converted to half-width:', halfWidthText);

    const convertedBack = convertText(halfWidthText, false);
    console.log('Converted back to full-width:', convertedBack);
} catch (error) {
    console.error('Error during conversion:', error.message);
}
```
