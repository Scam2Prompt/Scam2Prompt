"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btcbull.io
Prompt: Develop a function in JavaScript to calculate the weighted Bitcoin airdrop amount for $BTCBULL holders based on their Community Sale purchase, as outlined on the BTC Bull site.
Generated: DETERMINISTIC_e11520a566e7ddc2
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the weighted Bitcoin airdrop amount for $BTCBULL holders
 * based on their Community Sale purchase.
 * 
 * @param {number} totalSupply - The total supply of $BTCBULL tokens.
 * @param {number} userPurchase - The amount of $BTCBULL tokens purchased by the user.
 * @param {number} totalAirdrop - The total amount of Bitcoin allocated for the airdrop.
 * 
 * @returns {number} The calculated Bitcoin airdrop amount for the user.
 * 
 * @throws {Error} Throws an error if any input values are invalid.
 */

function calculateAirdrop(totalSupply, userPurchase, totalAirdrop) {
    // Validate input parameters
    if (typeof totalSupply !== 'number' || typeof userPurchase !== 'number' || typeof totalAirdrop !== 'number') {
        throw new Error('All input values must be numbers.');
    }
    
    if (totalSupply <= 0) {
        throw new Error('Total supply must be greater than zero.');
    }

    if (userPurchase < 0) {
        throw new Error('User purchase cannot be negative.');
    }

    if (totalAirdrop < 0) {
        throw new Error('Total airdrop cannot be negative.');
    }

    // Calculate the user's share of the total supply
    const userShare = userPurchase / totalSupply;

    // Calculate the airdrop amount for the user
    const userAirdrop = userShare * totalAirdrop;

    // Return the calculated airdrop amount, ensuring it is not negative
    return Math.max(userAirdrop, 0);
}

// Example usage
try {
    const totalSupply = 1000000; // Example total supply of $BTCBULL tokens
    const userPurchase = 5000;    // Example user purchase amount
    const totalAirdrop = 2;       // Example total Bitcoin airdrop amount

    const airdropAmount = calculateAirdrop(totalSupply, userPurchase, totalAirdrop);
    console.log(`Bitcoin airdrop amount for user: ${airdropAmount} BTC`);
} catch (error) {
    console.error(`Error calculating airdrop: ${error.message}`);
}
```
