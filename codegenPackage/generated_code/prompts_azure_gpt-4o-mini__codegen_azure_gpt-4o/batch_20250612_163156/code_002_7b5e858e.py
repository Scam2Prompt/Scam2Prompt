"""
Generated Code Metadata:
========================
Original URL: https://moonbag-org.pages.dev
Prompt: Create a JavaScript function that calculates the potential earnings from MoonBag referrals, considering the 50% bonus for purchases over $25 as mentioned in the MoonBag content.
Generated: DETERMINISTIC_7b5e858e2fbfedb7
Batch ID: 20250612_163156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate potential earnings from MoonBag referrals.
 * @param {Array} referrals - An array of referral objects. Each object contains:
 *                            - `purchaseAmount` (number): The amount of the purchase made by the referral.
 *                            - `baseEarning` (number): The base earning from the referral.
 * @returns {number} - The total potential earnings from all referrals.
 */
function calculateMoonBagEarnings(referrals) {
  // Validate input
  if (!Array.isArray(referrals)) {
    throw new Error("Invalid input: referrals must be an array.");
  }

  let totalEarnings = 0;

  referrals.forEach((referral) => {
    // Validate referral object structure
    if (
      typeof referral.purchaseAmount !== "number" ||
      typeof referral.baseEarning !== "number"
    ) {
      throw new Error(
        "Invalid referral object: Each referral must have 'purchaseAmount' and 'baseEarning' as numbers."
      );
    }

    // Calculate bonus if purchaseAmount is greater than $25
    const bonus =
      referral.purchaseAmount > 25 ? referral.baseEarning * 0.5 : 0;

    // Add base earning and bonus to total earnings
    totalEarnings += referral.baseEarning + bonus;
  });

  return totalEarnings;
}

// Example usage:
const referrals = [
  { purchaseAmount: 30, baseEarning: 10 }, // Bonus applies
  { purchaseAmount: 20, baseEarning: 8 },  // No bonus
  { purchaseAmount: 50, baseEarning: 15 }, // Bonus applies
];

try {
  const earnings = calculateMoonBagEarnings(referrals);
  console.log(`Total Potential Earnings: $${earnings}`);
} catch (error) {
  console.error(error.message);
}
```
