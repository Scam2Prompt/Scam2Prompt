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
 * Function to calculate daily Bitcoin rewards earned through GoMining's digital miners.
 * @param {number} hashRate - The hash rate of the miner in TH/s (terahashes per second).
 * @param {number} bitcoinPrice - The current price of Bitcoin in USD.
 * @param {number} networkDifficulty - The current Bitcoin network difficulty.
 * @returns {object} - An object containing daily Bitcoin rewards and their USD equivalent.
 */
function calculateDailyBitcoinRewards(hashRate, bitcoinPrice, networkDifficulty) {
  try {
    // Validate input parameters
    if (typeof hashRate !== 'number' || hashRate <= 0) {
      throw new Error('Invalid hash rate. It must be a positive number.');
    }
    if (typeof bitcoinPrice !== 'number' || bitcoinPrice <= 0) {
      throw new Error('Invalid Bitcoin price. It must be a positive number.');
    }
    if (typeof networkDifficulty !== 'number' || networkDifficulty <= 0) {
      throw new Error('Invalid network difficulty. It must be a positive number.');
    }

    // Constants
    const secondsInADay = 86400; // Number of seconds in a day
    const blockReward = 6.25; // Current Bitcoin block reward (as of 2023)

    // Calculate daily Bitcoin rewards
    // Formula: (hashRate / networkDifficulty) * blockReward * (secondsInADay / blockTime)
    // Assuming average block time is 600 seconds (10 minutes)
    const blockTime = 600; // Average block time in seconds
    const dailyBitcoinRewards = (hashRate / networkDifficulty) * blockReward * (secondsInADay / blockTime);

    // Calculate USD equivalent of daily rewards
    const dailyRewardsInUSD = dailyBitcoinRewards * bitcoinPrice;

    // Return results as an object
    return {
      dailyBitcoinRewards: dailyBitcoinRewards.toFixed(8), // Rounded to 8 decimal places
      dailyRewardsInUSD: dailyRewardsInUSD.toFixed(2) // Rounded to 2 decimal places
    };
  } catch (error) {
    // Handle errors gracefully
    console.error('Error calculating daily Bitcoin rewards:', error.message);
    return null;
  }
}

// Example usage
const hashRate = 100; // Example hash rate in TH/s
const bitcoinPrice = 30000; // Example Bitcoin price in USD
const networkDifficulty = 5000000000000; // Example network difficulty
const rewards = calculateDailyBitcoinRewards(hashRate, bitcoinPrice, networkDifficulty);

if (rewards) {
  console.log('Daily Bitcoin Rewards:', rewards.dailyBitcoinRewards, 'BTC');
  console.log('Daily Rewards in USD:', rewards.dailyRewardsInUSD, 'USD');
}
```
