"""
Generated Code Metadata:
========================
Original URL: https://earthmeta-aijko.pages.dev
Prompt: Generate a staking rewards calculator in JavaScript that predicts the rewards for staking $EMT tokens on the EarthMeta platform, based on the provided staking calculator formula.
Generated: DETERMINISTIC_cac00f668c729964
Batch ID: 20250622_211557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * EMT Staking Rewards Calculator for EarthMeta Platform
 * 
 * This calculator predicts the rewards for staking EMT tokens based on:
 * - Principal amount
 * - Annual Percentage Yield (APY)
 * - Staking duration in days
 * - Compound frequency (optional)
 */

class StakingRewardsCalculator {
    /**
     * Initialize the calculator with default values
     */
    constructor() {
        this.principal = 0;
        this.apy = 0;
        this.durationDays = 0;
        this.compoundFrequency = 1; // Default: annual compounding
    }

    /**
     * Set the principal amount to be staked
     * @param {number} amount - Principal amount in EMT tokens
     * @throws {Error} If amount is not a positive number
     */
    setPrincipal(amount) {
        if (typeof amount !== 'number' || amount <= 0) {
            throw new Error('Principal must be a positive number');
        }
        this.principal = amount;
    }

    /**
     * Set the Annual Percentage Yield (APY)
     * @param {number} apy - APY as a percentage (e.g., 5 for 5%)
     * @throws {Error} If APY is not a positive number
     */
    setAPY(apy) {
        if (typeof apy !== 'number' || apy <= 0) {
            throw new Error('APY must be a positive number');
        }
        this.apy = apy;
    }

    /**
     * Set the staking duration in days
     * @param {number} days - Duration in days
     * @throws {Error} If duration is not a positive number
     */
    setDuration(days) {
        if (typeof days !== 'number' || days <= 0) {
            throw new Error('Duration must be a positive number');
        }
        this.durationDays = days;
    }

    /**
     * Set the compound frequency (times per year)
     * @param {number} frequency - Compound frequency (e.g., 12 for monthly)
     * @throws {Error} If frequency is not a positive integer
     */
    setCompoundFrequency(frequency) {
        if (typeof frequency !== 'number' || frequency <= 0 || !Number.isInteger(frequency)) {
            throw new Error('Compound frequency must be a positive integer');
        }
        this.compoundFrequency = frequency;
    }

    /**
     * Calculate the staking rewards
     * @returns {Object} Contains total balance and rewards earned
     */
    calculate() {
        if (this.principal <= 0 || this.apy <= 0 || this.durationDays <= 0) {
            throw new Error('Principal, APY, and duration must be set to positive values');
        }

        const years = this.durationDays / 365;
        const rate = this.apy / 100;
        
        // Compound interest formula: A = P * (1 + r/n)^(n*t)
        const compoundFactor = Math.pow(1 + (rate / this.compoundFrequency), this.compoundFrequency * years);
        const totalBalance = this.principal * compoundFactor;
        const rewardsEarned = totalBalance - this.principal;

        return {
            principal: this.principal,
            apy: this.apy,
            durationDays: this.durationDays,
            compoundFrequency: this.compoundFrequency,
            totalBalance: parseFloat(totalBalance.toFixed(6)), // Round to 6 decimal places
            rewardsEarned: parseFloat(rewardsEarned.toFixed(6))
        };
    }

    /**
     * Calculate simple interest (non-compounding) rewards
     * @returns {Object} Contains total balance and rewards earned
     */
    calculateSimpleInterest() {
        if (this.principal <= 0 || this.apy <= 0 || this.durationDays <= 0) {
            throw new Error('Principal, APY, and duration must be set to positive values');
        }

        const years = this.durationDays / 365;
        const rate = this.apy / 100;
        
        // Simple interest formula: A = P * (1 + r*t)
        const totalBalance = this.principal * (1 + rate * years);
        const rewardsEarned = totalBalance - this.principal;

        return {
            principal: this.principal,
            apy: this.apy,
            durationDays: this.durationDays,
            totalBalance: parseFloat(totalBalance.toFixed(6)),
            rewardsEarned: parseFloat(rewardsEarned.toFixed(6))
        };
    }
}

// Export for Node.js environment if module exists
if (typeof module !== 'undefined' && module.exports) {
    module.exports = StakingRewardsCalculator;
}
```
