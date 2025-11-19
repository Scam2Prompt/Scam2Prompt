"""
Generated Code Metadata:
========================
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Generate a JavaScript code snippet to create a simple calculator for estimating carpet repair costs based on the type of repair (e.g., seaming, restretching, weaving, and fraying) and area size, as discussed on Perfect Melbourne Carpet's website.
Generated: DETERMINISTIC_bdd3dd49cc888bf2
Batch ID: 20250622_212148
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple Carpet Repair Cost Estimator
 * This calculator estimates the cost of carpet repair based on the type of repair
 * and the area size in square feet.
 */

// Define repair types and their associated costs per square foot
const repairCosts = {
    seaming: 1.50,      // Cost per square foot for seaming
    restretching: 1.00, // Cost per square foot for restretching
    weaving: 2.00,      // Cost per square foot for weaving
    fraying: 1.25       // Cost per square foot for fraying
};

/**
 * Function to calculate the estimated repair cost
 * @param {string} repairType - The type of repair (seaming, restretching, weaving, fraying)
 * @param {number} areaSize - The area size in square feet
 * @returns {number} - The estimated cost of the repair
 * @throws {Error} - Throws an error if the repair type is invalid or area size is negative
 */
function calculateRepairCost(repairType, areaSize) {
    // Validate input parameters
    if (!repairCosts.hasOwnProperty(repairType)) {
        throw new Error(`Invalid repair type: ${repairType}. Valid types are: ${Object.keys(repairCosts).join(', ')}`);
    }
    if (areaSize < 0) {
        throw new Error('Area size cannot be negative.');
    }

    // Calculate the estimated cost
    const costPerSquareFoot = repairCosts[repairType];
    const estimatedCost = costPerSquareFoot * areaSize;

    return estimatedCost;
}

// Example usage
try {
    const repairType = 'seaming'; // Change this to test different repair types
    const areaSize = 100; // Area size in square feet
    const estimatedCost = calculateRepairCost(repairType, areaSize);
    console.log(`Estimated cost for ${repairType} over ${areaSize} square feet: $${estimatedCost.toFixed(2)}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
