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
 * Calculates cost savings from replacing old windows with energy-efficient Aluplast windows.
 * @param {Object} params - Input parameters for the calculation
 * @param {number} params.oldWindowUValue - U-value of old windows (W/m²K)
 * @param {number} params.newWindowUValue - U-value of Aluplast windows (W/m²K)
 * @param {number} params.windowArea - Total window area in square meters
 * @param {number} params.heatingDegreeDays - Annual heating degree days for location
 * @param {number} params.energyPrice - Cost of energy per kWh in local currency
 * @param {number} params.heatingSystemEfficiency - Efficiency of heating system (0-1)
 * @param {number} params.lifespan - Expected lifespan of new windows in years
 * @param {number} params.installationCost - Total cost of window replacement
 * @returns {Object} - Returns an object containing savings details
 */
function calculateWindowSavings(params) {
    // Validate input parameters
    if (!params || typeof params !== 'object') {
        throw new Error('Invalid parameters: must provide an object with required properties');
    }

    const requiredParams = [
        'oldWindowUValue', 'newWindowUValue', 'windowArea', 
        'heatingDegreeDays', 'energyPrice', 'heatingSystemEfficiency',
        'lifespan', 'installationCost'
    ];

    for (const param of requiredParams) {
        if (typeof params[param] !== 'number' || isNaN(params[param])) {
            throw new Error(`Invalid parameter: ${param} must be a valid number`);
        }
    }

    // Constants
    const HOURS_IN_YEAR = 24 * 365;
    const W_TO_KW = 0.001;

    // Calculate annual energy savings
    const uValueDifference = params.oldWindowUValue - params.newWindowUValue;
    const annualEnergySavings = (
        uValueDifference * 
        params.windowArea * 
        params.heatingDegreeDays * 
        HOURS_IN_YEAR * 
        W_TO_KW
    ) / params.heatingSystemEfficiency;

    // Calculate annual cost savings
    const annualCostSavings = annualEnergySavings * params.energyPrice;

    // Calculate total savings over lifespan
    const totalSavings = annualCostSavings * params.lifespan;

    // Calculate net savings after installation cost
    const netSavings = totalSavings - params.installationCost;

    // Calculate payback period
    const paybackPeriod = params.installationCost / annualCostSavings;

    return {
        annualEnergySavings: parseFloat(annualEnergySavings.toFixed(2)),
        annualCostSavings: parseFloat(annualCostSavings.toFixed(2)),
        totalSavings: parseFloat(totalSavings.toFixed(2)),
        netSavings: parseFloat(netSavings.toFixed(2)),
        paybackPeriod: parseFloat(paybackPeriod.toFixed(1)),
        savingsPerYear: parseFloat((annualCostSavings / params.lifespan).toFixed(2))
    };
}

// Example usage:
/*
const savings = calculateWindowSavings({
    oldWindowUValue: 2.8,
    newWindowUValue: 1.4,
    windowArea: 15,
    heatingDegreeDays: 2500,
    energyPrice: 0.15,
    heatingSystemEfficiency: 0.85,
    lifespan: 20,
    installationCost: 5000
});

console.log(savings);
*/
```
