"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbag-org.pages.dev
Prompt: Create a JavaScript function that calculates the potential earnings from MoonBag referrals, considering the 50% bonus for purchases over $25 as mentioned in the MoonBag content.
Generated: DETERMINISTIC_7b5e858e2fbfedb7
Batch ID: 20250612_163156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the potential earnings from MoonBag referrals.
 * @param {number} purchaseAmount - The amount of the purchase made by the referral.
 * @param {number} referralBaseRate - The base rate for referral earnings (e.g., 10% as 0.10).
 * @returns {number} The total earnings from the referral, including any applicable bonuses.
 * @throws Will throw an error if purchaseAmount or referralBaseRate are invalid inputs.
 */
function calculateMoonBagEarnings(purchaseAmount, referralBaseRate) {
  // Input validation
  if (typeof purchaseAmount !== 'number' || purchaseAmount <= 0) {
    throw new Error('Invalid purchase amount. It should be a positive number.');
  }

  if (typeof referralBaseRate !== 'number' || referralBaseRate <= 0 || referralBaseRate > 1) {
    throw new Error(
      'Invalid referral base rate. It should be a positive number between 0 and 1.'
    );
  }

  // Calculate base earnings
  const baseEarnings = purchaseAmount * referralBaseRate;

  // Apply 50% bonus if purchase amount exceeds $25
  const bonus =
    purchaseAmount > 25 ? baseEarnings * 0.5 : 0;

  // Total earnings = Base earnings + Bonus
  const totalEarnings = baseEarnings + bonus;

  return totalEarnings;
}

// Example usage:
try {
  const purchaseAmount = 30; // Amount of purchase in dollars
  const referralBaseRate = 0.10; // 10% referral rate
  const earnings = calculateMoonBagEarnings(purchaseAmount, referralBaseRate);
  console.log(`Total Earnings: $${earnings.toFixed(2)}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
