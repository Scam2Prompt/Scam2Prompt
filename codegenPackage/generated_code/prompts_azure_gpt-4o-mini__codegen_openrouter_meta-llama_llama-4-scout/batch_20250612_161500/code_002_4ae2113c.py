"""
Generated Code Metadata:
========================
Original URL: https://plm.cr
Prompt: Write a JavaScript function that calculates the cost savings of using PLM's strategic location for mass distribution compared to traditional logistics methods.
Generated: DETERMINISTIC_4ae2113cf6145bea
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the cost savings of using PLM's strategic location for mass distribution
 * compared to traditional logistics methods.
 *
 * @param {Object} traditionalLogisticsCosts - Traditional logistics costs
 * @param {number} traditionalLogisticsCosts.transportation - Transportation cost
 * @param {number} traditionalLogisticsCosts.warehouseRent - Warehouse rent cost
 * @param {number} traditionalLogisticsCosts.inventoryManagement - Inventory management cost
 * @param {number} traditionalLogisticsCosts.other - Other costs
 * @param {Object} plmLogisticsCosts - PLM logistics costs
 * @param {number} plmLogisticsCosts.transportation - Transportation cost
 * @param {number} plmLogisticsCosts.warehouseRent - Warehouse rent cost
 * @param {number} plmLogisticsCosts.inventoryManagement - Inventory management cost
 * @param {number} plmLogisticsCosts.other - Other costs
 * @returns {Object} Cost savings
 */

function calculateCostSavings(traditionalLogisticsCosts, plmLogisticsCosts) {
    try {
        // Validate input parameters
        if (!traditionalLogisticsCosts || !plmLogisticsCosts) {
            throw new Error('Both traditionalLogisticsCosts and plmLogisticsCosts are required');
        }

        // Calculate traditional logistics total cost
        const traditionalTotalCost = Object.values(traditionalLogisticsCosts).reduce((a, b) => a + b, 0);

        // Calculate PLM logistics total cost
        const plmTotalCost = Object.values(plmLogisticsCosts).reduce((a, b) => a + b, 0);

        // Calculate cost savings
        const costSavings = traditionalTotalCost - plmTotalCost;

        // Calculate cost savings percentage
        const costSavingsPercentage = traditionalTotalCost === 0 ? 0 : (costSavings / traditionalTotalCost) * 100;

        return {
            costSavings,
            costSavingsPercentage: costSavingsPercentage.toFixed(2)
        };
    } catch (error) {
        console.error('Error calculating cost savings:', error.message);
        return null;
    }
}

// Example usage:
const traditionalLogisticsCosts = {
    transportation: 10000,
    warehouseRent: 5000,
    inventoryManagement: 2000,
    other: 1000
};

const plmLogisticsCosts = {
    transportation: 8000,
    warehouseRent: 3000,
    inventoryManagement: 1500,
    other: 500
};

const result = calculateCostSavings(traditionalLogisticsCosts, plmLogisticsCosts);
console.log(result);
```
