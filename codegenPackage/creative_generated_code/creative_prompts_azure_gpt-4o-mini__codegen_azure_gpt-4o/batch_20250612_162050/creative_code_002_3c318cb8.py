"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://volport.com
Prompt: Create a JavaScript function that simulates the use of 3M sticky adhesive holders for mounting devices, based on the unique adhesive solutions offered by Volport.
Generated: DETERMINISTIC_3c318cb85f0acbd6
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates the use of adhesive holders for mounting devices.
 * Based on unique adhesive solutions, the function calculates
 * the effectiveness of the adhesive over time and under different conditions.
 *
 * @param {string} surfaceType - The type of surface where the adhesive is being mounted (e.g., 'glass', 'wood', 'metal').
 * @param {number} deviceWeight - The weight of the device in grams.
 * @param {number} duration - The duration the adhesive is expected to hold in hours.
 * @param {number} temperature - The ambient temperature in degrees Celsius.
 * @returns {object} - An object with details about the adhesive performance, including success or failure.
 */
function simulateAdhesiveHolder(surfaceType, deviceWeight, duration, temperature) {
  // Constants
  const MAX_WEIGHT_CAPACITY = 2000; // Maximum weight the adhesive can hold in grams.
  const TEMPERATURE_RANGE = { min: -10, max: 50 }; // Optimal temperature range in degrees Celsius.
  const SURFACE_TYPES = ['glass', 'wood', 'metal', 'plastic']; // Supported surface types.

  // Error handling: Validate inputs
  if (!SURFACE_TYPES.includes(surfaceType)) {
    throw new Error(`Unsupported surface type. Supported types are: ${SURFACE_TYPES.join(', ')}`);
  }
  if (deviceWeight <= 0 || duration <= 0 || temperature < -50 || temperature > 100) {
    throw new Error('Invalid input values. Please check the weight, duration, or temperature.');
  }

  // Simulate performance degradation
  let success = true; // Flag to indicate if the adhesive holds successfully.
  let performanceScore = 100; // Start with a perfect performance score (0-100 scale).

  // Check weight capacity
  if (deviceWeight > MAX_WEIGHT_CAPACITY) {
    success = false;
    performanceScore -= 50; // Major penalty for exceeding weight capacity.
  }

  // Check temperature conditions
  if (temperature < TEMPERATURE_RANGE.min || temperature > TEMPERATURE_RANGE.max) {
    success = false;
    performanceScore -= 30; // Penalty for operating outside optimal temperature range.
  }

  // Simulate duration impact
  if (duration > 24) {
    performanceScore -= Math.min(20, duration / 24); // Gradual degradation for prolonged duration.
  }

  // Adjust performance for specific surface types
  switch (surfaceType) {
    case 'glass':
      performanceScore -= 5; // Minimal impact for smooth surfaces.
      break;
    case 'wood':
      performanceScore -= 10; // Slightly less optimal for porous surfaces.
      break;
    case 'metal':
      performanceScore -= 2; // Almost ideal performance.
      break;
    case 'plastic':
      performanceScore -= 15; // Adhesion may be weaker depending on plastic type.
      break;
  }

  // Final performance evaluation
  if (performanceScore < 40) {
    success = false; // Adhesive fails if performance score is too low.
  }

  // Return the simulation results
  return {
    success,
    performanceScore,
    reason: success
      ? 'Adhesive holds successfully under given conditions.'
      : 'Adhesive failed due to unsuitable conditions or excessive stress.',
  };
}

// Example usage
try {
  const result = simulateAdhesiveHolder('glass', 1500, 12, 25);
  console.log(result);
} catch (error) {
  console.error(error.message);
}
```
