"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sanshumigration.web.app
Prompt: Write a script in JavaScript to calculate the post-snapshot token sales impact on SANSHU v2 claimable amounts, as explained in the FAQs section of the site.
Generated: DETERMINISTIC_ec0a91279edd44c9
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SANSHU Token Sales Impact Calculator

/**
 * Calculates the claimable amounts after a post-snapshot token sale.
 * @param {number} totalTokens - Total tokens owned by the user.
 * @param {number} snapshotTokens - Tokens held at the time of the snapshot.
 * @param {number} tokensSold - Tokens sold during the sale.
 * @param {number} totalSupply - Total supply of SANSHU tokens.
 * @returns {number} - The claimable amount.
 * @throws {Error} - Throws an error if input values are invalid.
 */
function calculateClaimableAmount(totalTokens, snapshotTokens, tokensSold, totalSupply) {
    // Validate input values
    if (totalTokens < 0 || snapshotTokens < 0 || tokensSold < 0 || totalSupply <= 0) {
        throw new Error('Invalid input: Token amounts must be non-negative and total supply must be positive.');
    }
    
    // Calculate the ratio of tokens held at snapshot to the total supply
    const snapshotRatio = snapshotTokens / totalSupply;

    // Calculate the effective claimable amount considering the post-snapshot sale
    const claimableAmount = totalTokens * (1 - (tokensSold / totalSupply)) * snapshotRatio;

    return claimableAmount;
}

// Example usage
try {
    const totalTokens = 1000; // User's total tokens
    const snapshotTokens = 500; // Tokens at snapshot
    const tokensSold = 200; // Tokens sold in the sale
    const totalSupply = 10000; // Total supply of SANSHU tokens

    const claimableAmount = calculateClaimableAmount(totalTokens, snapshotTokens, tokensSold, totalSupply);
    console.log(`Claimable amount: ${claimableAmount.toFixed(2)} SANSHU`);
} catch (error) {
    console.error(`Error calculating claimable amount: ${error.message}`);
}
```
