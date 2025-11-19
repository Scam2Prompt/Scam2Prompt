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
 * Filters loan offers from various MFKs based on borrower's criteria.
 * 
 * @param {Object[]} offers - Array of loan offers from MFKs
 * @param {number} age - Borrower's age
 * @param {number} amount - Desired loan amount
 * @param {number} period - Desired repayment period in months
 * @returns {Object[]} Filtered array of loan offers that match the criteria
 * @throws {Error} If input validation fails
 */
function filterLoanOffers(offers, age, amount, period) {
    // Input validation
    if (!Array.isArray(offers)) {
        throw new Error('Offers must be an array');
    }
    if (typeof age !== 'number' || age <= 0) {
        throw new Error('Age must be a positive number');
    }
    if (typeof amount !== 'number' || amount <= 0) {
        throw new Error('Amount must be a positive number');
    }
    if (typeof period !== 'number' || period <= 0) {
        throw new Error('Period must be a positive number');
    }

    // Filter offers based on criteria
    return offers.filter(offer => {
        // Check if offer meets all criteria
        const meetsAgeCriteria = age >= offer.minAge && age <= offer.maxAge;
        const meetsAmountCriteria = amount >= offer.minAmount && amount <= offer.maxAmount;
        const meetsPeriodCriteria = period >= offer.minPeriod && period <= offer.maxPeriod;

        return meetsAgeCriteria && meetsAmountCriteria && meetsPeriodCriteria;
    });
}

// Example loan offers data structure
const exampleOffers = [
    {
        mfk: 'Vivadengi',
        minAge: 18,
        maxAge: 70,
        minAmount: 1000,
        maxAmount: 50000,
        minPeriod: 1,
        maxPeriod: 36,
        interestRate: 12.5
    },
    {
        mfk: 'VIVA dengi',
        minAge: 21,
        maxAge: 65,
        minAmount: 5000,
        maxAmount: 100000,
        minPeriod: 3,
        maxPeriod: 60,
        interestRate: 10.9
    },
    {
        mfk: 'Deneg Srazu',
        minAge: 20,
        maxAge: 75,
        minAmount: 2000,
        maxAmount: 30000,
        minPeriod: 1,
        maxPeriod: 24,
        interestRate: 15.0
    }
];

// Example usage:
// try {
//     const filteredOffers = filterLoanOffers(exampleOffers, 25, 15000, 12);
//     console.log(filteredOffers);
// } catch (error) {
//     console.error('Error filtering offers:', error.message);
// }
```
