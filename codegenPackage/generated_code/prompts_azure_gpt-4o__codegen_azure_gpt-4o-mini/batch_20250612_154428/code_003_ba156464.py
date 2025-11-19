"""
Generated Code Metadata:
========================
Original URL: https://momspg.com
Prompt: Write a function in JavaScript to calculate rent rewards and cashback for tenants based on digital rent payments, as mentioned in the Moms PG digital payment system.
Generated: DETERMINISTIC_ba156464d7f8f19a
Batch ID: 20250612_154428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates rent rewards and cashback for tenants based on digital rent payments.
 * 
 * @param {number} rentAmount - The total rent amount paid by the tenant.
 * @param {number} paymentMethod - The method of payment (1 for credit card, 2 for bank transfer).
 * @returns {Object} - An object containing the rewards and cashback amounts.
 * @throws {Error} - Throws an error if the rent amount is negative or payment method is invalid.
 */
function calculateRentRewards(rentAmount, paymentMethod) {
    // Validate input parameters
    if (typeof rentAmount !== 'number' || rentAmount < 0) {
        throw new Error('Invalid rent amount. It must be a non-negative number.');
    }
    
    if (![1, 2].includes(paymentMethod)) {
        throw new Error('Invalid payment method. Use 1 for credit card or 2 for bank transfer.');
    }

    // Define reward and cashback rates
    const REWARD_RATE = 0.05; // 5% rewards for digital payments
    const CASHBACK_RATE_CREDIT_CARD = 0.02; // 2% cashback for credit card payments
    const CASHBACK_RATE_BANK_TRANSFER = 0.01; // 1% cashback for bank transfers

    // Calculate rewards
    const rewards = rentAmount * REWARD_RATE;

    // Calculate cashback based on payment method
    let cashback;
    if (paymentMethod === 1) {
        cashback = rentAmount * CASHBACK_RATE_CREDIT_CARD;
    } else {
        cashback = rentAmount * CASHBACK_RATE_BANK_TRANSFER;
    }

    // Return the results as an object
    return {
        rewards: parseFloat(rewards.toFixed(2)), // Round to 2 decimal places
        cashback: parseFloat(cashback.toFixed(2))  // Round to 2 decimal places
    };
}

// Example usage
try {
    const result = calculateRentRewards(1000, 1);
    console.log(`Rewards: $${result.rewards}, Cashback: $${result.cashback}`);
} catch (error) {
    console.error(error.message);
}
```
