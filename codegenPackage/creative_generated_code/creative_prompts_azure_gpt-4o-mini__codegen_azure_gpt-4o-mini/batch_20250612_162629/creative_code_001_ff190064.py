"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ocuvana.com
Prompt: Create a JavaScript function that calculates the total cost of purchasing multiple sets of Ocuvana magnetic lashes, including discounts for bundles.
Generated: DETERMINISTIC_ff1900640cdb618d
Batch ID: 20250612_162629
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total cost of purchasing multiple sets of Ocuvana magnetic lashes.
 * 
 * @param {number} unitPrice - The price of a single unit of Ocuvana magnetic lashes.
 * @param {number} quantity - The total number of units being purchased.
 * @param {number} [bundleDiscount=0] - The discount percentage applied for bundles (optional).
 * @returns {number} - The total cost after applying bundle discounts.
 * @throws {Error} - Throws an error if unit price or quantity is less than zero.
 */
function calculateTotalCost(unitPrice, quantity, bundleDiscount = 0) {
    // Validate input values
    if (unitPrice < 0) {
        throw new Error("Unit price cannot be negative.");
    }
    if (quantity < 0) {
        throw new Error("Quantity cannot be negative.");
    }
    if (bundleDiscount < 0 || bundleDiscount > 100) {
        throw new Error("Bundle discount must be between 0 and 100.");
    }

    // Calculate total cost before discount
    let totalCost = unitPrice * quantity;

    // Apply bundle discount if applicable
    if (bundleDiscount > 0) {
        const discountAmount = (totalCost * bundleDiscount) / 100;
        totalCost -= discountAmount;
    }

    // Return the final total cost rounded to two decimal places
    return parseFloat(totalCost.toFixed(2));
}

// Example usage:
try {
    const total = calculateTotalCost(29.99, 3, 10);
    console.log(`Total cost: $${total}`);
} catch (error) {
    console.error(error.message);
}
```
