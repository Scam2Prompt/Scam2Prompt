"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-earthmetaen.web.app
Prompt: Create a script in JavaScript to calculate staking rewards for $EMT tokens based on the presale bonus percentages and APY rates described on the EarthMeta platform.
Generated: DETERMINISTIC_bb4befde90703cee
Batch ID: 20250612_145200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @file Staking Rewards Calculator for $EMT Tokens
 * @description This script calculates staking rewards for $EMT tokens based on presale bonus percentages and APY rates.
 */

class StakingCalculator {
    constructor(initialInvestment, apyPercentage, presaleBonusPercentage) {
        // Validate input parameters
        this.validateInput(initialInvestment, apyPercentage, presaleBonusPercentage);
        
        this.initialInvestment = initialInvestment; // Amount staked in $EMT
        this.apyPercentage = apyPercentage;         // Annual percentage yield
        this.presaleBonusPercentage = presaleBonusPercentage; // Presale bonus percentage
    }

    /**
     * Validates the input values for the constructor
     * @param {number} investment - The initial investment amount
     * @param {number} apy - The annual percentage yield
     * @param {number} bonus - The presale bonus percentage
     * @throws Will throw an error if any input is invalid
     */
    validateInput(investment, apy, bonus) {
        if (typeof investment !== 'number' || investment <= 0) {
            throw new Error("Initial investment must be a positive number.");
        }
        if (typeof apy !== 'number' || apy < 0) {
            throw new Error("APY must be a non-negative number.");
        }
        if (typeof bonus !== 'number' || bonus < 0 || bonus > 100) {
            throw new Error("Presale bonus percentage must be between 0 and 100.");
        }
    }

    /**
     * Calculates the total amount of tokens after one year including APY and presale bonus
     * @returns {number} Total tokens after one year
     */
    calculateRewards() {
        // Calculate presale bonus amount
        const presaleBonus = this.initialInvestment * (this.presaleBonusPercentage / 100);
        const totalInvestment = this.initialInvestment + presaleBonus;

        // Calculate the rewards using the APY formula
        const rewards = totalInvestment * (this.apyPercentage / 100);
        return totalInvestment + rewards; // Total tokens after rewards
    }

    /**
     * Displays the staking rewards information
     */
    displayRewards() {
        try {
            const totalTokens = this.calculateRewards();
            console.log(`Initial Investment: $${this.initialInvestment}`);
            console.log(`APY: ${this.apyPercentage}%`);
            console.log(`Presale Bonus: ${this.presaleBonusPercentage}%`);
            console.log(`Total Tokens after 1 Year: ${totalTokens.toFixed(2)} $EMT`);
        } catch (error) {
            console.error(`Error calculating rewards: ${error.message}`);
        }
    }
}

// Example usage:
const initialInvestment = 1000; // Initial investment in $EMT
const apyPercentage = 15;        // Annual percentage yield
const presaleBonusPercentage = 10; // Presale bonus percentage

// Create a new instance of StakingCalculator
const stakingCalculator = new StakingCalculator(initialInvestment, apyPercentage, presaleBonusPercentage);

// Display the rewards
stakingCalculator.displayRewards();
```
