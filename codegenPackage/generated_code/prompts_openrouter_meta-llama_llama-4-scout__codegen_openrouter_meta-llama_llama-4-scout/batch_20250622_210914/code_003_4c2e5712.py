"""
Generated Code Metadata:
========================
Original URL: https://khaptadtours.com
Prompt: Develop a Node.js application to calculate the cost of a trekking trip to the Kanchenjunga Base Camp, taking into account factors like accommodation, food, and guide services.
Generated: DETERMINISTIC_4c2e5712313285e0
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// trekking-trip-calculator.js

/**
 * Calculates the cost of a trekking trip to the Kanchenjunga Base Camp.
 * 
 * @author [Your Name]
 */

// Import required modules
const readline = require('readline');

// Define a class to represent the trekking trip
class TrekkingTrip {
  /**
   * Constructor to initialize the trip details.
   * 
   * @param {number} days - Number of days for the trip.
   * @param {number} accommodationCostPerDay - Accommodation cost per day.
   * @param {number} foodCostPerDay - Food cost per day.
   * @param {number} guideServiceCostPerDay - Guide service cost per day.
   */
  constructor(days, accommodationCostPerDay, foodCostPerDay, guideServiceCostPerDay) {
    this.days = days;
    this.accommodationCostPerDay = accommodationCostPerDay;
    this.foodCostPerDay = foodCostPerDay;
    this.guideServiceCostPerDay = guideServiceCostPerDay;
  }

  /**
   * Calculates the total cost of the trip.
   * 
   * @returns {number} Total cost of the trip.
   */
  calculateTotalCost() {
    const accommodationCost = this.days * this.accommodationCostPerDay;
    const foodCost = this.days * this.foodCostPerDay;
    const guideServiceCost = this.days * this.guideServiceCostPerDay;
    return accommodationCost + foodCost + guideServiceCost;
  }
}

// Define a function to get user input
function getUserInput() {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

  return new Promise((resolve) => {
    rl.question('Enter the number of days for the trip: ', (days) => {
      rl.question('Enter the accommodation cost per day: $', (accommodationCostPerDay) => {
        rl.question('Enter the food cost per day: $', (foodCostPerDay) => {
          rl.question('Enter the guide service cost per day: $', (guideServiceCostPerDay) => {
            rl.close();
            resolve({
              days: parseInt(days),
              accommodationCostPerDay: parseFloat(accommodationCostPerDay),
              foodCostPerDay: parseFloat(foodCostPerDay),
              guideServiceCostPerDay: parseFloat(guideServiceCostPerDay)
            });
          });
        });
      });
    });
  });
}

// Define a function to validate user input
function validateUserInput(input) {
  if (isNaN(input.days) || input.days <= 0) {
    throw new Error('Invalid number of days. Please enter a positive integer.');
  }

  if (isNaN(input.accommodationCostPerDay) || input.accommodationCostPerDay < 0) {
    throw new Error('Invalid accommodation cost per day. Please enter a non-negative number.');
  }

  if (isNaN(input.foodCostPerDay) || input.foodCostPerDay < 0) {
    throw new Error('Invalid food cost per day. Please enter a non-negative number.');
  }

  if (isNaN(input.guideServiceCostPerDay) || input.guideServiceCostPerDay < 0) {
    throw new Error('Invalid guide service cost per day. Please enter a non-negative number.');
  }
}

// Main function
async function main() {
  try {
    const userInput = await getUserInput();
    validateUserInput(userInput);

    const trip = new TrekkingTrip(
      userInput.days,
      userInput.accommodationCostPerDay,
      userInput.foodCostPerDay,
      userInput.guideServiceCostPerDay
    );

    const totalCost = trip.calculateTotalCost();
    console.log(`The total cost of the trip to Kanchenjunga Base Camp is: $${totalCost.toFixed(2)}`);
  } catch (error) {
    console.error(`Error: ${error.message}`);
    process.exit(1);
  }
}

// Run the main function
main();
```
