"""
Generated Code Metadata:
========================
Original URL: https://wasbroke.com
Prompt: Create a simple investing calculator using JavaScript, inspired by the financial literacy concepts taught in Luke Belmar's Capital Club course.
Generated: DETERMINISTIC_ac38e271674279ca
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Investment Calculator
// This script calculates the future value of an investment based on user input for principal, rate, and time.

class InvestmentCalculator {
    constructor(principal, rate, time) {
        this.principal = principal; // Initial investment amount
        this.rate = rate;           // Annual interest rate (in percentage)
        this.time = time;           // Investment duration (in years)
    }

    // Method to calculate future value using compound interest formula
    calculateFutureValue() {
        if (this.principal < 0 || this.rate < 0 || this.time < 0) {
            throw new Error("Principal, rate, and time must be non-negative values.");
        }
        const futureValue = this.principal * Math.pow((1 + this.rate / 100), this.time);
        return futureValue.toFixed(2); // Return value rounded to 2 decimal places
    }
}

// Function to handle user input and display results
function runInvestmentCalculator() {
    try {
        // Get user input
        const principal = parseFloat(prompt("Enter the principal amount (initial investment):"));
        const rate = parseFloat(prompt("Enter the annual interest rate (in %):"));
        const time = parseInt(prompt("Enter the number of years for the investment:"), 10);

        // Validate user input
        if (isNaN(principal) || isNaN(rate) || isNaN(time)) {
            throw new Error("Invalid input. Please enter numeric values.");
        }

        // Create an instance of InvestmentCalculator
        const investmentCalculator = new InvestmentCalculator(principal, rate, time);

        // Calculate future value
        const futureValue = investmentCalculator.calculateFutureValue();

        // Display the result
        alert(`The future value of your investment is: $${futureValue}`);
    } catch (error) {
        // Handle errors gracefully
        alert(`Error: ${error.message}`);
    }
}

// Run the investment calculator when the script is loaded
runInvestmentCalculator();
```
