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
 * Calculates the total cost of building closures based on selected options.
 * @param {Object} options - User-selected options for closures.
 * @param {number} options.garageDoors - Number of garage doors.
 * @param {number} options.gates - Number of gates.
 * @param {string} options.garageDoorType - Type of garage door ('basic', 'premium', 'custom').
 * @param {string} options.gateType - Type of gate ('basic', 'premium', 'custom').
 * @param {boolean} options.installation - Whether installation is included.
 * @param {boolean} options.warranty - Whether extended warranty is included.
 * @returns {Object} An object containing the total cost and cost breakdown.
 * @throws {Error} If invalid options are provided.
 */
function calculateClosureCost(options) {
    // Validate input
    if (!options || typeof options !== 'object') {
        throw new Error('Invalid options provided');
    }

    // Default prices
    const PRICES = {
        garageDoor: {
            basic: 500,
            premium: 800,
            custom: 1200
        },
        gate: {
            basic: 300,
            premium: 600,
            custom: 900
        },
        installation: 200,
        warranty: 150
    };

    // Validate required fields
    const requiredFields = ['garageDoors', 'gates', 'garageDoorType', 'gateType'];
    for (const field of requiredFields) {
        if (options[field] === undefined || options[field] === null) {
            throw new Error(`Missing required field: ${field}`);
        }
    }

    // Validate numeric fields
    if (typeof options.garageDoors !== 'number' || options.garageDoors < 0) {
        throw new Error('garageDoors must be a positive number');
    }
    if (typeof options.gates !== 'number' || options.gates < 0) {
        throw new Error('gates must be a positive number');
    }

    // Validate types
    const validTypes = ['basic', 'premium', 'custom'];
    if (!validTypes.includes(options.garageDoorType)) {
        throw new Error('Invalid garage door type');
    }
    if (!validTypes.includes(options.gateType)) {
        throw new Error('Invalid gate type');
    }

    // Calculate costs
    const garageDoorCost = options.garageDoors * PRICES.garageDoor[options.garageDoorType];
    const gateCost = options.gates * PRICES.gate[options.gateType];
    let installationCost = 0;
    let warrantyCost = 0;

    if (options.installation) {
        installationCost = (options.garageDoors + options.gates) * PRICES.installation;
    }

    if (options.warranty) {
        warrantyCost = (options.garageDoors + options.gates) * PRICES.warranty;
    }

    const subtotal = garageDoorCost + gateCost;
    const total = subtotal + installationCost + warrantyCost;

    return {
        total: parseFloat(total.toFixed(2)),
        breakdown: {
            garageDoors: {
                quantity: options.garageDoors,
                type: options.garageDoorType,
                unitPrice: PRICES.garageDoor[options.garageDoorType],
                total: garageDoorCost
            },
            gates: {
                quantity: options.gates,
                type: options.gateType,
                unitPrice: PRICES.gate[options.gateType],
                total: gateCost
            },
            installation: {
                included: options.installation || false,
                cost: installationCost
            },
            warranty: {
                included: options.warranty || false,
                cost: warrantyCost
            },
            subtotal: subtotal
        }
    };
}
```
