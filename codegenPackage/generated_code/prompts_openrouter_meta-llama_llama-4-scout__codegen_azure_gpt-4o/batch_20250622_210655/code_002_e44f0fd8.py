"""
Generated Code Metadata:
========================
Original URL: https://www.efeotokurtarma.com.tr
Prompt: Generate a JavaScript function to calculate the estimated cost of a towing service based on distance and vehicle type, considering Efem Oto Kurtarma's pricing model.
Generated: DETERMINISTIC_e44f0fd84664742c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculate the estimated cost of a towing service based on distance and vehicle type.
 * Efem Oto Kurtarma's pricing model:
 * - Base fee: 50 TRY
 * - Per kilometer fee:
 *   - Car: 5 TRY/km
 *   - Motorcycle: 3 TRY/km
 *   - Truck: 10 TRY/km
 * - Additional fees may apply for invalid inputs.
 *
 * @param {number} distance - The distance in kilometers (must be a positive number).
 * @param {string} vehicleType - The type of vehicle ("car", "motorcycle", "truck").
 * @returns {number} - The estimated cost in TRY.
 * @throws {Error} - Throws an error for invalid inputs.
 */
function calculateTowingCost(distance, vehicleType) {
  // Validate input parameters
  if (typeof distance !== 'number' || distance <= 0) {
    throw new Error('Invalid distance. Distance must be a positive number.');
  }

  if (typeof vehicleType !== 'string' || !['car', 'motorcycle', 'truck'].includes(vehicleType.toLowerCase())) {
    throw new Error('Invalid vehicle type. Vehicle type must be "car", "motorcycle", or "truck".');
  }

  // Pricing model
  const baseFee = 50; // Base fee in TRY
  const perKmFees = {
    car: 5,         // Fee per kilometer for cars
    motorcycle: 3,  // Fee per kilometer for motorcycles
    truck: 10       // Fee per kilometer for trucks
  };

  // Calculate the cost
  const vehicleTypeLower = vehicleType.toLowerCase(); // Normalize vehicle type
  const perKmFee = perKmFees[vehicleTypeLower];       // Get the per kilometer fee
  const totalCost = baseFee + (distance * perKmFee);  // Calculate total cost

  return totalCost; // Return the estimated cost
}

// Example usage:
try {
  const cost = calculateTowingCost(15, 'car'); // Calculate cost for 15 km towing a car
  console.log(`Estimated towing cost: ${cost} TRY`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
