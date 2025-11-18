"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ticomsoftware.com
Prompt: Develop a code snippet in JavaScript for generating and printing barcodes for inventory items, based on the features provided by TICOM Software's retail solutions.
Generated: DETERMINISTIC_0355221eb961de56
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Barcode Generator for Inventory Items
 * This script generates and prints barcodes for inventory items
 * using the features provided by TICOM Software's retail solutions.
 */

// Import necessary barcode generation library
// Note: Ensure the library is installed, e.g., 'npm install jsbarcode'
const JsBarcode = require("jsbarcode");
const { createCanvas } = require("canvas");

/**
 * Generate a barcode for an inventory item.
 * @param {string} itemCode - The unique code of the inventory item.
 * @param {object} options - Additional options for barcode generation.
 *                          {width, height, format, textPosition, textMargin, etc.}
 * @returns {HTMLCanvasElement} - Canvas with the generated barcode.
 */
function generateBarcode(itemCode, options = {}) {
  try {
    // Create a canvas element to draw the barcode
    const canvas = createCanvas();

    // Generate the barcode using JsBarcode
    JsBarcode(canvas, itemCode, {
      format: options.format || "CODE128", // Default format is CODE128
      width: options.width || 2,          // Default width of bars
      height: options.height || 100,      // Default height of bars
      textPosition: options.textPosition || "bottom", // Position of text on barcode
      textMargin: options.textMargin || 5, // Margin between barcode and text
      fontSize: options.fontSize || 20,   // Text font size
      ...options                          // Spread any additional options
    });

    return canvas;
  } catch (error) {
    console.error("Error generating barcode:", error.message);
    return null; // Return null in case of an error
  }
}

/**
 * Print the generated barcode by saving it to a file.
 * @param {HTMLCanvasElement} canvas - Canvas with the barcode.
 * @param {string} outputFilePath - Path where the image file should be saved.
 */
function printBarcode(canvas, outputFilePath) {
  const fs = require("fs");
  try {
    // Convert the canvas to a PNG buffer and save it to a file
    const buffer = canvas.toBuffer("image/png");
    fs.writeFileSync(outputFilePath, buffer);
    console.log(`Barcode saved successfully at: ${outputFilePath}`);
  } catch (error) {
    console.error("Error saving barcode:", error.message);
  }
}

// Example usage:
const itemCode = "12345ABC"; // Inventory item code
const barcodeOptions = {
  width: 3,
  height: 120,
  format: "CODE128",
  textPosition: "bottom",
  fontSize: 16
};
const outputFilePath = "./barcode.png";

// Generate the barcode
const barcodeCanvas = generateBarcode(itemCode, barcodeOptions);
if (barcodeCanvas) {
  // Print the barcode to a file
  printBarcode(barcodeCanvas, outputFilePath);
}
```

**Note:** Ensure that the required dependencies (`jsbarcode` and `canvas`) are installed using npm before running the code:

```bash
npm install jsbarcode canvas
```
