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
 * Calculates the budget for a construction project based on provided inputs.
 * 
 * @param {Object} projectDetails - An object containing details for the construction project.
 * @param {number} projectDetails.materialCost - Total cost of materials required for the project.
 * @param {number} projectDetails.laborCost - Total cost of labor for the project.
 * @param {number} projectDetails.permitFees - Fees for permits associated with the project.
 * @param {number} projectDetails.contingencyPercentage - Percentage of the total costs reserved for contingencies (e.g., unexpected expenses).
 * @param {number} projectDetails.managementFeePercentage - Project management fee percentage charged by TWM Associates.
 * @returns {number} - The total estimated budget for the construction project.
 * @throws {Error} - Throws an error if any of the inputs are invalid or missing.
 */
function calculateConstructionBudget(projectDetails) {
    try {
        // Validate input object and properties
        if (
            !projectDetails ||
            typeof projectDetails.materialCost !== 'number' ||
            typeof projectDetails.laborCost !== 'number' ||
            typeof projectDetails.permitFees !== 'number' ||
            typeof projectDetails.contingencyPercentage !== 'number' ||
            typeof projectDetails.managementFeePercentage !== 'number'
        ) {
            throw new Error('Invalid or missing project details. Please provide valid numeric values for all required fields.');
        }

        // Ensure all numeric values are non-negative
        if (
            projectDetails.materialCost < 0 ||
            projectDetails.laborCost < 0 ||
            projectDetails.permitFees < 0 ||
            projectDetails.contingencyPercentage < 0 ||
            projectDetails.managementFeePercentage < 0
        ) {
            throw new Error('All cost values and percentages must be non-negative.');
        }

        // Calculate the base cost (materials + labor + permits)
        const baseCost = projectDetails.materialCost + projectDetails.laborCost + projectDetails.permitFees;

        // Calculate contingency cost
        const contingencyCost = (projectDetails.contingencyPercentage / 100) * baseCost;

        // Calculate management fee
        const managementFee = (projectDetails.managementFeePercentage / 100) * baseCost;

        // Calculate total budget
        const totalBudget = baseCost + contingencyCost + managementFee;

        // Return the total budget rounded to two decimal places
        return parseFloat(totalBudget.toFixed(2));
    } catch (error) {
        console.error(`[Error]: ${error.message}`);
        throw error; // Re-throw error for further handling by the caller
    }
}

// Example usage:
try {
    const projectDetails = {
        materialCost: 50000,           // Cost of materials ($)
        laborCost: 30000,              // Cost of labor ($)
        permitFees: 2000,              // Permit fees ($)
        contingencyPercentage: 10,    // Contingency percentage (%)
        managementFeePercentage: 5    // Management fee percentage (%)
    };

    const totalBudget = calculateConstructionBudget(projectDetails);
    console.log(`Total Construction Budget: $${totalBudget}`);
} catch (error) {
    console.error('Failed to calculate construction budget:', error.message);
}
```
