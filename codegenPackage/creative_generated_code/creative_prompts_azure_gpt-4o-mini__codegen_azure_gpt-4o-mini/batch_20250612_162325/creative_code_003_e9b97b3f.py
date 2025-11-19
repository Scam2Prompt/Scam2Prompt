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
 * Calculates the fuel consumption of the MG HS in liters per 100 kilometers.
 * 
 * @param {number} distance - The distance traveled in kilometers.
 * @param {number} fuelUsed - The amount of fuel used in liters.
 * @returns {number} The fuel consumption in liters per 100 kilometers.
 * @throws {Error} Will throw an error if distance or fuelUsed is negative or zero.
 */
function calculateFuelConsumption(distance, fuelUsed) {
    // Validate input
    if (typeof distance !== 'number' || typeof fuelUsed !== 'number') {
        throw new Error('Both distance and fuelUsed should be numbers.');
    }
    if (distance <= 0) {
        throw new Error('Distance traveled must be greater than zero.');
    }
    if (fuelUsed <= 0) {
        throw new Error('Fuel used must be greater than zero.');
    }
    
    // Calculate fuel consumption
    const consumption = (fuelUsed / distance) * 100;

    return parseFloat(consumption.toFixed(2)); // Return the result rounded to 2 decimal places
}

// Example usage:
try {
    const distanceTraveled = 250; // kilometers
    const fuelUsed = 30; // liters
    const fuelConsumption = calculateFuelConsumption(distanceTraveled, fuelUsed);
    console.log(`Fuel consumption: ${fuelConsumption} L/100km`);
} catch (error) {
    console.error(error.message);
}
```
