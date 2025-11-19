"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welstrade.com
Prompt: Create a function in JavaScript that calculates potential ROI for different investment plans (Basic, Silver, Gold) offered by Welstrade.
Generated: DETERMINISTIC_6a9ba3ce337d93bf
Batch ID: 20250612_160411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate potential ROI for different investment plans offered by Welstrade.
 * 
 * @param {string} plan - The investment plan (Basic, Silver, or Gold).
 * @param {number} principal - The initial investment amount (must be positive).
 * @param {number} years - The investment duration in years (must be positive).
 * @returns {number} - The calculated ROI (Return on Investment) or throws an error for invalid input.
 */
function calculateROI(plan, principal, years) {
    // Validate input
    if (typeof plan !== 'string' || typeof principal !== 'number' || typeof years !== 'number') {
        throw new Error('Invalid input types. Expected (string, number, number).');
    }
    if (principal <= 0 || years <= 0) {
        throw new Error('Principal and years must be positive values.');
    }

    // Define interest rates for each investment plan
    const interestRates = {
        Basic: 0.05,  // 5% annual interest
        Silver: 0.07, // 7% annual interest
        Gold: 0.1     // 10% annual interest
    };

    // Check if the plan is valid
    if (!interestRates.hasOwnProperty(plan)) {
        throw new Error(`Invalid plan. Available plans are: ${Object.keys(interestRates).join(', ')}.`);
    }

    // Calculate ROI using compound interest formula: A = P * (1 + r)^t
    const rate = interestRates[plan];
    const roi = principal * Math.pow((1 + rate), years);

    // Return calculated ROI rounded to two decimal places
    return parseFloat(roi.toFixed(2));
}

// Example usage:
try {
    const plan = 'Silver';     // Investment plan
    const principal = 10000;   // Initial investment amount
    const years = 5;           // Investment duration in years

    const result = calculateROI(plan, principal, years);
    console.log(`Potential ROI for plan ${plan}: $${result}`);
} catch (error) {
    console.error(`Error calculating ROI: ${error.message}`);
}
```
