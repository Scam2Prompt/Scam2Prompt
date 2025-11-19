"""
Generated Code Metadata:
========================
Original URL: https://yieldeth.org
Prompt: "Explain how yieldETH's liquid staking token works, including its increasing exchange rate mechanism, and provide a code example in JavaScript to demonstrate the concept."
Generated: DETERMINISTIC_c126bd53b1f91352
Batch ID: 20250622_211141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Liquid Staking Token Example
 * 
 * This code demonstrates the concept of a liquid staking token with an increasing exchange rate mechanism.
 * The exchange rate increases over time as rewards are accrued, simulating the behavior of a staking system.
 * 
 * Key Concepts:
 * - `exchangeRate`: Represents the amount of staked ETH backing each liquid staking token.
 * - `totalStakedETH`: Tracks the total ETH staked in the system.
 * - `totalSupply`: Tracks the total supply of liquid staking tokens.
 * - Rewards increase the `totalStakedETH`, which in turn increases the `exchangeRate`.
 */

class LiquidStakingToken {
  constructor() {
    this.totalStakedETH = 0; // Total ETH staked in the system
    this.totalSupply = 0; // Total supply of liquid staking tokens
    this.exchangeRate = 1; // Initial exchange rate (1 token = 1 ETH)
  }

  /**
   * Stake ETH and mint liquid staking tokens.
   * @param {number} ethAmount - Amount of ETH to stake.
   * @returns {number} - Amount of liquid staking tokens minted.
   */
  stakeETH(ethAmount) {
    if (ethAmount <= 0) {
      throw new Error("Stake amount must be greater than zero.");
    }

    // Calculate the number of tokens to mint based on the current exchange rate
    const tokensToMint = ethAmount / this.exchangeRate;

    // Update system state
    this.totalStakedETH += ethAmount;
    this.totalSupply += tokensToMint;

    return tokensToMint;
  }

  /**
   * Simulate rewards being added to the staking pool.
   * @param {number} rewardAmount - Amount of ETH rewards to add.
   */
  addRewards(rewardAmount) {
    if (rewardAmount <= 0) {
      throw new Error("Reward amount must be greater than zero.");
    }

    // Add rewards to the total staked ETH
    this.totalStakedETH += rewardAmount;

    // Update the exchange rate based on the new total staked ETH
    this.exchangeRate = this.totalStakedETH / this.totalSupply;
  }

  /**
   * Get the current exchange rate (ETH per token).
   * @returns {number} - Current exchange rate.
   */
  getExchangeRate() {
    return this.exchangeRate;
  }

  /**
   * Redeem liquid staking tokens for ETH.
   * @param {number} tokenAmount - Amount of tokens to redeem.
   * @returns {number} - Amount of ETH received.
   */
  redeemTokens(tokenAmount) {
    if (tokenAmount <= 0) {
      throw new Error("Redeem amount must be greater than zero.");
    }
    if (tokenAmount > this.totalSupply) {
      throw new Error("Insufficient token supply for redemption.");
    }

    // Calculate the amount of ETH to return based on the current exchange rate
    const ethToReturn = tokenAmount * this.exchangeRate;

    // Update system state
    this.totalSupply -= tokenAmount;
    this.totalStakedETH -= ethToReturn;

    return ethToReturn;
  }
}

// Example Usage
try {
  const stakingToken = new LiquidStakingToken();

  // Stake 10 ETH
  const mintedTokens = stakingToken.stakeETH(10);
  console.log(`Minted Tokens: ${mintedTokens}`);
  console.log(`Exchange Rate: ${stakingToken.getExchangeRate()}`);

  // Add 2 ETH as rewards
  stakingToken.addRewards(2);
  console.log(`Exchange Rate after rewards: ${stakingToken.getExchangeRate()}`);

  // Redeem 5 tokens
  const redeemedETH = stakingToken.redeemTokens(5);
  console.log(`Redeemed ETH: ${redeemedETH}`);
  console.log(`Exchange Rate after redemption: ${stakingToken.getExchangeRate()}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
