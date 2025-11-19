"""
Generated Code Metadata:
========================
Original URL: https://www.ozonator.si
Prompt: Create a JavaScript function that calculates the optimal ozone concentration required for disinfecting a room based on its volume and humidity.
Generated: DETERMINISTIC_68ed4e5d73418bac
Batch ID: 20250612_160102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the optimal ozone concentration required for disinfecting a room.
 * 
 * @param {number} volume - The volume of the room in cubic meters (m³).
 * @param {number} humidity - The relative humidity of the room as a percentage (0-100).
 * @returns {number} - The optimal ozone concentration in parts per million (ppm).
 * @throws {Error} - Throws an error if the volume is less than or equal to zero,
 *                   or if the humidity is not within the range of 0 to 100.
 */
function calculateOptimalOzoneConcentration(volume, humidity) {
    // Validate input parameters
    if (volume <= 0) {
        throw new Error("Volume must be greater than zero.");
    }
    if (humidity < 0 || humidity > 100) {
        throw new Error("Humidity must be between 0 and 100.");
    }

    // Constants for ozone concentration calculation
    const baseConcentration = 0.1; // Base concentration in ppm for dry air
    const humidityFactor = 0.02; // Increase in concentration per percentage of humidity

    // Calculate the optimal ozone concentration
    const optimalConcentration = baseConcentration + (humidity * humidityFactor);

    // Adjust concentration based on room volume (assuming a linear relationship)
    const concentrationPerCubicMeter = optimalConcentration * volume;

    // Return the calculated concentration
    return concentrationPerCubicMeter;
}

// Example usage
try {
    const roomVolume = 50; // Room volume in m³
    const roomHumidity = 60; // Room humidity in percentage
    const ozoneConcentration = calculateOptimalOzoneConcentration(roomVolume, roomHumidity);
    console.log(`Optimal ozone concentration for disinfecting the room: ${ozoneConcentration.toFixed(2)} ppm`);
} catch (error) {
    console.error(`Error calculating ozone concentration: ${error.message}`);
}
```
