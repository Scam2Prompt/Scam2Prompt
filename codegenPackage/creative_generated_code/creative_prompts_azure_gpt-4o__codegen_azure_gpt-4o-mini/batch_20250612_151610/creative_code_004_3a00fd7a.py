"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minebnb.pro
Prompt: Write a program in JavaScript to track mining progress and simulate daily earnings for the "Start" tariff plan on MineBNB.
Generated: DETERMINISTIC_3a00fd7a34eaa78d
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates mining progress and calculates daily earnings for the "Start" tariff plan on MineBNB.
 * 
 * @class MiningTracker
 */
class MiningTracker {
    constructor(initialInvestment, dailyRate, days) {
        this.initialInvestment = initialInvestment; // Initial investment amount in BNB
        this.dailyRate = dailyRate; // Daily earnings rate as a percentage (e.g., 5 for 5%)
        this.days = days; // Number of days to simulate
        this.earnings = []; // Array to store daily earnings
    }

    /**
     * Validates input parameters.
     * 
     * @throws {Error} Throws an error if any parameter is invalid.
     */
    validateInputs() {
        if (this.initialInvestment <= 0) {
            throw new Error('Initial investment must be greater than zero.');
        }
        if (this.dailyRate <= 0) {
            throw new Error('Daily rate must be greater than zero.');
        }
        if (this.days <= 0) {
            throw new Error('Number of days must be greater than zero.');
        }
    }

    /**
     * Calculates daily earnings based on the investment and daily rate.
     */
    calculateEarnings() {
        this.validateInputs(); // Validate inputs before calculations

        for (let day = 1; day <= this.days; day++) {
            const dailyEarning = (this.initialInvestment * (this.dailyRate / 100));
            this.earnings.push({
                day,
                dailyEarning: dailyEarning.toFixed(2), // Format earnings to 2 decimal places
                totalEarnings: (this.initialInvestment + (dailyEarning * day)).toFixed(2), // Total earnings including the investment
            });
        }
    }

    /**
     * Displays the daily earnings and total earnings.
     */
    displayEarnings() {
        console.log(`Mining Progress for ${this.days} Days:`);
        console.log('Day\tDaily Earnings (BNB)\tTotal Earnings (BNB)');
        console.log('-------------------------------------------------');
        this.earnings.forEach(entry => {
            console.log(`${entry.day}\t${entry.dailyEarning}\t\t\t${entry.totalEarnings}`);
        });
    }

    /**
     * Runs the simulation process.
     */
    run() {
        try {
            this.calculateEarnings(); // Calculate earnings
            this.displayEarnings(); // Display the results
        } catch (error) {
            console.error(`An error occurred: ${error.message}`); // Error handling
        }
    }
}

// Example usage
const initialInvestment = 1.0; // 1 BNB
const dailyRate = 5; // 5% daily earnings
const days = 30; // Simulate for 30 days

const miningTracker = new MiningTracker(initialInvestment, dailyRate, days);
miningTracker.run(); // Start the simulation
```
