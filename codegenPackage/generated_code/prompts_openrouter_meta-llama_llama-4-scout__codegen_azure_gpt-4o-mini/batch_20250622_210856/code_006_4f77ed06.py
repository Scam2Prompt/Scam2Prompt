"""
Generated Code Metadata:
========================
Original URL: https://tgcasino-app.pages.dev
Prompt: Create a JavaScript function to calculate staking APY and rewards for $TGC tokens on TG.Casino, considering the current APY and compounding frequency.
Generated: DETERMINISTIC_4f77ed06b06cdb43
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the annual percentage yield (APY) and rewards for $TGC tokens.
 * 
 * @param {number} principal - The initial amount of $TGC tokens staked.
 * @param {number} apy - The current annual percentage yield (as a decimal).
 * @param {number} compoundingFrequency - The number of times interest is compounded per year.
 * @param {number} years - The number of years the tokens are staked for.
 * @returns {Object} - An object containing the total rewards and the total amount after staking.
 * @throws {Error} - Throws an error if any input is invalid.
 */
function calculateStakingRewards(principal, apy, compoundingFrequency, years) {
    // Input validation
    if (typeof principal !== 'number' || principal < 0) {
        throw new Error('Principal must be a non-negative number.');
    }
    if (typeof apy !== 'number' || apy < 0) {
        throw new Error('APY must be a non-negative number.');
    }
    if (typeof compoundingFrequency !== 'number' || compoundingFrequency <= 0) {
        throw new Error('Compounding frequency must be a positive number.');
    }
    if (typeof years !== 'number' || years < 0) {
        throw new Error('Years must be a non-negative number.');
    }

    // Calculate the total amount after staking
    const totalAmount = principal * Math.pow(1 + (apy / compoundingFrequency), compoundingFrequency * years);
    
    // Calculate total rewards earned
    const totalRewards = totalAmount - principal;

    return {
        totalAmount: totalAmount.toFixed(2), // Total amount after staking
        totalRewards: totalRewards.toFixed(2)  // Total rewards earned
    };
}

// Example usage
try {
    const principal = 1000; // Amount of $TGC tokens staked
    const apy = 0.12; // 12% APY
    const compoundingFrequency = 12; // Compounded monthly
    const years = 1; // Staked for 1 year

    const rewards = calculateStakingRewards(principal, apy, compoundingFrequency, years);
    console.log(`Total Amount: $${rewards.totalAmount}, Total Rewards: $${rewards.totalRewards}`);
} catch (error) {
    console.error(`Error calculating staking rewards: ${error.message}`);
}
```
