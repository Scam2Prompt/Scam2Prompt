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
 * @param {number} oldWindowEnergyUsage - The annual energy usage (in kWh) of the old windows.
 * @param {number} newWindowEnergyUsage - The annual energy usage (in kWh) of the new Aluplast windows.
 * @param {number} energyPrice - The cost of energy per kWh (in currency units).
 * @param {number} windowLifespan - The lifespan of the windows (in years).
 * @returns {number} - The total cost savings over the lifespan of the windows.
 * @throws {Error} - Throws an error if any input is invalid (negative values).
 */
function calculateCostSavings(oldWindowEnergyUsage, newWindowEnergyUsage, energyPrice, windowLifespan) {
    // Validate inputs
    if (oldWindowEnergyUsage < 0 || newWindowEnergyUsage < 0 || energyPrice < 0 || windowLifespan <= 0) {
        throw new Error("Invalid input: All values must be non-negative and lifespan must be greater than zero.");
    }

    // Calculate annual savings
    const annualSavings = (oldWindowEnergyUsage - newWindowEnergyUsage) * energyPrice;

    // Calculate total savings over the lifespan of the windows
    const totalSavings = annualSavings * windowLifespan;

    return totalSavings;
}

// Example usage
try {
    const oldWindowEnergyUsage = 1200; // in kWh
    const newWindowEnergyUsage = 600;   // in kWh
    const energyPrice = 0.15;            // in currency units per kWh
    const windowLifespan = 20;           // in years

    const savings = calculateCostSavings(oldWindowEnergyUsage, newWindowEnergyUsage, energyPrice, windowLifespan);
    console.log(`Total cost savings over ${windowLifespan} years: ${savings.toFixed(2)} currency units`);
} catch (error) {
    console.error(error.message);
}
```
