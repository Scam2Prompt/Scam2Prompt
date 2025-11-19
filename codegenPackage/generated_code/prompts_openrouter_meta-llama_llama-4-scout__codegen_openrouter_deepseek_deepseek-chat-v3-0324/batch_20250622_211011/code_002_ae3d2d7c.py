"""
Generated Code Metadata:
========================
Original URL: https://www.metisassets.com
Prompt: Generate a JavaScript code snippet for a simple calculator that estimates the cash offer for a house in San Francisco Bay Area based on user input.
Generated: DETERMINISTIC_ae3d2d7c542b2778
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple calculator to estimate cash offer for a house in San Francisco Bay Area
 * @param {Object} inputs - User input values
 * @param {number} inputs.marketValue - Current market value of the property
 * @param {number} inputs.repairCosts - Estimated repair costs
 * @param {number} inputs.closingCosts - Estimated closing costs
 * @param {number} inputs.desiredProfit - Investor's desired profit margin (as percentage)
 * @param {number} inputs.holdingCosts - Estimated holding costs (taxes, insurance, etc.)
 * @returns {number} Calculated cash offer amount
 * @throws {Error} If any input is invalid
 */
function calculateCashOffer(inputs) {
    // Validate inputs
    if (typeof inputs !== 'object' || inputs === null) {
        throw new Error('Inputs must be provided as an object');
    }

    const requiredFields = ['marketValue', 'repairCosts', 'closingCosts', 'desiredProfit', 'holdingCosts'];
    for (const field of requiredFields) {
        if (typeof inputs[field] !== 'number' || isNaN(inputs[field])) {
            throw new Error(`Invalid value for ${field}: must be a valid number`);
        }
        if (inputs[field] < 0) {
            throw new Error(`Invalid value for ${field}: cannot be negative`);
        }
    }

    if (inputs.desiredProfit > 100) {
        throw new Error('Desired profit cannot exceed 100%');
    }

    // Calculate cash offer
    const totalCosts = inputs.repairCosts + inputs.closingCosts + inputs.holdingCosts;
    const profitAmount = (inputs.desiredProfit / 100) * inputs.marketValue;
    const cashOffer = inputs.marketValue - totalCosts - profitAmount;

    // Ensure offer is reasonable (at least 50% of market value)
    const minimumOffer = inputs.marketValue * 0.5;
    return Math.max(cashOffer, minimumOffer);
}

/**
 * Handles form submission and displays results
 * @param {Event} event - Form submission event
 */
function handleFormSubmit(event) {
    event.preventDefault();
    
    try {
        // Get form values
        const marketValue = parseFloat(document.getElementById('marketValue').value);
        const repairCosts = parseFloat(document.getElementById('repairCosts').value);
        const closingCosts = parseFloat(document.getElementById('closingCosts').value);
        const desiredProfit = parseFloat(document.getElementById('desiredProfit').value);
        const holdingCosts = parseFloat(document.getElementById('holdingCosts').value);

        // Calculate offer
        const offer = calculateCashOffer({
            marketValue,
            repairCosts,
            closingCosts,
            desiredProfit,
            holdingCosts
        });

        // Display result
        document.getElementById('result').textContent = `Estimated Cash Offer: $${offer.toLocaleString('en-US', {maximumFractionDigits: 0})}`;
        document.getElementById('error').textContent = '';
    } catch (error) {
        document.getElementById('error').textContent = `Error: ${error.message}`;
        document.getElementById('result').textContent = '';
    }
}

// Initialize calculator when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('calculatorForm');
    if (form) {
        form.addEventListener('submit', handleFormSubmit);
    }
});
```
