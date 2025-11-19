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
 * Calculates the cost of a painting project based on surface area, paint type, and labor costs.
 * @param {number} surfaceArea - Total surface area to be painted in square meters.
 * @param {string} paintType - Type of paint ('standard', 'premium', 'luxury').
 * @param {boolean} includesLabor - Whether labor costs are included.
 * @param {number} [laborRate=50] - Hourly labor rate in AUD (default: 50).
 * @param {number} [hoursPerSqm=0.1] - Hours required per square meter (default: 0.1).
 * @returns {object} An object containing cost breakdown and total cost.
 * @throws {Error} If invalid parameters are provided.
 */
function calculatePaintingCost(
  surfaceArea,
  paintType,
  includesLabor,
  laborRate = 50,
  hoursPerSqm = 0.1
) {
  // Validate input parameters
  if (typeof surfaceArea !== 'number' || surfaceArea <= 0) {
    throw new Error('Surface area must be a positive number');
  }

  if (!['standard', 'premium', 'luxury'].includes(paintType)) {
    throw new Error('Invalid paint type. Must be standard, premium, or luxury');
  }

  if (typeof includesLabor !== 'boolean') {
    throw new Error('includesLabor must be a boolean value');
  }

  if (typeof laborRate !== 'number' || laborRate <= 0) {
    throw new Error('Labor rate must be a positive number');
  }

  if (typeof hoursPerSqm !== 'number' || hoursPerSqm <= 0) {
    throw new Error('Hours per square meter must be a positive number');
  }

  // Paint prices per square meter (AUD)
  const paintPrices = {
    standard: 5,
    premium: 8,
    luxury: 12
  };

  // Calculate paint cost
  const paintCost = surfaceArea * paintPrices[paintType];

  // Calculate labor cost if included
  let laborCost = 0;
  if (includesLabor) {
    laborCost = surfaceArea * hoursPerSqm * laborRate;
  }

  // Calculate total cost
  const totalCost = paintCost + laborCost;

  return {
    surfaceArea: surfaceArea,
    paintType: paintType,
    paintCost: parseFloat(paintCost.toFixed(2)),
    includesLabor: includesLabor,
    laborCost: includesLabor ? parseFloat(laborCost.toFixed(2)) : 0,
    totalCost: parseFloat(totalCost.toFixed(2)),
    currency: 'AUD'
  };
}

// Example usage:
try {
  const projectCost = calculatePaintingCost(100, 'premium', true);
  console.log(projectCost);
} catch (error) {
  console.error('Error calculating project cost:', error.message);
}
```
