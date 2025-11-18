"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getrise.pro
Prompt: Develop a JavaScript function to calculate rental costs based on user-selected dates and additional fees, similar to RainBNB.
Generated: DETERMINISTIC_4331239319797ace
Batch ID: 20250612_154158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total rental cost based on user-selected dates and additional fees.
 * @param {Date} startDate - The start date of the rental period.
 * @param {Date} endDate - The end date of the rental period.
 * @param {number} dailyRate - The daily rental rate.
 * @param {Object} additionalFees - An object containing additional fees, e.g., { cleaningFee: 50, serviceFee: 20 }.
 * @returns {number} - The total rental cost.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculateRentalCost(startDate, endDate, dailyRate, additionalFees) {
  // Validate inputs
  if (!(startDate instanceof Date) || !(endDate instanceof Date)) {
    throw new Error("Invalid dates provided. Please use valid Date objects.");
  }
  if (dailyRate <= 0 || typeof dailyRate !== "number") {
    throw new Error("Invalid daily rate. Please provide a positive number.");
  }
  if (endDate <= startDate) {
    throw new Error("End date must be after start date.");
  }
  if (!additionalFees || typeof additionalFees !== "object") {
    throw new Error("Invalid additional fees. Please provide an object.");
  }

  // Calculate the number of rental days
  const millisecondsPerDay = 24 * 60 * 60 * 1000;
  const rentalDays = Math.ceil((endDate - startDate) / millisecondsPerDay);

  // Calculate the base cost
  const baseCost = rentalDays * dailyRate;

  // Calculate additional fees
  const additionalCost = Object.values(additionalFees).reduce((acc, fee) => {
    if (typeof fee !== "number" || fee < 0) {
      throw new Error(`Invalid fee value: ${fee}. All fees must be positive numbers.`);
    }
    return acc + fee;
  }, 0);

  // Calculate total cost
  const totalCost = baseCost + additionalCost;

  return totalCost;
}

// Example usage:
try {
  const startDate = new Date("2023-10-01");
  const endDate = new Date("2023-10-05");
  const dailyRate = 100; // $100 per day
  const additionalFees = {
    cleaningFee: 50,
    serviceFee: 20,
  };

  const totalCost = calculateRentalCost(startDate, endDate, dailyRate, additionalFees);
  console.log(`Total rental cost: $${totalCost}`);
} catch (error) {
  console.error(error.message);
}
```
