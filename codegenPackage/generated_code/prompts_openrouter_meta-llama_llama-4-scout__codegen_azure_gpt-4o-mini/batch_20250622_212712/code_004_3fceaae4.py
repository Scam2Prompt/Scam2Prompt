"""
Generated Code Metadata:
========================
Original URL: https://jetsetgo.ky
Prompt: Generate a JavaScript function to calculate the total cost of attending the Cayman Islands Margarita Festival, including package prices and taxes.
Generated: DETERMINISTIC_3fceaae4fefa8253
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of attending the Cayman Islands Margarita Festival.
 * 
 * @param {number} packagePrice - The base price of the selected package.
 * @param {number} taxRate - The tax rate as a decimal (e.g., 0.07 for 7%).
 * @param {number} [discount=0] - Optional discount amount to be subtracted from the total.
 * @returns {number} - The total cost after applying tax and discount.
 * @throws {Error} - Throws an error if the input values are invalid.
 */
function calculateTotalCost(packagePrice, taxRate, discount = 0) {
    // Validate input parameters
    if (typeof packagePrice !== 'number' || packagePrice < 0) {
        throw new Error('Invalid package price. It must be a non-negative number.');
    }
    if (typeof taxRate !== 'number' || taxRate < 0) {
        throw new Error('Invalid tax rate. It must be a non-negative number.');
    }
    if (typeof discount !== 'number' || discount < 0) {
        throw new Error('Invalid discount. It must be a non-negative number.');
    }

    // Calculate tax
    const taxAmount = packagePrice * taxRate;

    // Calculate total cost
    const totalCost = packagePrice + taxAmount - discount;

    // Ensure total cost is not negative
    return Math.max(totalCost, 0);
}

// Example usage
try {
    const packagePrice = 200; // Example package price
    const taxRate = 0.07; // Example tax rate (7%)
    const discount = 20; // Example discount

    const total = calculateTotalCost(packagePrice, taxRate, discount);
    console.log(`The total cost of attending the festival is: $${total.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
