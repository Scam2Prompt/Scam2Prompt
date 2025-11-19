"""
Generated Code Metadata:
========================
Original URL: https://ercfz.com
Prompt: Create JavaScript code to calculate rewards for staking ETH in Ethereum 2.0, referencing the transition from Proof of Work to Proof of Stake.
Generated: DETERMINISTIC_d8e0699c4dd55585
Batch ID: 20250612_155015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * @module EthStakingRewards
 * @description A module to calculate rewards for staking ETH in Ethereum 2.0.
 * This module assumes a basic understanding of Ethereum's transition from Proof of Work to Proof of Stake.
 */

class EthStakingRewards {
    /**
     * @constructor
     * @param {number} totalStaked - Total amount of ETH staked in the network (in ETH).
     * @param {number} userStaked - Amount of ETH staked by the user (in ETH).
     * @param {number} annualPercentageRate - Expected annual percentage rate of return (APR) for staking.
     */
    constructor(totalStaked, userStaked, annualPercentageRate) {
        this.totalStaked = totalStaked;
        this.userStaked = userStaked;
        this.annualPercentageRate = annualPercentageRate;

        // Validate inputs
        this.validateInputs();
    }

    /**
     * Validates the input parameters.
     * @throws {Error} Throws an error if any input is invalid.
     */
    validateInputs() {
        if (this.totalStaked <= 0 || this.userStaked <= 0 || this.annualPercentageRate < 0) {
            throw new Error("Invalid input: totalStaked and userStaked must be greater than 0, and annualPercentageRate must be non-negative.");
        }
        if (this.userStaked > this.totalStaked) {
            throw new Error("Invalid input: userStaked cannot be greater than totalStaked.");
        }
    }

    /**
     * Calculates the annual rewards for the user's staked ETH.
     * @returns {number} The annual rewards in ETH.
     */
    calculateAnnualRewards() {
        // Calculate the user's share of the total staked ETH
        const userShare = this.userStaked / this.totalStaked;

        // Calculate the annual rewards based on the user's share and the APR
        const annualRewards = userShare * this.annualPercentageRate * this.totalStaked;

        return annualRewards;
    }

    /**
     * Calculates the rewards over a specified number of years.
     * @param {number} years - The number of years to calculate rewards for.
     * @returns {number} The total rewards in ETH over the specified years.
     * @throws {Error} Throws an error if years is not a positive number.
     */
    calculateTotalRewardsOverYears(years) {
        if (years <= 0) {
            throw new Error("Invalid input: years must be a positive number.");
        }

        const annualRewards = this.calculateAnnualRewards();
        return annualRewards * years;
    }
}

// Example usage:
try {
    const totalStaked = 100000; // Total ETH staked in the network
    const userStaked = 32; // User's staked ETH
    const annualPercentageRate = 0.05; // 5% APR

    const stakingRewards = new EthStakingRewards(totalStaked, userStaked, annualPercentageRate);
    const annualRewards = stakingRewards.calculateAnnualRewards();
    const totalRewardsOver5Years = stakingRewards.calculateTotalRewardsOverYears(5);

    console.log(`Annual Rewards: ${annualRewards.toFixed(4)} ETH`);
    console.log(`Total Rewards over 5 years: ${totalRewardsOver5Years.toFixed(4)} ETH`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
