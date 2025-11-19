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
 * Calculates loan eligibility based on microfinance criteria.
 * 
 * @param {number} income - The monthly income of the applicant.
 * @param {number} existingDebts - The total existing debts of the applicant.
 * @param {number} creditScore - The credit score of the applicant (0 to 850).
 * @param {number} loanAmount - The desired loan amount.
 * @returns {boolean} - Returns true if the applicant is eligible for the loan, false otherwise.
 * @throws {Error} - Throws an error if the inputs are invalid.
 */
function calculateLoanEligibility(income, existingDebts, creditScore, loanAmount) {
    // Validate inputs
    if (typeof income !== 'number' || income <= 0) {
        throw new Error('Income must be a positive number.');
    }
    if (typeof existingDebts !== 'number' || existingDebts < 0) {
        throw new Error('Existing debts must be a non-negative number.');
    }
    if (typeof creditScore !== 'number' || creditScore < 0 || creditScore > 850) {
        throw new Error('Credit score must be between 0 and 850.');
    }
    if (typeof loanAmount !== 'number' || loanAmount <= 0) {
        throw new Error('Loan amount must be a positive number.');
    }

    // Define eligibility criteria
    const maxDebtToIncomeRatio = 0.4; // Maximum debt to income ratio
    const minCreditScore = 650; // Minimum credit score for eligibility

    // Calculate debt to income ratio
    const debtToIncomeRatio = (existingDebts + loanAmount) / income;

    // Determine eligibility
    const isEligible = debtToIncomeRatio <= maxDebtToIncomeRatio && creditScore >= minCreditScore;

    return isEligible;
}

// Example usage (uncomment below lines to test)
// try {
//     const eligible = calculateLoanEligibility(3000, 500, 700, 1000);
//     console.log(`Loan eligibility: ${eligible}`); // Output: Loan eligibility: true
// } catch (error) {
//     console.error(error.message);
// }
```
