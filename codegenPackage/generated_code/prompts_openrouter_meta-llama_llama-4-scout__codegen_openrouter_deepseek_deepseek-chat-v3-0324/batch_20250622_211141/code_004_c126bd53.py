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
 * YieldETHLiquidStakingToken - A class representing a liquid staking token with an increasing exchange rate mechanism.
 * This token allows users to stake ETH and receive a liquid staking token (LST) in return.
 * The exchange rate between ETH and LST increases over time as staking rewards accumulate.
 */
class YieldETHLiquidStakingToken {
  /**
   * @param {string} name - The name of the token
   * @param {string} symbol - The symbol of the token
   * @param {number} initialExchangeRate - Initial exchange rate (LST per ETH)
   */
  constructor(name, symbol, initialExchangeRate) {
    this.name = name;
    this.symbol = symbol;
    this.totalStakedETH = 0;
    this.totalSupply = 0;
    this.exchangeRate = initialExchangeRate;
    this.lastUpdateTimestamp = Date.now();
    this.stakers = new Map(); // Maps addresses to their staked ETH balance
  }

  /**
   * Updates the exchange rate based on time elapsed and rewards earned
   * @param {number} annualRewardRate - Annual reward rate (e.g., 0.05 for 5%)
   */
  _updateExchangeRate(annualRewardRate) {
    const now = Date.now();
    const timeElapsed = (now - this.lastUpdateTimestamp) / (1000 * 60 * 60 * 24 * 365); // Convert to years
    if (timeElapsed <= 0) return;

    // Calculate the new exchange rate based on time elapsed and reward rate
    const rewardFactor = 1 + annualRewardRate * timeElapsed;
    this.exchangeRate *= rewardFactor;
    this.lastUpdateTimestamp = now;
  }

  /**
   * Stakes ETH and mints LST tokens
   * @param {string} stakerAddress - The address of the staker
   * @param {number} ethAmount - Amount of ETH to stake
   * @param {number} annualRewardRate - Annual reward rate
   * @returns {number} Amount of LST tokens minted
   */
  stakeETH(stakerAddress, ethAmount, annualRewardRate) {
    if (ethAmount <= 0) {
      throw new Error("ETH amount must be positive");
    }

    this._updateExchangeRate(annualRewardRate);

    // Calculate LST amount based on current exchange rate
    const lstAmount = ethAmount * this.exchangeRate;

    // Update balances
    this.totalStakedETH += ethAmount;
    this.totalSupply += lstAmount;
    this.stakers.set(stakerAddress, (this.stakers.get(stakerAddress) || 0) + ethAmount);

    return lstAmount;
  }

  /**
   * Unstakes ETH by burning LST tokens
   * @param {string} stakerAddress - The address of the staker
   * @param {number} lstAmount - Amount of LST tokens to burn
   * @param {number} annualRewardRate - Annual reward rate
   * @returns {number} Amount of ETH returned
   */
  unstakeETH(stakerAddress, lstAmount, annualRewardRate) {
    if (lstAmount <= 0) {
      throw new Error("LST amount must be positive");
    }

    this._updateExchangeRate(annualRewardRate);

    // Calculate ETH amount based on current exchange rate
    const ethAmount = lstAmount / this.exchangeRate;

    // Check if staker has enough ETH staked
    const stakedETH = this.stakers.get(stakerAddress) || 0;
    if (ethAmount > stakedETH) {
      throw new Error("Insufficient staked ETH balance");
    }

    // Update balances
    this.totalStakedETH -= ethAmount;
    this.totalSupply -= lstAmount;
    this.stakers.set(stakerAddress, stakedETH - ethAmount);

    return ethAmount;
  }

  /**
   * Gets the current exchange rate (LST per ETH)
   * @returns {number} Current exchange rate
   */
  getExchangeRate() {
    return this.exchangeRate;
  }

  /**
   * Gets the staked ETH balance for an address
   * @param {string} stakerAddress - The address to query
   * @returns {number} Staked ETH balance
   */
  getStakedBalance(stakerAddress) {
    return this.stakers.get(stakerAddress) || 0;
  }

  /**
   * Gets the LST balance for an address (calculated from staked ETH)
   * @param {string} stakerAddress - The address to query
   * @returns {number} LST balance
   */
  getLSTBalance(stakerAddress) {
    const stakedETH = this.stakers.get(stakerAddress) || 0;
    return stakedETH * this.exchangeRate;
  }
}

// Example usage
const main = () => {
  try {
    // Initialize with initial exchange rate of 1 LST = 1 ETH
    const lst = new YieldETHLiquidStakingToken("YieldETH", "yETH", 1.0);
    const annualRewardRate = 0.05; // 5% annual reward rate

    // Alice stakes 10 ETH
    const aliceAddress = "0xAlice";
    const aliceStakeAmount = 10;
    const aliceLST = lst.stakeETH(aliceAddress, aliceStakeAmount, annualRewardRate);
    console.log(`Alice staked ${aliceStakeAmount} ETH and received ${aliceLST} yETH`);
    console.log(`Current exchange rate: ${lst.getExchangeRate()} yETH/ETH`);

    // Simulate time passing (1 year)
    console.log("\n1 year later...");
    lst._updateExchangeRate(annualRewardRate); // Force update exchange rate

    // Bob stakes 5 ETH
    const bobAddress = "0xBob";
    const bobStakeAmount = 5;
    const bobLST = lst.stakeETH(bobAddress, bobStakeAmount, annualRewardRate);
    console.log(`Bob staked ${bobStakeAmount} ETH and received ${bobLST} yETH`);
    console.log(`Current exchange rate: ${lst.getExchangeRate()} yETH/ETH`);

    // Check balances
    console.log("\nBalances:");
    console.log(`Alice staked ETH: ${lst.getStakedBalance(aliceAddress)}`);
    console.log(`Alice yETH balance: ${lst.getLSTBalance(aliceAddress)}`);
    console.log(`Bob staked ETH: ${lst.getStakedBalance(bobAddress)}`);
    console.log(`Bob yETH balance: ${lst.getLSTBalance(bobAddress)}`);

    // Alice unstakes half her position
    console.log("\nAlice unstakes half her position...");
    const aliceUnstakeAmount = lst.getLSTBalance(aliceAddress) / 2;
    const aliceReceivedETH = lst.unstakeETH(aliceAddress, aliceUnstakeAmount, annualRewardRate);
    console.log(`Alice received ${aliceReceivedETH} ETH by burning ${aliceUnstakeAmount} yETH`);
    console.log(`Current exchange rate: ${lst.getExchangeRate()} yETH/ETH`);

    // Final balances
    console.log("\nFinal balances:");
    console.log(`Alice staked ETH: ${lst.getStakedBalance(aliceAddress)}`);
    console.log(`Alice yETH balance: ${lst.getLSTBalance(aliceAddress)}`);
    console.log(`Bob staked ETH: ${lst.getStakedBalance(bobAddress)}`);
    console.log(`Bob yETH balance: ${lst.getLSTBalance(bobAddress)}`);
    console.log(`Total staked ETH: ${lst.totalStakedETH}`);
    console.log(`Total yETH supply: ${lst.totalSupply}`);

  } catch (error) {
    console.error("Error:", error.message);
  }
};

main();
```
