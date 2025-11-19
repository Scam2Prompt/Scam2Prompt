"""
Generated Code Metadata:
========================
Original URL: https://yourmaidinheaven.com
Prompt: Create a JavaScript function that calculates the cost of cleaning services based on user input, inspired by the pricing structure of Maid in Heaven's cleaning plans.
Generated: DETERMINISTIC_d3641bfb0d5e7e95
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the cost of cleaning services based on user input.
 * 
 * Pricing structure:
 * - 1-2 rooms: $75 per visit
 * - 3-4 rooms: $100 per visit
 * - 5 or more rooms: $150 per visit
 * 
 * Additional services:
 * - Deep cleaning: $25 per visit
 * - Special requests (e.g. move-in/move-out): $50 per visit
 */

// Define the cleaning service pricing structure
const cleaningPlans = {
  low: { rooms: 1, 2, price: 75 },
  medium: { rooms: 3, 4, price: 100 },
  high: { rooms: 5, Infinity, price: 150 }
};

const additionalServices = {
  deepCleaning: 25,
  specialRequests: 50
};

/**
 * Calculates the base cost of cleaning services based on the number of rooms.
 * 
 * @param {number} numRooms The number of rooms to be cleaned.
 * @returns {number} The base cost of cleaning services.
 */
function calculateBaseCost(numRooms) {
  for (const plan in cleaningPlans) {
    if (numRooms >= cleaningPlans[plan].rooms[0] && numRooms <= cleaningPlans[plan].rooms[1]) {
      return cleaningPlans[plan].price;
    }
  }
  throw new Error('Invalid number of rooms');
}

/**
 * Calculates the total cost of cleaning services including additional services.
 * 
 * @param {number} numRooms The number of rooms to be cleaned.
 * @param {boolean} deepCleaning Whether deep cleaning is required.
 * @param {boolean} specialRequests Whether special requests are required.
 * @returns {number} The total cost of cleaning services.
 */
function calculateCleaningCost(numRooms, deepCleaning = false, specialRequests = false) {
  try {
    const baseCost = calculateBaseCost(numRooms);
    let totalCost = baseCost;

    if (deepCleaning) {
      totalCost += additionalServices.deepCleaning;
    }

    if (specialRequests) {
      totalCost += additionalServices.specialRequests;
    }

    return totalCost;
  } catch (error) {
    console.error(error.message);
    return null;
  }
}

// Example usage:
function main() {
  const numRooms = 4;
  const deepCleaning = true;
  const specialRequests = false;

  const totalCost = calculateCleaningCost(numRooms, deepCleaning, specialRequests);

  if (totalCost !== null) {
    console.log(`The total cost of cleaning services is: $${totalCost}`);
  }
}

main();
```
