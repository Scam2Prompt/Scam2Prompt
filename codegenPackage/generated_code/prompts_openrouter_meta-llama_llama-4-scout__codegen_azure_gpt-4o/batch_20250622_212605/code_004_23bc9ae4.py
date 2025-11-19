"""
Generated Code Metadata:
========================
Original URL: https://unichain-pass.nfts2.me
Prompt: Design a JavaScript function to calculate referral fees for an NFT project based on the number of mints completed through a referrer's unique link.
Generated: DETERMINISTIC_23bc9ae46055123a
Batch ID: 20250622_212605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate referral fees for an NFT project.
 * @param {number} mintsCompleted - The number of mints completed through the referrer's unique link.
 * @param {number} mintPrice - The price of a single mint in the NFT project.
 * @param {number} referralRate - The percentage of the mint price awarded as a referral fee (e.g., 0.05 for 5%).
 * @returns {number} - The total referral fee earned by the referrer.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculateReferralFee(mintsCompleted, mintPrice, referralRate) {
  // Input validation
  if (typeof mintsCompleted !== 'number' || mintsCompleted < 0 || !Number.isInteger(mintsCompleted)) {
    throw new Error('Invalid input: mintsCompleted must be a non-negative integer.');
  }
  if (typeof mintPrice !== 'number' || mintPrice <= 0) {
    throw new Error('Invalid input: mintPrice must be a positive number.');
  }
  if (typeof referralRate !== 'number' || referralRate < 0 || referralRate > 1) {
    throw new Error('Invalid input: referralRate must be a number between 0 and 1.');
  }

  // Calculate referral fee
  const totalReferralFee = mintsCompleted * mintPrice * referralRate;

  // Return the result rounded to two decimal places for monetary precision
  return parseFloat(totalReferralFee.toFixed(2));
}

// Example usage:
try {
  const mintsCompleted = 10; // Number of mints completed
  const mintPrice = 0.1; // Price of a single mint (e.g., 0.1 ETH)
  const referralRate = 0.05; // Referral rate (e.g., 5%)

  const referralFee = calculateReferralFee(mintsCompleted, mintPrice, referralRate);
  console.log(`Total Referral Fee: ${referralFee} ETH`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
