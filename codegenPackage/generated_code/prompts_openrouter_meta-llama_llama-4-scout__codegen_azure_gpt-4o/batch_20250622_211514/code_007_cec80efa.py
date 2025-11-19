"""
Generated Code Metadata:
========================
Original URL: https://clarkconstructionllc.net
Prompt: Write a JavaScript code snippet to create a simple calculator for estimating the cost of painting and drywall services offered by Clark Construction LLC.
Generated: DETERMINISTIC_cec80efad102c581
Batch ID: 20250622_211514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Clark Construction LLC - Painting and Drywall Cost Estimator
 * This script calculates the estimated cost for painting and drywall services.
 * 
 * Services:
 * - Painting: $1.50 per square foot
 * - Drywall: $2.00 per square foot
 * 
 * Usage:
 * Call `calculateCost(paintingArea, drywallArea)` with the respective areas in square feet.
 */

// Constants for service rates
const PAINTING_RATE_PER_SQFT = 1.50; // Cost per square foot for painting
const DRYWALL_RATE_PER_SQFT = 2.00; // Cost per square foot for drywall

/**
 * Validates the input to ensure it is a positive number.
 * @param {number} value - The value to validate.
 * @returns {boolean} - True if the value is valid, false otherwise.
 */
function isValidInput(value) {
  return typeof value === 'number' && value >= 0;
}

/**
 * Calculates the total cost for painting and drywall services.
 * @param {number} paintingArea - The area in square feet to be painted.
 * @param {number} drywallArea - The area in square feet for drywall installation.
 * @returns {string} - The formatted cost estimate or an error message.
 */
function calculateCost(paintingArea, drywallArea) {
  // Validate inputs
  if (!isValidInput(paintingArea) || !isValidInput(drywallArea)) {
    return 'Error: Both paintingArea and drywallArea must be non-negative numbers.';
  }

  // Calculate costs
  const paintingCost = paintingArea * PAINTING_RATE_PER_SQFT;
  const drywallCost = drywallArea * DRYWALL_RATE_PER_SQFT;
  const totalCost = paintingCost + drywallCost;

  // Return formatted result
  return `Cost Estimate:
  - Painting: $${paintingCost.toFixed(2)}
  - Drywall: $${drywallCost.toFixed(2)}
  - Total: $${totalCost.toFixed(2)}`;
}

// Example usage
const paintingArea = 500; // Example painting area in square feet
const drywallArea = 300;  // Example drywall area in square feet
console.log(calculateCost(paintingArea, drywallArea));
```
