"""
Generated Code Metadata:
========================
Original URL: https://claim-scottytheai.web.app
Prompt: "Create a simple staking calculator in JavaScript for $SCOTTY tokens, considering the APY and lock period for reward multipliers."
Generated: DETERMINISTIC_b57b2c1856b7b152
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Staking Calculator for $SCOTTY Tokens
 * This calculator computes the potential rewards based on the amount staked,
 * the Annual Percentage Yield (APY), and the lock period for reward multipliers.
 */

class StakingCalculator {
    /**
     * Constructor for the StakingCalculator class.
     * @param {number} amount - The amount of $SCOTTY tokens to stake.
     * @param {number} apy - The annual percentage yield (in percentage).
     * @param {number} lockPeriod - The lock period in months.
     */
    constructor(amount, apy, lockPeriod) {
        this.amount = amount;
        this.apy = apy;
        this.lockPeriod = lockPeriod;

        // Validate inputs
        this.validateInputs();
    }

    /**
     * Validates the input parameters.
     * @throws Will throw an error if any input is invalid.
     */
    validateInputs() {
        if (typeof this.amount !== 'number' || this.amount <= 0) {
            throw new Error('Amount must be a positive number.');
        }
        if (typeof this.apy !== 'number' || this.apy < 0) {
            throw new Error('APY must be a non-negative number.');
        }
        if (typeof this.lockPeriod !== 'number' || this.lockPeriod <= 0) {
            throw new Error('Lock period must be a positive number.');
        }
    }

    /**
     * Calculates the total rewards based on the staking parameters.
     * @returns {number} The total rewards earned after the lock period.
     */
    calculateRewards() {
        // Convert APY from percentage to decimal
        const apyDecimal = this.apy / 100;

        // Calculate the total rewards using the formula for compound interest
        const totalRewards = this.amount * Math.pow((1 + apyDecimal / 12), this.lockPeriod) - this.amount;

        return totalRewards;
    }

    /**
     * Displays the staking summary including the initial amount, total rewards, and final amount.
     */
    displaySummary() {
        const totalRewards = this.calculateRewards();
        const finalAmount = this.amount + totalRewards;

        console.log(`Staking Summary for $SCOTTY Tokens:`);
        console.log(`-------------------------------------`);
        console.log(`Initial Amount: $${this.amount.toFixed(2)}`);
        console.log(`APY: ${this.apy}%`);
        console.log(`Lock Period: ${this.lockPeriod} months`);
        console.log(`Total Rewards: $${totalRewards.toFixed(2)}`);
        console.log(`Final Amount after Lock Period: $${finalAmount.toFixed(2)}`);
    }
}

// Example usage:
try {
    const stakingCalculator = new StakingCalculator(1000, 12, 6);
    stakingCalculator.displaySummary();
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
