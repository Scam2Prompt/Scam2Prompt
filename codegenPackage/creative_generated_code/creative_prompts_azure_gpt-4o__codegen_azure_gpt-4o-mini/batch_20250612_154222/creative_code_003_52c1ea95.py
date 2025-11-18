"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supportfix.online
Prompt: Write a function in JavaScript to calculate the estimated repair cost for household appliances based on appliance type, brand, and reported issue severity.
Generated: DETERMINISTIC_52c1ea9575f1651c
Batch ID: 20250612_154222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the estimated repair cost for household appliances.
 * 
 * @param {string} applianceType - Type of the appliance (e.g., 'washing machine', 'refrigerator').
 * @param {string} brand - Brand of the appliance (e.g., 'Whirlpool', 'LG').
 * @param {number} issueSeverity - Severity of the reported issue on a scale from 1 to 10.
 * @returns {number} Estimated repair cost in dollars.
 * @throws {Error} Throws an error if inputs are invalid.
 */
function calculateRepairCost(applianceType, brand, issueSeverity) {
    // Validate inputs
    if (typeof applianceType !== 'string' || applianceType.trim() === '') {
        throw new Error('Invalid appliance type. It must be a non-empty string.');
    }

    if (typeof brand !== 'string' || brand.trim() === '') {
        throw new Error('Invalid brand. It must be a non-empty string.');
    }

    if (typeof issueSeverity !== 'number' || issueSeverity < 1 || issueSeverity > 10) {
        throw new Error('Invalid issue severity. It must be a number between 1 and 10.');
    }

    // Base cost mapping for different appliance types
    const baseCosts = {
        'washing machine': 100,
        'refrigerator': 150,
        'dishwasher': 120,
        'oven': 130,
        'microwave': 80
    };

    // Get the base cost for the given appliance type
    const baseCost = baseCosts[applianceType.toLowerCase()];
    if (baseCost === undefined) {
        throw new Error('Appliance type not recognized. Valid types are: ' + Object.keys(baseCosts).join(', '));
    }

    // Calculate estimated cost based on issue severity
    const estimatedCost = baseCost + (issueSeverity * 20);

    return estimatedCost;
}

// Example usage
try {
    const cost = calculateRepairCost('Washing Machine', 'Whirlpool', 5);
    console.log(`The estimated repair cost is: $${cost}`);
} catch (error) {
    console.error(`Error calculating repair cost: ${error.message}`);
}
```
