"""
Generated Code Metadata:
========================
Original URL: https://twmassociates.co.za
Prompt: Create a JavaScript function that calculates the budget for a construction project, considering the unique aspects of project management highlighted by TWM Associates.
Generated: DETERMINISTIC_f04808a04e143861
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
 * Calculates the budget for a construction project based on various cost factors.
 * 
 * @param {Object} projectDetails - An object containing project details.
 * @param {number} projectDetails.totalArea - Total area of the project in square feet.
 * @param {number} projectDetails.costPerSqFt - Cost per square foot.
 * @param {number} projectDetails.laborCost - Total labor cost.
 * @param {number} projectDetails.materialCost - Total material cost.
 * @param {number} projectDetails.permitsAndFees - Cost of permits and fees.
 * @param {number} projectDetails.contingencyPercentage - Contingency percentage (e.g., 10 for 10%).
 * @param {number} projectDetails.profitMarginPercentage - Profit margin percentage (e.g., 15 for 15%).
 * @returns {Object} An object containing the calculated budget breakdown.
 * @throws {Error} If any required parameter is missing or invalid.
 */
function calculateConstructionBudget(projectDetails) {
    // Validate input parameters
    if (!projectDetails || typeof projectDetails !== 'object') {
        throw new Error('Project details must be provided as an object.');
    }

    const requiredFields = [
        'totalArea',
        'costPerSqFt',
        'laborCost',
        'materialCost',
        'permitsAndFees',
        'contingencyPercentage',
        'profitMarginPercentage'
    ];

    for (const field of requiredFields) {
        if (projectDetails[field] === undefined || projectDetails[field] === null) {
            throw new Error(`Missing required field: ${field}`);
        }
        if (typeof projectDetails[field] !== 'number' || projectDetails[field] < 0) {
            throw new Error(`Invalid value for ${field}: must be a positive number`);
        }
    }

    // Calculate base construction cost
    const baseConstructionCost = projectDetails.totalArea * projectDetails.costPerSqFt;

    // Calculate total direct costs
    const totalDirectCosts = baseConstructionCost + projectDetails.laborCost + projectDetails.materialCost + projectDetails.permitsAndFees;

    // Calculate contingency amount
    const contingencyAmount = totalDirectCosts * (projectDetails.contingencyPercentage / 100);

    // Calculate subtotal before profit
    const subtotalBeforeProfit = totalDirectCosts + contingencyAmount;

    // Calculate profit amount
    const profitAmount = subtotalBeforeProfit * (projectDetails.profitMarginPercentage / 100);

    // Calculate total budget
    const totalBudget = subtotalBeforeProfit + profitAmount;

    return {
        baseConstructionCost: parseFloat(baseConstructionCost.toFixed(2)),
        totalDirectCosts: parseFloat(totalDirectCosts.toFixed(2)),
        contingencyAmount: parseFloat(contingencyAmount.toFixed(2)),
        subtotalBeforeProfit: parseFloat(subtotalBeforeProfit.toFixed(2)),
        profitAmount: parseFloat(profitAmount.toFixed(2)),
        totalBudget: parseFloat(totalBudget.toFixed(2))
    };
}

// Example usage:
// const project = {
//     totalArea: 2000,
//     costPerSqFt: 150,
//     laborCost: 50000,
//     materialCost: 100000,
//     permitsAndFees: 15000,
//     contingencyPercentage: 10,
//     profitMarginPercentage: 15
// };
// const budget = calculateConstructionBudget(project);
// console.log(budget);
```
