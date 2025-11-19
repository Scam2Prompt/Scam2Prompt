"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://distribution-menuiserie.fr
Prompt: Create a JavaScript function that calculates the total cost of various building closures, including garage doors and gates, based on user-selected options.
Generated: DETERMINISTIC_4f853c30d3093eb9
Batch ID: 20250612_140107
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total cost of building closures based on user-selected options.
 * 
 * @param {Object} options - The selected options for building closures.
 * @param {number} options.garageDoorCount - The number of garage doors.
 * @param {number} options.gateCount - The number of gates.
 * @param {number} options.garageDoorPrice - The price per garage door.
 * @param {number} options.gatePrice - The price per gate.
 * @returns {number} The total calculated cost.
 * @throws {Error} Throws an error if any of the prices or counts are negative.
 */
function calculateTotalCost(options) {
    // Destructure the options object for easier access
    const { garageDoorCount, gateCount, garageDoorPrice, gatePrice } = options;

    // Validate input parameters to ensure they are non-negative numbers
    if (typeof garageDoorCount !== 'number' || garageDoorCount < 0) {
        throw new Error('Invalid garage door count. It must be a non-negative number.');
    }
    if (typeof gateCount !== 'number' || gateCount < 0) {
        throw new Error('Invalid gate count. It must be a non-negative number.');
    }
    if (typeof garageDoorPrice !== 'number' || garageDoorPrice < 0) {
        throw new Error('Invalid garage door price. It must be a non-negative number.');
    }
    if (typeof gatePrice !== 'number' || gatePrice < 0) {
        throw new Error('Invalid gate price. It must be a non-negative number.');
    }

    // Calculate total cost
    const totalGarageDoorCost = garageDoorCount * garageDoorPrice;
    const totalGateCost = gateCount * gatePrice;
    
    // Return the total cost
    return totalGarageDoorCost + totalGateCost;
}

// Example usage
try {
    const options = {
        garageDoorCount: 3,
        gateCount: 2,
        garageDoorPrice: 500,
        gatePrice: 300,
    };
    
    const totalCost = calculateTotalCost(options);
    console.log(`Total cost of building closures: $${totalCost}`);
} catch (error) {
    console.error(error.message);
}
```
