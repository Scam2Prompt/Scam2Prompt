"""
Generated Code Metadata:
========================
Original URL: https://paintersmorningtonpeninsula.com.au
Prompt: Create a JavaScript code snippet to calculate the cost of a painting project in Mornington Peninsula, considering factors like surface area, paint type, and labor costs, as offered by Prestige Painters Mornington Peninsula.
Generated: DETERMINISTIC_ab2710ff5c251d6f
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculate the cost of a painting project in Mornington Peninsula.
 * Factors considered: surface area, paint type, and labor costs.
 * 
 * @param {number} surfaceArea - The total surface area to be painted (in square meters).
 * @param {string} paintType - The type of paint to be used (e.g., "standard", "premium").
 * @param {number} laborRate - The hourly labor rate (in AUD).
 * @param {number} hoursRequired - The estimated hours required for the project.
 * @returns {number} - The total cost of the painting project (in AUD).
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculatePaintingCost(surfaceArea, paintType, laborRate, hoursRequired) {
  // Validate inputs
  if (typeof surfaceArea !== 'number' || surfaceArea <= 0) {
    throw new Error("Invalid surface area. Must be a positive number.");
  }
  if (typeof paintType !== 'string' || !["standard", "premium"].includes(paintType.toLowerCase())) {
    throw new Error("Invalid paint type. Must be 'standard' or 'premium'.");
  }
  if (typeof laborRate !== 'number' || laborRate <= 0) {
    throw new Error("Invalid labor rate. Must be a positive number.");
  }
  if (typeof hoursRequired !== 'number' || hoursRequired <= 0) {
    throw new Error("Invalid hours required. Must be a positive number.");
  }

  // Define paint cost per square meter based on paint type
  const paintCostPerSquareMeter = {
    standard: 5, // AUD per square meter
    premium: 10  // AUD per square meter
  };

  // Calculate paint cost
  const paintCost = surfaceArea * paintCostPerSquareMeter[paintType.toLowerCase()];

  // Calculate labor cost
  const laborCost = laborRate * hoursRequired;

  // Calculate total cost
  const totalCost = paintCost + laborCost;

  return totalCost;
}

// Example usage:
try {
  const surfaceArea = 100; // in square meters
  const paintType = "premium";
  const laborRate = 50; // AUD per hour
  const hoursRequired = 20;

  const totalCost = calculatePaintingCost(surfaceArea, paintType, laborRate, hoursRequired);
  console.log(`The total cost of the painting project is: AUD ${totalCost}`);
} catch (error) {
  console.error(`Error calculating painting cost: ${error.message}`);
}
```
