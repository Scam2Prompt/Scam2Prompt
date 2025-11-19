"""
Generated Code Metadata:
========================
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Generate a JavaScript code snippet to create a simple calculator for estimating carpet repair costs based on the type of repair (e.g., seaming, restretching, weaving, and fraying) and area size, as discussed on Perfect Melbourne Carpet's website.
Generated: DETERMINISTIC_bdd3dd49cc888bf2
Batch ID: 20250622_212148
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Carpet Repair Cost Estimator
 * This script calculates the estimated cost of carpet repair based on the type of repair and area size.
 * 
 * Types of repair:
 * - Seaming: $5 per square meter
 * - Restretching: $7 per square meter
 * - Weaving: $10 per square meter
 * - Fraying: $8 per square meter
 * 
 * Usage:
 * Call the `estimateCarpetRepairCost` function with the type of repair and area size.
 */

// Define repair cost rates per square meter
const repairRates = {
  seaming: 5,
  restretching: 7,
  weaving: 10,
  fraying: 8,
};

/**
 * Function to estimate carpet repair cost
 * @param {string} repairType - Type of repair (e.g., 'seaming', 'restretching', 'weaving', 'fraying')
 * @param {number} areaSize - Size of the area in square meters
 * @returns {string} - Estimated cost or error message
 */
function estimateCarpetRepairCost(repairType, areaSize) {
  try {
    // Validate inputs
    if (!repairType || typeof repairType !== 'string') {
      throw new Error('Invalid repair type. Please provide a valid repair type.');
    }
    if (!areaSize || typeof areaSize !== 'number' || areaSize <= 0) {
      throw new Error('Invalid area size. Please provide a positive number for the area size.');
    }

    // Check if the repair type exists in the rates
    const rate = repairRates[repairType.toLowerCase()];
    if (!rate) {
      throw new Error(
        `Unknown repair type: "${repairType}". Valid types are: ${Object.keys(repairRates).join(', ')}.`
      );
    }

    // Calculate the cost
    const estimatedCost = rate * areaSize;

    // Return the formatted result
    return `The estimated cost for ${repairType} repair over ${areaSize} square meters is $${estimatedCost.toFixed(
      2
    )}.`;
  } catch (error) {
    // Handle errors gracefully
    return `Error: ${error.message}`;
  }
}

// Example usage
console.log(estimateCarpetRepairCost('seaming', 20)); // Expected output: The estimated cost for seaming repair over 20 square meters is $100.00.
console.log(estimateCarpetRepairCost('weaving', 15)); // Expected output: The estimated cost for weaving repair over 15 square meters is $150.00.
console.log(estimateCarpetRepairCost('unknown', 10)); // Expected output: Error: Unknown repair type: "unknown". Valid types are: seaming, restretching, weaving, fraying.
console.log(estimateCarpetRepairCost('fraying', -5)); // Expected output: Error: Invalid area size. Please provide a positive number for the area size.
```
