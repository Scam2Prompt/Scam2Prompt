"""
Generated Code Metadata:
========================
Original URL: https://globalfxoption.com
Prompt: Create a JavaScript function that calculates potential ROI based on the investment plans outlined by Global FX Option, including daily percentages for different tiers.
Generated: DETERMINISTIC_cfc3837e4520abe8
Batch ID: 20250612_155651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the potential Return on Investment (ROI) based on the investment plans
 * outlined by Global FX Option. The function takes an investment amount and a tier level,
 * and returns the potential ROI based on predefined daily percentages for each tier.
 *
 * @param {number} investment - The amount of money invested.
 * @param {string} tier - The investment tier ('basic', 'standard', 'premium').
 * @param {number} days - The number of days the investment is held.
 * @returns {number} - The potential ROI after the specified number of days.
 * @throws {Error} - Throws an error if the investment amount is negative or if the tier is invalid.
 */
function calculateROI(investment, tier, days) {
    // Define daily percentage returns for each tier
    const tierRates = {
        basic: 0.01,    // 1% daily return
        standard: 0.02,  // 2% daily return
        premium: 0.03    // 3% daily return
    };

    // Validate input parameters
    if (typeof investment !== 'number' || investment < 0) {
        throw new Error('Investment amount must be a non-negative number.');
    }
    if (typeof tier !== 'string' || !tierRates.hasOwnProperty(tier)) {
        throw new Error('Invalid tier specified. Valid tiers are: basic, standard, premium.');
    }
    if (typeof days !== 'number' || days < 0) {
        throw new Error('Days must be a non-negative number.');
    }

    // Calculate the potential ROI
    const dailyRate = tierRates[tier];
    const potentialROI = investment * Math.pow((1 + dailyRate), days) - investment;

    return potentialROI;
}

// Example usage
try {
    const investmentAmount = 1000; // Example investment amount
    const investmentTier = 'standard'; // Example tier
    const investmentDays = 30; // Example duration in days

    const roi = calculateROI(investmentAmount, investmentTier, investmentDays);
    console.log(`Potential ROI for ${investmentDays} days at ${investmentTier} tier: $${roi.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
