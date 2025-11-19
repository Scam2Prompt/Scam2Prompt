"""
Generated Code Metadata:
========================
Original URL: https://maximuslimited.com
Prompt: "Create a JavaScript function to calculate the financial impact of business transformation on a company's operations and organization."
Generated: DETERMINISTIC_6dd712b6179495a0
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the financial impact of business transformation on a company.
 * @param {Object} params - Input parameters for the calculation
 * @param {number} params.currentRevenue - Current annual revenue in USD
 * @param {number} params.currentCosts - Current annual operational costs in USD
 * @param {number} params.transformationCost - One-time transformation cost in USD
 * @param {number} params.revenueGrowthRate - Expected annual revenue growth rate (decimal)
 * @param {number} params.costReductionRate - Expected annual cost reduction rate (decimal)
 * @param {number} params.years - Number of years to project
 * @returns {Object} Financial impact analysis with yearly projections and summary
 */
function calculateTransformationImpact(params) {
    // Validate input parameters
    if (!params || typeof params !== 'object') {
        throw new Error('Invalid input: params must be an object');
    }

    const requiredParams = [
        'currentRevenue',
        'currentCosts',
        'transformationCost',
        'revenueGrowthRate',
        'costReductionRate',
        'years'
    ];

    for (const param of requiredParams) {
        if (typeof params[param] !== 'number' || isNaN(params[param])) {
            throw new Error(`Invalid input: ${param} must be a valid number`);
        }
    }

    if (params.years <= 0) {
        throw new Error('Invalid input: years must be greater than 0');
    }

    // Initialize variables
    const results = {
        yearlyProjections: [],
        summary: {
            totalRevenue: 0,
            totalCosts: 0,
            totalSavings: 0,
            netImpact: 0,
            roi: 0
        }
    };

    let currentRevenue = params.currentRevenue;
    let currentCosts = params.currentCosts;
    let cumulativeSavings = 0;

    // Calculate yearly projections
    for (let year = 1; year <= params.years; year++) {
        const yearlyProjection = {
            year,
            revenue: currentRevenue,
            costs: currentCosts,
            profit: currentRevenue - currentCosts,
            savings: year === 1 ? 0 : (params.currentCosts - currentCosts),
            cumulativeSavings: year === 1 ? 0 : cumulativeSavings
        };

        if (year === 1) {
            yearlyProjection.transformationCost = params.transformationCost;
            yearlyProjection.netImpact = yearlyProjection.profit - params.transformationCost;
        } else {
            yearlyProjection.netImpact = yearlyProjection.profit + yearlyProjection.savings;
        }

        results.yearlyProjections.push(yearlyProjection);
        results.summary.totalRevenue += currentRevenue;
        results.summary.totalCosts += currentCosts;

        if (year > 1) {
            cumulativeSavings += yearlyProjection.savings;
            results.summary.totalSavings += yearlyProjection.savings;
        }

        // Update for next year
        currentRevenue *= (1 + params.revenueGrowthRate);
        currentCosts *= (1 - params.costReductionRate);
    }

    // Calculate summary metrics
    results.summary.netImpact = results.summary.totalRevenue - 
                               results.summary.totalCosts - 
                               params.transformationCost + 
                               results.summary.totalSavings;

    results.summary.roi = ((results.summary.netImpact - (-params.transformationCost)) / 
                          params.transformationCost) * 100;

    return results;
}
```
