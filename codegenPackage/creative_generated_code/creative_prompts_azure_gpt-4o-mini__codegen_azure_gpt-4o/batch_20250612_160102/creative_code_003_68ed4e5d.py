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
 * The formula considers room volume and humidity level to determine the
 * required ozone concentration in parts per million (ppm).
 *
 * @param {number} volume - The volume of the room in cubic meters (m³).
 * @param {number} humidity - The relative humidity of the room in percentage (%).
 * @returns {number} The optimal ozone concentration in ppm.
 * @throws {Error} Throws an error if inputs are invalid (negative or non-numeric).
 */
function calculateOzoneConcentration(volume, humidity) {
    // Input validation: Ensure both volume and humidity are positive numbers
    if (typeof volume !== 'number' || volume <= 0) {
        throw new Error("Invalid room volume. It must be a positive number.");
    }
    if (typeof humidity !== 'number' || humidity < 0 || humidity > 100) {
        throw new Error("Invalid humidity level. It must be a number between 0 and 100.");
    }

    // Base ozone concentration per cubic meter (ppm)
    const BASE_CONCENTRATION_PER_M3 = 0.05;

    // Humidity adjustment factor:
    // Higher humidity reduces ozone effectiveness, requiring higher concentration.
    const HUMIDITY_FACTOR = 1 + (humidity / 100) * 0.5;

    // Calculate the ozone concentration
    const ozoneConcentration = volume * BASE_CONCENTRATION_PER_M3 * HUMIDITY_FACTOR;

    // Return the calculated concentration rounded to two decimal places
    return Math.round(ozoneConcentration * 100) / 100;
}

// Example usage:
try {
    const roomVolume = 50; // Room volume in m³
    const roomHumidity = 60; // Humidity percentage
    const optimalOzoneConcentration = calculateOzoneConcentration(roomVolume, roomHumidity);
    console.log(`Optimal Ozone Concentration: ${optimalOzoneConcentration} ppm`);
} catch (error) {
    console.error(error.message);
}
```
