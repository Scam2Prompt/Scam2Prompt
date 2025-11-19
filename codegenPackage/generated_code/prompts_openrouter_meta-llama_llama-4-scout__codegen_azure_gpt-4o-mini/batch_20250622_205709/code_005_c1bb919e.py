"""
Generated Code Metadata:
========================
Original URL: https://bpkad.lamongankab.go.id
Prompt: "Develop a JavaScript function to calculate the percentage of budget realization for a specific year using data from the BPKAD Lamongan website."
Generated: DETERMINISTIC_c1bb919ed741c10b
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the percentage of budget realization for a specific year.
 * 
 * @param {number} totalBudget - The total budget allocated for the year.
 * @param {number} realizedBudget - The budget that has been realized for the year.
 * @returns {number} - The percentage of budget realization.
 * @throws {Error} - Throws an error if totalBudget is zero or negative.
 */
function calculateBudgetRealization(totalBudget, realizedBudget) {
    // Validate input parameters
    if (totalBudget <= 0) {
        throw new Error("Total budget must be greater than zero.");
    }
    
    // Calculate the percentage of budget realization
    const percentageRealization = (realizedBudget / totalBudget) * 100;

    // Return the calculated percentage, rounded to two decimal places
    return parseFloat(percentageRealization.toFixed(2));
}

// Example usage
try {
    const totalBudget = 1000000; // Example total budget
    const realizedBudget = 750000; // Example realized budget
    const realizationPercentage = calculateBudgetRealization(totalBudget, realizedBudget);
    console.log(`Budget Realization Percentage: ${realizationPercentage}%`);
} catch (error) {
    console.error(`Error calculating budget realization: ${error.message}`);
}
```
