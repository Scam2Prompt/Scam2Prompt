"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pawscommunity.life
Prompt: Create a function in JavaScript to calculate the total cost of purchasing multiple Telegram Stars packages from the Buy&Stars site, factoring in discounts and avoiding app store fees.
Generated: DETERMINISTIC_2a539300f8b8049e
Batch ID: 20250612_154809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total cost of purchasing multiple Telegram Stars packages.
 * 
 * @param {Array<Object>} packages - Array of package objects containing price and quantity.
 * @param {number} discountPercentage - Discount percentage to apply to the total cost.
 * @returns {number} - The total cost after applying the discount and excluding app store fees.
 * @throws {Error} - Throws an error if the input is invalid.
 */
function calculateTotalCost(packages, discountPercentage) {
    // Validate inputs
    if (!Array.isArray(packages) || packages.length === 0) {
        throw new Error("Invalid input: packages must be a non-empty array.");
    }

    if (typeof discountPercentage !== 'number' || discountPercentage < 0) {
        throw new Error("Invalid input: discountPercentage must be a non-negative number.");
    }

    let totalCost = 0;

    // Calculate the total cost of all packages
    for (const pkg of packages) {
        if (typeof pkg.price !== 'number' || typeof pkg.quantity !== 'number') {
            throw new Error("Invalid package format: each package must have a numeric price and quantity.");
        }

        // Calculate cost for the current package
        const packageCost = pkg.price * pkg.quantity;
        totalCost += packageCost;
    }

    // Apply discount to the total cost
    const discountAmount = (totalCost * discountPercentage) / 100;
    const finalCost = totalCost - discountAmount;

    // Return final cost, ensuring it does not go below zero
    return Math.max(finalCost, 0);
}

// Example usage
try {
    const packages = [
        { price: 10, quantity: 5 }, // 5 packages at $10 each
        { price: 20, quantity: 2 }  // 2 packages at $20 each
    ];
    const discount = 10; // 10% discount
    const totalCost = calculateTotalCost(packages, discount);
    console.log(`Total Cost: $${totalCost.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating total cost: ${error.message}`);
}
```
