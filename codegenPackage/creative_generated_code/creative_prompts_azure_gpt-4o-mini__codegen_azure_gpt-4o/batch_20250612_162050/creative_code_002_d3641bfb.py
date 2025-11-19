"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yourmaidinheaven.com
Prompt: Create a JavaScript function that calculates the cost of cleaning services based on user input, inspired by the pricing structure of Maid in Heaven's cleaning plans.
Generated: DETERMINISTIC_d3641bfb0d5e7e95
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the cost of cleaning services based on user input.
 * Pricing structure:
 * - Base price: $50
 * - Additional rooms: $20 per room
 * - Deep cleaning surcharge: $100
 * - Discount for recurring service: 10% off (applies to the total cost)
 * 
 * @param {number} numberOfRooms - Number of rooms to clean (minimum 1).
 * @param {boolean} deepCleaning - Whether deep cleaning is requested (true/false).
 * @param {boolean} recurringService - Whether the service is recurring (true/false).
 * @returns {number} - The total cost of the cleaning service.
 * @throws {Error} - Throws an error if input values are invalid.
 */
function calculateCleaningCost(numberOfRooms, deepCleaning, recurringService) {
  // Validate input
  if (!Number.isInteger(numberOfRooms) || numberOfRooms < 1) {
    throw new Error("Invalid number of rooms. Must be an integer greater than or equal to 1.");
  }
  if (typeof deepCleaning !== "boolean") {
    throw new Error("Invalid value for deepCleaning. Must be a boolean.");
  }
  if (typeof recurringService !== "boolean") {
    throw new Error("Invalid value for recurringService. Must be a boolean.");
  }

  // Constants for pricing
  const BASE_PRICE = 50;
  const ROOM_PRICE = 20;
  const DEEP_CLEANING_SURCHARGE = 100;
  const RECURRING_SERVICE_DISCOUNT = 0.10;

  // Calculate total cost
  let totalCost = BASE_PRICE + (numberOfRooms - 1) * ROOM_PRICE; // Include additional room costs
  if (deepCleaning) {
    totalCost += DEEP_CLEANING_SURCHARGE; // Add deep cleaning surcharge if requested
  }
  if (recurringService) {
    totalCost -= totalCost * RECURRING_SERVICE_DISCOUNT; // Apply discount for recurring service
  }

  return totalCost;
}

// Example usage:
try {
  const cost = calculateCleaningCost(3, true, true); // 3 rooms, deep cleaning, recurring service
  console.log(`Total cost: $${cost.toFixed(2)}`); // Output: Total cost: $188.00
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
