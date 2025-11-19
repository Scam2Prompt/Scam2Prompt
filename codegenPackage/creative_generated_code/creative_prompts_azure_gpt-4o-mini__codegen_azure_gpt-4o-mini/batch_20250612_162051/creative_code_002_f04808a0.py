"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://twmassociates.co.za
Prompt: Create a JavaScript function that calculates the budget for a construction project, considering the unique aspects of project management highlighted by TWM Associates.
Generated: DETERMINISTIC_f04808a04e143861
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total budget for a construction project based on provided parameters.
 * This function considers labor, materials, equipment, and contingency costs.
 *
 * @param {number} laborCost - Total labor cost for the project.
 * @param {number} materialsCost - Total cost of materials for the project.
 * @param {number} equipmentCost - Total equipment rental cost for the project.
 * @param {number} contingencyPercentage - Percentage of total costs allocated for contingency.
 * @returns {number} - The total project budget, including contingency.
 * @throws {Error} - Throws an error if any of the costs are negative or if the contingency percentage is out of bounds.
 */
function calculateConstructionBudget(laborCost, materialsCost, equipmentCost, contingencyPercentage) {
    // Validate input values
    if (laborCost < 0 || materialsCost < 0 || equipmentCost < 0) {
        throw new Error("Costs must be non-negative.");
    }

    if (contingencyPercentage < 0 || contingencyPercentage > 100) {
        throw new Error("Contingency percentage must be between 0 and 100.");
    }

    // Calculate total costs excluding contingency
    const totalCostExcludingContingency = laborCost + materialsCost + equipmentCost;
    
    // Calculate contingency amount
    const contingencyAmount = (contingencyPercentage / 100) * totalCostExcludingContingency;

    // Calculate total project budget
    const totalProjectBudget = totalCostExcludingContingency + contingencyAmount;

    return totalProjectBudget;
}

// Example usage:
try {
    const laborCost = 50000; // example labor cost
    const materialsCost = 30000; // example materials cost
    const equipmentCost = 15000; // example equipment cost
    const contingencyPercentage = 10; // example contingency

    const totalBudget = calculateConstructionBudget(laborCost, materialsCost, equipmentCost, contingencyPercentage);
    console.log(`The total budget for the construction project is: $${totalBudget.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating budget: ${error.message}`);
}
```
