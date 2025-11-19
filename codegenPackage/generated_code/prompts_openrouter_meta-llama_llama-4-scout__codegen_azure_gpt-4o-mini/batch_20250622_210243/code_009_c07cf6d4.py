"""
Generated Code Metadata:
========================
Original URL: https://ordifypro.pages.dev
Prompt: "Write a script in JavaScript to calculate and display the vesting schedule for Ordify's token allocation, given the provided tokenomics data."
Generated: DETERMINISTIC_c07cf6d4752fb29b
Batch ID: 20250622_210243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Vesting Schedule Calculator for Ordify's Token Allocation
 * 
 * This script calculates and displays the vesting schedule based on the provided tokenomics data.
 * 
 * Tokenomics data structure:
 * {
 *   totalSupply: Number, // Total tokens allocated
 *   cliffDuration: Number, // Duration of the cliff in months
 *   vestingDuration: Number, // Total vesting duration in months
 *   monthlyVestingAmount: Number // Amount of tokens vested each month after the cliff
 * }
 */

class VestingSchedule {
    constructor(tokenomics) {
        this.totalSupply = tokenomics.totalSupply;
        this.cliffDuration = tokenomics.cliffDuration;
        this.vestingDuration = tokenomics.vestingDuration;
        this.monthlyVestingAmount = tokenomics.monthlyVestingAmount;

        // Validate input data
        this.validateTokenomics();
    }

    /**
     * Validates the tokenomics data to ensure all required fields are present and valid.
     * @throws Will throw an error if validation fails.
     */
    validateTokenomics() {
        if (typeof this.totalSupply !== 'number' || this.totalSupply <= 0) {
            throw new Error('Invalid totalSupply: must be a positive number.');
        }
        if (typeof this.cliffDuration !== 'number' || this.cliffDuration < 0) {
            throw new Error('Invalid cliffDuration: must be a non-negative number.');
        }
        if (typeof this.vestingDuration !== 'number' || this.vestingDuration <= 0) {
            throw new Error('Invalid vestingDuration: must be a positive number.');
        }
        if (typeof this.monthlyVestingAmount !== 'number' || this.monthlyVestingAmount <= 0) {
            throw new Error('Invalid monthlyVestingAmount: must be a positive number.');
        }
        if (this.cliffDuration + this.vestingDuration > 12) {
            throw new Error('Total duration (cliff + vesting) cannot exceed 12 months.');
        }
    }

    /**
     * Calculates the vesting schedule.
     * @returns {Array} An array of objects representing the vesting schedule.
     */
    calculateVestingSchedule() {
        const schedule = [];
        const totalVestingMonths = this.cliffDuration + this.vestingDuration;

        for (let month = 1; month <= totalVestingMonths; month++) {
            let vestedAmount = 0;

            if (month > this.cliffDuration) {
                vestedAmount = this.monthlyVestingAmount * (month - this.cliffDuration);
                // Ensure we do not exceed total supply
                vestedAmount = Math.min(vestedAmount, this.totalSupply);
            }

            schedule.push({
                month: month,
                vestedAmount: vestedAmount,
                totalVested: Math.min(vestedAmount, this.totalSupply)
            });
        }

        return schedule;
    }

    /**
     * Displays the vesting schedule in a readable format.
     */
    displayVestingSchedule() {
        const schedule = this.calculateVestingSchedule();
        console.log('Vesting Schedule:');
        console.log('Month | Vested Amount | Total Vested');
        console.log('--------------------------------------');

        schedule.forEach(entry => {
            console.log(`${entry.month.toString().padStart(5)} | ${entry.vestedAmount.toString().padStart(13)} | ${entry.totalVested.toString().padStart(12)}`);
        });
    }
}

// Example tokenomics data
const tokenomicsData = {
    totalSupply: 1000000, // Total tokens allocated
    cliffDuration: 3, // Duration of the cliff in months
    vestingDuration: 9, // Total vesting duration in months
    monthlyVestingAmount: 10000 // Amount of tokens vested each month after the cliff
};

// Create a new VestingSchedule instance and display the schedule
try {
    const vestingSchedule = new VestingSchedule(tokenomicsData);
    vestingSchedule.displayVestingSchedule();
} catch (error) {
    console.error('Error calculating vesting schedule:', error.message);
}
```
