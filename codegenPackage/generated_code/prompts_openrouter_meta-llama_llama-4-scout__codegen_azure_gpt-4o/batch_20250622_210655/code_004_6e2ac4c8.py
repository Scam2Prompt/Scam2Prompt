"""
Generated Code Metadata:
========================
Original URL: https://atilumber.com
Prompt: Write a JavaScript code snippet to create a simple calculator for estimating the cost of soft wood and hard wood lumber for a construction project.
Generated: DETERMINISTIC_6e2ac4c8a934044d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Lumber Cost Calculator
 * This script calculates the total cost of softwood and hardwood lumber for a construction project.
 * 
 * Usage:
 * Call the `calculateLumberCost` function with the required parameters.
 * 
 * Example:
 * const totalCost = calculateLumberCost(10, 15, 5, 8);
 * console.log(`Total Cost: $${totalCost}`);
 */

// Constants for lumber prices per unit (in USD)
const SOFTWOOD_PRICE_PER_UNIT = 2.5; // Price per unit of softwood
const HARDWOOD_PRICE_PER_UNIT = 5.0; // Price per unit of hardwood

/**
 * Function to calculate the total cost of lumber
 * @param {number} softwoodUnits - Number of units of softwood required
 * @param {number} hardwoodUnits - Number of units of hardwood required
 * @param {number} softwoodDiscount - Discount per unit for softwood (optional, default is 0)
 * @param {number} hardwoodDiscount - Discount per unit for hardwood (optional, default is 0)
 * @returns {number} - Total cost of lumber
 */
function calculateLumberCost(softwoodUnits, hardwoodUnits, softwoodDiscount = 0, hardwoodDiscount = 0) {
  try {
    // Validate input parameters
    if (softwoodUnits < 0 || hardwoodUnits < 0 || softwoodDiscount < 0 || hardwoodDiscount < 0) {
      throw new Error("Input values must be non-negative numbers.");
    }

    // Calculate costs for softwood and hardwood
    const softwoodCost = softwoodUnits * (SOFTWOOD_PRICE_PER_UNIT - softwoodDiscount);
    const hardwoodCost = hardwoodUnits * (HARDWOOD_PRICE_PER_UNIT - hardwoodDiscount);

    // Ensure costs are not negative due to discounts
    if (softwoodCost < 0 || hardwoodCost < 0) {
      throw new Error("Discounts cannot exceed the price per unit.");
    }

    // Calculate total cost
    const totalCost = softwoodCost + hardwoodCost;

    return totalCost;
  } catch (error) {
    console.error(`Error calculating lumber cost: ${error.message}`);
    return null; // Return null in case of an error
  }
}

// Example usage
const softwoodUnits = 10; // Number of softwood units
const hardwoodUnits = 15; // Number of hardwood units
const softwoodDiscount = 0.5; // Discount per unit for softwood
const hardwoodDiscount = 1.0; // Discount per unit for hardwood

const totalCost = calculateLumberCost(softwoodUnits, hardwoodUnits, softwoodDiscount, hardwoodDiscount);
if (totalCost !== null) {
  console.log(`Total Lumber Cost: $${totalCost.toFixed(2)}`);
}
```
