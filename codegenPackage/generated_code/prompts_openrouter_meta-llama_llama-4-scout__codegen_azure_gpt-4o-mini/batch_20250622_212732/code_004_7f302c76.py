"""
Generated Code Metadata:
========================
Original URL: https://www.gomining.site
Prompt: Create a JavaScript function to calculate the daily Bitcoin rewards earned through GoMining's digital miners, considering the miner's hash rate and the current Bitcoin price.
Generated: DETERMINISTIC_7f302c76897ba06d
Batch ID: 20250622_212732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the daily Bitcoin rewards earned through GoMining's digital miners.
 * 
 * @param {number} hashRate - The hash rate of the miner in TH/s (terahashes per second).
 * @param {number} bitcoinPrice - The current price of Bitcoin in USD.
 * @param {number} networkHashRate - The total network hash rate in TH/s (terahashes per second).
 * @param {number} blockReward - The current Bitcoin block reward in BTC.
 * @returns {number} - The daily Bitcoin rewards earned.
 * @throws {Error} - Throws an error if any input is invalid.
 */
function calculateDailyBitcoinRewards(hashRate, bitcoinPrice, networkHashRate, blockReward) {
    // Validate inputs
    if (typeof hashRate !== 'number' || hashRate <= 0) {
        throw new Error('Invalid hashRate: must be a positive number.');
    }
    if (typeof bitcoinPrice !== 'number' || bitcoinPrice <= 0) {
        throw new Error('Invalid bitcoinPrice: must be a positive number.');
    }
    if (typeof networkHashRate !== 'number' || networkHashRate <= 0) {
        throw new Error('Invalid networkHashRate: must be a positive number.');
    }
    if (typeof blockReward !== 'number' || blockReward <= 0) {
        throw new Error('Invalid blockReward: must be a positive number.');
    }

    // Calculate the miner's share of the total network hash rate
    const minerShare = hashRate / networkHashRate;

    // Calculate the daily rewards in BTC
    const dailyRewardsBTC = minerShare * blockReward * (24 * 60 * 60) / 600; // 600 seconds per block

    // Return the daily rewards in BTC
    return dailyRewardsBTC;
}

// Example usage
try {
    const hashRate = 100; // in TH/s
    const bitcoinPrice = 30000; // in USD
    const networkHashRate = 200000; // in TH/s
    const blockReward = 6.25; // in BTC

    const dailyRewards = calculateDailyBitcoinRewards(hashRate, bitcoinPrice, networkHashRate, blockReward);
    console.log(`Daily Bitcoin Rewards: ${dailyRewards} BTC`);
} catch (error) {
    console.error(`Error calculating daily Bitcoin rewards: ${error.message}`);
}
```
