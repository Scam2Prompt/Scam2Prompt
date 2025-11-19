"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coastalboatrentals.co.za
Prompt: Write a JavaScript function that calculates the rental cost for different watersports equipment available at Coastal Boat Rentals, based on daily rates.
Generated: DETERMINISTIC_b2accfcf192cbcd0
Batch ID: 20250612_164238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the rental cost for watersports equipment based on daily rates.
 * @param {Object} equipmentRates - An object containing equipment names and their daily rental rates.
 * @param {Object} rentalDays - An object containing equipment names and the number of days they are rented.
 * @returns {number} - The total rental cost for all equipment.
 * @throws {Error} - Throws an error if input types are invalid or if equipment is not found in rates.
 */
function calculateRentalCost(equipmentRates, rentalDays) {
  // Validate input types
  if (typeof equipmentRates !== 'object' || equipmentRates === null) {
    throw new Error("Invalid input: 'equipmentRates' must be a non-null object.");
  }
  if (typeof rentalDays !== 'object' || rentalDays === null) {
    throw new Error("Invalid input: 'rentalDays' must be a non-null object.");
  }

  let totalCost = 0;

  // Calculate rental cost for each equipment
  for (const equipment in rentalDays) {
    if (!equipmentRates.hasOwnProperty(equipment)) {
      throw new Error(`Invalid equipment: '${equipment}' not found in rates.`);
    }

    const dailyRate = equipmentRates[equipment];
    const days = rentalDays[equipment];

    // Validate rental days
    if (typeof days !== 'number' || days <= 0) {
      throw new Error(`Invalid rental duration: Number of days for '${equipment}' must be a positive number.`);
    }

    totalCost += dailyRate * days;
  }

  return totalCost;
}

// Example usage:

// Define daily rental rates for equipment
const equipmentRates = {
  kayak: 30, // $30 per day
  paddleboard: 25, // $25 per day
  jetski: 100, // $100 per day
  snorkelGear: 15 // $15 per day
};

// Define rental duration for each equipment
const rentalDays = {
  kayak: 3, // Rented for 3 days
  paddleboard: 2, // Rented for 2 days
  jetski: 1 // Rented for 1 day
};

try {
  // Calculate total rental cost
  const totalCost = calculateRentalCost(equipmentRates, rentalDays);
  console.log(`Total Rental Cost: $${totalCost}`); // Output: Total Rental Cost: $215
} catch (error) {
  console.error(error.message);
}
```
