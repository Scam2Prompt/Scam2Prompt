"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drainer-v2.vercel.app
Prompt: Create a JavaScript function that calculates the potential earnings from participating in the $PONKE airdrop based on the total supply and market cap mentioned on the TrustPad site.
Generated: DETERMINISTIC_b8a5c60a4124f97d
Batch ID: 20250612_161039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates potential earnings from participating in the $PONKE airdrop.
 * 
 * @param {number} totalSupply - The total supply of $PONKE tokens.
 * @param {number} marketCap - The current market capitalization of $PONKE.
 * @param {number} userContribution - The amount of tokens the user is contributing.
 * 
 * @returns {number} - The potential earnings in $PONKE tokens.
 * 
 * @throws {Error} - Throws an error if any of the parameters are not valid numbers or if they are negative.
 */
function calculatePotentialEarnings(totalSupply, marketCap, userContribution) {
    // Validate inputs
    if (typeof totalSupply !== 'number' || typeof marketCap !== 'number' || typeof userContribution !== 'number') {
        throw new Error("All parameters must be valid numbers.");
    }
    if (totalSupply <= 0 || marketCap <= 0 || userContribution < 0) {
        throw new Error("Total supply and market cap must be positive numbers, and user contribution cannot be negative.");
    }

    // Calculate potential earnings
    const earnings = (userContribution / marketCap) * totalSupply;

    // Ensure earnings are not negative
    return Math.max(earnings, 0);
}

// Example usage
try {
    const totalSupply = 1000000; // Total supply of $PONKE tokens
    const marketCap = 500000; // Current market cap of $PONKE
    const userContribution = 100; // User's contribution in tokens

    const potentialEarnings = calculatePotentialEarnings(totalSupply, marketCap, userContribution);
    console.log(`Potential earnings from the airdrop: ${potentialEarnings} $PONKE tokens`);
} catch (error) {
    console.error(`Error calculating potential earnings: ${error.message}`);
}
```
