"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fxoption-int.com
Prompt: Write a JavaScript function that calculates potential returns based on the investment plan selected at FX Option INT, considering the 50%+ ROI mentioned on the site.
Generated: DETERMINISTIC_16efa2e8c4fa75f8
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the potential returns based on the investment plan selected
 * at FX Option INT, considering a minimum of 50% Return on Investment (ROI).
 * 
 * @param {number} initialInvestment - The amount of money invested.
 * @param {number} roiPercentage - The percentage of return on investment (default is 50%).
 * @returns {number} - The total amount after applying the ROI.
 * @throws {Error} - Throws an error if the initialInvestment is not a positive number.
 */
function calculatePotentialReturns(initialInvestment, roiPercentage = 50) {
    // Validate input: Check if initialInvestment is a positive number
    if (typeof initialInvestment !== 'number' || initialInvestment <= 0) {
        throw new Error('Initial investment must be a positive number.');
    }

    // Validate ROI percentage: Check if roiPercentage is a number and non-negative
    if (typeof roiPercentage !== 'number' || roiPercentage < 0) {
        throw new Error('ROI percentage must be a non-negative number.');
    }

    // Calculate potential returns
    const potentialReturns = initialInvestment + (initialInvestment * (roiPercentage / 100));

    return potentialReturns;
}

// Example usage:
try {
    const initialInvestment = 1000; // Example initial investment amount
    const roi = 50; // Example ROI percentage
    const returns = calculatePotentialReturns(initialInvestment, roi);
    console.log(`The potential returns for an investment of $${initialInvestment} at ${roi}% ROI is $${returns}.`);
} catch (error) {
    console.error(`Error calculating potential returns: ${error.message}`);
}
```
