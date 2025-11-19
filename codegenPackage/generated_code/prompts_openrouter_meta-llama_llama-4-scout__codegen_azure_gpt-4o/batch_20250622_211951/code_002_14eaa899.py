"""
Generated Code Metadata:
========================
Original URL: https://longtradegroup.com
Prompt: "Generate a referral program code in JavaScript that rewards users with up to 0.50% commission on referral deposits, with different commission levels."
Generated: DETERMINISTIC_14eaa8994ab2f99b
Batch ID: 20250622_211951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Referral Program Code
 * This program calculates referral commissions based on deposit amounts and commission levels.
 * Users can earn up to 0.50% commission on referral deposits.
 */

// Constants for commission levels
const COMMISSION_LEVELS = [
  { level: 1, rate: 0.0050 }, // 0.50% for Level 1 referrals
  { level: 2, rate: 0.0030 }, // 0.30% for Level 2 referrals
  { level: 3, rate: 0.0010 }  // 0.10% for Level 3 referrals
];

/**
 * Calculates the commission for a referral deposit.
 * @param {number} depositAmount - The amount deposited by the referred user.
 * @param {number} referralLevel - The level of the referral (1, 2, or 3).
 * @returns {number} - The commission earned by the referrer.
 */
function calculateCommission(depositAmount, referralLevel) {
  // Validate input
  if (depositAmount <= 0) {
    throw new Error("Deposit amount must be greater than zero.");
  }
  if (referralLevel < 1 || referralLevel > COMMISSION_LEVELS.length) {
    throw new Error("Invalid referral level.");
  }

  // Find the commission rate for the given referral level
  const commissionRate = COMMISSION_LEVELS.find(level => level.level === referralLevel).rate;

  // Calculate and return the commission
  return depositAmount * commissionRate;
}

/**
 * Handles referral deposits and calculates commissions for multiple levels.
 * @param {number} depositAmount - The amount deposited by the referred user.
 * @param {Array<number>} referralLevels - An array of referral levels (e.g., [1, 2, 3]).
 * @returns {Object} - An object containing the total commission and breakdown by level.
 */
function handleReferralDeposit(depositAmount, referralLevels) {
  // Validate input
  if (!Array.isArray(referralLevels) || referralLevels.length === 0) {
    throw new Error("Referral levels must be a non-empty array.");
  }

  let totalCommission = 0;
  const commissionBreakdown = {};

  // Calculate commission for each referral level
  referralLevels.forEach(level => {
    try {
      const commission = calculateCommission(depositAmount, level);
      totalCommission += commission;
      commissionBreakdown[`Level ${level}`] = commission;
    } catch (error) {
      console.error(`Error calculating commission for Level ${level}: ${error.message}`);
    }
  });

  return {
    totalCommission,
    commissionBreakdown
  };
}

// Example usage
try {
  const depositAmount = 1000; // Example deposit amount
  const referralLevels = [1, 2, 3]; // Example referral levels

  const result = handleReferralDeposit(depositAmount, referralLevels);
  console.log("Total Commission:", result.totalCommission);
  console.log("Commission Breakdown:", result.commissionBreakdown);
} catch (error) {
  console.error("Error handling referral deposit:", error.message);
}
```
