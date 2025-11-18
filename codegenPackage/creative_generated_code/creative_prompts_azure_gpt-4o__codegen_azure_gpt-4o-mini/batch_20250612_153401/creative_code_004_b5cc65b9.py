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
 * Converts temperature between Celsius and Fahrenheit.
 * 
 * @param {number} temperature - The temperature value to convert.
 * @param {string} unit - The unit of the input temperature. Accepts 'C' for Celsius and 'F' for Fahrenheit.
 * @returns {number} - The converted temperature in the target unit.
 * @throws {Error} - Throws an error if the input unit is invalid.
 */
function convertTemperature(temperature, unit) {
    // Check if the temperature is a number
    if (typeof temperature !== 'number') {
        throw new Error('Temperature must be a number.');
    }

    // Normalize the unit input
    unit = unit.toUpperCase();

    // Convert based on the input unit
    switch (unit) {
        case 'C': // Celsius to Fahrenheit
            return (temperature * 9/5) + 32;

        case 'F': // Fahrenheit to Celsius
            return (temperature - 32) * 5/9;

        default:
            throw new Error('Invalid unit. Please use "C" for Celsius or "F" for Fahrenheit.');
    }
}

// Example usage:
try {
    const celsius = 25;
    const fahrenheit = convertTemperature(celsius, 'C');
    console.log(`${celsius}°C is equal to ${fahrenheit}°F`);

    const fahrenheitValue = 77;
    const celsiusValue = convertTemperature(fahrenheitValue, 'F');
    console.log(`${fahrenheitValue}°F is equal to ${celsiusValue}°C`);
} catch (error) {
    console.error(error.message);
}
```
