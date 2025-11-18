"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoallstars-launch.web.app
Prompt: Create a JavaScript function using ethers.js to calculate dynamic APY rewards for $STARS token staking during the presale phase.
Generated: DETERMINISTIC_0d6b5667682c32d5
Batch ID: 20250612_154307
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import ethers.js library
const { ethers } = require('ethers');

/**
 * Calculates the dynamic Annual Percentage Yield (APY) rewards for $STARS token staking.
 * 
 * @param {string} stakingContractAddress - The address of the staking contract.
 * @param {string} userAddress - The address of the user staking $STARS tokens.
 * @param {number} durationDays - The duration in days for which to calculate APY.
 * @param {number} totalStaked - The total amount of $STARS tokens staked.
 * @param {number} presaleRate - The dynamic APY rate during the presale phase.
 * @returns {Promise<number>} - The calculated APY rewards in $STARS tokens.
 */
async function calculateDynamicAPY(stakingContractAddress, userAddress, durationDays, totalStaked, presaleRate) {
    // Validate input parameters
    if (!ethers.utils.isAddress(stakingContractAddress)) {
        throw new Error("Invalid staking contract address.");
    }
    if (!ethers.utils.isAddress(userAddress)) {
        throw new Error("Invalid user address.");
    }
    if (durationDays <= 0) {
        throw new Error("Duration must be greater than 0 days.");
    }
    if (totalStaked <= 0) {
        throw new Error("Total staked amount must be greater than 0.");
    }
    if (presaleRate < 0) {
        throw new Error("Presale rate cannot be negative.");
    }

    // Calculate the yearly reward based on user stake and presale APY rate
    const dailyRate = presaleRate / 365; // Convert APY to daily rate
    const rewards = (totalStaked * dailyRate * durationDays) / 100; // APY calculation

    // Return the calculated rewards
    return rewards;
}

// Example usage (should be replaced with actual contract and user addresses):
(async () => {
    try {
        const stakingContractAddress = '0xYourStakingContractAddress';
        const userAddress = '0xYourUserAddress';
        const durationDays = 30; // Example duration
        const totalStaked = ethers.utils.parseUnits('100', 18); // Example total staked
        const presaleRate = 20; // Example presale APY rate in percentage

        const rewards = await calculateDynamicAPY(stakingContractAddress, userAddress, durationDays, totalStaked, presaleRate);
        console.log(`Calculated APY rewards in $STARS: ${ethers.utils.formatUnits(rewards, 18)}`);
    } catch (error) {
        console.error(`Error calculating APY rewards: ${error.message}`);
    }
})();
```
