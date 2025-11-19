"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalfxoption.com
Prompt: Create a JavaScript function that calculates potential ROI based on the investment plans outlined by Global FX Option, including daily percentages for different tiers.
Generated: DETERMINISTIC_cfc3837e4520abe8
Batch ID: 20250612_155651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the potential Return on Investment (ROI) based on daily percentages for different tiers.
 * 
 * @param {number} investment - The initial amount invested.
 * @param {string} tier - The investment tier ('basic', 'standard', 'premium').
 * @param {number} days - The number of days to calculate the ROI for.
 * @returns {number} - The total potential return after the specified number of days.
 * @throws {Error} - Throws an error if the investment is not a positive number or if the tier is invalid.
 */
function calculateROI(investment, tier, days) {
    // Define the daily percentage returns for each investment tier
    const tiers = {
        basic: 0.01,    // 1% daily return
        standard: 0.02, // 2% daily return
        premium: 0.03   // 3% daily return
    };

    // Check for valid investment amount
    if (typeof investment !== 'number' || investment <= 0) {
        throw new Error('Investment must be a positive number.');
    }

    // Check for valid investment tier
    if (!tiers.hasOwnProperty(tier)) {
        throw new Error('Invalid tier specified. Must be one of: basic, standard, premium.');
    }

    // Check for valid days
    if (typeof days !== 'number' || days <= 0) {
        throw new Error('Days must be a positive number.');
    }

    // Calculate the total return
    const dailyReturnRate = tiers[tier];
    const totalReturn = investment * Math.pow((1 + dailyReturnRate), days);

    // Return the total potential return rounded to two decimal places
    return parseFloat(totalReturn.toFixed(2));
}

// Example usage (Uncomment to test):
// try {
//     const roi = calculateROI(1000, 'standard', 30);
//     console.log(`Potential ROI: $${roi}`);
// } catch (error) {
//     console.error(error.message);
// }
```
