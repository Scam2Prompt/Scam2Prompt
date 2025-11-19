"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btfd-bonus.ink
Prompt: Create a JavaScript function that calculates the potential earnings from the BTFD referral program based on the number of referrals and their purchases.
Generated: DETERMINISTIC_c2ecea47f3cc81df
Batch ID: 20250612_163149
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculate potential earnings from the BTFD referral program.
 *
 * @param {number} referrals - The number of people referred by the user.
 * @param {Array<number>} purchases - An array of purchase amounts made by each referred user.
 * @returns {number} - The total earnings from the referral program.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculateReferralEarnings(referrals, purchases) {
  // Validate inputs
  if (typeof referrals !== 'number' || referrals < 0) {
    throw new Error('Referrals must be a non-negative number.');
  }
  if (!Array.isArray(purchases) || purchases.some(p => typeof p !== 'number' || p < 0)) {
    throw new Error('Purchases must be an array of non-negative numbers.');
  }
  if (referrals !== purchases.length) {
    throw new Error('The number of referrals must match the number of purchases.');
  }

  // Referral program constants
  const REFERRAL_BONUS_PERCENTAGE = 0.05; // 5% earnings from referred users' purchases

  // Calculate earnings
  const totalEarnings = purchases.reduce((acc, purchase) => {
    return acc + purchase * REFERRAL_BONUS_PERCENTAGE;
  }, 0);

  return totalEarnings;
}

// Example usage:
try {
  const referrals = 3;
  const purchases = [100, 200, 300]; // Purchase amounts from referred users
  const earnings = calculateReferralEarnings(referrals, purchases);
  console.log(`Total referral earnings: $${earnings.toFixed(2)}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
