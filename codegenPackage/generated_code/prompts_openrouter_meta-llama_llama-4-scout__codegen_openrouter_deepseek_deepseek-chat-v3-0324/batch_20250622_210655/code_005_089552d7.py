"""
Generated Code Metadata:
========================
Original URL: https://printserves.com
Prompt: "Develop a simple calculator using JavaScript to estimate the cost of printing services based on factors like quantity, material, and size, similar to what is offered on Printserves."
Generated: DETERMINISTIC_089552d7b4151080
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple Printing Cost Calculator
 * 
 * This script calculates the estimated cost of printing services based on:
 * - Quantity
 * - Material type
 * - Size
 */

// Price configuration (could be fetched from a database in a real application)
const PRICE_CONFIG = {
    materials: {
        'standard': 0.10,    // per unit
        'premium': 0.25,     // per unit
        'eco-friendly': 0.15 // per unit
    },
    sizes: {
        'small': 1.0,        // multiplier
        'medium': 1.5,
        'large': 2.0,
        'x-large': 2.5
    },
    discounts: {
        minQuantityForDiscount: 100,
        discountPercentage: 0.1 // 10%
    }
};

/**
 * Calculate the total printing cost
 * @param {number} quantity - Number of items to print
 * @param {string} material - Type of material ('standard', 'premium', 'eco-friendly')
 * @param {string} size - Size of the print ('small', 'medium', 'large', 'x-large')
 * @returns {number} Total cost
 * @throws {Error} If invalid parameters are provided
 */
function calculatePrintingCost(quantity, material, size) {
    // Validate inputs
    if (!Number.isInteger(quantity) || quantity <= 0) {
        throw new Error('Quantity must be a positive integer');
    }

    if (!PRICE_CONFIG.materials[material]) {
        throw new Error(`Invalid material type: ${material}`);
    }

    if (!PRICE_CONFIG.sizes[size]) {
        throw new Error(`Invalid size: ${size}`);
    }

    // Calculate base cost
    const baseCost = PRICE_CONFIG.materials[material] * quantity;
    
    // Apply size multiplier
    const sizedCost = baseCost * PRICE_CONFIG.sizes[size];
    
    // Apply discount if applicable
    let finalCost = sizedCost;
    if (quantity >= PRICE_CONFIG.discounts.minQuantityForDiscount) {
        finalCost *= (1 - PRICE_CONFIG.discounts.discountPercentage);
    }

    return parseFloat(finalCost.toFixed(2));
}

/**
 * Main function to handle form submission and display results
 */
function handleCalculatorForm() {
    const form = document.getElementById('printingCalculatorForm');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        
        try {
            const quantity = parseInt(document.getElementById('quantity').value);
            const material = document.getElementById('material').value;
            const size = document.getElementById('size').value;

            const totalCost = calculatePrintingCost(quantity, material, size);
            resultDiv.innerHTML = `
                <div class="result-success">
                    <h3>Estimated Cost</h3>
                    <p>Quantity: ${quantity}</p>
                    <p>Material: ${material}</p>
                    <p>Size: ${size}</p>
                    <p class="total-cost">Total: $${totalCost}</p>
                </div>
            `;
        } catch (error) {
            resultDiv.innerHTML = `
                <div class="result-error">
                    <p>Error: ${error.message}</p>
                </div>
            `;
        }
    });
}

// Initialize the calculator when the DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    handleCalculatorForm();
});
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Printing Cost Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }
        form {
            display: grid;
            gap: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input, select {
            width: 100%;
            padding: 8px;
            box-sizing: border-box;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            border: none;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #45a049;
        }
        .result-success, .result-error {
            margin-top: 20px;
            padding: 15px;
            border-radius: 5px;
        }
        .result-success {
            background-color: #dff0d8;
            border: 1px solid #d6e9c6;
        }
        .result-error {
            background-color: #f2dede;
            border: 1px solid #ebccd1;
        }
        .total-cost {
            font-weight: bold;
            font-size: 1.2em;
        }
    </style>
</head>
<body>
    <h1>Printing Cost Calculator</h1>
    <form id="printingCalculatorForm">
        <div>
            <label for="quantity">Quantity:</label>
            <input type="number" id="quantity" min="1" required>
        </div>
        <div>
            <label for="material">Material:</label>
            <select id="material" required>
                <option value="standard">Standard</option>
                <option value="premium">Premium</option>
                <option value="eco-friendly">Eco-Friendly</option>
            </select>
        </div>
        <div>
            <label for="size">Size:</label>
            <select id="size" required>
                <option value="small">Small</option>
                <option value="medium">Medium</option>
                <option value="large">Large</option>
                <option value="x-large">Extra Large</option>
            </select>
        </div>
        <button type="submit">Calculate</button>
    </form>
    <div id="result"></div>
    <script src="calculator.js"></script>
</body>
</html>
```
