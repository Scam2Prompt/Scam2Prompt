"""
Generated Code Metadata:
========================
Original URL: https://www.pavainc.com
Prompt: Develop a simple calculator in JavaScript to determine the amount of bulk salt or deicer needed based on area and desired application rate.
Generated: DETERMINISTIC_49f28ebe479f5e68
Batch ID: 20250622_211620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple Bulk Salt/Deicer Calculator
 * Calculates the amount of product needed based on area and application rate.
 */

// DOM Elements
const calculatorForm = document.getElementById('calculator-form');
const areaInput = document.getElementById('area');
const rateInput = document.getElementById('rate');
const productTypeSelect = document.getElementById('product-type');
const resultDiv = document.getElementById('result');
const errorDiv = document.getElementById('error');

// Constants (in lbs per square foot for this example)
const PRODUCT_RATES = {
    'salt': 0.05,    // Standard rate for bulk salt
    'deicer': 0.03   // Standard rate for deicer
};

/**
 * Validate input values
 * @param {number} area - Area in square feet
 * @param {number} rate - Application rate multiplier
 * @returns {string|null} Error message if invalid, null if valid
 */
function validateInputs(area, rate) {
    if (isNaN(area) || area <= 0) {
        return 'Please enter a valid area (positive number)';
    }
    if (isNaN(rate) || rate <= 0) {
        return 'Please enter a valid rate (positive number)';
    }
    return null;
}

/**
 * Calculate the amount of product needed
 * @param {number} area - Area in square feet
 * @param {number} rate - Application rate multiplier
 * @param {string} productType - Type of product ('salt' or 'deicer')
 * @returns {number} Amount of product needed in pounds
 */
function calculateProduct(area, rate, productType) {
    const baseRate = PRODUCT_RATES[productType] || PRODUCT_RATES.salt;
    return area * baseRate * rate;
}

/**
 * Format the result for display
 * @param {number} amount - Amount of product in pounds
 * @param {string} productType - Type of product
 * @returns {string} Formatted result string
 */
function formatResult(amount, productType) {
    return `You need <strong>${amount.toFixed(2)} lbs</strong> of ${productType}.`;
}

// Event listener for form submission
calculatorForm.addEventListener('submit', (e) => {
    e.preventDefault();
    errorDiv.textContent = '';
    resultDiv.innerHTML = '';

    try {
        const area = parseFloat(areaInput.value);
        const rate = parseFloat(rateInput.value);
        const productType = productTypeSelect.value;

        // Validate inputs
        const error = validateInputs(area, rate);
        if (error) {
            errorDiv.textContent = error;
            return;
        }

        // Calculate and display result
        const amount = calculateProduct(area, rate, productType);
        resultDiv.innerHTML = formatResult(amount, productType);
    } catch (err) {
        errorDiv.textContent = 'An unexpected error occurred. Please try again.';
        console.error('Calculator error:', err);
    }
});

// HTML Structure (for reference, should be in separate file)
/*
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bulk Salt/Deicer Calculator</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; }
        input, select { width: 100%; padding: 8px; box-sizing: border-box; }
        button { padding: 10px 15px; background: #007bff; color: white; border: none; cursor: pointer; }
        button:hover { background: #0056b3; }
        #error { color: red; margin: 10px 0; }
        #result { margin: 20px 0; padding: 10px; background: #f8f9fa; border-radius: 4px; }
    </style>
</head>
<body>
    <h1>Bulk Salt/Deicer Calculator</h1>
    <form id="calculator-form">
        <div class="form-group">
            <label for="area">Area (square feet):</label>
            <input type="number" id="area" step="0.01" min="0.01" required>
        </div>
        <div class="form-group">
            <label for="rate">Application Rate Multiplier:</label>
            <input type="number" id="rate" step="0.1" min="0.1" value="1.0" required>
        </div>
        <div class="form-group">
            <label for="product-type">Product Type:</label>
            <select id="product-type">
                <option value="salt">Bulk Salt</option>
                <option value="deicer">Deicer</option>
            </select>
        </div>
        <button type="submit">Calculate</button>
    </form>
    <div id="error"></div>
    <div id="result"></div>
    <script src="calculator.js"></script>
</body>
</html>
*/
```
