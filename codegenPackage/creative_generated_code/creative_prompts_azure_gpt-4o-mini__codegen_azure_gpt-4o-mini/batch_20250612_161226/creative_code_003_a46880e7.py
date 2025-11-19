"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nextsophon.io
Prompt: Develop a JavaScript function that calculates the total cost for purchasing $SOPH tokens based on the presale price and bonus percentage.
Generated: DETERMINISTIC_a46880e72e1c001c
Batch ID: 20250612_161226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total cost for purchasing SOPH tokens.
 * 
 * @param {number} tokenAmount - The number of SOPH tokens to purchase.
 * @param {number} presalePrice - The price per SOPH token in USD.
 * @param {number} bonusPercentage - The bonus percentage to apply to the purchase.
 * @returns {number} The total cost after applying the bonus.
 * @throws {Error} Throws an error if any parameter is invalid.
 */
function calculateTotalCost(tokenAmount, presalePrice, bonusPercentage) {
    // Validate inputs
    if (typeof tokenAmount !== 'number' || tokenAmount <= 0) {
        throw new Error('Invalid tokenAmount: Must be a positive number.');
    }
    if (typeof presalePrice !== 'number' || presalePrice <= 0) {
        throw new Error('Invalid presalePrice: Must be a positive number.');
    }
    if (typeof bonusPercentage !== 'number' || bonusPercentage < 0) {
        throw new Error('Invalid bonusPercentage: Must be a non-negative number.');
    }

    // Calculate the total cost before the bonus
    const totalCostBeforeBonus = tokenAmount * presalePrice;

    // Calculate the bonus amount
    const bonusAmount = (bonusPercentage / 100) * totalCostBeforeBonus;

    // Calculate the total cost after applying the bonus
    const totalCost = totalCostBeforeBonus + bonusAmount;

    return totalCost;
}

// Example usage:
try {
    const tokens = 100; // Number of SOPH tokens
    const pricePerToken = 2.5; // Presale price in USD
    const bonus = 10; // Bonus percentage

    const total = calculateTotalCost(tokens, pricePerToken, bonus);
    console.log(`Total cost for purchasing ${tokens} SOPH tokens: $${total.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
