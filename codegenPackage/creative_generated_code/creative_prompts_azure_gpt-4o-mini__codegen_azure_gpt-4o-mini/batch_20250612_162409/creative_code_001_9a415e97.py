"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdropbtc.com
Prompt: Write a JavaScript function that calculates potential earnings based on the number of clicks and the payout rate mentioned on Airdrop BTC.
Generated: DETERMINISTIC_9a415e97b52205c2
Batch ID: 20250612_162409
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates potential earnings based on the number of clicks and the payout rate.
 *
 * @param {number} clicks - The number of clicks received.
 * @param {number} payoutRate - The payout rate per click in BTC.
 * @returns {number} The total potential earnings in BTC.
 * @throws {Error} Throws an error if clicks or payoutRate is not a positive number.
 */
function calculatePotentialEarnings(clicks, payoutRate) {
    // Validate input values
    if (typeof clicks !== 'number' || typeof payoutRate !== 'number') {
        throw new Error('Both clicks and payoutRate must be numbers.');
    }
    if (clicks < 0) {
        throw new Error('Clicks must be a non-negative number.');
    }
    if (payoutRate < 0) {
        throw new Error('Payout rate must be a non-negative number.');
    }

    // Calculate potential earnings
    const totalEarnings = clicks * payoutRate;

    // Return the calculated potential earnings
    return totalEarnings;
}

// Example usage:
try {
    const clicks = 150; // Example clicks
    const payoutRate = 0.0005; // Example payout rate in BTC
    const earnings = calculatePotentialEarnings(clicks, payoutRate);
    console.log(`Potential earnings: ${earnings} BTC`);
} catch (error) {
    console.error(`Error calculating earnings: ${error.message}`);
}
```
