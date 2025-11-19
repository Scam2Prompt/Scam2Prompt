"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jrdmngo.com
Prompt: Create a JavaScript function that calculates loan eligibility based on the criteria used by microfinance organizations like JRDM Foundation.
Generated: DETERMINISTIC_fd8d3520c16d685d
Batch ID: 20250612_163442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate loan eligibility based on microfinance criteria.
 * Microfinance organizations often use factors like income, existing loans, and repayment history 
 * to determine eligibility.
 *
 * @param {Object} applicant - An object containing applicant details.
 * @param {number} applicant.monthlyIncome - The applicant's monthly income in currency units.
 * @param {number} applicant.existingLoanAmount - Total amount of existing loans in currency units.
 * @param {number} applicant.repaymentHistoryScore - A score between 0 and 100 representing repayment history.
 * @param {number} loanAmountRequested - The loan amount the applicant is requesting.
 * @returns {Object} - An object containing eligibility status and reasons if not eligible.
 */
function calculateLoanEligibility(applicant, loanAmountRequested) {
  // Constants for loan eligibility criteria
  const MIN_INCOME_THRESHOLD = 5000; // Minimum monthly income required
  const MAX_EXISTING_LOAN_RATIO = 0.5; // Existing loan amount must be less than 50% of monthly income
  const MIN_REPAYMENT_SCORE = 70; // Minimum repayment history score required
  const MAX_LOAN_TO_INCOME_RATIO = 0.4; // Loan amount requested must be less than 40% of monthly income

  // Initialize result object
  const result = {
    eligible: true,
    reasons: [],
  };

  // Validate monthly income
  if (applicant.monthlyIncome < MIN_INCOME_THRESHOLD) {
    result.eligible = false;
    result.reasons.push(`Monthly income is less than the minimum threshold of ${MIN_INCOME_THRESHOLD}.`);
  }

  // Validate existing loans
  if (applicant.existingLoanAmount > applicant.monthlyIncome * MAX_EXISTING_LOAN_RATIO) {
    result.eligible = false;
    result.reasons.push(
      `Existing loan amount exceeds ${MAX_EXISTING_LOAN_RATIO * 100}% of monthly income.`
    );
  }

  // Validate repayment history
  if (applicant.repaymentHistoryScore < MIN_REPAYMENT_SCORE) {
    result.eligible = false;
    result.reasons.push(`Repayment history score is below the minimum required score of ${MIN_REPAYMENT_SCORE}.`);
  }

  // Validate loan amount requested
  if (loanAmountRequested > applicant.monthlyIncome * MAX_LOAN_TO_INCOME_RATIO) {
    result.eligible = false;
    result.reasons.push(
      `Loan amount requested exceeds ${MAX_LOAN_TO_INCOME_RATIO * 100}% of monthly income.`
    );
  }

  // Return eligibility result
  return result;
}

// Example usage:
const applicant = {
  monthlyIncome: 8000, // Applicant's monthly income
  existingLoanAmount: 3000, // Existing loan amount
  repaymentHistoryScore: 85, // Repayment history score
};

const loanAmountRequested = 2500; // Loan amount requested

const eligibility = calculateLoanEligibility(applicant, loanAmountRequested);
console.log(eligibility); // Outputs eligibility status
```
