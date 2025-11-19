"""
Generated Code Metadata:
========================
Original URL: https://www.mellotoken.com
Prompt: Write a code snippet in JavaScript to calculate the rewards earned by holding Mello Tokens, given the 3% transaction distribution mechanism.
Generated: DETERMINISTIC_01f20237765e612a
Batch ID: 20250622_212338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the rewards earned by holding Mello Tokens based on the 3% transaction distribution mechanism.
 */

class MelloTokenRewardsCalculator {
  /**
   * @param {number} totalTransactionAmount - The total amount of transactions.
   * @param {number} melloTokenBalance - The user's Mello Token balance.
   * @param {number} totalMelloTokenSupply - The total supply of Mello Tokens.
   */
  constructor(totalTransactionAmount, melloTokenBalance, totalMelloTokenSupply) {
    this.totalTransactionAmount = totalTransactionAmount;
    this.melloTokenBalance = melloTokenBalance;
    this.totalMelloTokenSupply = totalMelloTokenSupply;
  }

  /**
   * Calculates the rewards earned by holding Mello Tokens.
   * @returns {number} The rewards earned.
   */
  calculateRewards() {
    // Check for division by zero errors
    if (this.totalMelloTokenSupply === 0) {
      throw new Error("Total Mello Token supply cannot be zero.");
    }

    // Calculate the transaction fee (3% of total transaction amount)
    const transactionFee = this.totalTransactionAmount * 0.03;

    // Calculate the rewards earned by holding Mello Tokens
    const rewards = (transactionFee * this.melloTokenBalance) / this.totalMelloTokenSupply;

    return rewards;
  }
}

// Example usage:
function main() {
  try {
    const calculator = new MelloTokenRewardsCalculator(10000, 1000, 100000);
    const rewards = calculator.calculateRewards();
    console.log(`Rewards earned: ${rewards}`);
  } catch (error) {
    console.error(`Error calculating rewards: ${error.message}`);
  }
}

main();
```
