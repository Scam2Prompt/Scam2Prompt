"""
Generated Code Metadata:
========================
Original URL: https://cartoansurperu.com
Prompt: Create a function in JavaScript to calculate the cost savings of using stretch films with high elongation and low density, as detailed in the "Stretch Film 18 pulgadas" product description.
Generated: DETERMINISTIC_166b24586231408a
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the cost savings of using stretch films with high elongation and low density.
 * 
 * @param {number} standardFilmDensity - Density of standard film (g/cm³)
 * @param {number} highElongationFilmDensity - Density of high elongation film (g/cm³)
 * @param {number} standardFilmCost - Cost per unit of standard film (USD)
 * @param {number} highElongationFilmCost - Cost per unit of high elongation film (USD)
 * @param {number} standardFilmUsage - Amount of standard film used per unit (meters)
 * @param {number} highElongationFilmUsage - Amount of high elongation film used per unit (meters)
 * @param {number} annualUsage - Annual film usage (units)
 * @returns {Object} An object containing cost savings details
 * @throws {Error} If any input parameter is invalid
 */
function calculateStretchFilmSavings(
    standardFilmDensity,
    highElongationFilmDensity,
    standardFilmCost,
    highElongationFilmCost,
    standardFilmUsage,
    highElongationFilmUsage,
    annualUsage
) {
    // Validate input parameters
    if (
        typeof standardFilmDensity !== 'number' || standardFilmDensity <= 0 ||
        typeof highElongationFilmDensity !== 'number' || highElongationFilmDensity <= 0 ||
        typeof standardFilmCost !== 'number' || standardFilmCost <= 0 ||
        typeof highElongationFilmCost !== 'number' || highElongationFilmCost <= 0 ||
        typeof standardFilmUsage !== 'number' || standardFilmUsage <= 0 ||
        typeof highElongationFilmUsage !== 'number' || highElongationFilmUsage <= 0 ||
        typeof annualUsage !== 'number' || annualUsage <= 0
    ) {
        throw new Error('All parameters must be positive numbers');
    }

    // Calculate weight per unit for both films
    const standardFilmWeight = standardFilmUsage * standardFilmDensity;
    const highElongationFilmWeight = highElongationFilmUsage * highElongationFilmDensity;

    // Calculate cost per weight unit
    const standardCostPerWeight = standardFilmCost / standardFilmWeight;
    const highElongationCostPerWeight = highElongationFilmCost / highElongationFilmWeight;

    // Calculate annual costs
    const standardAnnualCost = standardFilmCost * annualUsage;
    const highElongationAnnualCost = highElongationFilmCost * annualUsage;

    // Calculate savings
    const costDifference = standardAnnualCost - highElongationAnnualCost;
    const percentageSavings = (costDifference / standardAnnualCost) * 100;
    const weightSavings = (standardFilmWeight - highElongationFilmWeight) * annualUsage;

    return {
        standardAnnualCost: parseFloat(standardAnnualCost.toFixed(2)),
        highElongationAnnualCost: parseFloat(highElongationAnnualCost.toFixed(2)),
        costDifference: parseFloat(costDifference.toFixed(2)),
        percentageSavings: parseFloat(percentageSavings.toFixed(2)),
        weightSavings: parseFloat(weightSavings.toFixed(2)),
        standardCostPerWeight: parseFloat(standardCostPerWeight.toFixed(4)),
        highElongationCostPerWeight: parseFloat(highElongationCostPerWeight.toFixed(4))
    };
}
```
