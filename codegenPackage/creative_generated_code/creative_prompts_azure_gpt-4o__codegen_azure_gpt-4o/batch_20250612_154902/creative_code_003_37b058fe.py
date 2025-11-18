"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniair.id
Prompt: Create a function in JavaScript to automate cargo insurance calculations based on Uniair Cargo's brokerage services for accidental damage coverage.
Generated: DETERMINISTIC_37b058fe04d1ea63
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate cargo insurance cost based on Uniair Cargo's brokerage services.
 * 
 * @param {number} cargoValue - The total value of the cargo (in USD).
 * @param {number} coverageRate - The insurance coverage rate (percentage as a decimal: e.g., 0.02 for 2%).
 * @returns {number} insuranceCost - The calculated insurance cost.
 * @throws {Error} Throws an error if input values are invalid.
 */
function calculateCargoInsurance(cargoValue, coverageRate) {
  // Validate cargoValue
  if (typeof cargoValue !== 'number' || cargoValue <= 0) {
    throw new Error("Invalid cargo value. It must be a positive number.");
  }

  // Validate coverageRate
  if (typeof coverageRate !== 'number' || coverageRate <= 0 || coverageRate > 1) {
    throw new Error("Invalid coverage rate. It must be a positive decimal between 0 and 1.");
  }

  // Calculate insurance cost
  const insuranceCost = cargoValue * coverageRate;

  // Ensure result is rounded to two decimal places for currency formatting
  return parseFloat(insuranceCost.toFixed(2));
}

// Example usage:
try {
  const cargoValue = 5000; // Example cargo value in USD
  const coverageRate = 0.02; // Example coverage rate (2%)
  const insuranceCost = calculateCargoInsurance(cargoValue, coverageRate);
  console.log(`The insurance cost for a cargo value of $${cargoValue} at a ${coverageRate * 100}% coverage rate is $${insuranceCost}.`);
} catch (error) {
  console.error(`Error calculating cargo insurance: ${error.message}`);
}
```
