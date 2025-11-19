"""
Generated Code Metadata:
========================
Original URL: https://mariahousekeepers.net
Prompt: Write a code snippet in JavaScript to create a simple calculator for estimating cleaning service costs based on the services offered by Maria HouseKeepers.
Generated: DETERMINISTIC_e96f73b16172b321
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
 * Simple Calculator for Estimating Cleaning Service Costs
 * Services offered by Maria HouseKeepers:
 * - Basic Cleaning: $50 per hour
 * - Deep Cleaning: $80 per hour
 * - Window Cleaning: $30 per window
 * - Carpet Cleaning: $100 per room
 */

class CleaningServiceCalculator {
  constructor() {
    // Define service rates
    this.serviceRates = {
      basicCleaning: 50, // $50 per hour
      deepCleaning: 80,  // $80 per hour
      windowCleaning: 30, // $30 per window
      carpetCleaning: 100 // $100 per room
    };
  }

  /**
   * Calculate the total cost based on user input
   * @param {number} hoursBasicCleaning - Number of hours for basic cleaning
   * @param {number} hoursDeepCleaning - Number of hours for deep cleaning
   * @param {number} numWindows - Number of windows for window cleaning
   * @param {number} numRooms - Number of rooms for carpet cleaning
   * @returns {number} - Total estimated cost
   */
  calculateCost(hoursBasicCleaning, hoursDeepCleaning, numWindows, numRooms) {
    try {
      // Validate inputs
      if (
        hoursBasicCleaning < 0 ||
        hoursDeepCleaning < 0 ||
        numWindows < 0 ||
        numRooms < 0
      ) {
        throw new Error("Input values cannot be negative.");
      }

      // Calculate individual costs
      const basicCleaningCost = hoursBasicCleaning * this.serviceRates.basicCleaning;
      const deepCleaningCost = hoursDeepCleaning * this.serviceRates.deepCleaning;
      const windowCleaningCost = numWindows * this.serviceRates.windowCleaning;
      const carpetCleaningCost = numRooms * this.serviceRates.carpetCleaning;

      // Calculate total cost
      const totalCost =
        basicCleaningCost +
        deepCleaningCost +
        windowCleaningCost +
        carpetCleaningCost;

      return totalCost;
    } catch (error) {
      console.error("Error calculating cost:", error.message);
      return null; // Return null in case of error
    }
  }
}

// Example usage
const calculator = new CleaningServiceCalculator();

// User inputs
const hoursBasicCleaning = 3; // 3 hours of basic cleaning
const hoursDeepCleaning = 2; // 2 hours of deep cleaning
const numWindows = 5; // 5 windows to clean
const numRooms = 2; // 2 rooms for carpet cleaning

// Calculate and display the total cost
const totalCost = calculator.calculateCost(
  hoursBasicCleaning,
  hoursDeepCleaning,
  numWindows,
  numRooms
);

if (totalCost !== null) {
  console.log(`Total estimated cost: $${totalCost}`);
} else {
  console.log("Failed to calculate the cost due to an error.");
}
```
