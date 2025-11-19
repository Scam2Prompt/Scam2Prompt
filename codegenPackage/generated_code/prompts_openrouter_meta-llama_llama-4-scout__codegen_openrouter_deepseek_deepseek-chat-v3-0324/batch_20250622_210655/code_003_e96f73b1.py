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
 * Maria HouseKeepers Cleaning Service Cost Calculator
 * 
 * This script calculates the total cost of cleaning services based on selected options.
 * It supports different service types, property sizes, and add-ons with proper validation.
 */

class CleaningCostCalculator {
  /**
   * Initialize the calculator with service pricing and options
   */
  constructor() {
    // Base prices for different service types
    this.servicePrices = {
      standard: 50,       // Standard cleaning per hour
      deep: 75,           // Deep cleaning per hour
      moveInOut: 100      // Move-in/out cleaning per hour
    };

    // Size multipliers (base size is 1-2 bedrooms)
    this.sizeMultipliers = {
      small: 1.0,         // 1-2 bedrooms
      medium: 1.5,        // 3-4 bedrooms
      large: 2.0          // 5+ bedrooms
    };

    // Add-on services with fixed prices
    this.addOnPrices = {
      windowCleaning: 30,
      fridgeCleaning: 25,
      ovenCleaning: 20,
      laundry: 15
    };
  }

  /**
   * Calculate the total cost based on selected options
   * @param {string} serviceType - Type of cleaning service
   * @param {string} propertySize - Size of the property
   * @param {number} hours - Number of hours needed
   * @param {Array} addOns - Selected add-on services
   * @returns {number} Total cost in USD
   * @throws {Error} If invalid input is provided
   */
  calculateCost(serviceType, propertySize, hours, addOns = []) {
    // Validate inputs
    if (!this.servicePrices.hasOwnProperty(serviceType)) {
      throw new Error(`Invalid service type: ${serviceType}`);
    }

    if (!this.sizeMultipliers.hasOwnProperty(propertySize)) {
      throw new Error(`Invalid property size: ${propertySize}`);
    }

    if (typeof hours !== 'number' || hours <= 0) {
      throw new Error(`Hours must be a positive number: ${hours}`);
    }

    // Calculate base cost
    const baseCost = this.servicePrices[serviceType] * hours;
    const sizeAdjustedCost = baseCost * this.sizeMultipliers[propertySize];

    // Calculate add-ons cost
    let addOnCost = 0;
    if (Array.isArray(addOns)) {
      addOns.forEach(addOn => {
        if (this.addOnPrices.hasOwnProperty(addOn)) {
          addOnCost += this.addOnPrices[addOn];
        }
      });
    }

    // Return total cost rounded to 2 decimal places
    return parseFloat((sizeAdjustedCost + addOnCost).toFixed(2));
  }
}

// Example usage:
try {
  const calculator = new CleaningCostCalculator();
  const totalCost = calculator.calculateCost(
    'deep',             // Service type
    'medium',           // Property size
    3,                  // Hours
    ['windowCleaning', 'ovenCleaning'] // Add-ons
  );
  console.log(`Total estimated cost: $${totalCost}`);
} catch (error) {
  console.error('Error calculating cost:', error.message);
}
```
