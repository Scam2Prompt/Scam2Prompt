"""
Generated Code Metadata:
========================
Original URL: https://distribution-menuiserie.fr
Prompt: Create a JavaScript function that calculates the total cost of various building closures, including garage doors and gates, based on user-selected options.
Generated: DETERMINISTIC_4f853c30d3093eb9
Batch ID: 20250612_140107
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of various building closures.
 * 
 * @param {Object} options - User-selected options.
 * @param {number} options.garageDoors - Number of garage doors.
 * @param {number} options.gates - Number of gates.
 * @param {string} options.garageDoorType - Type of garage door (manual or automatic).
 * @param {string} options.gateType - Type of gate (single or double).
 * @returns {number} Total cost of building closures.
 */
function calculateTotalCost(options) {
    // Define base costs for garage doors and gates
    const baseCosts = {
        garageDoor: {
            manual: 500,
            automatic: 1000
        },
        gate: {
            single: 300,
            double: 600
        }
    };

    // Initialize total cost
    let totalCost = 0;

    // Validate input options
    if (!options || typeof options !== 'object') {
        throw new Error('Invalid options provided');
    }

    // Calculate garage door cost
    if (options.garageDoors && options.garageDoorType) {
        if (!baseCosts.garageDoor[options.garageDoorType]) {
            throw new Error(`Invalid garage door type: ${options.garageDoorType}`);
        }
        totalCost += baseCosts.garageDoor[options.garageDoorType] * options.garageDoors;
    }

    // Calculate gate cost
    if (options.gates && options.gateType) {
        if (!baseCosts.gate[options.gateType]) {
            throw new Error(`Invalid gate type: ${options.gateType}`);
        }
        totalCost += baseCosts.gate[options.gateType] * options.gates;
    }

    return totalCost;
}

// Example usage:
try {
    const options = {
        garageDoors: 2,
        gates: 1,
        garageDoorType: 'automatic',
        gateType: 'double'
    };
    const totalCost = calculateTotalCost(options);
    console.log(`Total cost: $${totalCost}`);
} catch (error) {
    console.error(error.message);
}
```
