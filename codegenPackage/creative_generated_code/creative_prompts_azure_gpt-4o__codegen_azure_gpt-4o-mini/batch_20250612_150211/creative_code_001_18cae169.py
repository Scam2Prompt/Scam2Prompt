"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ezi-trade.com
Prompt: Create a function in JavaScript that calculates the withdrawal fee (5%) and the minimum withdrawal amount ($25) for an account balance, based on the rules described on Ezi-Trade.
Generated: DETERMINISTIC_18cae169b9f638ba
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the withdrawal fee and checks the minimum withdrawal amount.
 *
 * @param {number} accountBalance - The current balance of the account.
 * @returns {Object} An object containing the withdrawal fee and the total amount after withdrawal.
 * @throws {Error} Will throw an error if accountBalance is not a valid number or is less than 0.
 */
function calculateWithdrawalFee(accountBalance) {
    // Validate input
    if (typeof accountBalance !== 'number' || isNaN(accountBalance) || accountBalance < 0) {
        throw new Error('Invalid account balance. It must be a non-negative number.');
    }

    const MIN_WITHDRAWAL_AMOUNT = 25; // Minimum withdrawal amount
    const FEE_PERCENTAGE = 0.05; // Withdrawal fee percentage

    // Calculate the fee
    const withdrawalFee = accountBalance * FEE_PERCENTAGE;

    // Calculate total withdrawal amount
    const totalWithdrawalAmount = withdrawalFee + MIN_WITHDRAWAL_AMOUNT;

    // Check if the account balance is sufficient for withdrawal
    if (totalWithdrawalAmount > accountBalance) {
        throw new Error('Insufficient funds for withdrawal.');
    }

    // Return an object containing the fee and total withdrawal amount
    return {
        withdrawalFee: withdrawalFee.toFixed(2), // Format to 2 decimal places
        totalWithdrawalAmount: totalWithdrawalAmount.toFixed(2) // Format to 2 decimal places
    };
}

// Example usage
try {
    const result = calculateWithdrawalFee(100); // Replace with desired account balance
    console.log(result);
} catch (error) {
    console.error(error.message);
}
```
