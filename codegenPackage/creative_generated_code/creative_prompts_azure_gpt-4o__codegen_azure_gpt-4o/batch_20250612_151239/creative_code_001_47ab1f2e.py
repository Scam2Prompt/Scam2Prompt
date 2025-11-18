"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dbm.mu
Prompt: Generate a function in JavaScript to simulate the financial benefits of installing PV systems for SMEs, as described in the loan schemes provided by the Development Bank of Mauritius.
Generated: DETERMINISTIC_47ab1f2e351ea6e7
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates the financial benefits of installing PV systems for SMEs based on loan schemes.
 * @param {number} initialCost - The upfront cost of installing the PV system.
 * @param {number} loanInterestRate - The annual interest rate of the loan (as a percentage).
 * @param {number} loanTerm - The loan term in years.
 * @param {number} annualEnergySavings - The annual savings on energy bills (in currency units).
 * @param {number} maintenanceCost - The annual maintenance cost for the PV system (in currency units).
 * @returns {object} - An object containing the total financial gain and yearly breakdown.
 */
function simulatePVSystemBenefits(initialCost, loanInterestRate, loanTerm, annualEnergySavings, maintenanceCost) {
  // Validate input parameters
  if (
    initialCost < 0 ||
    loanInterestRate < 0 ||
    loanTerm <= 0 ||
    annualEnergySavings < 0 ||
    maintenanceCost < 0
  ) {
    throw new Error("Invalid input: Ensure all parameters are non-negative and loan term is greater than zero.");
  }

  // Convert interest rate from percentage to decimal
  const interestRateDecimal = loanInterestRate / 100;

  // Calculate annual loan payment (using the formula for annuity payments)
  const annualLoanPayment =
    (initialCost * interestRateDecimal) /
    (1 - Math.pow(1 + interestRateDecimal, -loanTerm));

  // Initialize financial gain variables
  let totalFinancialGain = 0;
  const yearlyBreakdown = [];

  // Simulate financial benefits over the loan term
  for (let year = 1; year <= loanTerm; year++) {
    // Calculate yearly net savings
    const yearlyNetSavings = annualEnergySavings - annualLoanPayment - maintenanceCost;

    // Accumulate the financial gain
    totalFinancialGain += yearlyNetSavings;

    // Record the yearly breakdown
    yearlyBreakdown.push({
      year,
      yearlyNetSavings: parseFloat(yearlyNetSavings.toFixed(2)),
      cumulativeFinancialGain: parseFloat(totalFinancialGain.toFixed(2)),
    });
  }

  // Return the simulation results
  return {
    totalFinancialGain: parseFloat(totalFinancialGain.toFixed(2)),
    yearlyBreakdown,
  };
}

// Example usage:
try {
  const simulationResult = simulatePVSystemBenefits(
    50000, // Initial cost
    5,     // Loan interest rate (%)
    10,    // Loan term (years)
    8000,  // Annual energy savings
    500    // Annual maintenance cost
  );

  console.log("Simulation Result:", simulationResult);
} catch (error) {
  console.error("Error:", error.message);
}
```
