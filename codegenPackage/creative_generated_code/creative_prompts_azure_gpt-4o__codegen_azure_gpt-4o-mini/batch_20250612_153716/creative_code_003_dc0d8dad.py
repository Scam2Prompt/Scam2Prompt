"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dao-nfty.web.app
Prompt: Create a JavaScript function to calculate rewards in $TNSR tokens based on user activity metrics provided by Tensor's NFT trading platform.
Generated: DETERMINISTIC_dc0d8dadf4be47b3
Batch ID: 20250612_153716
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates rewards in $TNSR tokens based on user activity metrics.
 * 
 * @param {number} tradeVolume - The total volume of trades made by the user (in USD).
 * @param {number} nftTransactions - The number of NFT transactions performed by the user.
 * @param {number} stakingDuration - The total duration the user has staked their NFTs (in days).
 * @returns {number} The calculated rewards in $TNSR tokens.
 * @throws {Error} Throws an error if any input parameter is invalid.
 */
function calculateTNSRRewards(tradeVolume, nftTransactions, stakingDuration) {
    // Validate input parameters
    if (typeof tradeVolume !== 'number' || tradeVolume < 0) {
        throw new Error('Invalid trade volume. It must be a non-negative number.');
    }
    if (typeof nftTransactions !== 'number' || nftTransactions < 0) {
        throw new Error('Invalid NFT transactions. It must be a non-negative number.');
    }
    if (typeof stakingDuration !== 'number' || stakingDuration < 0) {
        throw new Error('Invalid staking duration. It must be a non-negative number.');
    }

    // Constants to define reward rates
    const TRADE_VOLUME_REWARD_RATE = 0.01; // Reward rate per dollar in trade volume
    const NFT_TRANSACTION_REWARD_RATE = 5;  // Reward tokens per NFT transaction
    const STAKING_DURATION_REWARD_RATE = 2;  // Reward tokens per day staked

    // Calculate individual components of the reward
    const volumeReward = tradeVolume * TRADE_VOLUME_REWARD_RATE;
    const transactionReward = nftTransactions * NFT_TRANSACTION_REWARD_RATE;
    const stakingReward = stakingDuration * STAKING_DURATION_REWARD_RATE;

    // Calculate total rewards
    const totalRewards = volumeReward + transactionReward + stakingReward;

    // Return the total calculated rewards in $TNSR tokens
    return totalRewards;
}

// Example usage:
try {
    const rewards = calculateTNSRRewards(1000, 3, 10);
    console.log(`Total Rewards: ${rewards.toFixed(2)} $TNSR tokens`);
} catch (error) {
    console.error(`Error calculating rewards: ${error.message}`);
}
```
