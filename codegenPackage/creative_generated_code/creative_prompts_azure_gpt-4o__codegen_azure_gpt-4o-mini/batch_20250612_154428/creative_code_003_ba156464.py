"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://momspg.com
Prompt: Write a function in JavaScript to calculate rent rewards and cashback for tenants based on digital rent payments, as mentioned in the Moms PG digital payment system.
Generated: DETERMINISTIC_ba156464d7f8f19a
Batch ID: 20250612_154428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the rent rewards and cashback for tenants based on digital rent payments.
 * The rewards and cashback are calculated based on predefined percentages.
 * 
 * @param {number} rentAmount - The total rent amount paid by the tenant.
 * @param {number} paymentMethod - The method of payment (1 for debit/credit card, 2 for bank transfer).
 * @returns {Object} An object containing rewards and cashback amounts.
 * @throws {Error} Throws an error if rentAmount is not a positive number or paymentMethod is not valid.
 */
function calculateRentRewards(rentAmount, paymentMethod) {
    // Validate input parameters
    if (typeof rentAmount !== 'number' || rentAmount <= 0) {
        throw new Error('Invalid rent amount. It should be a positive number.');
    }
    
    if (![1, 2].includes(paymentMethod)) {
        throw new Error('Invalid payment method. Use 1 for debit/credit card or 2 for bank transfer.');
    }

    // Define reward and cashback percentages based on payment method
    const rewardsPercentage = paymentMethod === 1 ? 0.05 : 0.03; // 5% for card payments, 3% for bank transfers
    const cashbackPercentage = paymentMethod === 1 ? 0.02 : 0.01; // 2% for card payments, 1% for bank transfers

    // Calculate rewards and cashback amounts
    const rewards = rentAmount * rewardsPercentage;
    const cashback = rentAmount * cashbackPercentage;

    // Return the results in an object
    return {
        rewards: parseFloat(rewards.toFixed(2)), // Format to two decimal places
        cashback: parseFloat(cashback.toFixed(2)) // Format to two decimal places
    };
}

// Example usage
try {
    const result = calculateRentRewards(1500, 1);
    console.log('Rewards:', result.rewards); // Outputs rewards
    console.log('Cashback:', result.cashback); // Outputs cashback
} catch (error) {
    console.error('Error:', error.message); // Handle errors gracefully
}
```
