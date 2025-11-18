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
 * Function to convert full-width text to half-width
 * @param {string} input - The full-width text to be converted
 * @returns {string} - The converted half-width text
 */
function convertToHalfWidth(input) {
    if (typeof input !== "string") {
        throw new TypeError("Input must be a string");
    }
    return input.replace(/[\uFF01-\uFF5E]/g, (char) => {
        // Convert full-width characters to half-width by subtracting 0xFEE0
        return String.fromCharCode(char.charCodeAt(0) - 0xFEE0);
    }).replace(/\u3000/g, " "); // Convert full-width space to half-width space
}

/**
 * Function to convert half-width text to full-width
 * @param {string} input - The half-width text to be converted
 * @returns {string} - The converted full-width text
 */
function convertToFullWidth(input) {
    if (typeof input !== "string") {
        throw new TypeError("Input must be a string");
    }
    return input.replace(/[\u0020-\u007E]/g, (char) => {
        // Convert half-width characters to full-width by adding 0xFEE0
        return String.fromCharCode(char.charCodeAt(0) + 0xFEE0);
    }).replace(/ /g, "\u3000"); // Convert half-width space to full-width space
}

// Example usage:
try {
    const fullWidthText = "Ｈｅｌｌｏ　Ｗｏｒｌｄ！";
    const halfWidthText = "Hello World!";

    console.log("Full-width to Half-width:", convertToHalfWidth(fullWidthText));
    console.log("Half-width to Full-width:", convertToFullWidth(halfWidthText));
} catch (error) {
    console.error("Error:", error.message);
}
```
