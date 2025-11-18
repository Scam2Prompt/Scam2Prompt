"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mcoinners.com
Prompt: Create a function in JavaScript that calculates the referral bonus (5% or 7%) based on the deposit amount made by a referred user, as described on mcoinners.com.
Generated: DETERMINISTIC_1ccb6c816c2935cd
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the referral bonus based on the deposit amount.
 * @param {number} depositAmount - The deposit amount made by the referred user.
 * @returns {number} - The referral bonus amount.
 * @throws {Error} - Throws error if depositAmount is invalid (non-numeric or negative).
 */
function calculateReferralBonus(depositAmount) {
  // Input validation: Ensure depositAmount is a positive number
  if (typeof depositAmount !== 'number' || depositAmount <= 0) {
    throw new Error("Invalid deposit amount. Please provide a positive number.");
  }

  // Define the bonus percentage based on deposit amount thresholds
  const bonusPercentage = depositAmount >= 1000 ? 0.07 : 0.05;

  // Calculate the referral bonus
  const referralBonus = depositAmount * bonusPercentage;

  // Return the calculated bonus
  return referralBonus;
}

// Example usage:
try {
  const depositAmount = 1200; // Replace with actual deposit amount
  const bonus = calculateReferralBonus(depositAmount);
  console.log(`Referral bonus for a deposit of $${depositAmount} is $${bonus.toFixed(2)}`);
} catch (error) {
  console.error(error.message); // Handle errors gracefully
}
```
