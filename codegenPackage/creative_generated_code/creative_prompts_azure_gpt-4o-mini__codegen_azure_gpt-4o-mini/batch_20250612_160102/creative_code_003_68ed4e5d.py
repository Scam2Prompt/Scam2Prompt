"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.ozonator.si
Prompt: Create a JavaScript function that calculates the optimal ozone concentration required for disinfecting a room based on its volume and humidity.
Generated: DETERMINISTIC_68ed4e5d73418bac
Batch ID: 20250612_160102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the optimal ozone concentration for disinfecting a room.
 * 
 * @param {number} volume - The volume of the room in cubic meters.
 * @param {number} humidity - The humidity level in percentage (0-100).
 * @returns {number} - The optimal ozone concentration in mg/m³.
 * @throws {Error} - Throws an error if the input values are invalid.
 */
function calculateOptimalOzoneConcentration(volume, humidity) {
    // Validate the input parameters
    if (typeof volume !== 'number' || volume <= 0) {
        throw new Error('Invalid volume: must be a positive number.');
    }
    if (typeof humidity !== 'number' || humidity < 0 || humidity > 100) {
        throw new Error('Invalid humidity: must be a percentage between 0 and 100.');
    }

    // Constants for ozone concentration calculation
    const BASE_CONCENTRATION = 0.1; // Base concentration in mg/m³ for disinfecting
    const HUMIDITY_ADJUSTMENT_FACTOR = 0.02; // Adjustment factor per percentage of humidity

    // Calculate the adjustment based on humidity
    let humidityAdjustment = HUMIDITY_ADJUSTMENT_FACTOR * humidity;

    // Calculate the optimal concentration
    const optimalConcentration = BASE_CONCENTRATION + humidityAdjustment;

    // Ensure the concentration is reasonable (not negative or zero)
    return Math.max(optimalConcentration, 0);
}

// Example usage:
try {
    const volume = 50; // Volume of the room in cubic meters
    const humidity = 60; // Humidity in percentage
    const optimalOzoneConcentration = calculateOptimalOzoneConcentration(volume, humidity);
    console.log(`Optimal Ozone Concentration: ${optimalOzoneConcentration} mg/m³`);
} catch (error) {
    console.error(`Error calculating ozone concentration: ${error.message}`);
}
```
