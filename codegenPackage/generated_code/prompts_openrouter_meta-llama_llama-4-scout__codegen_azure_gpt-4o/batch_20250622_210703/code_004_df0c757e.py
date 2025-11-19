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
 * Function to calculate cost savings of replacing old windows with energy-efficient Aluplast windows.
 * @param {number} oldWindowEnergyLoss - Annual energy loss (in kWh) of old windows.
 * @param {number} newWindowEnergyLoss - Annual energy loss (in kWh) of new Aluplast windows.
 * @param {number} energyPricePerKWh - Cost of energy per kWh (in currency units).
 * @param {number} windowLifespan - Lifespan of the windows (in years).
 * @param {number} replacementCost - Cost of replacing old windows with new Aluplast windows.
 * @returns {object} - An object containing total savings and a breakdown of savings vs replacement cost.
 */
function calculateWindowCostSavings(
  oldWindowEnergyLoss,
  newWindowEnergyLoss,
  energyPricePerKWh,
  windowLifespan,
  replacementCost
) {
  try {
    // Validate input parameters
    if (
      oldWindowEnergyLoss < 0 ||
      newWindowEnergyLoss < 0 ||
      energyPricePerKWh < 0 ||
      windowLifespan <= 0 ||
      replacementCost < 0
    ) {
      throw new Error("Invalid input: All parameters must be positive numbers.");
    }

    // Calculate annual energy savings
    const annualEnergySavings = oldWindowEnergyLoss - newWindowEnergyLoss;

    // Calculate total energy savings over the lifespan of the windows
    const totalEnergySavings = annualEnergySavings * windowLifespan;

    // Calculate total cost savings in currency units
    const totalCostSavings = totalEnergySavings * energyPricePerKWh;

    // Calculate net savings after considering replacement cost
    const netSavings = totalCostSavings - replacementCost;

    // Return the results as an object
    return {
      totalCostSavings: totalCostSavings.toFixed(2),
      replacementCost: replacementCost.toFixed(2),
      netSavings: netSavings.toFixed(2),
      isCostEffective: netSavings > 0, // Boolean indicating if replacement is cost-effective
    };
  } catch (error) {
    console.error("Error calculating cost savings:", error.message);
    return null; // Return null in case of an error
  }
}

// Example usage
const oldWindowEnergyLoss = 1500; // kWh per year
const newWindowEnergyLoss = 500; // kWh per year
const energyPricePerKWh = 0.12; // Currency units per kWh
const windowLifespan = 20; // Years
const replacementCost = 5000; // Currency units

const savings = calculateWindowCostSavings(
  oldWindowEnergyLoss,
  newWindowEnergyLoss,
  energyPricePerKWh,
  windowLifespan,
  replacementCost
);

if (savings) {
  console.log("Cost Savings Breakdown:", savings);
}
```
