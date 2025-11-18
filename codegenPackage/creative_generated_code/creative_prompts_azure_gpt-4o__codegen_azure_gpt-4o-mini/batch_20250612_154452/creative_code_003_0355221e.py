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
// BarcodeGenerator.js
class BarcodeGenerator {
    constructor() {
        // Include the library for barcode generation, e.g., JsBarcode
        this.JsBarcode = require('jsbarcode');
    }

    /**
     * Generates a barcode for the given item.
     * @param {string} itemId - The unique identifier for the inventory item.
     * @param {string} format - The format of the barcode (e.g., "CODE128", "EAN", etc.).
     * @param {string} outputType - The output type for the barcode (e.g., "svg", "png").
     * @returns {string} - The generated barcode data URL or SVG string.
     * @throws {Error} - Throws an error if itemId is invalid or if generating the barcode fails.
     */
    generateBarcode(itemId, format = 'CODE128', outputType = 'svg') {
        if (!itemId || typeof itemId !== 'string') {
            throw new Error('Invalid item ID provided.');
        }

        // Create a canvas element to generate the barcode
        const canvas = document.createElement('canvas');

        try {
            // Generate the barcode using JsBarcode
            this.JsBarcode(canvas, itemId, {
                format: format,
                width: 2,
                height: 100,
                displayValue: true,
                textAlign: 'center'
            });

            // Return the barcode as a data URL or SVG
            return outputType === 'svg' ? canvas.toDataURL('image/svg+xml') : canvas.toDataURL('image/png');
        } catch (error) {
            throw new Error(`Barcode generation failed: ${error.message}`);
        }
    }

    /**
     * Prints the generated barcode by adding it to the document and invoking the print dialog.
     * @param {string} barcodeData - The generated barcode data URL or SVG string.
     */
    printBarcode(barcodeData) {
        const printWindow = window.open('', '_blank');
        printWindow.document.write(`
            <html>
                <head>
                    <title>Print Barcode</title>
                </head>
                <body>
                    <img src="${barcodeData}" alt="Barcode"/>
                </body>
            </html>
        `);
        printWindow.document.close();
        printWindow.print();
    }
}

// Example usage
try {
    const barcodeGen = new BarcodeGenerator();
    const itemId = '123456789012'; // Replace with the actual item ID
    const barcodeData = barcodeGen.generateBarcode(itemId);
    barcodeGen.printBarcode(barcodeData);
} catch (error) {
    console.error(error.message);
}
```

**Note:** Ensure to install the JsBarcode library by running `npm install jsbarcode` and include it correctly in your project setup. This code assumes a browser environment where `document` and `window` are available. Adjustments may be necessary for a Node.js environment.
