"""
Generated Code Metadata:
========================
Original URL: https://thechampionsshop.com
Prompt: Write a JavaScript function to calculate the total cost of purchasing 3 MLB Title Belts and 2 NFL Title Belts from The Champions Shop, considering a 10% discount for bulk orders.
Generated: DETERMINISTIC_75c0dd71b2a73077
Batch ID: 20250622_204844
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of purchasing MLB and NFL Title Belts from The Champions Shop.
 * Applies a 10% discount for bulk orders (5 or more belts).
 *
 * @param {number} mlbBeltPrice - The price of a single MLB Title Belt.
 * @param {number} nflBeltPrice - The price of a single NFL Title Belt.
 * @param {number} mlbQuantity - The quantity of MLB Title Belts to purchase.
 * @param {number} nflQuantity - The quantity of NFL Title Belts to purchase.
 * @returns {number} - The total cost after applying any discounts.
 * @throws {Error} - Throws an error if any price or quantity is negative.
 */
function calculateTotalCost(mlbBeltPrice, nflBeltPrice, mlbQuantity, nflQuantity) {
    // Validate input parameters
    if (mlbBeltPrice < 0 || nflBeltPrice < 0 || mlbQuantity < 0 || nflQuantity < 0) {
        throw new Error("Prices and quantities must be non-negative.");
    }

    // Calculate the total cost without discount
    const totalMLBCost = mlbBeltPrice * mlbQuantity;
    const totalNFLCost = nflBeltPrice * nflQuantity;
    const totalCost = totalMLBCost + totalNFLCost;

    // Calculate total quantity for discount eligibility
    const totalQuantity = mlbQuantity + nflQuantity;

    // Apply a 10% discount if the total quantity is 5 or more
    const discount = totalQuantity >= 5 ? 0.10 : 0;
    const finalCost = totalCost * (1 - discount);

    return finalCost;
}

// Example usage
try {
    const mlbBeltPrice = 29.99; // Price of a single MLB Title Belt
    const nflBeltPrice = 34.99; // Price of a single NFL Title Belt
    const mlbQuantity = 3;       // Quantity of MLB Title Belts
    const nflQuantity = 2;       // Quantity of NFL Title Belts

    const totalCost = calculateTotalCost(mlbBeltPrice, nflBeltPrice, mlbQuantity, nflQuantity);
    console.log(`Total cost: $${totalCost.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
