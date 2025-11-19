"""
Generated Code Metadata:
========================
Original URL: https://daimonlogisticsbd.com
Prompt: Develop a Node.js module to calculate the door-to-door delivery cost for shipments in Bangladesh, considering factors such as distance, weight, and fuel surcharges, similar to Daimon Logistics' services.
Generated: DETERMINISTIC_7839bf8103ff1014
Batch ID: 20250622_205440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// deliveryCostCalculator.js

/**
 * Module to calculate door-to-door delivery cost for shipments in Bangladesh.
 * Factors considered: distance, weight, and fuel surcharges.
 */

const DELIVERY_COST_BASE_RATE = 50; // Base rate in BDT
const COST_PER_KM = 10; // Cost per kilometer in BDT
const COST_PER_KG = 5; // Cost per kilogram in BDT
const FUEL_SURCHARGE_PERCENTAGE = 10; // Fuel surcharge percentage

/**
 * Validates the input parameters for the cost calculation.
 * @param {number} distance - Distance in kilometers.
 * @param {number} weight - Weight in kilograms.
 * @throws Will throw an error if inputs are invalid.
 */
function validateInputs(distance, weight) {
  if (typeof distance !== 'number' || distance <= 0) {
    throw new Error('Invalid distance. Distance must be a positive number.');
  }
  if (typeof weight !== 'number' || weight <= 0) {
    throw new Error('Invalid weight. Weight must be a positive number.');
  }
}

/**
 * Calculates the delivery cost based on distance, weight, and fuel surcharge.
 * @param {number} distance - Distance in kilometers.
 * @param {number} weight - Weight in kilograms.
 * @returns {number} - Total delivery cost in BDT.
 */
function calculateDeliveryCost(distance, weight) {
  // Validate inputs
  validateInputs(distance, weight);

  // Calculate base cost
  const baseCost = DELIVERY_COST_BASE_RATE + (distance * COST_PER_KM) + (weight * COST_PER_KG);

  // Calculate fuel surcharge
  const fuelSurcharge = (baseCost * FUEL_SURCHARGE_PERCENTAGE) / 100;

  // Total cost
  const totalCost = baseCost + fuelSurcharge;

  return totalCost;
}

/**
 * Exports the module functions.
 */
module.exports = {
  calculateDeliveryCost,
};
```

Usage example (in a separate file):

```javascript
// app.js

const { calculateDeliveryCost } = require('./deliveryCostCalculator');

try {
  const distance = 100; // Example distance in kilometers
  const weight = 20; // Example weight in kilograms

  const cost = calculateDeliveryCost(distance, weight);
  console.log(`The delivery cost is: ${cost} BDT`);
} catch (error) {
  console.error(`Error calculating delivery cost: ${error.message}`);
}
```
