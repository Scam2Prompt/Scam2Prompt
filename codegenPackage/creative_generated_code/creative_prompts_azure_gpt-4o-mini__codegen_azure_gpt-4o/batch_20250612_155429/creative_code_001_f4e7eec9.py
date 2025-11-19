"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zircuitzrc.com
Prompt: Write a JavaScript function that calculates the estimated cost of cleaning services based on the size of the house and the frequency of visits, as described on Zrc Inc's website.
Generated: DETERMINISTIC_f4e7eec9ec231ea9
Batch ID: 20250612_155429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the estimated cost of cleaning services.
 * 
 * @param {number} houseSize - The size of the house in square feet.
 * @param {number} frequency - The frequency of cleaning visits per month.
 * @returns {number} - The estimated cost of cleaning services.
 * @throws {Error} - Throws an error if input parameters are invalid.
 */
function calculateCleaningCost(houseSize, frequency) {
  // Validate inputs
  if (typeof houseSize !== 'number' || houseSize <= 0) {
    throw new Error("Invalid house size. Please provide a positive number.");
  }
  if (typeof frequency !== 'number' || frequency <= 0) {
    throw new Error("Invalid frequency. Please provide a positive number.");
  }

  // Base rate per square foot
  const baseRatePerSquareFoot = 0.10; // Example: $0.10 per square foot
  // Discount rate per visit frequency
  const frequencyDiscounts = {
    1: 1.0,   // No discount for once a month
    2: 0.95,  // 5% discount for twice a month
    4: 0.90,  // 10% discount for four times a month
  };

  // Determine discount based on frequency
  const discount = frequencyDiscounts[frequency] || 0.85; // Default: 15% discount for frequent visits

  // Calculate the total cost
  const cost = houseSize * baseRatePerSquareFoot * discount;

  // Return rounded cost for simplicity
  return parseFloat(cost.toFixed(2));
}

// Example usage:
try {
  const estimatedCost = calculateCleaningCost(1500, 2); // 1500 sq ft, twice a month
  console.log(`Estimated cost: $${estimatedCost}`);
} catch (error) {
  console.error(error.message);
}
```
