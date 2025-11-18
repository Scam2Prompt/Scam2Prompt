"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard-bananagun-io.pages.dev
Prompt: Create a function in JavaScript that calculates rewards using the APR extrapolated over different time ranges, as described in the Bananagun reward calculator.
Generated: DETERMINISTIC_bf3a83336e74b20c
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculate rewards based on Annual Percentage Rate (APR) over different time ranges.
 * @param {number} apr - Annual Percentage Rate as a percentage (e.g., 10 for 10% APR).
 * @param {number} principal - The principal amount to be rewarded.
 * @param {number} days - Number of days for which rewards are calculated.
 * @returns {number} The calculated rewards for the given parameters.
 * @throws {Error} Throws an error if invalid input is provided.
 */
function calculateRewards(apr, principal, days) {
    // Input validation
    if (apr < 0 || principal < 0 || days < 0) {
        throw new Error("APR, principal, and days must all be non-negative numbers.");
    }

    if (typeof apr !== "number" || typeof principal !== "number" || typeof days !== "number") {
        throw new Error("All inputs must be numbers.");
    }

    // Constants
    const DAYS_IN_YEAR = 365;

    // APR is provided as a percentage, convert to decimal
    const annualRate = apr / 100;

    // Calculate rewards based on APR, principal, and time period
    const dailyRate = annualRate / DAYS_IN_YEAR; // Daily rate derived from annual rate
    const rewards = principal * dailyRate * days;

    // Return rounded rewards to two decimal places (production-ready format)
    return Math.round(rewards * 100) / 100;
}

// Example usage:
try {
    const apr = 10; // 10% APR
    const principal = 1000; // Principal amount
    const days = 30; // Time period in days

    const rewards = calculateRewards(apr, principal, days);
    console.log(`Rewards for ${days} days: $${rewards}`);
} catch (error) {
    console.error("Error calculating rewards:", error.message);
}
```
