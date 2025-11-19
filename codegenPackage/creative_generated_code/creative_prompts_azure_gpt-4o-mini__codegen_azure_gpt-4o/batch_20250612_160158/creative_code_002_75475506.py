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
 * Function to calculate the total repayment amount for a business cash advance.
 * 
 * @param {number} loanAmount - The initial loan amount provided to the business.
 * @param {number} repaymentRate - The percentage of future sales to be repaid (e.g., 1.25 for 125%).
 * @returns {number} - The total repayment amount.
 * 
 * @throws {Error} Throws an error if inputs are invalid.
 */
function calculateTotalRepayment(loanAmount, repaymentRate) {
    // Input validation
    if (typeof loanAmount !== 'number' || loanAmount <= 0) {
        throw new Error('Invalid loan amount. It must be a positive number.');
    }
    if (typeof repaymentRate !== 'number' || repaymentRate <= 0) {
        throw new Error('Invalid repayment rate. It must be a positive number.');
    }

    // Calculate total repayment amount
    const totalRepayment = loanAmount * repaymentRate;

    // Return the result
    return totalRepayment;
}

// Example usage:
try {
    const loanAmount = 10000; // Example loan amount
    const repaymentRate = 1.25; // Example repayment rate (125% of future sales)
    const totalRepayment = calculateTotalRepayment(loanAmount, repaymentRate);
    console.log(`Total Repayment Amount: $${totalRepayment.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
