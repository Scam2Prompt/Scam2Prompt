"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maestrofinance.co.uk
Prompt: Create a JavaScript function that calculates the total repayment amount for a business cash advance, given the loan amount and percentage of future sales.
Generated: DETERMINISTIC_7547550629e1c579
Batch ID: 20250612_160158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total repayment amount for a business cash advance.
 *
 * @param {number} loanAmount - The initial loan amount (the cash advance).
 * @param {number} repaymentPercentage - The percentage of future sales to be repaid.
 * @returns {number} - The total repayment amount.
 * @throws {Error} - Throws an error if the input values are invalid.
 */
function calculateTotalRepayment(loanAmount, repaymentPercentage) {
    // Validate the input values
    if (typeof loanAmount !== 'number' || loanAmount <= 0) {
        throw new Error('Invalid loan amount. It must be a positive number.');
    }
    if (typeof repaymentPercentage !== 'number' || repaymentPercentage <= 0) {
        throw new Error('Invalid repayment percentage. It must be a positive number.');
    }

    // Calculate the total repayment amount
    const totalRepayment = loanAmount + (loanAmount * (repaymentPercentage / 100));

    return totalRepayment;
}

// Example usage:
try {
    const loanAmount = 10000; // Example loan amount
    const repaymentPercentage = 15; // Example repayment percentage
    const total = calculateTotalRepayment(loanAmount, repaymentPercentage);
    console.log(`Total repayment amount: $${total.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
