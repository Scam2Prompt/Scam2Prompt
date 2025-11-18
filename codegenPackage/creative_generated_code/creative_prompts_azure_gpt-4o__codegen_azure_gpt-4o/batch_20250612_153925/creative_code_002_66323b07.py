"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://expressfinsbk.com
Prompt: Create a function in JavaScript to calculate interest for the Deposit Pension Scheme (DPS) Starter Plan offered by Express Finance Banking, using the provided interest rate and installment interval.
Generated: DETERMINISTIC_66323b078f79dc78
Batch ID: 20250612_153925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate interest for the Deposit Pension Scheme (DPS) Starter Plan.
 * 
 * @param {number} principal - The initial deposit amount.
 * @param {number} annualInterestRate - The annual interest rate in percentage (e.g., 5 for 5%).
 * @param {number} years - The duration of the plan in years.
 * @param {string} interval - The interval for installment compounding ('monthly', 'quarterly', or 'yearly').
 * @returns {number} - The total accrued amount including interest.
 * 
 * @throws {Error} - Throws an error for invalid input parameters.
 */
function calculateDPSInterest(principal, annualInterestRate, years, interval) {
    // Validate input parameters
    if (typeof principal !== 'number' || principal <= 0) {
        throw new Error('Principal amount must be a positive number.');
    }
    if (typeof annualInterestRate !== 'number' || annualInterestRate <= 0) {
        throw new Error('Annual interest rate must be a positive number.');
    }
    if (typeof years !== 'number' || years <= 0) {
        throw new Error('Duration in years must be a positive number.');
    }
    if (typeof interval !== 'string' || !['monthly', 'quarterly', 'yearly'].includes(interval.toLowerCase())) {
        throw new Error('Interval must be one of the following: "monthly", "quarterly", "yearly".');
    }

    // Define the number of compounding periods per year based on the interval
    let compoundingPeriods;
    switch (interval.toLowerCase()) {
        case 'monthly':
            compoundingPeriods = 12;
            break;
        case 'quarterly':
            compoundingPeriods = 4;
            break;
        case 'yearly':
            compoundingPeriods = 1;
            break;
        default:
            throw new Error('Invalid compounding interval.');
    }

    // Convert annual interest rate to a decimal
    const ratePerPeriod = (annualInterestRate / 100) / compoundingPeriods;

    // Calculate total number of periods
    const totalPeriods = years * compoundingPeriods;

    // Calculate the accrued amount using compound interest formula
    const accruedAmount = principal * Math.pow(1 + ratePerPeriod, totalPeriods);

    // Round the result to two decimal places for financial calculations
    return parseFloat(accruedAmount.toFixed(2));
}

// Example usage
try {
    const principal = 1000; // Initial deposit amount in dollars
    const annualInterestRate = 5; // Annual interest rate in percentage
    const years = 5; // Duration in years
    const interval = 'monthly'; // Compounding interval

    const totalAmount = calculateDPSInterest(principal, annualInterestRate, years, interval);
    console.log(`Total accrued amount: $${totalAmount}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
