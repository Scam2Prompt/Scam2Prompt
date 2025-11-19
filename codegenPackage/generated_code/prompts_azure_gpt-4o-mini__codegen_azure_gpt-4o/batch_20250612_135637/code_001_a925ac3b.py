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
 * Function to calculate potential ROI (Return on Investment) for MINE BNB's Exclusive plan.
 * The Exclusive plan offers a 15% daily rate.
 *
 * @param {number} initialInvestment - The initial amount invested (in BNB).
 * @param {number} days - The number of days the investment is held.
 * @returns {number} - The potential ROI after the specified number of days.
 * @throws {Error} - Throws an error if input values are invalid.
 */
function calculateExclusivePlanROI(initialInvestment, days) {
  // Validate input parameters
  if (typeof initialInvestment !== 'number' || initialInvestment <= 0) {
    throw new Error('Invalid initial investment amount. It must be a positive number.');
  }
  if (typeof days !== 'number' || days <= 0) {
    throw new Error('Invalid number of days. It must be a positive integer.');
  }

  // Define the daily rate for the Exclusive plan
  const dailyRate = 0.15;

  // Calculate ROI using compound interest formula
  const roi = initialInvestment * Math.pow(1 + dailyRate, days);

  // Return the calculated ROI
  return roi;
}

// Example usage:
try {
  const initialInvestment = 10; // Example: 10 BNB
  const days = 30; // Example: 30 days
  const potentialROI = calculateExclusivePlanROI(initialInvestment, days);
  console.log(`Potential ROI after ${days} days: ${potentialROI.toFixed(2)} BNB`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
