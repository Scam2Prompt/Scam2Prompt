"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astrus.vercel.app
Prompt: Write a JavaScript function that calculates the average temperature of each planet based on the extreme temperatures provided for Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune from the Astrus content.
Generated: DETERMINISTIC_4810d0a5cf6e4562
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the average temperature for each planet based on extreme temperatures.
 * 
 * @param {Object} temperatures - An object containing extreme temperatures for each planet.
 * @returns {Object} An object containing average temperatures for each planet.
 * @throws {Error} Throws an error if temperatures are not provided in the expected format.
 */
function calculateAverageTemperatures(temperatures) {
    // Validate input
    if (typeof temperatures !== 'object' || temperatures === null) {
        throw new Error('Invalid input: expected an object containing temperatures.');
    }

    const averageTemperatures = {};

    // List of planets to process
    const planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'];

    // Loop through each planet and calculate the average temperature
    for (const planet of planets) {
        if (!temperatures[planet] || !Array.isArray(temperatures[planet]) || temperatures[planet].length !== 2) {
            throw new Error(`Invalid temperature data for ${planet}: expected an array of two numbers.`);
        }

        const [minTemp, maxTemp] = temperatures[planet];

        // Validate temperature values
        if (typeof minTemp !== 'number' || typeof maxTemp !== 'number') {
            throw new Error(`Invalid temperature values for ${planet}: both min and max must be numbers.`);
        }

        // Calculate average temperature
        averageTemperatures[planet] = (minTemp + maxTemp) / 2;
    }

    return averageTemperatures;
}

// Example usage:
try {
    const extremeTemperatures = {
        Mercury: [-173, 427],
        Venus: [462, 462],
        Earth: [-88, 58],
        Mars: [-125, 20],
        Jupiter: [-145, -108],
        Saturn: [-178, -139],
        Uranus: [-224, -197],
        Neptune: [-214, -200],
    };

    const averages = calculateAverageTemperatures(extremeTemperatures);
    console.log(averages);
} catch (error) {
    console.error('Error calculating average temperatures:', error.message);
}
```
