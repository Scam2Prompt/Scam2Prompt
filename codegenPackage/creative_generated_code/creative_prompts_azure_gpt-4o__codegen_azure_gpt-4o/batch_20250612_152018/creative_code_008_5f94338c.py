"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asx-capital.pages.dev
Prompt: Generate code in JavaScript to calculate rewards in $USDC for $ASX token holders based on the mechanics of multiple revenue streams described on the ASX Capital site.
Generated: DETERMINISTIC_5f94338c3552449d
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @file Calculate rewards for $ASX token holders based on multiple revenue streams.
 * @description This script calculates rewards in $USDC for $ASX token holders.
 * The mechanics of revenue streams are assumed to be based on the ASX Capital site.
 * Ensure this code is run with the required data inputs and proper environment setup.
 * 
 * @author Your Name
 */

// Constants
const USDC_DECIMALS = 6; // USDC typically uses 6 decimal places
const ASX_TOKEN_TOTAL_SUPPLY = 1000000; // Example total supply of $ASX tokens (replace as needed)

// Error handling utility
function handleErrors(message) {
    console.error(`Error: ${message}`);
    throw new Error(message);
}

/**
 * Calculate rewards for $ASX token holders based on revenue streams.
 * @param {Array} holders - Array of token holder objects with `wallet`, `asxBalance`.
 * @param {Array} revenueStreams - Array of revenue stream objects with `name` and `amount` (in $USDC).
 * @returns {Array} Rewards breakdown for each holder with total $USDC reward.
 */
function calculateRewards(holders, revenueStreams) {
    // Validate inputs
    if (!Array.isArray(holders) || !Array.isArray(revenueStreams)) {
        handleErrors("Invalid input: Both holders and revenueStreams must be arrays.");
    }

    const totalRevenueUSDC = revenueStreams.reduce((sum, stream) => {
        if (typeof stream.amount !== 'number' || stream.amount < 0) {
            handleErrors(`Invalid revenue stream amount for ${stream.name}`);
        }
        return sum + stream.amount;
    }, 0);
    
    if (totalRevenueUSDC === 0) {
        handleErrors("Total revenue is zero. Cannot calculate rewards.");
    }

    const rewards = holders.map(holder => {
        const { wallet, asxBalance } = holder;

        // Validate holder data
        if (typeof wallet !== 'string' || typeof asxBalance !== 'number' || asxBalance < 0) {
            handleErrors(`Invalid holder data for wallet: ${wallet}`);
        }

        // Calculate holder's percentage share of total rewards
        const percentageShare = asxBalance / ASX_TOKEN_TOTAL_SUPPLY;
        const rewardUSDC = totalRevenueUSDC * percentageShare;

        return {
            wallet, 
            asxBalance, 
            rewardUSDC: parseFloat(rewardUSDC.toFixed(USDC_DECIMALS)) // Round to USDC decimals
        };
    });

    return rewards;
}

// Example Usage:

// Token holder data
const holders = [
    { wallet: "0x123", asxBalance: 5000 },
    { wallet: "0x456", asxBalance: 15000 },
    { wallet: "0x789", asxBalance: 30000 },
];

// Revenue stream data in $USDC
const revenueStreams = [
    { name: "Stream A", amount: 10000 },
    { name: "Stream B", amount: 5000 },
    { name: "Stream C", amount: 2500 },
];

// Calculate rewards
try {
    const rewards = calculateRewards(holders, revenueStreams);
    console.log("Rewards Distribution:", rewards);
} catch (error) {
    console.error("Failed to calculate rewards:", error.message);
}
```
