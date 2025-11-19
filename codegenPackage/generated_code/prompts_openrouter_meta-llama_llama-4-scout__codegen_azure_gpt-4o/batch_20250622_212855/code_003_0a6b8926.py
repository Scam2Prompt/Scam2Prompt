"""
Generated Code Metadata:
========================
Original URL: https://autorepairapps.com
Prompt: Create a Node.js function to calculate the cost of car maintenance based on factors like vehicle type, mileage, and repair services required.
Generated: DETERMINISTIC_0a6b892649927727
Batch ID: 20250622_212855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate the cost of car maintenance based on vehicle type, mileage, and repair services required.
 * @param {string} vehicleType - Type of the vehicle (e.g., "sedan", "SUV", "truck").
 * @param {number} mileage - Mileage of the vehicle in kilometers.
 * @param {Array<{service: string, cost: number}>} repairServices - List of repair services required with their respective costs.
 * @returns {number} - Total maintenance cost.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculateMaintenanceCost(vehicleType, mileage, repairServices) {
  // Validate inputs
  if (typeof vehicleType !== 'string' || !vehicleType.trim()) {
    throw new Error('Invalid vehicle type. It must be a non-empty string.');
  }
  if (typeof mileage !== 'number' || mileage < 0) {
    throw new Error('Invalid mileage. It must be a non-negative number.');
  }
  if (!Array.isArray(repairServices) || repairServices.some(service => typeof service.service !== 'string' || typeof service.cost !== 'number' || service.cost < 0)) {
    throw new Error('Invalid repair services. Each service must have a valid name and non-negative cost.');
  }

  // Base cost multiplier based on vehicle type
  const vehicleTypeMultiplier = {
    sedan: 1.0,
    SUV: 1.2,
    truck: 1.5,
  };

  const multiplier = vehicleTypeMultiplier[vehicleType.toLowerCase()];
  if (!multiplier) {
    throw new Error('Unsupported vehicle type. Supported types are: sedan, SUV, truck.');
  }

  // Calculate mileage-based cost adjustment
  let mileageAdjustment = 0;
  if (mileage > 50000 && mileage <= 100000) {
    mileageAdjustment = 0.1; // 10% increase for mileage between 50,000 and 100,000 km
  } else if (mileage > 100000) {
    mileageAdjustment = 0.2; // 20% increase for mileage above 100,000 km
  }

  // Calculate total repair service cost
  const repairCost = repairServices.reduce((total, service) => total + service.cost, 0);

  // Calculate final maintenance cost
  const totalCost = repairCost * multiplier * (1 + mileageAdjustment);

  return totalCost;
}

// Example usage:
try {
  const vehicleType = 'SUV';
  const mileage = 75000;
  const repairServices = [
    { service: 'Oil Change', cost: 50 },
    { service: 'Brake Replacement', cost: 200 },
    { service: 'Tire Rotation', cost: 100 },
  ];

  const totalCost = calculateMaintenanceCost(vehicleType, mileage, repairServices);
  console.log(`Total Maintenance Cost: $${totalCost.toFixed(2)}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
