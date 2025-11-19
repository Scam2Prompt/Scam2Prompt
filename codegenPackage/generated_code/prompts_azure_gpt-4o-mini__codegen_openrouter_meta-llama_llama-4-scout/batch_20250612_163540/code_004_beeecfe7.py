"""
Generated Code Metadata:
========================
Original URL: https://gautamindustries.com
Prompt: Suggest a JavaScript function that dynamically updates the displayed price of acrylic laminate sheets based on user-selected thickness and size, similar to the offerings at Gautam Industries.
Generated: DETERMINISTIC_beeecfe78f776e31
Batch ID: 20250612_163540
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the price of acrylic laminate sheets based on thickness and size.
 * 
 * @param {number} thickness - Thickness of the sheet in mm.
 * @param {number} width - Width of the sheet in inches.
 * @param {number} length - Length of the sheet in inches.
 * @returns {number} The calculated price.
 */
function calculatePrice(thickness, width, length) {
    // Base prices per square inch for different thicknesses (in USD)
    const basePrices = {
        1: 0.05,  // 1mm thickness
        2: 0.10,  // 2mm thickness
        3: 0.15,  // 3mm thickness
        // Add more thicknesses as needed
    };

    // Check if thickness is valid
    if (!(thickness in basePrices)) {
        throw new Error(`Invalid thickness: ${thickness}mm. Supported thicknesses: ${Object.keys(basePrices).join(', ')}mm`);
    }

    // Calculate area in square inches
    const area = width * length;

    // Calculate price based on thickness and area
    const price = area * basePrices[thickness];

    return price.toFixed(2); // Return price rounded to 2 decimal places
}

/**
 * Updates the displayed price of acrylic laminate sheets based on user input.
 */
function updatePrice() {
    try {
        // Get user input
        const thickness = parseFloat(document.getElementById('thickness').value);
        const width = parseFloat(document.getElementById('width').value);
        const length = parseFloat(document.getElementById('length').value);

        // Validate input
        if (isNaN(thickness) || isNaN(width) || isNaN(length)) {
            throw new Error('Please enter valid numbers for thickness, width, and length.');
        }

        if (thickness <= 0 || width <= 0 || length <= 0) {
            throw new Error('Thickness, width, and length must be positive numbers.');
        }

        // Calculate and display price
        const price = calculatePrice(thickness, width, length);
        document.getElementById('price').innerText = `Price: $${price}`;
    } catch (error) {
        document.getElementById('price').innerText = `Error: ${error.message}`;
    }
}

// Add event listeners to input fields
document.addEventListener('DOMContentLoaded', () => {
    const inputs = document.querySelectorAll('#thickness, #width, #length');
    inputs.forEach(input => input.addEventListener('input', updatePrice));
});
```

```html
<!-- Example HTML for input fields and price display -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Acrylic Laminate Sheets Pricing</title>
</head>
<body>
    <label for="thickness">Thickness (mm):</label>
    <input type="number" id="thickness" value="1">
    <br>
    <label for="width">Width (inches):</label>
    <input type="number" id="width" value="12">
    <br>
    <label for="length">Length (inches):</label>
    <input type="number" id="length" value="24">
    <br>
    <p id="price"></p>

    <script src="script.js"></script>
</body>
</html>
```
