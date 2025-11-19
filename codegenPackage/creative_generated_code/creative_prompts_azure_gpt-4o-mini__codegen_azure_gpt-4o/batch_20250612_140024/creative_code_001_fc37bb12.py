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
 * Function to calculate the diagonal screen size of an iPhone model based on its width and height in pixels.
 * @param {string} model - iPhone model name.
 * @returns {string} Diagonal screen size in inches or an error message if the model is unknown.
 */
function calculateDiagonalScreenSize(model) {
  // Specifications for iPhone models (width, height in pixels, and pixel density in PPI)
  const iPhoneSpecs = {
    "iPhone SE (2nd Gen)": { width: 750, height: 1334, ppi: 326 },
    "iPhone 12 Mini": { width: 1080, height: 2340, ppi: 476 },
    "iPhone 13": { width: 1170, height: 2532, ppi: 460 },
    "iPhone 14 Pro Max": { width: 1290, height: 2796, ppi: 460 },
    // Add more models here as needed
  };

  // Check if the model exists in the specifications
  if (!iPhoneSpecs[model]) {
    return `Error: Unknown iPhone model '${model}'. Please provide a valid model name.`;
  }

  const { width, height, ppi } = iPhoneSpecs[model];

  try {
    // Calculate the diagonal size in pixels using the Pythagorean theorem
    const diagonalPixels = Math.sqrt(width ** 2 + height ** 2);

    // Convert pixels to inches using the pixel density (PPI)
    const diagonalInches = diagonalPixels / ppi;

    // Return the diagonal screen size rounded to 2 decimal places
    return `${diagonalInches.toFixed(2)} inches`;
  } catch (error) {
    return `Error: Unable to calculate screen size due to an unexpected error - ${error.message}`;
  }
}

// Example usage:
// console.log(calculateDiagonalScreenSize("iPhone 14 Pro Max")); // Expected output: "6.69 inches"
// console.log(calculateDiagonalScreenSize("Unknown Model")); // Expected output: Error message
```
