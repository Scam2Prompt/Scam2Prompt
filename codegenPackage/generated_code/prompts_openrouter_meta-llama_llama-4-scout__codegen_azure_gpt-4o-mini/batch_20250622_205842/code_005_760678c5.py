"""
Generated Code Metadata:
========================
Original URL: https://earno-trade.net
Prompt: "Develop a basic calculator in JavaScript to determine the potential earnings from a real estate investment, considering factors like property appreciation and rental income."
Generated: DETERMINISTIC_760678c53ebc16d4
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * A basic calculator for determining potential earnings from a real estate investment.
 * This calculator considers property appreciation and rental income.
 */

class RealEstateCalculator {
    constructor(initialInvestment, annualAppreciationRate, annualRentalIncome) {
        this.initialInvestment = initialInvestment; // Initial investment amount
        this.annualAppreciationRate = annualAppreciationRate; // Annual appreciation rate (as a decimal)
        this.annualRentalIncome = annualRentalIncome; // Annual rental income
    }

    /**
     * Calculates the total value of the property after a given number of years.
     * @param {number} years - The number of years to calculate appreciation for.
     * @returns {number} - The total value of the property after appreciation.
     */
    calculateAppreciation(years) {
        if (years < 0) {
            throw new Error("Years must be a non-negative number.");
        }
        return this.initialInvestment * Math.pow(1 + this.annualAppreciationRate, years);
    }

    /**
     * Calculates the total rental income over a given number of years.
     * @param {number} years - The number of years to calculate rental income for.
     * @returns {number} - The total rental income over the specified years.
     */
    calculateRentalIncome(years) {
        if (years < 0) {
            throw new Error("Years must be a non-negative number.");
        }
        return this.annualRentalIncome * years;
    }

    /**
     * Calculates the total potential earnings from the investment after a given number of years.
     * @param {number} years - The number of years to calculate potential earnings for.
     * @returns {number} - The total potential earnings from appreciation and rental income.
     */
    calculateTotalEarnings(years) {
        const appreciation = this.calculateAppreciation(years);
        const rentalIncome = this.calculateRentalIncome(years);
        return appreciation + rentalIncome - this.initialInvestment; // Subtract initial investment to get net earnings
    }
}

// Example usage:
try {
    const investment = new RealEstateCalculator(100000, 0.05, 12000); // $100,000 investment, 5% appreciation, $12,000 rental income
    const years = 10; // Calculate for 10 years

    const totalEarnings = investment.calculateTotalEarnings(years);
    console.log(`Total potential earnings after ${years} years: $${totalEarnings.toFixed(2)}`);
} catch (error) {
    console.error("Error:", error.message);
}
```
