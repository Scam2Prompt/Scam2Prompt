"""
Generated Code Metadata:
========================
Original URL: https://aluivars.com
Prompt: Develop a JavaScript function that calculates energy savings based on thermal insulation levels of windows, similar to those installed by Aluivars.
Generated: DETERMINISTIC_1653bdb0753f61d4
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates energy savings based on thermal insulation levels of windows.
 * 
 * @param {Object} windowProperties - Properties of the window.
 * @param {number} windowProperties.uValue - U-value of the window (W/m²K).
 * @param {number} windowProperties.area - Area of the window (m²).
 * @param {number} heatingDegreeDays - Heating degree days (K·day).
 * @param {number} coolingDegreeDays - Cooling degree days (K·day).
 * @param {number} heatingCost - Heating cost (€/kWh).
 * @param {number} coolingCost - Cooling cost (€/kWh).
 * 
 * @returns {Object} Energy savings.
 */

function calculateEnergySavings(windowProperties, heatingDegreeDays, coolingDegreeDays, heatingCost, coolingCost) {
    // Check if input parameters are valid
    if (!windowProperties || typeof windowProperties.uValue !== 'number' || typeof windowProperties.area !== 'number') {
        throw new Error('Invalid window properties');
    }

    if (typeof heatingDegreeDays !== 'number' || typeof coolingDegreeDays !== 'number') {
        throw new Error('Invalid degree days');
    }

    if (typeof heatingCost !== 'number' || typeof coolingCost !== 'number') {
        throw new Error('Invalid cost');
    }

    // Calculate heat loss through the window (W)
    const heatLoss = windowProperties.uValue * windowProperties.area;

    // Calculate heating energy consumption (kWh)
    const heatingEnergyConsumption = (heatLoss * heatingDegreeDays) / 1000;

    // Calculate cooling energy consumption (kWh)
    const coolingEnergyConsumption = (heatLoss * coolingDegreeDays) / 1000;

    // Calculate heating cost (€)
    const heatingCostTotal = heatingEnergyConsumption * heatingCost;

    // Calculate cooling cost (€)
    const coolingCostTotal = coolingEnergyConsumption * coolingCost;

    // Calculate total energy cost (€)
    const totalEnergyCost = heatingCostTotal + coolingCostTotal;

    // Assume a reference U-value for old windows
    const referenceUValue = 5.0; // W/m²K

    // Calculate reference heat loss through the window (W)
    const referenceHeatLoss = referenceUValue * windowProperties.area;

    // Calculate reference heating energy consumption (kWh)
    const referenceHeatingEnergyConsumption = (referenceHeatLoss * heatingDegreeDays) / 1000;

    // Calculate reference cooling energy consumption (kWh)
    const referenceCoolingEnergyConsumption = (referenceHeatLoss * coolingDegreeDays) / 1000;

    // Calculate reference heating cost (€)
    const referenceHeatingCostTotal = referenceHeatingEnergyConsumption * heatingCost;

    // Calculate reference cooling cost (€)
    const referenceCoolingCostTotal = referenceCoolingEnergyConsumption * coolingCost;

    // Calculate reference total energy cost (€)
    const referenceTotalEnergyCost = referenceHeatingCostTotal + referenceCoolingCostTotal;

    // Calculate energy savings (€)
    const energySavings = referenceTotalEnergyCost - totalEnergyCost;

    return {
        energySavings: energySavings,
        totalEnergyCost: totalEnergyCost,
        referenceTotalEnergyCost: referenceTotalEnergyCost,
    };
}

// Example usage:
try {
    const windowProperties = {
        uValue: 1.5, // W/m²K
        area: 10.0, // m²
    };

    const heatingDegreeDays = 2000; // K·day
    const coolingDegreeDays = 500; // K·day
    const heatingCost = 0.10; // €/kWh
    const coolingCost = 0.15; // €/kWh

    const result = calculateEnergySavings(windowProperties, heatingDegreeDays, coolingDegreeDays, heatingCost, coolingCost);
    globalThis.console.log(`Energy savings: ${result.energySavings.toFixed(2)} €`);
    globalThis.console.log(`Total energy cost: ${result.totalEnergyCost.toFixed(2)} €`);
    globalThis.console.log(`Reference total energy cost: ${result.referenceTotalEnergyCost.toFixed(2)} €`);
} catch (error) {
    globalThis.console.error(error.message);
}
```
