"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prospectlimited.com
Prompt: Create a JavaScript program to calculate referral earnings based on Prospect Limited's referral program structure, including tiered income levels.
Generated: DETERMINISTIC_460b8682aa4a3053
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Referral Earnings Calculator for Prospect Limited's Referral Program

/**
 * Function to calculate referral earnings based on a tiered structure.
 * @param {number} directReferrals - Number of direct referrals made by the user.
 * @param {number} secondLevelReferrals - Number of referrals made by the direct referrals (2nd tier).
 * @param {number} thirdLevelReferrals - Number of referrals made by the 2nd tier referrals (3rd tier).
 * @returns {number} - Total earnings from all tiers.
 */
function calculateReferralEarnings(directReferrals, secondLevelReferrals, thirdLevelReferrals) {
  // Define the earnings for each tier
  const tier1EarningPerReferral = 50; // Earnings for direct referrals
  const tier2EarningPerReferral = 20; // Earnings for second-level referrals
  const tier3EarningPerReferral = 10; // Earnings for third-level referrals

  // Input validation
  if (
    typeof directReferrals !== 'number' ||
    typeof secondLevelReferrals !== 'number' ||
    typeof thirdLevelReferrals !== 'number' ||
    directReferrals < 0 ||
    secondLevelReferrals < 0 ||
    thirdLevelReferrals < 0
  ) {
    throw new Error('Invalid input: All referral counts must be non-negative numbers.');
  }

  // Calculate earnings for each tier
  const tier1Earnings = directReferrals * tier1EarningPerReferral;
  const tier2Earnings = secondLevelReferrals * tier2EarningPerReferral;
  const tier3Earnings = thirdLevelReferrals * tier3EarningPerReferral;

  // Calculate total earnings
  const totalEarnings = tier1Earnings + tier2Earnings + tier3Earnings;

  return totalEarnings;
}

// Example usage
try {
  // Inputs
  const directReferrals = 5; // Number of direct referrals
  const secondLevelReferrals = 10; // Number of second-level referrals
  const thirdLevelReferrals = 15; // Number of third-level referrals

  // Calculate earnings
  const totalEarnings = calculateReferralEarnings(
    directReferrals,
    secondLevelReferrals,
    thirdLevelReferrals
  );

  // Output the result
  console.log(`Total Referral Earnings: $${totalEarnings}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
