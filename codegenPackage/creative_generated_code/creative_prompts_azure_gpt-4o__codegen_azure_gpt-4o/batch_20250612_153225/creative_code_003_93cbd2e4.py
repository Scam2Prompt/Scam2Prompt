"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rentalcarelena.it
Prompt: Write a function in JavaScript to calculate rental costs based on vehicle type, rental duration, and optional services, ensuring flexibility for hybrid and bifuel cars.
Generated: DETERMINISTIC_93cbd2e492411324
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate rental costs based on vehicle type, rental duration, and optional services.
 * @param {string} vehicleType - The type of vehicle (e.g., "sedan", "SUV", "hybrid", "bifuel").
 * @param {number} rentalDuration - The rental duration in days.
 * @param {object} optionalServices - An object specifying optional services (e.g., { gps: true, childSeat: true }).
 * @returns {number} - The total rental cost.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculateRentalCost(vehicleType, rentalDuration, optionalServices = {}) {
  // Validate inputs
  if (typeof vehicleType !== "string" || typeof rentalDuration !== "number" || rentalDuration <= 0) {
    throw new Error("Invalid inputs. Ensure vehicleType is a string and rentalDuration is a positive number.");
  }

  // Base daily rates for different vehicle types
  const dailyRates = {
    sedan: 50,
    SUV: 100,
    hybrid: 80,
    bifuel: 90,
  };

  // Check if the vehicle type exists in the rates table
  if (!dailyRates[vehicleType]) {
    throw new Error(`Unsupported vehicle type: ${vehicleType}. Allowed types are: ${Object.keys(dailyRates).join(", ")}`);
  }

  // Optional service fees
  const serviceFees = {
    gps: 10, // Daily fee for GPS
    childSeat: 5, // Daily fee for child seat
    additionalDriver: 20, // Daily fee for an additional driver
  };

  // Calculate base cost
  const baseCost = dailyRates[vehicleType] * rentalDuration;

  // Calculate optional services cost
  let optionalServicesCost = 0;
  for (const [service, enabled] of Object.entries(optionalServices)) {
    if (enabled && serviceFees[service] !== undefined) {
      optionalServicesCost += serviceFees[service] * rentalDuration;
    }
  }

  // Calculate total cost
  const totalCost = baseCost + optionalServicesCost;

  return totalCost;
}

// Example usage:
try {
  const vehicleType = "hybrid";
  const rentalDuration = 5;
  const optionalServices = { gps: true, childSeat: true, additionalDriver: false };
  
  const totalCost = calculateRentalCost(vehicleType, rentalDuration, optionalServices);
  console.log(`Total Rental Cost: $${totalCost}`);
} catch (error) {
  console.error(error.message);
}
```
