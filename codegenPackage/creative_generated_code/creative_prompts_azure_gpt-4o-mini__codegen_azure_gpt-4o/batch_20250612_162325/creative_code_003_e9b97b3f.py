"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mgcaugiay.com
Prompt: Develop a JavaScript function that calculates the fuel consumption of the MG HS based on user input for distance traveled and fuel used.
Generated: DETERMINISTIC_e9b97b3f6f57a833
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate fuel consumption for the MG HS.
 * Fuel consumption is calculated as liters used per 100 kilometers (L/100km).
 * 
 * @param {number} distance - Distance traveled in kilometers.
 * @param {number} fuelUsed - Fuel used in liters.
 * @returns {string} Fuel consumption in L/100km or an error message if inputs are invalid.
 */
function calculateFuelConsumption(distance, fuelUsed) {
  try {
    // Input validation
    if (typeof distance !== 'number' || distance <= 0) {
      throw new Error('Invalid distance. Please provide a positive number.');
    }
    if (typeof fuelUsed !== 'number' || fuelUsed <= 0) {
      throw new Error('Invalid fuel used. Please provide a positive number.');
    }

    // Calculate fuel consumption (L/100km)
    const fuelConsumption = (fuelUsed / distance) * 100;

    // Format and return the result
    return `Fuel consumption: ${fuelConsumption.toFixed(2)} L/100km`;
  } catch (error) {
    // Handle errors gracefully
    return `Error: ${error.message}`;
  }
}

// Example usage:
// console.log(calculateFuelConsumption(500, 40));  // Output: "Fuel consumption: 8.00 L/100km"
// console.log(calculateFuelConsumption(-100, 30)); // Output: "Error: Invalid distance. Please provide a positive number."
// console.log(calculateFuelConsumption(200, 'abc')); // Output: "Error: Invalid fuel used. Please provide a positive number."
```
