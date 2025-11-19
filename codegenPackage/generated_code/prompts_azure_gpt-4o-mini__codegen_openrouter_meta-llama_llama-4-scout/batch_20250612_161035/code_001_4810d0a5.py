"""
Generated Code Metadata:
========================
Original URL: https://astrus.vercel.app
Prompt: Write a JavaScript function that calculates the average temperature of each planet based on the extreme temperatures provided for Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune from the Astrus content.
Generated: DETERMINISTIC_4810d0a5cf6e4562
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the average temperature of each planet in our solar system.
 * 
 * @param {Object} planetTemperatures - An object containing the extreme temperatures of each planet.
 * @returns {Object} An object with the average temperature of each planet.
 */
function calculateAverageTemperatures(planetTemperatures) {
    // Define the planets in our solar system
    const planets = [
        'Mercury', 
        'Venus', 
        'Earth', 
        'Mars', 
        'Jupiter', 
        'Saturn', 
        'Uranus', 
        'Neptune'
    ];

    // Initialize an object to store the average temperatures
    const averageTemperatures = {};

    // Check if planetTemperatures is an object
    if (typeof planetTemperatures !== 'object') {
        throw new Error('Invalid input: planetTemperatures must be an object');
    }

    // Iterate over each planet
    planets.forEach(planet => {
        // Check if the planet has temperature data
        if (!planetTemperatures[planet]) {
            throw new Error(`Temperature data not found for ${planet}`);
        }

        // Destructure the temperature data
        const { min, max } = planetTemperatures[planet];

        // Check if the temperature data is valid
        if (typeof min !== 'number' || typeof max !== 'number') {
            throw new Error(`Invalid temperature data for ${planet}`);
        }

        // Calculate the average temperature
        const averageTemperature = (min + max) / 2;

        // Store the average temperature
        averageTemperatures[planet] = averageTemperature;
    });

    return averageTemperatures;
}

// Example usage:
const planetTemperatures = {
    Mercury: { min: -173, max: 427 },
    Venus: { min: 462, max: 482 },
    Earth: { min: -89, max: 57 },
    Mars: { min: -125, max: 20 },
    Jupiter: { min: -150, max: -110 },
    Saturn: { min: -178, max: -145 },
    Uranus: { min: -216, max: -173 },
    Neptune: { min: -224, max: -201 }
};

try {
    const averageTemperatures = calculateAverageTemperatures(planetTemperatures);
    console.log(averageTemperatures);
} catch (error) {
    console.error(error.message);
}
```
