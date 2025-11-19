"""
Generated Code Metadata:
========================
Original URL: https://redstone.cx
Prompt: Implement a function in JavaScript to distribute $INIT tokens to users based on their BNB or ETH purchases during the presale, considering the first-come, first-served principle.
Generated: DETERMINISTIC_c2738332ed54c60f
Batch ID: 20250622_212208
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Distribute $INIT tokens to users based on their BNB or ETH purchases during the presale.
 * The distribution follows a first-come, first-served principle.
 * 
 * @param {Array} purchases - An array of purchase objects containing user addresses and amounts.
 * @param {number} totalTokens - The total amount of $INIT tokens available for distribution.
 * @returns {Array} - An array of distribution results for each user.
 */
function distributeTokens(purchases, totalTokens) {
    // Validate input parameters
    if (!Array.isArray(purchases) || typeof totalTokens !== 'number' || totalTokens <= 0) {
        throw new Error('Invalid input: purchases must be an array and totalTokens must be a positive number.');
    }

    // Calculate total amount purchased
    const totalPurchased = purchases.reduce((sum, purchase) => {
        if (typeof purchase.amount !== 'number' || purchase.amount <= 0) {
            throw new Error(`Invalid purchase amount for user ${purchase.address}`);
        }
        return sum + purchase.amount;
    }, 0);

    // Check if totalPurchased is greater than zero to avoid division by zero
    if (totalPurchased === 0) {
        throw new Error('Total purchased amount cannot be zero.');
    }

    // Distribute tokens based on purchase amounts
    const distributionResults = purchases.map(purchase => {
        const userTokens = (purchase.amount / totalPurchased) * totalTokens;
        return {
            address: purchase.address,
            tokens: parseFloat(userTokens.toFixed(2)) // Round to 2 decimal places
        };
    });

    return distributionResults;
}

// Example usage
try {
    const purchases = [
        { address: '0x123...', amount: 1.5 },
        { address: '0x456...', amount: 2.0 },
        { address: '0x789...', amount: 0.5 }
    ];
    const totalTokens = 1000;

    const results = distributeTokens(purchases, totalTokens);
    console.log('Token Distribution Results:', results);
} catch (error) {
    console.error('Error during token distribution:', error.message);
}
```
