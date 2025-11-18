"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wizfairllc.com
Prompt: Generate a function in JavaScript to calculate the total cost of a customizable holiday package, including flights, hotels, and sightseeing options, based on Wizfair LLC's pricing structure.
Generated: DETERMINISTIC_f87cd4db9ff1adbe
Batch ID: 20250612_151247
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the total cost of a customizable holiday package.
 * Includes flights, hotels, and sightseeing options based on Wizfair LLC's pricing structure.
 *
 * @param {Object} packageDetails - The holiday package details.
 * @param {number} packageDetails.flightCost - Cost of the flight per person.
 * @param {number} packageDetails.hotelCost - Cost of the hotel per night.
 * @param {number} packageDetails.sightseeingCost - Cost of sightseeing per person.
 * @param {number} packageDetails.numPeople - Number of people in the package.
 * @param {number} packageDetails.numNights - Number of nights for the hotel stay.
 * @returns {number} - The total cost of the holiday package.
 * @throws {Error} - Throws an error if invalid input is provided.
 */
function calculateHolidayPackageCost(packageDetails) {
  // Validate input
  if (
    typeof packageDetails.flightCost !== "number" ||
    typeof packageDetails.hotelCost !== "number" ||
    typeof packageDetails.sightseeingCost !== "number" ||
    typeof packageDetails.numPeople !== "number" ||
    typeof packageDetails.numNights !== "number"
  ) {
    throw new Error("Invalid input: All inputs must be numbers.");
  }

  if (
    packageDetails.flightCost < 0 ||
    packageDetails.hotelCost < 0 ||
    packageDetails.sightseeingCost < 0 ||
    packageDetails.numPeople <= 0 ||
    packageDetails.numNights <= 0
  ) {
    throw new Error("Invalid input: Costs must be non-negative, and numbers of people/nights must be positive.");
  }

  // Calculate total costs
  const flightTotal = packageDetails.flightCost * packageDetails.numPeople; // Cost of flights
  const hotelTotal = packageDetails.hotelCost * packageDetails.numNights * packageDetails.numPeople; // Cost of hotels
  const sightseeingTotal = packageDetails.sightseeingCost * packageDetails.numPeople; // Cost of sightseeing

  // Total package cost
  const totalCost = flightTotal + hotelTotal + sightseeingTotal;

  return totalCost;
}

// Example usage
try {
  const packageDetails = {
    flightCost: 300, // cost per person
    hotelCost: 100, // cost per night
    sightseeingCost: 50, // cost per person
    numPeople: 2, // number of people
    numNights: 5, // number of nights
  };
  const totalCost = calculateHolidayPackageCost(packageDetails);
  console.log(`The total cost of the holiday package is $${totalCost}`);
} catch (error) {
  console.error(error.message);
}
```
