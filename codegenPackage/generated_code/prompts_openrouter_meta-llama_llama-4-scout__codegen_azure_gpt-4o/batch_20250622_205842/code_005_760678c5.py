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
 * Real Estate Investment Calculator
 * This script calculates potential earnings from a real estate investment
 * considering property appreciation and rental income.
 * 
 * Author: Expert Programmer
 * Date: YYYY-MM-DD
 */

// Function to calculate potential earnings
function calculateEarnings(initialInvestment, annualAppreciationRate, monthlyRentalIncome, years) {
    try {
        // Input validation
        if (initialInvestment <= 0 || annualAppreciationRate < 0 || monthlyRentalIncome < 0 || years <= 0) {
            throw new Error("Invalid input values. Please ensure all inputs are positive numbers.");
        }

        // Calculate property value after appreciation
        const finalPropertyValue = initialInvestment * Math.pow(1 + annualAppreciationRate / 100, years);

        // Calculate total rental income over the years
        const totalRentalIncome = monthlyRentalIncome * 12 * years;

        // Calculate total earnings
        const totalEarnings = finalPropertyValue + totalRentalIncome;

        // Return results
        return {
            initialInvestment: initialInvestment.toFixed(2),
            finalPropertyValue: finalPropertyValue.toFixed(2),
            totalRentalIncome: totalRentalIncome.toFixed(2),
            totalEarnings: totalEarnings.toFixed(2),
        };
    } catch (error) {
        console.error("Error calculating earnings:", error.message);
        return null;
    }
}

// Example usage
const initialInvestment = 200000; // Initial property investment in dollars
const annualAppreciationRate = 5; // Annual appreciation rate in percentage
const monthlyRentalIncome = 1500; // Monthly rental income in dollars
const years = 10; // Investment duration in years

const result = calculateEarnings(initialInvestment, annualAppreciationRate, monthlyRentalIncome, years);

if (result) {
    console.log("Real Estate Investment Earnings:");
    console.log(`Initial Investment: $${result.initialInvestment}`);
    console.log(`Final Property Value: $${result.finalPropertyValue}`);
    console.log(`Total Rental Income: $${result.totalRentalIncome}`);
    console.log(`Total Earnings: $${result.totalEarnings}`);
}
```
