"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://steredapharmacy.com
Prompt: Write a JavaScript function that calculates the total cost of purchasing Sterevite Syrup and applies a 5% discount for loyalty card holders.
Generated: DETERMINISTIC_1472d3ffa8006e07
Batch ID: 20250612_160019
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total cost of purchasing Sterevite Syrup, including a 5% discount for loyalty card holders.
 * 
 * @param {number} pricePerBottle - The price of one bottle of Sterevite Syrup.
 * @param {number} quantity - The number of bottles being purchased.
 * @param {boolean} hasLoyaltyCard - Whether the customer has a loyalty card.
 * @returns {number} The total cost after applying the discount (if applicable).
 * @throws {Error} Throws an error if invalid inputs are provided.
 */
function calculateTotalCost(pricePerBottle, quantity, hasLoyaltyCard) {
    // Validate inputs
    if (typeof pricePerBottle !== 'number' || pricePerBottle <= 0) {
        throw new Error("Invalid price per bottle. It must be a positive number.");
    }
    if (typeof quantity !== 'number' || quantity <= 0) {
        throw new Error("Invalid quantity. It must be a positive number.");
    }
    if (typeof hasLoyaltyCard !== 'boolean') {
        throw new Error("Invalid loyalty card status. It must be a boolean.");
    }

    // Calculate the total cost
    let totalCost = pricePerBottle * quantity;

    // Apply a 5% discount if the customer has a loyalty card
    if (hasLoyaltyCard) {
        totalCost *= 0.95; // Apply a 5% discount
    }

    // Return the total cost rounded to two decimal places
    return parseFloat(totalCost.toFixed(2));
}

// Example Usage:
// const totalCost = calculateTotalCost(10.5, 3, true);
// console.log("Total Cost:", totalCost);
```
