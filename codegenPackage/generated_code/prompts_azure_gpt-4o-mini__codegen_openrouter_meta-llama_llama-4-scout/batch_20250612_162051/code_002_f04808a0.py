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
 * Calculates the budget for a construction project.
 * 
 * @param {Object} projectDetails - Project details object.
 * @param {number} projectDetails.directCosts - Direct costs of the project.
 * @param {number} projectDetails.indirectCosts - Indirect costs of the project.
 * @param {number} projectDetails.contingencyFundPercentage - Contingency fund percentage.
 * @param {number} projectDetails.overheadPercentage - Overhead percentage.
 * @param {number} projectDetails.profitPercentage - Profit percentage.
 * 
 * @returns {Object} Project budget object.
 */
function calculateConstructionProjectBudget(projectDetails) {
    try {
        // Validate input parameters
        if (typeof projectDetails !== 'object' ||
            typeof projectDetails.directCosts !== 'number' ||
            typeof projectDetails.indirectCosts !== 'number' ||
            typeof projectDetails.contingencyFundPercentage !== 'number' ||
            typeof projectDetails.overheadPercentage !== 'number' ||
            typeof projectDetails.profitPercentage !== 'number') {
            throw new Error('Invalid input parameters');
        }

        // Calculate total costs
        const totalCosts = projectDetails.directCosts + projectDetails.indirectCosts;

        // Calculate contingency fund
        const contingencyFund = totalCosts * (projectDetails.contingencyFundPercentage / 100);

        // Calculate overhead
        const overhead = totalCosts * (projectDetails.overheadPercentage / 100);

        // Calculate profit
        const profit = totalCosts * (projectDetails.profitPercentage / 100);

        // Calculate total budget
        const totalBudget = totalCosts + contingencyFund + overhead + profit;

        // Return project budget object
        return {
            totalCosts,
            contingencyFund,
            overhead,
            profit,
            totalBudget
        };
    } catch (error) {
        // Log and rethrow error
        console.error('Error calculating project budget:', error.message);
        throw error;
    }
}

// Example usage:
const projectDetails = {
    directCosts: 100000,
    indirectCosts: 20000,
    contingencyFundPercentage: 10,
    overheadPercentage: 5,
    profitPercentage: 15
};

const projectBudget = calculateConstructionProjectBudget(projectDetails);
console.log('Project Budget:');
console.log(`Total Costs: $${projectBudget.totalCosts.toLocaleString()}`);
console.log(`Contingency Fund: $${projectBudget.contingencyFund.toLocaleString()}`);
console.log(`Overhead: $${projectBudget.overhead.toLocaleString()}`);
console.log(`Profit: $${projectBudget.profit.toLocaleString()}`);
console.log(`Total Budget: $${projectBudget.totalBudget.toLocaleString()}`);
```
