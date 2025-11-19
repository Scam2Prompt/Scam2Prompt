"""
Generated Code Metadata:
========================
Original URL: https://dbm.mu
Prompt: Generate a function in JavaScript to simulate the financial benefits of installing PV systems for SMEs, as described in the loan schemes provided by the Development Bank of Mauritius.
Generated: DETERMINISTIC_47ab1f2e351ea6e7
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simulates the financial benefits of installing photovoltaic (PV) systems for small and medium enterprises (SMEs).
 * 
 * @param {number} initialInvestment - The initial cost of installing the PV system.
 * @param {number} annualSavings - The annual savings on electricity bills due to the PV system.
 * @param {number} loanInterestRate - The annual interest rate of the loan for financing the PV system (in percentage).
 * @param {number} loanTerm - The term of the loan in years.
 * @returns {Object} - An object containing the total cost, total savings, net savings, and return on investment (ROI).
 * @throws {Error} - Throws an error if any input is invalid (negative values, non-numeric).
 */
function simulatePVSystemBenefits(initialInvestment, annualSavings, loanInterestRate, loanTerm) {
    // Input validation
    if (typeof initialInvestment !== 'number' || initialInvestment < 0) {
        throw new Error('Invalid initial investment amount. It must be a non-negative number.');
    }
    if (typeof annualSavings !== 'number' || annualSavings < 0) {
        throw new Error('Invalid annual savings amount. It must be a non-negative number.');
    }
    if (typeof loanInterestRate !== 'number' || loanInterestRate < 0) {
        throw new Error('Invalid loan interest rate. It must be a non-negative number.');
    }
    if (typeof loanTerm !== 'number' || loanTerm <= 0) {
        throw new Error('Invalid loan term. It must be a positive number.');
    }

    // Calculate total loan cost using the formula for an annuity
    const monthlyInterestRate = loanInterestRate / 100 / 12;
    const numberOfPayments = loanTerm * 12;
    const monthlyPayment = (initialInvestment * monthlyInterestRate) / 
                           (1 - Math.pow(1 + monthlyInterestRate, -numberOfPayments));
    const totalLoanCost = monthlyPayment * numberOfPayments;

    // Calculate total savings over the loan term
    const totalSavings = annualSavings * loanTerm;

    // Calculate net savings
    const netSavings = totalSavings - totalLoanCost;

    // Calculate return on investment (ROI)
    const roi = (netSavings / totalLoanCost) * 100;

    // Return the results as an object
    return {
        totalLoanCost: totalLoanCost.toFixed(2),
        totalSavings: totalSavings.toFixed(2),
        netSavings: netSavings.toFixed(2),
        roi: roi.toFixed(2) + '%'
    };
}

// Example usage
try {
    const results = simulatePVSystemBenefits(50000, 8000, 5, 10);
    console.log('Financial Benefits of PV System Installation:', results);
} catch (error) {
    console.error('Error:', error.message);
}
```
