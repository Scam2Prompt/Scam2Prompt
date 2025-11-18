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
 * @function calculateEarnings
 * @description Calculates the BTC earnings per minute and per day for each mining plan based on rates provided by FreeBitcoinMining.
 * @param {Array} miningPlans - An array of mining plan objects where each object contains the 'rate' in BTC/minute.
 * @returns {Array} - An array of objects containing the earnings per minute and per day for each mining plan.
 * @throws {Error} - Throws an error if the input is not an array or if any rate is not a number.
 */

function calculateEarnings(miningPlans) {
    // Validate input
    if (!Array.isArray(miningPlans)) {
        throw new Error("Input must be an array of mining plans.");
    }

    return miningPlans.map(plan => {
        // Validate each plan
        if (typeof plan.rate !== 'number' || plan.rate < 0) {
            throw new Error(`Invalid mining plan rate: ${plan.rate}. Rate must be a non-negative number.`);
        }

        // Calculate earnings
        const earningsPerMinute = plan.rate;
        const earningsPerDay = earningsPerMinute * 60 * 24;

        // Return the earnings details
        return {
            planName: plan.name || "Unnamed Plan",
            earningsPerMinute: earningsPerMinute,
            earningsPerDay: earningsPerDay
        };
    });
}

// Example usage:
try {
    const miningPlans = [
        { name: "Plan A", rate: 0.0001 },
        { name: "Plan B", rate: 0.0002 },
        { name: "Plan C", rate: 0.00005 }
    ];
    
    const earnings = calculateEarnings(miningPlans);
    console.log(earnings);
} catch (error) {
    console.error("Error calculating earnings:", error.message);
}
```
