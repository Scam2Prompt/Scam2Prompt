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
 * Calculates the total cost of building closures based on user-selected options.
 * 
 * @param {Object} options - An object containing the selected options for closures.
 * @param {number} options.garageDoors - The number of garage doors selected.
 * @param {number} options.gate - The number of gates selected.
 * @param {number} options.garageDoorCost - The cost per garage door.
 * @param {number} options.gateCost - The cost per gate.
 * @returns {number} - The total cost of the selected closures.
 * @throws {Error} - Throws an error if any input is invalid.
 */
function calculateTotalCost(options) {
    // Validate input
    if (typeof options !== 'object' || options === null) {
        throw new Error('Invalid input: options must be a non-null object.');
    }

    const { garageDoors, gate, garageDoorCost, gateCost } = options;

    // Validate individual properties
    if (typeof garageDoors !== 'number' || garageDoors < 0) {
        throw new Error('Invalid input: garageDoors must be a non-negative number.');
    }
    if (typeof gate !== 'number' || gate < 0) {
        throw new Error('Invalid input: gate must be a non-negative number.');
    }
    if (typeof garageDoorCost !== 'number' || garageDoorCost < 0) {
        throw new Error('Invalid input: garageDoorCost must be a non-negative number.');
    }
    if (typeof gateCost !== 'number' || gateCost < 0) {
        throw new Error('Invalid input: gateCost must be a non-negative number.');
    }

    // Calculate total cost
    const totalCost = (garageDoors * garageDoorCost) + (gate * gateCost);

    return totalCost;
}

// Example usage
try {
    const options = {
        garageDoors: 3,
        gate: 2,
        garageDoorCost: 500,
        gateCost: 300
    };
    
    const total = calculateTotalCost(options);
    console.log(`Total cost of building closures: $${total}`);
} catch (error) {
    console.error(error.message);
}
```
