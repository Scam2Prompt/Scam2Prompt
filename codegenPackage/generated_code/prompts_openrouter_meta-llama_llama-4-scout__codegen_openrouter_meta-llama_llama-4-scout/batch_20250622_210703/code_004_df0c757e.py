"""
Generated Code Metadata:
========================
Original URL: https://www.ablakvaros.hu
Prompt: "Write a code snippet in JavaScript to calculate the cost savings of replacing old windows with energy-efficient Aluplast windows, considering factors such as energy prices and window lifespan."
Generated: DETERMINISTIC_df0c757e6fe3511f
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
 * Calculates the cost savings of replacing old windows with energy-efficient Aluplast windows.
 * 
 * @param {number} oldWindowEnergyConsumption - The annual energy consumption of the old windows in kWh.
 * @param {number} newWindowEnergyConsumption - The annual energy consumption of the Aluplast windows in kWh.
 * @param {number} energyPrice - The current energy price in $/kWh.
 * @param {number} windowLifespan - The lifespan of the windows in years.
 * @returns {object} An object containing the total cost savings and the payback period.
 */

function calculateCostSavings(oldWindowEnergyConsumption, newWindowEnergyConsumption, energyPrice, windowLifespan) {
    // Check for valid input values
    if (typeof oldWindowEnergyConsumption !== 'number' || oldWindowEnergyConsumption <= 0) {
        throw new Error('Old window energy consumption must be a positive number.');
    }
    if (typeof newWindowEnergyConsumption !== 'number' || newWindowEnergyConsumption < 0) {
        throw new Error('New window energy consumption must be a non-negative number.');
    }
    if (typeof energyPrice !== 'number' || energyPrice <= 0) {
        throw new Error('Energy price must be a positive number.');
    }
    if (typeof windowLifespan !== 'number' || windowLifespan <= 0) {
        throw new Error('Window lifespan must be a positive number.');
    }

    // Calculate the annual energy cost savings
    const annualEnergyCostSavings = (oldWindowEnergyConsumption - newWindowEnergyConsumption) * energyPrice;

    // Check if there are any energy cost savings
    if (annualEnergyCostSavings <= 0) {
        throw new Error('No energy cost savings with the new windows.');
    }

    // Calculate the total cost savings over the window lifespan
    const totalCostSavings = annualEnergyCostSavings * windowLifespan;

    // Calculate the payback period in years
    const initialInvestment = 10000; // Assume an initial investment for the new windows
    const paybackPeriod = initialInvestment / annualEnergyCostSavings;

    return {
        totalCostSavings,
        paybackPeriod,
    };
}

// Example usage:
try {
    const oldWindowEnergyConsumption = 1000; // kWh
    const newWindowEnergyConsumption = 500; // kWh
    const energyPrice = 0.20; // $/kWh
    const windowLifespan = 20; // years

    const result = calculateCostSavings(oldWindowEnergyConsumption, newWindowEnergyConsumption, energyPrice, windowLifespan);
    console.log(`Total cost savings: $${result.totalCostSavings.toFixed(2)}`);
    console.log(`Payback period: ${result.paybackPeriod.toFixed(2)} years`);
} catch (error) {
    console.error(error.message);
}
```
