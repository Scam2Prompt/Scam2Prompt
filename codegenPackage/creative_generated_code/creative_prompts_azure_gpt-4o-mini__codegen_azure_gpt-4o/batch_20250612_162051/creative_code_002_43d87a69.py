"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://antalyasehiricinakliye.com
Prompt: Create a JavaScript function that calculates the estimated cost of moving services based on the type of items (e.g., small furniture, appliances) and distance within Antalya.
Generated: DETERMINISTIC_43d87a69e74b0bb0
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculate the estimated cost of moving services.
 * 
 * @param {Array<Object>} items - Array of items to be moved. Each item should have:
 *   - type {string}: Type of the item (e.g., "small furniture", "appliance").
 *   - quantity {number}: Quantity of the item.
 * @param {number} distance - Distance of the move in kilometers within Antalya.
 * @returns {number} - The estimated cost of the move.
 * @throws {Error} - Throws an error if input parameters are invalid.
 */
function calculateMovingCost(items, distance) {
  // Validate input parameters
  if (!Array.isArray(items)) {
    throw new Error("Invalid input: 'items' must be an array.");
  }
  if (typeof distance !== 'number' || distance < 0) {
    throw new Error("Invalid input: 'distance' must be a non-negative number.");
  }

  // Base rate per kilometer within Antalya
  const baseRatePerKm = 2; // Example: 2 currency units per km

  // Rates for item types
  const itemRates = {
    "small furniture": 50, // 50 currency units per item
    "appliance": 100      // 100 currency units per item
  };

  // Calculate total item cost
  let totalItemCost = 0;
  items.forEach((item) => {
    const { type, quantity } = item;

    if (!itemRates[type] || typeof quantity !== 'number' || quantity <= 0) {
      throw new Error(`Invalid item configuration: ${JSON.stringify(item)}`);
    }

    totalItemCost += itemRates[type] * quantity;
  });

  // Calculate total distance cost
  const totalDistanceCost = baseRatePerKm * distance;

  // Calculate final estimated cost
  const estimatedCost = totalItemCost + totalDistanceCost;

  return estimatedCost;
}

// Example usage:
try {
  const items = [
    { type: "small furniture", quantity: 3 },
    { type: "appliance", quantity: 2 }
  ];
  const distance = 15; // 15 kilometers
  
  const cost = calculateMovingCost(items, distance);
  console.log(`Estimated Moving Cost: ${cost}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
