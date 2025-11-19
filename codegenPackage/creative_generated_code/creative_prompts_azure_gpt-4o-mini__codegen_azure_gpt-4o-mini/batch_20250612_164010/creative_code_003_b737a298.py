"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somcivil.com
Prompt: Develop a JavaScript function that calculates the estimated cost for structural repairs and restoration projects, similar to the estimation services provided by SOM Civil.
Generated: DETERMINISTIC_b737a2982e642169
Batch ID: 20250612_164010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the estimated cost for structural repairs and restoration projects.
 * 
 * @param {number} laborCostPerHour - The cost of labor per hour.
 * @param {number} materialCost - The total cost of materials required.
 * @param {number} hoursRequired - The estimated number of hours required for labor.
 * @param {number} overheadPercentage - The overhead percentage applied to the total cost.
 * @returns {number} - The total estimated cost including labor, materials, and overhead.
 * @throws {Error} - Throws an error if any of the input parameters are negative.
 */
function calculateRepairCost(laborCostPerHour, materialCost, hoursRequired, overheadPercentage) {
    // Validate input parameters
    if (laborCostPerHour < 0 || materialCost < 0 || hoursRequired < 0 || overheadPercentage < 0) {
        throw new Error("All input parameters must be non-negative.");
    }

    // Calculate labor cost
    const laborCost = laborCostPerHour * hoursRequired;

    // Calculate total cost
    const totalCost = laborCost + materialCost;

    // Calculate overhead cost based on the total cost
    const overheadCost = (overheadPercentage / 100) * totalCost;

    // Calculate final estimated cost
    const estimatedCost = totalCost + overheadCost;

    return estimatedCost;
}

// Example usage
try {
    const laborCostPerHour = 50; // Example labor cost in dollars
    const materialCost = 1000;    // Example material cost in dollars
    const hoursRequired = 20;      // Estimated labor hours
    const overheadPercentage = 15;  // Overhead percentage

    const estimatedCost = calculateRepairCost(laborCostPerHour, materialCost, hoursRequired, overheadPercentage);
    console.log(`The estimated cost for the project is: $${estimatedCost.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating estimated cost: ${error.message}`);
}
```
