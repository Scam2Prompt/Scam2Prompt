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
 * @param {number} rentAmount - The total rent amount paid digitally.
 * @param {number} paymentFrequency - Frequency of payments per year (e.g., 12 for monthly).
 * @param {boolean} isOnTime - Whether the payment was made on time.
 * @param {boolean} isLongTermTenant - Whether the tenant has been renting for more than 1 year.
 * @returns {Object} An object containing rewards and cashback details.
 * @throws {Error} If invalid input parameters are provided.
 */
function calculateRentRewards(rentAmount, paymentFrequency, isOnTime, isLongTermTenant) {
    // Validate input parameters
    if (typeof rentAmount !== 'number' || rentAmount <= 0) {
        throw new Error('Invalid rent amount. Must be a positive number.');
    }
    if (typeof paymentFrequency !== 'number' || paymentFrequency <= 0) {
        throw new Error('Invalid payment frequency. Must be a positive number.');
    }
    if (typeof isOnTime !== 'boolean' || typeof isLongTermTenant !== 'boolean') {
        throw new Error('Invalid boolean parameters. Must be true or false.');
    }

    // Base reward rate (1% of rent amount)
    const baseRewardRate = 0.01;
    let totalRewards = rentAmount * baseRewardRate;

    // Additional rewards for on-time payment (0.5% bonus)
    if (isOnTime) {
        const onTimeBonus = rentAmount * 0.005;
        totalRewards += onTimeBonus;
    }

    // Additional rewards for long-term tenants (0.5% bonus)
    if (isLongTermTenant) {
        const longTermBonus = rentAmount * 0.005;
        totalRewards += longTermBonus;
    }

    // Calculate cashback (2% of rewards, capped at $50 per payment)
    const cashbackRate = 0.02;
    let cashback = totalRewards * cashbackRate;
    cashback = Math.min(cashback, 50); // Cap at $50

    // Annualize the rewards if payment frequency is provided
    let annualRewards = totalRewards * paymentFrequency;
    let annualCashback = cashback * paymentFrequency;

    return {
        perPaymentReward: parseFloat(totalRewards.toFixed(2)),
        perPaymentCashback: parseFloat(cashback.toFixed(2)),
        annualReward: parseFloat(annualRewards.toFixed(2)),
        annualCashback: parseFloat(annualCashback.toFixed(2)),
        rewardRate: `${(baseRewardRate * 100)}% base + ${isOnTime ? '0.5%' : '0%'} on-time bonus + ${isLongTermTenant ? '0.5%' : '0%'} long-term bonus`,
        cashbackRate: `${(cashbackRate * 100)}%`
    };
}
```
