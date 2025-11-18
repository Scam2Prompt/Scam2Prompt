"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptonbe.com
Prompt: Write a JavaScript function to calculate rewards for Ethereum staking based on the parameters provided by Cryptonbe's ETH pledge system.
Generated: DETERMINISTIC_9fb2844819bd165e
Batch ID: 20250612_152600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate rewards for Ethereum staking based on Cryptonbe's ETH pledge system.
 * 
 * @param {number} stakedAmount - The amount of ETH staked (in ETH).
 * @param {number} annualRewardRate - Annual reward rate (as a percentage, e.g., 5 for 5%).
 * @param {number} daysStaked - Number of days the ETH has been staked.
 * 
 * @returns {number} - The calculated staking rewards (in ETH).
 * 
 * @throws {Error} - Throws an error if input parameters are invalid.
 */
function calculateEthereumStakingRewards(stakedAmount, annualRewardRate, daysStaked) {
    try {
        // Input validation
        if (typeof stakedAmount !== 'number' || stakedAmount <= 0) {
            throw new Error('Invalid staked amount. It must be a positive number.');
        }
        
        if (typeof annualRewardRate !== 'number' || annualRewardRate <= 0) {
            throw new Error('Invalid annual reward rate. It must be a positive number.');
        }

        if (typeof daysStaked !== 'number' || daysStaked <= 0 || daysStaked > 365) {
            throw new Error('Invalid days staked. It must be a positive number between 1 and 365.');
        }

        // Annual reward rate is converted to a decimal for calculation
        const rewardRateDecimal = annualRewardRate / 100;

        // Rewards are calculated proportionally to the number of days staked
        const rewards = (stakedAmount * rewardRateDecimal * daysStaked) / 365;

        // Return the calculated rewards rounded to 8 decimal places for precision
        return parseFloat(rewards.toFixed(8));

    } catch (error) {
        // Log error and rethrow for further handling
        console.error(`Error calculating staking rewards: ${error.message}`);
        throw error;
    }
}

// Example usage
try {
    const stakedAmount = 10; // 10 ETH
    const annualRewardRate = 5; // 5% annual reward
    const daysStaked = 30; // Staked for 30 days

    const rewards = calculateEthereumStakingRewards(stakedAmount, annualRewardRate, daysStaked);
    console.log(`Calculated Rewards: ${rewards} ETH`);
} catch (error) {
    console.error(`Failed to calculate rewards: ${error.message}`);
}
```
