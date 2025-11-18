"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://freebitcoinmining.website
Prompt: Build a JavaScript function to calculate the BTC/minute and BTC/day earnings for each mining plan, using the rates provided by FreeBitcoinMining.
Generated: DETERMINISTIC_987ecc5995c0955e
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate BTC earnings for mining plans.
 * 
 * @param {Array} miningPlans - Array of mining plans with the following structure:
 *                              [{ name: 'Plan A', rate: 0.000001 }, { name: 'Plan B', rate: 0.000005 }, ...]
 * @returns {Array} - Array of objects containing earnings per minute and per day for each plan.
 *                    [{ name: 'Plan A', btcPerMinute: 0.000001, btcPerDay: 0.00144 }, ...]
 */
function calculateMiningEarnings(miningPlans) {
    // Validate input
    if (!Array.isArray(miningPlans)) {
        throw new Error('Invalid input: miningPlans must be an array.');
    }

    // Constants for time conversion
    const MINUTES_IN_DAY = 1440; // 24 hours * 60 minutes

    // Result array to store calculated earnings for each plan
    const earnings = miningPlans.map(plan => {
        // Validate each plan's structure
        if (!plan.name || typeof plan.rate !== 'number') {
            throw new Error('Invalid mining plan structure. Each plan must have a name and a numeric rate.');
        }

        // Calculate BTC earnings per minute and per day
        const btcPerMinute = plan.rate;
        const btcPerDay = btcPerMinute * MINUTES_IN_DAY;

        // Return the mining plan's earnings
        return {
            name: plan.name,
            btcPerMinute,
            btcPerDay
        };
    });

    return earnings;
}

// Example usage:
const miningPlans = [
    { name: 'Basic Plan', rate: 0.000001 },
    { name: 'Pro Plan', rate: 0.000005 },
    { name: 'Elite Plan', rate: 0.00001 }
];

try {
    const earnings = calculateMiningEarnings(miningPlans);
    console.log(earnings);
    // Output:
    // [
    //   { name: 'Basic Plan', btcPerMinute: 0.000001, btcPerDay: 0.00144 },
    //   { name: 'Pro Plan', btcPerMinute: 0.000005, btcPerDay: 0.0072 },
    //   { name: 'Elite Plan', btcPerMinute: 0.00001, btcPerDay: 0.0144 }
    // ]
} catch (error) {
    console.error('Error calculating earnings:', error.message);
}
```
