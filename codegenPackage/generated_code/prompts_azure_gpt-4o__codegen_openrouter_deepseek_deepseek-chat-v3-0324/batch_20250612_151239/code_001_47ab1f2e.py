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
 * Simulates the financial benefits of installing PV systems for SMEs based on loan schemes.
 * @param {Object} params - Input parameters for the simulation.
 * @param {number} params.systemCost - Total cost of the PV system (MUR).
 * @param {number} params.loanAmount - Loan amount requested (MUR).
 * @param {number} params.loanTerm - Loan term in years.
 * @param {number} params.interestRate - Annual interest rate (decimal, e.g., 0.05 for 5%).
 * @param {number} params.annualSavings - Estimated annual savings from PV system (MUR).
 * @param {number} [params.grantPercentage=0] - Percentage of grant (decimal, e.g., 0.2 for 20%).
 * @param {number} [params.inflationRate=0.02] - Annual inflation rate (decimal, default 2%).
 * @returns {Object} - Simulation results including financial metrics.
 */
function simulatePVSystemBenefits(params) {
    // Validate input parameters
    if (!params || typeof params !== 'object') {
        throw new Error('Invalid input: params must be an object');
    }
    const requiredParams = ['systemCost', 'loanAmount', 'loanTerm', 'interestRate', 'annualSavings'];
    for (const param of requiredParams) {
        if (params[param] === undefined || params[param] === null) {
            throw new Error(`Missing required parameter: ${param}`);
        }
        if (typeof params[param] !== 'number' || params[param] < 0) {
            throw new Error(`Invalid parameter: ${param} must be a positive number`);
        }
    }

    // Set default values for optional parameters
    const grantPercentage = params.grantPercentage || 0;
    const inflationRate = params.inflationRate || 0.02;

    // Calculate grant amount
    const grantAmount = params.systemCost * grantPercentage;

    // Calculate monthly loan payment (using annuity formula)
    const monthlyInterestRate = params.interestRate / 12;
    const numberOfPayments = params.loanTerm * 12;
    const monthlyPayment = (params.loanAmount * monthlyInterestRate) /
        (1 - Math.pow(1 + monthlyInterestRate, -numberOfPayments));

    // Calculate total loan cost
    const totalLoanCost = monthlyPayment * numberOfPayments;

    // Calculate net system cost after grant
    const netSystemCost = params.systemCost - grantAmount;

    // Calculate annual savings adjusted for inflation
    const savingsOverTerm = [];
    let cumulativeSavings = 0;
    for (let year = 1; year <= params.loanTerm; year++) {
        const inflatedSavings = params.annualSavings * Math.pow(1 + inflationRate, year - 1);
        cumulativeSavings += inflatedSavings;
        savingsOverTerm.push({
            year,
            annualSavings: inflatedSavings,
            cumulativeSavings
        });
    }

    // Calculate payback period
    let paybackPeriod = null;
    let runningCost = netSystemCost;
    for (let year = 1; year <= params.loanTerm; year++) {
        const savings = params.annualSavings * Math.pow(1 + inflationRate, year - 1);
        runningCost -= savings;
        if (runningCost <= 0) {
            paybackPeriod = year - 1 + (Math.abs(runningCost) / savings);
            break;
        }
    }

    // Calculate return on investment (ROI)
    const totalSavings = savingsOverTerm[savingsOverTerm.length - 1].cumulativeSavings;
    const roi = ((totalSavings - netSystemCost) / netSystemCost) * 100;

    // Return simulation results
    return {
        systemCost: params.systemCost,
        grantAmount,
        netSystemCost,
        loanAmount: params.loanAmount,
        loanTerm: params.loanTerm,
        interestRate: params.interestRate,
        monthlyPayment: parseFloat(monthlyPayment.toFixed(2)),
        totalLoanCost: parseFloat(totalLoanCost.toFixed(2)),
        annualSavings: params.annualSavings,
        savingsOverTerm,
        paybackPeriod: paybackPeriod ? parseFloat(paybackPeriod.toFixed(2)) : null,
        roi: parseFloat(roi.toFixed(2)),
        breakEvenYear: paybackPeriod ? Math.ceil(paybackPeriod) : null
    };
}

// Example usage:
// const results = simulatePVSystemBenefits({
//     systemCost: 500000,
//     loanAmount: 400000,
//     loanTerm: 10,
//     interestRate: 0.05,
//     annualSavings: 120000,
//     grantPercentage: 0.2
// });
// console.log(results);
```
