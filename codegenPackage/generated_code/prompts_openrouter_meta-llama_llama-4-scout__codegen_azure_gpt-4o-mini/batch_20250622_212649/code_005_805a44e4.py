"""
Generated Code Metadata:
========================
Original URL: https://unichain-rooster.nfts2.me
Prompt: Create a JavaScript function to calculate referral earnings for an NFT collection on Unichain, based on the number of mints made through a referrer's link.
Generated: DETERMINISTIC_805a44e4fe27f683
Batch ID: 20250622_212649
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates referral earnings for an NFT collection on Unichain.
 * 
 * @param {number} mints - The number of mints made through the referrer's link.
 * @param {number} earningsPerMint - The earnings generated per mint.
 * @returns {number} - The total referral earnings.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculateReferralEarnings(mints, earningsPerMint) {
    // Validate inputs
    if (typeof mints !== 'number' || typeof earningsPerMint !== 'number') {
        throw new Error('Both mints and earningsPerMint must be numbers.');
    }
    if (mints < 0 || earningsPerMint < 0) {
        throw new Error('Both mints and earningsPerMint must be non-negative.');
    }

    // Calculate total earnings
    const totalEarnings = mints * earningsPerMint;

    // Return the calculated earnings
    return totalEarnings;
}

// Example usage
try {
    const mints = 10; // Number of mints through the referrer's link
    const earningsPerMint = 0.05; // Earnings per mint in ETH
    const earnings = calculateReferralEarnings(mints, earningsPerMint);
    console.log(`Total referral earnings: ${earnings} ETH`);
} catch (error) {
    console.error(`Error calculating referral earnings: ${error.message}`);
}
```
