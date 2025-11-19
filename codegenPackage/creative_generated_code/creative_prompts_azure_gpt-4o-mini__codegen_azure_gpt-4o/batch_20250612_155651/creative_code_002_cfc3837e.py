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
 * Function to calculate potential ROI (Return on Investment) based on investment plans.
 * @param {number} principal - The initial investment amount.
 * @param {number} days - The number of days the investment will grow.
 * @param {string} tier - The investment tier (e.g., "Basic", "Standard", "Premium").
 * @returns {number} - The calculated ROI (rounded to two decimal places).
 * @throws Will throw an error if invalid inputs are provided.
 */
function calculateROI(principal, days, tier) {
  // Validate inputs
  if (typeof principal !== 'number' || principal <= 0) {
    throw new Error("Invalid principal amount. Must be a positive number.");
  }
  if (typeof days !== 'number' || days <= 0) {
    throw new Error("Invalid number of days. Must be a positive number.");
  }
  if (typeof tier !== 'string') {
    throw new Error("Invalid tier. Must be a string.");
  }
  
  // Define daily percentage rates for each tier
  const tierRates = {
    Basic: 0.01,     // 1% daily
    Standard: 0.015, // 1.5% daily
    Premium: 0.02    // 2% daily
  };

  // Check if the provided tier exists
  if (!tierRates[tier]) {
    throw new Error("Invalid tier. Available options are: Basic, Standard, Premium.");
  }

  // Calculate ROI
  const dailyRate = tierRates[tier];
  const roi = principal * Math.pow(1 + dailyRate, days);

  // Return the result rounded to two decimal places
  return Number(roi.toFixed(2));
}

// Example usage:
try {
  const principal = 1000; // Initial investment amount
  const days = 30;        // Number of days
  const tier = "Standard"; // Investment tier
  
  const result = calculateROI(principal, days, tier);
  console.log(`Potential ROI: $${result}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
