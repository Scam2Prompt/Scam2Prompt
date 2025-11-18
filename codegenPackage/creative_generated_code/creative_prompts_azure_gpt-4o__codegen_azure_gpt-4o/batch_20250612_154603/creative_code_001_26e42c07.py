"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://equityglobal-funds.com
Prompt: Create a function in JavaScript to simulate referral bonus calculations (e.g., 10% commission for referrals) based on the Equity Global Funds partnership program.
Generated: DETERMINISTIC_26e42c07a5c05c27
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Referral bonus calculation for the Equity Global Funds partnership program.
 * 
 * This function calculates the referral bonus based on a 10% commission rate.
 * It accepts the referral's contribution amount and returns the commission earned.
 * 
 * @param {number} referralAmount - The amount contributed by the referral.
 * @returns {number} - The calculated referral bonus.
 * @throws {Error} If the input is not a valid positive number.
 */
function calculateReferralBonus(referralAmount) {
  // Validate input
  if (typeof referralAmount !== 'number' || referralAmount <= 0) {
    throw new Error('Invalid referral amount. Amount must be a positive number.');
  }

  // Define commission rate
  const commissionRate = 0.10; // 10%

  // Calculate referral bonus
  const referralBonus = referralAmount * commissionRate;

  return referralBonus;
}

// Example usage:
try {
  const referralAmount = 500; // Example contribution amount from referral
  const bonus = calculateReferralBonus(referralAmount);
  console.log(`Referral Bonus: $${bonus.toFixed(2)}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
