"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suzuki-capital.com
Prompt: Create a JavaScript function to calculate the estimated cost of repairs based on Suzuki Capital Motors' workshop services, factoring in labor and parts costs.
Generated: DETERMINISTIC_846a9304166bfb08
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the estimated cost of repairs for Suzuki Capital Motors' workshop services.
 * 
 * @param {number} laborHours - The number of hours of labor required for the repair.
 * @param {number} laborRate - The hourly rate for labor.
 * @param {Array<{ partName: string, partCost: number }>} parts - An array of parts needed for the repair, 
 * where each part is an object with a name and cost.
 * @returns {number} - The estimated total cost of repairs.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculateRepairCost(laborHours, laborRate, parts) {
    // Validate inputs
    if (typeof laborHours !== 'number' || laborHours < 0) {
        throw new Error('Invalid labor hours. Must be a non-negative number.');
    }
    if (typeof laborRate !== 'number' || laborRate < 0) {
        throw new Error('Invalid labor rate. Must be a non-negative number.');
    }
    if (!Array.isArray(parts)) {
        throw new Error('Parts must be an array.');
    }
    
    // Calculate labor cost
    const laborCost = laborHours * laborRate;

    // Calculate total parts cost
    let totalPartsCost = 0;
    for (const part of parts) {
        if (typeof part.partCost !== 'number' || part.partCost < 0) {
            throw new Error(`Invalid part cost for ${part.partName}. Must be a non-negative number.`);
        }
        totalPartsCost += part.partCost;
    }

    // Calculate total estimated cost
    const totalCost = laborCost + totalPartsCost;
    
    return totalCost;
}

// Example usage:
// const laborHours = 5;
// const laborRate = 50;
// const parts = [{ partName: 'Brake Pads', partCost: 100 }, { partName: 'Oil Filter', partCost: 30 }];
// const estimatedCost = calculateRepairCost(laborHours, laborRate, parts);
// console.log(`Estimated cost of repairs: $${estimatedCost}`);
```
