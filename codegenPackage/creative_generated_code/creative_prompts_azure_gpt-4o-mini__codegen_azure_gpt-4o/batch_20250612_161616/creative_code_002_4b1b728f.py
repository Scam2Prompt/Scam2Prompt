"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mpl-liner.com
Prompt: Create a function in JavaScript that calculates the estimated cost for sea freight services based on weight and distance, as described by Malaysia Pacific Logistics.
Generated: DETERMINISTIC_4b1b728f94f7c9ab
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculate the estimated cost for sea freight services.
 * 
 * Malaysia Pacific Logistics pricing model:
 * - Base rate: $50
 * - Cost per kilogram: $0.20
 * - Cost per kilometer: $0.10
 * 
 * @param {number} weight - Weight of the cargo in kilograms.
 * @param {number} distance - Distance to be traveled in kilometers.
 * @returns {number} Estimated cost of the freight service.
 * @throws {Error} Throws an error if weight or distance are invalid.
 */
function calculateSeaFreightCost(weight, distance) {
  // Validate input
  if (typeof weight !== 'number' || typeof distance !== 'number') {
    throw new Error('Both weight and distance must be numbers.');
  }
  if (weight <= 0) {
    throw new Error('Weight must be greater than zero.');
  }
  if (distance <= 0) {
    throw new Error('Distance must be greater than zero.');
  }

  // Pricing constants
  const BASE_RATE = 50; // Base cost in USD
  const COST_PER_KILOGRAM = 0.20; // Cost per kilogram in USD
  const COST_PER_KILOMETER = 0.10; // Cost per kilometer in USD

  // Calculate total cost
  const weightCost = weight * COST_PER_KILOGRAM;
  const distanceCost = distance * COST_PER_KILOMETER;
  const totalCost = BASE_RATE + weightCost + distanceCost;

  return totalCost;
}

// Example usage
try {
  const estimatedCost = calculateSeaFreightCost(500, 1000);
  console.log(`Estimated cost: $${estimatedCost.toFixed(2)}`);
} catch (error) {
  console.error(error.message);
}
```
