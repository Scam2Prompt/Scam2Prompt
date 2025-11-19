"""
Generated Code Metadata:
========================
Original URL: https://evinblue.com
Prompt: Generate a JavaScript code snippet to create a simple calculator for determining DEF consumption based on vehicle mileage and engine type (e.g., Mercedes Benz, Tata, Bharat Benz).
Generated: DETERMINISTIC_728734ea01d7739f
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
 * DEF Consumption Calculator
 * Calculates DEF consumption based on vehicle mileage and engine type.
 */

class DEFCalculator {
  /**
   * DEF consumption rates (liters per kilometer) for different engine types.
   * These values are examples and should be adjusted based on actual specifications.
   */
  static DEF_CONSUMPTION_RATES = {
    'Mercedes Benz': 0.015,
    'Tata': 0.012,
    'Bharat Benz': 0.014
  };

  /**
   * Calculates DEF consumption based on mileage and engine type.
   * @param {number} mileage - Vehicle mileage in kilometers.
   * @param {string} engineType - Engine type (e.g., 'Mercedes Benz', 'Tata', 'Bharat Benz').
   * @returns {number} DEF consumption in liters.
   * @throws {Error} If mileage is invalid or engine type is not supported.
   */
  static calculateDEFConsumption(mileage, engineType) {
    if (typeof mileage !== 'number' || mileage <= 0) {
      throw new Error('Mileage must be a positive number');
    }

    const consumptionRate = this.DEF_CONSUMPTION_RATES[engineType];
    if (consumptionRate === undefined) {
      throw new Error('Unsupported engine type');
    }

    return mileage * consumptionRate;
  }
}

// Example usage
try {
  const mileage = 500; // km
  const engineType = 'Mercedes Benz';
  const defConsumption = DEFCalculator.calculateDEFConsumption(mileage, engineType);
  console.log(`DEF Consumption for ${engineType} over ${mileage} km: ${defConsumption.toFixed(2)} liters`);
} catch (error) {
  console.error('Error calculating DEF consumption:', error.message);
}
```
