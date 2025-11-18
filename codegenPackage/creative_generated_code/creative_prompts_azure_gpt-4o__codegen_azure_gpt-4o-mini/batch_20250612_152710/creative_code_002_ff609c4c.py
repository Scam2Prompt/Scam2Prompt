"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smogtoken-def.pages.dev
Prompt: Create a function in JavaScript to calculate airdrop points for SMOG token holders based on wallet activity and staking status.
Generated: DETERMINISTIC_ff609c4c93891e02
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates airdrop points for SMOG token holders based on wallet activity and staking status.
 * 
 * @param {Object} wallet - The wallet object of the token holder.
 * @param {number} wallet.stakedAmount - The amount of SMOG tokens staked.
 * @param {number} wallet.transactionCount - The number of transactions made by the wallet.
 * @param {boolean} wallet.isActive - Indicates if the wallet is active (recent activity).
 * @returns {number} - The calculated airdrop points.
 * @throws {Error} - Throws an error if the input parameters are invalid.
 */
function calculateAirdropPoints(wallet) {
    // Validate input parameters
    if (!wallet || typeof wallet !== 'object') {
        throw new Error('Invalid wallet object provided.');
    }
    if (typeof wallet.stakedAmount !== 'number' || wallet.stakedAmount < 0) {
        throw new Error('Invalid staked amount. It must be a non-negative number.');
    }
    if (typeof wallet.transactionCount !== 'number' || wallet.transactionCount < 0) {
        throw new Error('Invalid transaction count. It must be a non-negative number.');
    }
    if (typeof wallet.isActive !== 'boolean') {
        throw new Error('Invalid active status. It must be a boolean.');
    }

    // Initialize points
    let points = 0;

    // Calculate points based on staked amount
    if (wallet.stakedAmount > 0) {
        // 1 point for every SMOG token staked
        points += wallet.stakedAmount;
    }

    // Calculate points based on transaction activity
    if (wallet.transactionCount > 0) {
        // 0.5 points for each transaction
        points += wallet.transactionCount * 0.5;
    }

    // Bonus points for active wallets
    if (wallet.isActive) {
        points += 10; // Fixed bonus for active wallets
    }

    // Return the total calculated points
    return points;
}

// Example usage:
try {
    const wallet = {
        stakedAmount: 100,
        transactionCount: 50,
        isActive: true
    };
    const points = calculateAirdropPoints(wallet);
    console.log(`Airdrop Points: ${points}`);
} catch (error) {
    console.error(`Error calculating airdrop points: ${error.message}`);
}
```
