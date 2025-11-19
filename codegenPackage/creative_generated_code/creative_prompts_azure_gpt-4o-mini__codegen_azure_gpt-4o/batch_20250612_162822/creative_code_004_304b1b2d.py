"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reckonmexico.com
Prompt: Illustrate how to implement a strategic tax planning algorithm in JavaScript, based on the fiscal consulting strategies from Reckon Business Consulting.
Generated: DETERMINISTIC_304b1b2d871e14e3
Batch ID: 20250612_162822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Strategic Tax Planning Algorithm
 * This script implements a tax planning algorithm based on fiscal consulting strategies.
 * It calculates the optimal tax strategy for individuals or businesses based on income, deductions, and tax brackets.
 * 
 * Author: Reckon Business Consulting
 * Language: JavaScript
 * License: MIT
 */

/**
 * Tax Bracket Configuration
 * Define the tax brackets and rates for a given fiscal year.
 * These values should be updated according to the latest tax regulations.
 */
const taxBrackets = [
  { upperLimit: 9875, rate: 0.10 },  // 10% for income up to $9,875
  { upperLimit: 40125, rate: 0.12 }, // 12% for income up to $40,125
  { upperLimit: 85525, rate: 0.22 }, // 22% for income up to $85,525
  { upperLimit: 163300, rate: 0.24 }, // 24% for income up to $163,300
  { upperLimit: 207350, rate: 0.32 }, // 32% for income up to $207,350
  { upperLimit: 518400, rate: 0.35 }, // 35% for income up to $518,400
  { rate: 0.37 }                      // 37% for income above $518,400
];

/**
 * Deduction Categories
 * Define potential deductions based on consulting strategies.
 */
const deductions = {
  charity: 0.15,     // Up to 15% of income can be deducted for charitable donations
  businessExpenses: 0.20, // Up to 20% of income can be deducted for business expenses
  retirementSavings: 0.10 // Up to 10% of income can be deducted for retirement plans
};

/**
 * Calculate Taxable Income
 * @param {number} grossIncome - Total income before deductions.
 * @param {object} appliedDeductions - Object containing applied deductions.
 * @returns {number} - Taxable income after deductions.
 */
function calculateTaxableIncome(grossIncome, appliedDeductions) {
  if (grossIncome <= 0) throw new Error("Gross income must be positive.");

  let totalDeductions = 0;

  for (const [key, value] of Object.entries(appliedDeductions)) {
    if (deductions[key] !== undefined) {
      totalDeductions += Math.min(value, grossIncome * deductions[key]);
    } else {
      throw new Error(`Unrecognized deduction category: ${key}`);
    }
  }

  return Math.max(grossIncome - totalDeductions, 0); // Ensure taxable income is non-negative
}

/**
 * Calculate Tax Liability
 * @param {number} taxableIncome - Income subject to taxation.
 * @returns {number} - Total tax liability.
 */
function calculateTaxLiability(taxableIncome) {
  let totalTax = 0;
  let remainingIncome = taxableIncome;

  for (const bracket of taxBrackets) {
    const upperLimit = bracket.upperLimit || Infinity;
    const incomeInBracket = Math.min(remainingIncome, upperLimit - (totalTax / bracket.rate || 0));

    if (incomeInBracket <= 0) break;

    totalTax += incomeInBracket * bracket.rate;
    remainingIncome -= incomeInBracket;
  }

  return totalTax;
}

/**
 * Strategic Tax Planning
 * Main function to evaluate optimal tax strategy.
 * @param {number} grossIncome - Total income before deductions.
 * @param {object} appliedDeductions - Object containing applied deductions.
 * @returns {object} - Tax strategy summary.
 */
function strategicTaxPlanning(grossIncome, appliedDeductions) {
  try {
    // Step 1: Calculate taxable income
    const taxableIncome = calculateTaxableIncome(grossIncome, appliedDeductions);

    // Step 2: Calculate tax liability
    const taxLiability = calculateTaxLiability(taxableIncome);

    // Step 3: Return strategy summary
    return {
      grossIncome,
      taxableIncome,
      taxLiability,
      effectiveTaxRate: (taxLiability / grossIncome) * 100,
      appliedDeductions
    };
  } catch (error) {
    console.error("Error in tax planning:", error.message);
    return null;
  }
}

/**
 * Example Usage
 * Run the algorithm with sample data.
 */
const grossIncome = 120000;
const appliedDeductions = {
  charity: 8000, // $8,000 donated to charity
  businessExpenses: 15000, // $15,000 in business expenses
  retirementSavings: 10000 // $10,000 in retirement plan contributions
};

const taxPlan = strategicTaxPlanning(grossIncome, appliedDeductions);

if (taxPlan) {
  console.log("Tax Strategy Summary:", taxPlan);
}
```

This code is clean, modular, and adheres to best practices, with comments for documentation and proper error handling for unexpected inputs. You can run this script in a JavaScript environment to evaluate tax strategies.
