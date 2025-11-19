"""
Generated Code Metadata:
========================
Original URL: https://btcbull.io
Prompt: Create a function in JavaScript to track and calculate $BTCBULL airdrops based on Bitcoin price milestones ($150,000 and $200,000) and user holdings.
Generated: DETERMINISTIC_bbddc070c69d5691
Batch ID: 20250622_212208
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Airdrop Tracker for BTCBULL based on Bitcoin price milestones.
 * 
 * This function calculates the airdrop amount for a user based on their 
 * Bitcoin holdings and the current Bitcoin price. Airdrops are triggered 
 * at price milestones of $150,000 and $200,000.
 * 
 * @param {number} bitcoinPrice - The current price of Bitcoin.
 * @param {number} userHoldings - The amount of Bitcoin the user holds.
 * @returns {object} - An object containing the airdrop details.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculateAirdrop(bitcoinPrice, userHoldings) {
    // Validate inputs
    if (typeof bitcoinPrice !== 'number' || bitcoinPrice <= 0) {
        throw new Error('Invalid Bitcoin price. It must be a positive number.');
    }
    if (typeof userHoldings !== 'number' || userHoldings < 0) {
        throw new Error('Invalid user holdings. It must be a non-negative number.');
    }

    // Initialize airdrop details
    const airdropDetails = {
        milestone: null,
        airdropAmount: 0,
    };

    // Check for price milestones and calculate airdrop
    if (bitcoinPrice >= 200000) {
        airdropDetails.milestone = '$200,000';
        airdropDetails.airdropAmount = userHoldings * 0.1; // 10% airdrop
    } else if (bitcoinPrice >= 150000) {
        airdropDetails.milestone = '$150,000';
        airdropDetails.airdropAmount = userHoldings * 0.05; // 5% airdrop
    }

    // Return airdrop details if any airdrop is applicable
    return airdropDetails.airdropAmount > 0 ? airdropDetails : { message: 'No airdrop available at this price.' };
}

// Example usage
try {
    const currentPrice = 160000; // Example current Bitcoin price
    const userBitcoinHoldings = 2; // Example user holdings in Bitcoin
    const airdrop = calculateAirdrop(currentPrice, userBitcoinHoldings);
    console.log(airdrop);
} catch (error) {
    console.error('Error calculating airdrop:', error.message);
}
```
