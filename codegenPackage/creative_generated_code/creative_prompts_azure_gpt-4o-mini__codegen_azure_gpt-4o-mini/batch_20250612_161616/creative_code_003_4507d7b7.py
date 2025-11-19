"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ntalo.co.za
Prompt: Develop a JavaScript function that calculates project costs based on equipment hire and safety compliance, reflecting the pricing model used by Ntalo Investments.
Generated: DETERMINISTIC_4507d7b7ac0c8ab3
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total project cost based on equipment hire and safety compliance.
 * 
 * @param {Object} options - The options for calculating the project cost.
 * @param {number} options.equipmentCost - The total cost of equipment hire.
 * @param {number} options.safetyComplianceCost - The cost associated with safety compliance.
 * @param {number} [options.additionalFees=0] - Any additional fees (optional).
 * @returns {number} The total project cost.
 * @throws {Error} Throws an error if any of the monetary values are negative or not numbers.
 */
function calculateProjectCost({ equipmentCost, safetyComplianceCost, additionalFees = 0 }) {
    // Validate input parameters
    if (typeof equipmentCost !== 'number' || equipmentCost < 0) {
        throw new Error('Invalid equipment cost: Must be a non-negative number.');
    }
    if (typeof safetyComplianceCost !== 'number' || safetyComplianceCost < 0) {
        throw new Error('Invalid safety compliance cost: Must be a non-negative number.');
    }
    if (typeof additionalFees !== 'number' || additionalFees < 0) {
        throw new Error('Invalid additional fees: Must be a non-negative number.');
    }

    // Calculate the total project cost
    const totalCost = equipmentCost + safetyComplianceCost + additionalFees;

    return totalCost;
}

// Example Usage
try {
    const projectCost = calculateProjectCost({
        equipmentCost: 5000,
        safetyComplianceCost: 1200,
        additionalFees: 300
    });
    console.log(`Total Project Cost: $${projectCost.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating project cost: ${error.message}`);
}
```
