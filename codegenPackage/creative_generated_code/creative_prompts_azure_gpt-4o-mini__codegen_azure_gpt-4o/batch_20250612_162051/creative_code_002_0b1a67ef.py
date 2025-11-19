"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.nexenergetic.com
Prompt: Create a JavaScript function that simulates the energy production of a photovoltaic system for isolated autoconsumption, referencing Nexe Energetic's offerings.
Generated: DETERMINISTIC_0b1a67efcbf89402
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
 * Simulates the energy production of a photovoltaic system for isolated autoconsumption.
 * 
 * @param {number} solarIrradiance - The solar irradiance in kWh/m² (average daily value).
 * @param {number} panelEfficiency - The efficiency of the photovoltaic panel as a decimal (e.g., 0.18 for 18% efficiency).
 * @param {number} panelArea - The total area of the photovoltaic panels in m².
 * @param {number} systemLossFactor - System loss factor as a decimal (e.g., 0.15 for 15% losses).
 * @returns {number} - The estimated daily energy production in kWh.
 */
function simulateEnergyProduction(solarIrradiance, panelEfficiency, panelArea, systemLossFactor) {
  try {
    // Input validation
    if (
      typeof solarIrradiance !== 'number' || solarIrradiance <= 0 ||
      typeof panelEfficiency !== 'number' || panelEfficiency <= 0 || panelEfficiency > 1 ||
      typeof panelArea !== 'number' || panelArea <= 0 ||
      typeof systemLossFactor !== 'number' || systemLossFactor < 0 || systemLossFactor > 1
    ) {
      throw new Error('Invalid input parameters. Please ensure all inputs are positive numbers and within expected ranges.');
    }

    // Calculate raw energy production without system losses
    const rawEnergyProduction = solarIrradiance * panelEfficiency * panelArea;

    // Adjust for system losses
    const adjustedEnergyProduction = rawEnergyProduction * (1 - systemLossFactor);

    // Return the final energy production value rounded to 2 decimal places
    return parseFloat(adjustedEnergyProduction.toFixed(2));
  } catch (error) {
    // Handle errors gracefully and log to console
    console.error(error.message);
    return null; // Return null to indicate failure
  }
}

// Example usage:
// Parameters:
// - Solar irradiance: 5.5 kWh/m²/day (average)
// - Panel efficiency: 18% (0.18)
// - Panel area: 20 m²
// - System loss factor: 15% (0.15)
const dailyEnergyProduction = simulateEnergyProduction(5.5, 0.18, 20, 0.15);
console.log(`Estimated Daily Energy Production: ${dailyEnergyProduction} kWh`);
```
