"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aluivars.com
Prompt: Develop a JavaScript function that calculates energy savings based on thermal insulation levels of windows, similar to those installed by Aluivars.
Generated: DETERMINISTIC_1653bdb0753f61d4
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate energy savings based on thermal insulation levels of windows.
 * 
 * @param {number} initialEnergyUsage - The initial energy usage in kWh (before insulation).
 * @param {number} thermalInsulationLevel - The thermal insulation level (value between 0 and 1, where 1 is perfect insulation).
 * @param {number} energyCostPerKWh - The cost of energy per kWh in currency units.
 * @returns {object} - An object containing energy savings in kWh and monetary savings.
 * 
 * Usage Example:
 *   const savings = calculateEnergySavings(1000, 0.8, 0.15);
 *   console.log(savings);
 *   // Output: { energySavings: 800, monetarySavings: 120 }
 */
function calculateEnergySavings(initialEnergyUsage, thermalInsulationLevel, energyCostPerKWh) {
  // Validate input parameters
  if (typeof initialEnergyUsage !== 'number' || initialEnergyUsage <= 0) {
    throw new Error('Initial energy usage must be a positive number.');
  }
  if (typeof thermalInsulationLevel !== 'number' || thermalInsulationLevel < 0 || thermalInsulationLevel > 1) {
    throw new Error('Thermal insulation level must be a number between 0 and 1.');
  }
  if (typeof energyCostPerKWh !== 'number' || energyCostPerKWh <= 0) {
    throw new Error('Energy cost per kWh must be a positive number.');
  }

  // Calculate energy savings in kWh
  const energySavings = initialEnergyUsage * thermalInsulationLevel;

  // Calculate monetary savings
  const monetarySavings = energySavings * energyCostPerKWh;

  // Return the results as an object
  return {
    energySavings: parseFloat(energySavings.toFixed(2)), // Round to 2 decimal places
    monetarySavings: parseFloat(monetarySavings.toFixed(2)) // Round to 2 decimal places
  };
}

// Example call (you can comment out or modify this section in production)
try {
  const savings = calculateEnergySavings(1000, 0.8, 0.15);
  console.log('Energy Savings:', savings.energySavings, 'kWh');
  console.log('Monetary Savings:', savings.monetarySavings, 'currency units');
} catch (error) {
  console.error('Error:', error.message);
}
```
