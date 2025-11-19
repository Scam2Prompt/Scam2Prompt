"""
Generated Code Metadata:
========================
Original URL: https://screciclados.mx
Prompt: Develop a function in JavaScript that calculates the environmental impact of recycling metals, based on the mission of SCR Reciclados.
Generated: DETERMINISTIC_d111cddc8a253866
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate the environmental impact of recycling metals.
 * Based on the mission of SCR Reciclados, this function estimates the 
 * reduction in energy consumption and CO2 emissions achieved by recycling.
 *
 * @param {Object} metalData - An object containing details about the metals recycled.
 * @param {number} metalData.weight - Total weight of the metal recycled in kilograms.
 * @param {string} metalData.type - Type of metal recycled (e.g., "aluminum", "steel", "copper").
 * @returns {Object} - An object containing the estimated environmental impact:
 *                     - energySaved (kWh)
 *                     - co2Reduced (kg)
 */
function calculateEnvironmentalImpact(metalData) {
  // Validate input
  if (!metalData || typeof metalData.weight !== 'number' || metalData.weight <= 0 || typeof metalData.type !== 'string') {
    throw new Error('Invalid input: metalData must contain a positive weight and a valid type.');
  }

  // Constants for energy savings and CO2 reduction per kilogram of recycled metal
  const impactFactors = {
    aluminum: { energySavedPerKg: 14, co2ReducedPerKg: 9 },
    steel: { energySavedPerKg: 4, co2ReducedPerKg: 2 },
    copper: { energySavedPerKg: 8, co2ReducedPerKg: 5 },
  };

  // Check if the metal type is supported
  const metalImpact = impactFactors[metalData.type.toLowerCase()];
  if (!metalImpact) {
    throw new Error(`Unsupported metal type: ${metalData.type}. Supported types are aluminum, steel, and copper.`);
  }

  // Calculate environmental impact
  const energySaved = metalData.weight * metalImpact.energySavedPerKg;
  const co2Reduced = metalData.weight * metalImpact.co2ReducedPerKg;

  // Return the results
  return {
    energySaved: energySaved.toFixed(2), // Round to 2 decimal places
    co2Reduced: co2Reduced.toFixed(2),  // Round to 2 decimal places
  };
}

// Example usage:
try {
  const impact = calculateEnvironmentalImpact({ weight: 100, type: 'aluminum' });
  console.log('Environmental Impact:', impact);
} catch (error) {
  console.error('Error:', error.message);
}
```
