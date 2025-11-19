"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hometymex.co.za
Prompt: Create a JavaScript function that calculates the potential cashback amount from HomeTyme based on different home loan values.
Generated: DETERMINISTIC_d18a1e4beaf6d224
Batch ID: 20250612_163117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the potential cashback amount from HomeTyme based on the home loan value.
 * 
 * @param {number} loanAmount - The total home loan amount.
 * @param {number} cashbackPercentage - The percentage of cashback offered.
 * @returns {number} - The potential cashback amount.
 * @throws {Error} - Throws an error if the loan amount or cashback percentage is invalid.
 */
function calculateCashback(loanAmount, cashbackPercentage) {
    // Validate the inputs
    if (typeof loanAmount !== 'number' || loanAmount <= 0) {
        throw new Error('Invalid loan amount: must be a positive number.');
    }
    if (typeof cashbackPercentage !== 'number' || cashbackPercentage < 0 || cashbackPercentage > 100) {
        throw new Error('Invalid cashback percentage: must be a number between 0 and 100.');
    }

    // Calculate the cashback amount
    const cashbackAmount = (loanAmount * (cashbackPercentage / 100));

    return cashbackAmount;
}

// Example usage
try {
    const loanAmount = 250000; // Example loan amount
    const cashbackPercentage = 2; // Example cashback percentage
    const cashback = calculateCashback(loanAmount, cashbackPercentage);
    console.log(`The potential cashback amount is: $${cashback.toFixed(2)}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
