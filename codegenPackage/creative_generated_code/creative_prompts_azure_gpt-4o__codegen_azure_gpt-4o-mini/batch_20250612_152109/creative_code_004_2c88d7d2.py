"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://papeairdropclaim.pages.dev
Prompt: Write JavaScript code to display the current presale progress for $PAPE, including the amount of ETH invested and the percentage of the funding goal achieved.
Generated: DETERMINISTIC_2c88d7d2b4be460d
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * PresaleProgress class to manage and display the presale progress for $PAPE.
 */
class PresaleProgress {
    constructor(fundingGoal) {
        this.fundingGoal = fundingGoal; // Total funding goal in ETH
        this.totalInvested = 0; // Total amount of ETH invested
    }

    /**
     * Updates the total invested amount.
     * @param {number} amount - The amount of ETH invested.
     */
    updateInvestment(amount) {
        if (amount <= 0) {
            console.error('Investment amount must be greater than zero.');
            return;
        }
        this.totalInvested += amount;
        this.displayProgress();
    }

    /**
     * Calculates the percentage of the funding goal that has been achieved.
     * @returns {number} - The percentage of the funding goal achieved.
     */
    calculatePercentage() {
        return ((this.totalInvested / this.fundingGoal) * 100).toFixed(2);
    }

    /**
     * Displays the current presale progress in the console.
     */
    displayProgress() {
        const percentage = this.calculatePercentage();
        console.log(`Total ETH Invested: ${this.totalInvested} ETH`);
        console.log(`Funding Goal Achieved: ${percentage}%`);

        if (percentage >= 100) {
            console.log('Funding goal has been reached! Presale is successful.');
        } else {
            console.log('Presale is ongoing. Keep investing!');
        }
    }
}

// Example usage:

// Define the funding goal for the presale
const fundingGoal = 100; // Set the funding goal to 100 ETH

// Create an instance of PresaleProgress
const presale = new PresaleProgress(fundingGoal);

// Simulate investments
presale.updateInvestment(10); // First investment of 10 ETH
presale.updateInvestment(20); // Second investment of 20 ETH
presale.updateInvestment(80); // Third investment of 80 ETH
```
