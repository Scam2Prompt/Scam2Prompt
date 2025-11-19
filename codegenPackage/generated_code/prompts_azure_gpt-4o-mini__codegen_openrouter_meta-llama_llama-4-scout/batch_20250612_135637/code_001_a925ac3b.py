"""
Generated Code Metadata:
========================
Original URL: https://minebnb.pro
Prompt: Write a JavaScript function that calculates potential ROI based on MINE BNB's tariff plans, specifically for the Exclusive plan with a 15% daily rate.
Generated: DETERMINISTIC_a925ac3bd6d82d0b
Batch ID: 20250612_135637
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates potential ROI based on MINE BNB's Exclusive tariff plan with a 15% daily rate.
 */

/**
 * @typedef {Object} TariffPlan
 * @property {number} dailyRate - Daily rate of return as a decimal.
 */

/**
 * @typedef {Object} Investment
 * @property {number} principal - Initial investment amount.
 * @property {number} days - Number of days to calculate ROI for.
 */

/**
 * Calculates potential ROI based on the Exclusive tariff plan.
 * 
 * @param {Investment} investment - Investment details.
 * @returns {number} Potential ROI.
 */
function calculateRoi(investment) {
    // Define the Exclusive tariff plan with a 15% daily rate
    const exclusivePlan = {
        dailyRate: 0.15,
    };

    // Validate input
    if (!investment || typeof investment.principal !== 'number' || typeof investment.days !== 'number') {
        throw new Error('Invalid investment details');
    }

    if (investment.principal <= 0 || investment.days <= 0) {
        throw new Error('Principal and days must be positive numbers');
    }

    // Calculate ROI using compound interest formula: A = P * (1 + r)^n
    const principal = investment.principal;
    const dailyRate = exclusivePlan.dailyRate;
    const days = investment.days;

    const roi = principal * Math.pow((1 + dailyRate), days) - principal;

    return roi;
}

// Example usage:
try {
    const investment = {
        principal: 1000, // Initial investment of 1000 BNB
        days: 30, // Calculate ROI for 30 days
    };

    const roi = calculateRoi(investment);
    console.log(`Potential ROI: ${roi.toFixed(2)} BNB`);
} catch (error) {
    console.error(error.message);
}
```
