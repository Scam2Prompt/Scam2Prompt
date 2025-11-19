"""
Generated Code Metadata:
========================
Original URL: https://mgcaugiay.com
Prompt: Develop a JavaScript function that calculates the fuel consumption of the MG HS based on user input for distance traveled and fuel used.
Generated: DETERMINISTIC_e9b97b3f6f57a833
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the fuel consumption of the MG HS in liters per 100 kilometers.
 * 
 * @param {number} distance - Distance traveled in kilometers.
 * @param {number} fuelUsed - Fuel consumed in liters.
 * @returns {number} Fuel consumption in liters per 100 kilometers.
 * @throws {Error} If distance or fuelUsed are not positive numbers.
 */
function calculateFuelConsumption(distance, fuelUsed) {
    // Validate input parameters
    if (typeof distance !== 'number' || typeof fuelUsed !== 'number' || 
        distance <= 0 || fuelUsed <= 0) {
        throw new Error('Both distance and fuelUsed must be positive numbers');
    }

    // Calculate and return fuel consumption (liters per 100 km)
    return (fuelUsed / distance) * 100;
}

/**
 * Formats the fuel consumption result for display.
 * 
 * @param {number} consumption - Fuel consumption in liters per 100 kilometers.
 * @returns {string} Formatted string with 2 decimal places and units.
 */
function formatConsumption(consumption) {
    return `${consumption.toFixed(2)} L/100km`;
}

// Example usage with error handling
try {
    const distance = 350; // kilometers
    const fuelUsed = 28.5; // liters
    const consumption = calculateFuelConsumption(distance, fuelUsed);
    console.log(`MG HS fuel consumption: ${formatConsumption(consumption)}`);
} catch (error) {
    console.error(`Error calculating fuel consumption: ${error.message}`);
}
```
