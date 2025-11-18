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
/**
 * Referral Earnings Calculator for Prospect Limited's Referral Program
 * 
 * This program calculates the earnings based on the number of referrals 
 * made and the tiered income structure defined by the company.
 * 
 * Tiers:
 * - Tier 1: 10% for the first 10 referrals
 * - Tier 2: 15% for referrals 11 to 20
 * - Tier 3: 20% for referrals 21 and above
 * 
 * Usage: 
 * Call `calculateReferralEarnings(referrals, earningsPerReferral)` where 
 * `referrals` is the number of successful referrals and `earningsPerReferral` 
 * is the base earnings for each referral.
 */

/**
 * Calculate the total referral earnings based on the number of referrals
 * and the earnings per referral.
 * 
 * @param {number} referrals - The total number of referrals made.
 * @param {number} earningsPerReferral - The base earnings for each referral.
 * @returns {number} - The total earnings calculated based on tiers.
 * @throws {Error} - Throws an error if `referrals` or `earningsPerReferral` are negative.
 */
function calculateReferralEarnings(referrals, earningsPerReferral) {
    // Validate input parameters
    if (referrals < 0 || earningsPerReferral < 0) {
        throw new Error("Number of referrals and earnings per referral must be non-negative.");
    }

    let totalEarnings = 0;

    // Calculate earnings based on tiers
    if (referrals > 0) {
        // Tier 1: First 10 referrals
        const tier1Referrals = Math.min(referrals, 10);
        totalEarnings += tier1Referrals * earningsPerReferral * 0.10;

        // Tier 2: Referrals 11 to 20
        const tier2Referrals = Math.max(0, Math.min(referrals - 10, 10));
        totalEarnings += tier2Referrals * earningsPerReferral * 0.15;

        // Tier 3: Referrals 21 and above
        const tier3Referrals = Math.max(0, referrals - 20);
        totalEarnings += tier3Referrals * earningsPerReferral * 0.20;
    }

    return totalEarnings;
}

// Example usage
try {
    const referrals = 25; // Example number of referrals
    const earningsPerReferral = 100; // Example earnings per referral in currency
    const totalEarnings = calculateReferralEarnings(referrals, earningsPerReferral);
    console.log(`Total Earnings from ${referrals} referrals: $${totalEarnings.toFixed(2)}`);
} catch (error) {
    console.error(`An error occurred: ${error.message}`);
}
```
