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
 * Function to calculate the average temperature of planets.
 * The function returns an object with the average temperature for each planet.
 */
function calculateAverageTemperatures() {
  // Extreme temperature data for each planet (in Celsius)
  const planetTemperatures = {
    Mercury: { min: -173, max: 427 },
    Venus: { min: 462, max: 462 }, // Surface temperature is nearly uniform
    Earth: { min: -89, max: 58 },
    Mars: { min: -125, max: 20 },
    Jupiter: { min: -108, max: -108 }, // Estimated upper atmosphere temperature
    Saturn: { min: -139, max: -139 }, // Estimated upper atmosphere temperature
    Uranus: { min: -195, max: -195 }, // Estimated upper atmosphere temperature
    Neptune: { min: -200, max: -200 } // Estimated upper atmosphere temperature
  };

  /**
   * Helper function to calculate average temperature.
   * @param {number} min - Minimum temperature.
   * @param {number} max - Maximum temperature.
   * @returns {number} The average temperature.
   */
  function calculateAverage(min, max) {
    return (min + max) / 2;
  }

  // Object to store average temperatures for each planet
  const averageTemperatures = {};

  // Iterate through the planet temperatures and calculate the averages
  for (const planet in planetTemperatures) {
    if (Object.hasOwnProperty.call(planetTemperatures, planet)) {
      const { min, max } = planetTemperatures[planet];
      // Calculate the average temperature
      averageTemperatures[planet] = calculateAverage(min, max);
    }
  }

  return averageTemperatures;
}

// Example usage:
// Print average temperatures for all planets
try {
  console.log(calculateAverageTemperatures());
} catch (error) {
  console.error("An error occurred during calculation: ", error.message);
}
```
