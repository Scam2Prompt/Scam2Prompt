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
 * @param {Object} params - Input parameters.
 * @param {number} params.standardFilmCost - The cost of the standard film per unit.
 * @param {number} params.standardFilmWeight - The weight of the standard film per unit (in grams).
 * @param {number} params.highElongationFilmCost - The cost of the high elongation film per unit.
 * @param {number} params.highElongationFilmWeight - The weight of the high elongation film per unit (in grams).
 * @param {number} params.usageRate - The usage rate of the film per unit (in grams).
 * @returns {Object} An object containing the cost savings and the percentage reduction.
 */
function calculateCostSavings(params) {
    try {
        // Validate input parameters
        if (typeof params !== 'object' ||
            typeof params.standardFilmCost !== 'number' ||
            typeof params.standardFilmWeight !== 'number' ||
            typeof params.highElongationFilmCost !== 'number' ||
            typeof params.highElongationFilmWeight !== 'number' ||
            typeof params.usageRate !== 'number') {
            throw new Error('Invalid input parameters');
        }

        // Calculate the cost per gram for each film type
        const standardFilmCostPerGram = params.standardFilmCost / params.standardFilmWeight;
        const highElongationFilmCostPerGram = params.highElongationFilmCost / params.highElongationFilmWeight;

        // Calculate the cost of using each film type for the given usage rate
        const standardFilmUsageCost = standardFilmCostPerGram * params.usageRate;
        const highElongationFilmUsageCost = highElongationFilmCostPerGram * params.usageRate;

        // Calculate the cost savings
        const costSavings = standardFilmUsageCost - highElongationFilmUsageCost;

        // Calculate the percentage reduction
        const percentageReduction = (costSavings / standardFilmUsageCost) * 100;

        // Return the cost savings and percentage reduction
        return {
            costSavings: costSavings.toFixed(2),
            percentageReduction: percentageReduction.toFixed(2)
        };
    } catch (error) {
        // Log and rethrow the error
        console.error('Error calculating cost savings:', error);
        throw error;
    }
}

// Example usage:
const params = {
    standardFilmCost: 100,
    standardFilmWeight: 500,
    highElongationFilmCost: 120,
    highElongationFilmWeight: 400,
    usageRate: 200
};

const result = calculateCostSavings(params);
console.log(`Cost savings: $${result.costSavings}`);
console.log(`Percentage reduction: ${result.percentageReduction}%`);
```
