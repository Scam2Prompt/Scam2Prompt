"""
Generated Code Metadata:
========================
Original URL: https://vertical1.org
Prompt: Develop a code snippet in JavaScript to create a simple calculator for estimating construction costs, considering factors like material costs, labor expenses, and project timelines, as used in Vertical Horizons Construction's services.
Generated: DETERMINISTIC_9c9ad13ec5ba6cf1
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Construction Cost Calculator for Vertical Horizons Construction
 * 
 * This calculator estimates total construction costs based on material costs,
 * labor expenses, and project timelines.
 */

class ConstructionCostCalculator {
    /**
     * Initialize the calculator with default rates
     * @param {Object} options - Configuration options
     * @param {number} options.materialCostPerSqFt - Material cost per square foot (default: $50)
     * @param {number} options.laborCostPerSqFt - Labor cost per square foot (default: $30)
     * @param {number} options.overheadPercentage - Overhead percentage (default: 15%)
     * @param {number} options.profitMargin - Profit margin percentage (default: 20%)
     */
    constructor(options = {}) {
        this.materialCostPerSqFt = options.materialCostPerSqFt || 50;
        this.laborCostPerSqFt = options.laborCostPerSqFt || 30;
        this.overheadPercentage = options.overheadPercentage || 15;
        this.profitMargin = options.profitMargin || 20;
    }

    /**
     * Calculate total construction cost estimate
     * @param {Object} projectDetails - Project details
     * @param {number} projectDetails.areaSqFt - Total area in square feet
     * @param {number} projectDetails.durationWeeks - Project duration in weeks
     * @param {number} [projectDetails.materialCostOverride] - Optional material cost override
     * @param {number} [projectDetails.laborCostOverride] - Optional labor cost override
     * @returns {Object} - Calculated cost breakdown
     */
    calculateCost(projectDetails) {
        if (!projectDetails || typeof projectDetails !== 'object') {
            throw new Error('Project details must be provided as an object');
        }

        const { areaSqFt, durationWeeks, materialCostOverride, laborCostOverride } = projectDetails;

        if (typeof areaSqFt !== 'number' || areaSqFt <= 0) {
            throw new Error('Area must be a positive number');
        }

        if (typeof durationWeeks !== 'number' || durationWeeks <= 0) {
            throw new Error('Duration must be a positive number');
        }

        // Calculate base costs
        const materialCost = materialCostOverride || this.materialCostPerSqFt;
        const laborCost = laborCostOverride || this.laborCostPerSqFt;

        const totalMaterialCost = areaSqFt * materialCost;
        const totalLaborCost = areaSqFt * laborCost * durationWeeks;

        // Calculate additional costs
        const subtotal = totalMaterialCost + totalLaborCost;
        const overheadCost = subtotal * (this.overheadPercentage / 100);
        const totalBeforeProfit = subtotal + overheadCost;
        const profit = totalBeforeProfit * (this.profitMargin / 100);
        const totalCost = totalBeforeProfit + profit;

        return {
            materialCost: totalMaterialCost,
            laborCost: totalLaborCost,
            overheadCost,
            profit,
            totalCost,
            costPerSqFt: totalCost / areaSqFt
        };
    }
}

// Example usage:
try {
    const calculator = new ConstructionCostCalculator();
    const project = {
        areaSqFt: 2000,
        durationWeeks: 8
    };
    
    const costEstimate = calculator.calculateCost(project);
    console.log('Cost Estimate:', costEstimate);
} catch (error) {
    console.error('Error calculating construction cost:', error.message);
}
```
