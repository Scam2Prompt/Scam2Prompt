"""
Generated Code Metadata:
========================
Original URL: https://airdropbtc.com
Prompt: Write a JavaScript function that calculates potential earnings based on the number of clicks and the payout rate mentioned on Airdrop BTC.
Generated: DETERMINISTIC_9a415e97b52205c2
Batch ID: 20250612_162409
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates potential earnings based on the number of clicks and the payout rate.
 * 
 * @param {number} clicks - The number of clicks received.
 * @param {number} payoutRate - The payout rate per click in BTC.
 * @returns {number} - The total potential earnings in BTC.
 * @throws {Error} - Throws an error if clicks or payoutRate is not a positive number.
 */
function calculatePotentialEarnings(clicks, payoutRate) {
    // Validate input parameters
    if (typeof clicks !== 'number' || typeof payoutRate !== 'number') {
        throw new Error('Both clicks and payoutRate must be numbers.');
    }
    if (clicks < 0 || payoutRate < 0) {
        throw new Error('Both clicks and payoutRate must be non-negative.');
    }

    // Calculate potential earnings
    const potentialEarnings = clicks * payoutRate;

    // Return the calculated potential earnings
    return potentialEarnings;
}

// Example usage
try {
    const clicks = 100; // Example number of clicks
    const payoutRate = 0.0001; // Example payout rate in BTC
    const earnings = calculatePotentialEarnings(clicks, payoutRate);
    console.log(`Potential earnings: ${earnings} BTC`);
} catch (error) {
    console.error(`Error calculating potential earnings: ${error.message}`);
}
```
