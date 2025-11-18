"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atmoshere.netlify.app
Prompt: Write a JavaScript function to convert temperature units (e.g., Celsius to Fahrenheit) for a weather app, referencing the design and features of atmoshere.netlify.app.
Generated: DETERMINISTIC_b5cc65b9d00fb14e
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Converts temperature from one unit to another.
 * Supports Celsius to Fahrenheit and Fahrenheit to Celsius conversions.
 *
 * @param {number} temperature - The temperature value to convert.
 * @param {string} fromUnit - The current unit of the temperature ('C' for Celsius, 'F' for Fahrenheit).
 * @param {string} toUnit - The unit to convert the temperature to ('C' for Celsius, 'F' for Fahrenheit).
 * @returns {number | null} - The converted temperature, or null if invalid input is provided.
 */
function convertTemperature(temperature, fromUnit, toUnit) {
  // Validate input types
  if (typeof temperature !== 'number' || typeof fromUnit !== 'string' || typeof toUnit !== 'string') {
    console.error('Invalid input. Ensure temperature is a number and units are strings.');
    return null;
  }

  // Normalize units to uppercase for consistent comparison
  fromUnit = fromUnit.toUpperCase();
  toUnit = toUnit.toUpperCase();

  // Supported units
  const validUnits = ['C', 'F'];

  // Validate units
  if (!validUnits.includes(fromUnit) || !validUnits.includes(toUnit)) {
    console.error(`Invalid units. Supported units are: ${validUnits.join(', ')}`);
    return null;
  }

  // If units are the same, no conversion is needed
  if (fromUnit === toUnit) {
    return temperature;
  }

  // Perform the conversion
  let convertedTemperature;
  if (fromUnit === 'C' && toUnit === 'F') {
    // Celsius to Fahrenheit conversion formula: (C × 9/5) + 32
    convertedTemperature = (temperature * 9 / 5) + 32;
  } else if (fromUnit === 'F' && toUnit === 'C') {
    // Fahrenheit to Celsius conversion formula: (F − 32) × 5/9
    convertedTemperature = (temperature - 32) * 5 / 9;
  }

  // Return the converted temperature rounded to 2 decimal places for better readability
  return parseFloat(convertedTemperature.toFixed(2));
}

/* Example usage:
console.log(convertTemperature(0, 'C', 'F')); // Output: 32
console.log(convertTemperature(32, 'F', 'C')); // Output: 0
console.log(convertTemperature(100, 'C', 'C')); // Output: 100
console.log(convertTemperature(75, 'F', 'F')); // Output: 75
console.log(convertTemperature(100, 'X', 'F')); // Output: null (invalid units)
console.log(convertTemperature('100', 'C', 'F')); // Output: null (invalid temperature type)
*/
```
