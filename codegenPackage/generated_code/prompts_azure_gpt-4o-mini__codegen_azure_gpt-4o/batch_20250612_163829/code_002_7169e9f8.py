"""
Generated Code Metadata:
========================
Original URL: https://moonhop.pages.dev
Prompt: Create a JavaScript function that generates a unique referral code for the MOONHOP referral program and tracks the number of referrals.
Generated: DETERMINISTIC_7169e9f8ac1e62b8
Batch ID: 20250612_163829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * MOONHOP Referral Program
 * This module generates unique referral codes and tracks the number of referrals.
 */

// Object to store referral data
const referralData = {};

/**
 * Generates a unique referral code for a user.
 * @param {string} userId - The unique identifier for the user.
 * @returns {string} - A unique referral code.
 */
function generateReferralCode(userId) {
  if (!userId || typeof userId !== 'string') {
    throw new Error('Invalid userId. It must be a non-empty string.');
  }

  // Generate a unique referral code using userId and a random string
  const randomString = Math.random().toString(36).substring(2, 8).toUpperCase();
  const referralCode = `${userId}-${randomString}`;

  // Ensure the referral code is unique
  if (referralData[referralCode]) {
    return generateReferralCode(userId); // Retry if collision occurs
  }

  // Initialize referral count for the new code
  referralData[referralCode] = 0;

  return referralCode;
}

/**
 * Tracks a referral for a given referral code.
 * @param {string} referralCode - The referral code to track.
 * @returns {number} - The updated referral count.
 */
function trackReferral(referralCode) {
  if (!referralCode || typeof referralCode !== 'string') {
    throw new Error('Invalid referralCode. It must be a non-empty string.');
  }

  if (!referralData[referralCode]) {
    throw new Error('Referral code not found.');
  }

  // Increment the referral count
  referralData[referralCode] += 1;

  return referralData[referralCode];
}

/**
 * Retrieves the referral count for a given referral code.
 * @param {string} referralCode - The referral code to query.
 * @returns {number} - The current referral count.
 */
function getReferralCount(referralCode) {
  if (!referralCode || typeof referralCode !== 'string') {
    throw new Error('Invalid referralCode. It must be a non-empty string.');
  }

  if (!referralData[referralCode]) {
    throw new Error('Referral code not found.');
  }

  return referralData[referralCode];
}

// Example usage:
// const code = generateReferralCode('user123');
// console.log(`Generated Code: ${code}`);
// trackReferral(code);
// console.log(`Referral Count: ${getReferralCount(code)}`);
```
