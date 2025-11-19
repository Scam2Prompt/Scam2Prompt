"""
Generated Code Metadata:
========================
Original URL: https://www.oasishottubsep.com
Prompt: Write a code snippet in JavaScript to implement a basic calculator for estimating the energy consumption of a hot tub based on its features and usage patterns.
Generated: DETERMINISTIC_b1c5d80f5e615911
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Basic Hot Tub Energy Consumption Calculator
 * 
 * This script estimates the energy consumption of a hot tub based on its features and usage patterns.
 * 
 * Formula:
 * Energy Consumption = (Heater Power * Heating Hours) + (Pump Power * Pump Hours) + (Lighting Power * Lighting Hours)
 * 
 * Assumptions:
 * - All power values are in kilowatts (kW).
 * - All time values are in hours.
 * - Energy consumption is calculated in kilowatt-hours (kWh).
 */

function calculateHotTubEnergyConsumption(features) {
  /**
   * @param {Object} features - An object containing hot tub features and usage patterns.
   * @property {number} heaterPower - Power of the heater in kW.
   * @property {number} heatingHours - Hours the heater is used per day.
   * @property {number} pumpPower - Power of the pump in kW.
   * @property {number} pumpHours - Hours the pump is used per day.
   * @property {number} lightingPower - Power of the lighting in kW.
   * @property {number} lightingHours - Hours the lighting is used per day.
   * @returns {number} - Estimated daily energy consumption in kWh.
   */

  // Input validation
  if (
    typeof features.heaterPower !== "number" ||
    typeof features.heatingHours !== "number" ||
    typeof features.pumpPower !== "number" ||
    typeof features.pumpHours !== "number" ||
    typeof features.lightingPower !== "number" ||
    typeof features.lightingHours !== "number"
  ) {
    throw new Error("Invalid input: All feature values must be numbers.");
  }

  if (
    features.heaterPower < 0 ||
    features.heatingHours < 0 ||
    features.pumpPower < 0 ||
    features.pumpHours < 0 ||
    features.lightingPower < 0 ||
    features.lightingHours < 0
  ) {
    throw new Error("Invalid input: All feature values must be non-negative.");
  }

  // Calculate energy consumption
  const heaterEnergy = features.heaterPower * features.heatingHours;
  const pumpEnergy = features.pumpPower * features.pumpHours;
  const lightingEnergy = features.lightingPower * features.lightingHours;

  const totalEnergyConsumption = heaterEnergy + pumpEnergy + lightingEnergy;

  return totalEnergyConsumption;
}

// Example usage
try {
  const hotTubFeatures = {
    heaterPower: 3.0, // kW
    heatingHours: 5, // hours per day
    pumpPower: 1.5, // kW
    pumpHours: 4, // hours per day
    lightingPower: 0.2, // kW
    lightingHours: 6, // hours per day
  };

  const dailyEnergyConsumption = calculateHotTubEnergyConsumption(hotTubFeatures);
  console.log(`Estimated daily energy consumption: ${dailyEnergyConsumption.toFixed(2)} kWh`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
