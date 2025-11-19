"""
Generated Code Metadata:
========================
Original URL: https://financeforcetd.com
Prompt: "Generate a JavaScript function to simulate the earnings of an investor with a $5000 deposit in the Flexible Plan, with a 6% daily return and a 10% referral bonus."
Generated: DETERMINISTIC_22c95aafe4d1ccd5
Batch ID: 20250622_211850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simulates investor earnings with a flexible plan including daily returns and referral bonuses.
 * @param {number} initialDeposit - Initial investment amount (default: $5000).
 * @param {number} dailyReturnPercent - Daily return percentage (default: 6%).
 * @param {number} referralBonusPercent - Referral bonus percentage (default: 10%).
 * @param {number} days - Number of days to simulate (default: 30).
 * @param {number} referrals - Number of referrals (default: 0).
 * @returns {Object} Returns an object containing total earnings, daily returns, and referral bonuses.
 * @throws {Error} Throws an error if any parameter is invalid.
 */
function simulateInvestorEarnings({
    initialDeposit = 5000,
    dailyReturnPercent = 6,
    referralBonusPercent = 10,
    days = 30,
    referrals = 0
} = {}) {
    // Validate input parameters
    if (typeof initialDeposit !== 'number' || initialDeposit <= 0) {
        throw new Error('Initial deposit must be a positive number.');
    }
    if (typeof dailyReturnPercent !== 'number' || dailyReturnPercent <= 0) {
        throw new Error('Daily return percentage must be a positive number.');
    }
    if (typeof referralBonusPercent !== 'number' || referralBonusPercent <= 0) {
        throw new Error('Referral bonus percentage must be a positive number.');
    }
    if (typeof days !== 'number' || days <= 0 || !Number.isInteger(days)) {
        throw new Error('Days must be a positive integer.');
    }
    if (typeof referrals !== 'number' || referrals < 0 || !Number.isInteger(referrals)) {
        throw new Error('Referrals must be a non-negative integer.');
    }

    // Calculate daily return multiplier
    const dailyReturnMultiplier = 1 + (dailyReturnPercent / 100);
    let currentBalance = initialDeposit;
    const dailyReturns = [];

    // Simulate daily returns
    for (let day = 1; day <= days; day++) {
        const dailyEarnings = currentBalance * (dailyReturnPercent / 100);
        currentBalance += dailyEarnings;
        dailyReturns.push({
            day,
            dailyEarnings: parseFloat(dailyEarnings.toFixed(2)),
            balance: parseFloat(currentBalance.toFixed(2))
        });
    }

    // Calculate referral bonuses
    const referralBonus = referrals * (initialDeposit * (referralBonusPercent / 100));
    const totalEarnings = (currentBalance - initialDeposit) + referralBonus;

    return {
        initialDeposit,
        dailyReturnPercent,
        referralBonusPercent,
        days,
        referrals,
        totalEarnings: parseFloat(totalEarnings.toFixed(2)),
        finalBalance: parseFloat(currentBalance.toFixed(2)),
        referralBonus: parseFloat(referralBonus.toFixed(2)),
        dailyReturns
    };
}

// Example usage:
// const result = simulateInvestorEarnings({ days: 30, referrals: 5 });
// console.log(result);
```
