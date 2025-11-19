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
 * Calculator for estimating cleaning service costs based on services offered by Maria HouseKeepers.
 */

// Define a class for the calculator
class CleaningServiceCalculator {
  /**
   * Constructor to initialize service costs.
   */
  constructor() {
    // Define service costs per hour
    this.serviceCosts = {
      generalCleaning: 50,
      deepCleaning: 75,
      moveInMoveOut: 100,
      specialEvent: 150,
    };

    // Define additional costs
    this.additionalCosts = {
      supplies: 10,
      equipment: 20,
      travel: 30,
    };
  }

  /**
   * Calculate the total cost for a cleaning service.
   * @param {string} serviceType - Type of cleaning service.
   * @param {number} hours - Number of hours required for the service.
   * @param {object} [additionalServices] - Additional services required.
   * @returns {number} The total cost for the cleaning service.
   */
  calculateCost(serviceType, hours, additionalServices = {}) {
    // Check if the service type is valid
    if (!(serviceType in this.serviceCosts)) {
      throw new Error(`Invalid service type: ${serviceType}`);
    }

    // Calculate the base cost
    let baseCost = this.serviceCosts[serviceType] * hours;

    // Calculate additional costs
    let additionalCost = 0;
    for (const [service, quantity] of Object.entries(additionalServices)) {
      if (!(service in this.additionalCosts)) {
        throw new Error(`Invalid additional service: ${service}`);
      }
      additionalCost += this.additionalCosts[service] * quantity;
    }

    // Return the total cost
    return baseCost + additionalCost;
  }
}

// Example usage
function main() {
  try {
    const calculator = new CleaningServiceCalculator();

    // Calculate cost for general cleaning
    const generalCleaningCost = calculator.calculateCost(
      'generalCleaning',
      2,
      { supplies: 1, equipment: 1 }
    );
    console.log(`General cleaning cost: $${generalCleaningCost}`);

    // Calculate cost for deep cleaning
    const deepCleaningCost = calculator.calculateCost(
      'deepCleaning',
      3,
      { travel: 1 }
    );
    console.log(`Deep cleaning cost: $${deepCleaningCost}`);

    // Calculate cost for invalid service type
    calculator.calculateCost('invalidService', 2);
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
