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
 * Represents a liquid staking token, similar to yieldETH.
 */
class LiquidStakingToken {
  /**
   * Initializes the liquid staking token with an initial exchange rate of 1:1.
   */
  constructor() {
    // Initial exchange rate is 1:1 (1 staked ETH = 1 liquid staking token)
    this.exchangeRate = 1;
    // Total staked ETH
    this.totalStakedEth = 0;
    // Total liquid staking tokens minted
    this.totalTokensMinted = 0;
  }

  /**
   * Stakes ETH and mints liquid staking tokens.
   * @param {number} amount - The amount of ETH to stake.
   * @returns {number} The number of liquid staking tokens minted.
   */
  stakeEth(amount) {
    // Update total staked ETH
    this.totalStakedEth += amount;
    // Calculate the number of liquid staking tokens to mint based on the current exchange rate
    const tokensToMint = amount / this.exchangeRate;
    // Update total tokens minted
    this.totalTokensMinted += tokensToMint;
    return tokensToMint;
  }

  /**
   * Unstakes ETH and burns liquid staking tokens.
   * @param {number} tokensToBurn - The number of liquid staking tokens to burn.
   * @returns {number} The amount of ETH unstaked.
   */
  unstakeEth(tokensToBurn) {
    // Check if there are enough tokens to burn
    if (tokensToBurn > this.totalTokensMinted) {
      throw new Error("Not enough tokens to burn");
    }
    // Calculate the amount of ETH to unstake based on the current exchange rate
    const ethToUnstake = tokensToBurn * this.exchangeRate;
    // Update total staked ETH
    this.totalStakedEth -= ethToUnstake;
    // Update total tokens minted
    this.totalTokensMinted -= tokensToBurn;
    return ethToUnstake;
  }

  /**
   * Increases the exchange rate, effectively increasing the value of each liquid staking token.
   * @param {number} reward - The reward in ETH to distribute to stakers.
   */
  increaseExchangeRate(reward) {
    // Calculate the new exchange rate
    const newExchangeRate = this.exchangeRate + (reward / this.totalTokensMinted);
    // Update the exchange rate
    this.exchangeRate = newExchangeRate;
  }

  /**
   * Gets the current exchange rate.
   * @returns {number} The current exchange rate.
   */
  getExchangeRate() {
    return this.exchangeRate;
  }

  /**
   * Gets the total staked ETH.
   * @returns {number} The total staked ETH.
   */
  getTotalStakedEth() {
    return this.totalStakedEth;
  }

  /**
   * Gets the total liquid staking tokens minted.
   * @returns {number} The total liquid staking tokens minted.
   */
  getTotalTokensMinted() {
    return this.totalTokensMinted;
  }
}

// Example usage:
function main() {
  try {
    const liquidStakingToken = new LiquidStakingToken();

    // Stake 10 ETH and mint liquid staking tokens
    const tokensMinted = liquidStakingToken.stakeEth(10);
    console.log(`Minted ${tokensMinted} liquid staking tokens`);

    // Increase exchange rate with a reward of 2 ETH
    liquidStakingToken.increaseExchangeRate(2);
    console.log(`New exchange rate: ${liquidStakingToken.getExchangeRate()}`);

    // Unstake 5 liquid staking tokens and get ETH
    const ethUnstaked = liquidStakingToken.unstakeEth(5);
    console.log(`Unstaked ${ethUnstaked} ETH`);

    console.log(`Total staked ETH: ${liquidStakingToken.getTotalStakedEth()}`);
    console.log(`Total liquid staking tokens minted: ${liquidStakingToken.getTotalTokensMinted()}`);
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
