"""
Generated Code Metadata:
========================
Original URL: https://realorigin.org
Prompt: Develop a JavaScript function that calculates the cost-effectiveness of solar panel installations, inspired by the discussion in "Why are solar panels becoming so Much more Popular over the Past Decade?"
Generated: DETERMINISTIC_2647065301f2c80c
Batch ID: 20250612_160657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the cost-effectiveness of solar panel installations.
 * 
 * @param {number} installationCost - The total cost of the solar panel installation.
 * @param {number} annualSavings - The annual savings on electricity bills due to solar energy.
 * @param {number} lifespan - The expected lifespan of the solar panels in years.
 * @returns {object} An object containing the payback period and the cost-effectiveness ratio.
 * @throws {Error} Throws an error if any input is negative or if installationCost is zero.
 */
function calculateSolarCostEffectiveness(installationCost, annualSavings, lifespan) {
    // Validate inputs
    if (installationCost < 0 || annualSavings < 0 || lifespan <= 0) {
        throw new Error("Installation cost, annual savings, and lifespan must be non-negative and lifespan must be greater than zero.");
    }

    // Calculate payback period in years
    const paybackPeriod = installationCost / annualSavings;

    // Calculate total savings over the lifespan of the solar panels
    const totalSavings = annualSavings * lifespan;

    // Calculate cost-effectiveness ratio
    const costEffectivenessRatio = totalSavings / installationCost;

    // Return results as an object
    return {
        paybackPeriod: paybackPeriod,
        costEffectivenessRatio: costEffectivenessRatio
    };
}

// Example usage
try {
    const result = calculateSolarCostEffectiveness(15000, 1200, 25);
    console.log(`Payback Period: ${result.paybackPeriod.toFixed(2)} years`);
    console.log(`Cost-Effectiveness Ratio: ${result.costEffectivenessRatio.toFixed(2)}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
