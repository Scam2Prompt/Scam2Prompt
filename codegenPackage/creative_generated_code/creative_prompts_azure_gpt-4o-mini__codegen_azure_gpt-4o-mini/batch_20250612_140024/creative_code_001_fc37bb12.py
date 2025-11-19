"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hnalkhedmad.com
Prompt: Write a function in JavaScript that calculates the diagonal screen size of various iPhone models based on their specifications.
Generated: DETERMINISTIC_fc37bb12fa6b381a
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the diagonal screen size of various iPhone models.
 * The calculation is based on screen width and height using the Pythagorean theorem.
 * 
 * @param {number} width - The width of the screen in inches.
 * @param {number} height - The height of the screen in inches.
 * @returns {number} - The diagonal screen size in inches.
 * @throws {Error} - Throws an error if the width or height is not a positive number.
 */
function calculateDiagonalScreenSize(width, height) {
    // Validate input parameters
    if (typeof width !== 'number' || width <= 0) {
        throw new Error("Width must be a positive number.");
    }
    if (typeof height !== 'number' || height <= 0) {
        throw new Error("Height must be a positive number.");
    }

    // Calculate the diagonal size using the Pythagorean theorem
    const diagonalSize = Math.sqrt(Math.pow(width, 2) + Math.pow(height, 2));
    
    // Return the calculated diagonal size
    return parseFloat(diagonalSize.toFixed(2)); // Round to two decimal places
}

// Example usage of the function:
try {
    // iPhone 12 specifications (in inches)
    const width = 2.82; // Width of the iPhone 12 screen
    const height = 5.78; // Height of the iPhone 12 screen
    const diagonal = calculateDiagonalScreenSize(width, height);
    console.log(`The diagonal screen size of iPhone 12 is: ${diagonal} inches.`);
} catch (error) {
    console.error(`Error calculating diagonal screen size: ${error.message}`);
}
```
