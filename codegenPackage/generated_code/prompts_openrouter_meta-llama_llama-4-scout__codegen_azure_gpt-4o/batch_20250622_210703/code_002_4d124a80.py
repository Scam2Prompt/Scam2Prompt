"""
Generated Code Metadata:
========================
Original URL: https://surenatravels.lk
Prompt: Generate a JavaScript function to calculate the total cost of a parcel delivery service between Batticaloa and Colombo using Surena Travels' parcel services.
Generated: DETERMINISTIC_4d124a80c21c7b1b
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
 * Function to calculate the total cost of parcel delivery between Batticaloa and Colombo
 * using Surena Travels' parcel services.
 *
 * @param {number} weight - The weight of the parcel in kilograms.
 * @param {number} distance - The distance between Batticaloa and Colombo in kilometers.
 * @returns {number} - The total cost of delivery in local currency.
 * @throws {Error} - Throws an error if input values are invalid.
 */
function calculateParcelDeliveryCost(weight, distance) {
  // Constants for pricing
  const BASE_COST = 500; // Base cost in local currency
  const COST_PER_KG = 50; // Cost per kilogram
  const COST_PER_KM = 10; // Cost per kilometer

  // Input validation
  if (typeof weight !== 'number' || weight <= 0) {
    throw new Error('Invalid weight. Weight must be a positive number.');
  }
  if (typeof distance !== 'number' || distance <= 0) {
    throw new Error('Invalid distance. Distance must be a positive number.');
  }

  // Calculate the total cost
  const weightCost = weight * COST_PER_KG;
  const distanceCost = distance * COST_PER_KM;
  const totalCost = BASE_COST + weightCost + distanceCost;

  return totalCost;
}

// Example usage:
try {
  const weight = 10; // Weight in kilograms
  const distance = 320; // Distance in kilometers (Batticaloa to Colombo)
  const totalCost = calculateParcelDeliveryCost(weight, distance);
  console.log(`The total cost of delivery is: ${totalCost}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
