"""
Generated Code Metadata:
========================
Original URL: https://loancomparison.online
Prompt: Write a JavaScript function to filter loan offers from various MFKs, such as Vivadengi, VIVA dengi, and Deneg Srazu, based on the borrower's age, loan amount, and desired repayment period.
Generated: DETERMINISTIC_b6c536081f7da8f7
Batch ID: 20250622_211628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Represents a loan offer from an MFK.
 */
class LoanOffer {
  /**
   * Creates a new LoanOffer instance.
   * @param {string} provider - The MFK provider (e.g., Vivadengi, VIVA dengi, Deneg Srazu).
   * @param {number} minAge - The minimum age required for the loan.
   * @param {number} maxAge - The maximum age required for the loan.
   * @param {number} minLoanAmount - The minimum loan amount offered.
   * @param {number} maxLoanAmount - The maximum loan amount offered.
   * @param {number} minRepaymentPeriod - The minimum repayment period in months.
   * @param {number} maxRepaymentPeriod - The maximum repayment period in months.
   */
  constructor(provider, minAge, maxAge, minLoanAmount, maxLoanAmount, minRepaymentPeriod, maxRepaymentPeriod) {
    this.provider = provider;
    this.minAge = minAge;
    this.maxAge = maxAge;
    this.minLoanAmount = minLoanAmount;
    this.maxLoanAmount = maxLoanAmount;
    this.minRepaymentPeriod = minRepaymentPeriod;
    this.maxRepaymentPeriod = maxRepaymentPeriod;
  }
}

/**
 * Filters loan offers based on the borrower's age, loan amount, and desired repayment period.
 * @param {number} age - The borrower's age.
 * @param {number} loanAmount - The desired loan amount.
 * @param {number} repaymentPeriod - The desired repayment period in months.
 * @param {LoanOffer[]} loanOffers - An array of LoanOffer instances.
 * @returns {LoanOffer[]} An array of LoanOffer instances that match the borrower's criteria.
 */
function filterLoanOffers(age, loanAmount, repaymentPeriod, loanOffers) {
  if (typeof age !== 'number' || typeof loanAmount !== 'number' || typeof repaymentPeriod !== 'number') {
    throw new Error('Age, loan amount, and repayment period must be numbers.');
  }

  if (!Array.isArray(loanOffers)) {
    throw new Error('Loan offers must be an array.');
  }

  return loanOffers.filter((offer) => {
    return age >= offer.minAge && age <= offer.maxAge
      && loanAmount >= offer.minLoanAmount && loanAmount <= offer.maxLoanAmount
      && repaymentPeriod >= offer.minRepaymentPeriod && repaymentPeriod <= offer.maxRepaymentPeriod;
  });
}

// Example usage:
const loanOffers = [
  new LoanOffer('Vivadengi', 18, 65, 10000, 50000, 3, 36),
  new LoanOffer('VIVA dengi', 20, 60, 15000, 60000, 6, 48),
  new LoanOffer('Deneg Srazu', 22, 55, 20000, 70000, 12, 60),
];

try {
  const filteredOffers = filterLoanOffers(30, 30000, 24, loanOffers);
  console.log(filteredOffers);
} catch (error) {
  console.error(error.message);
}
```
