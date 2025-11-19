"""
Generated Code Metadata:
========================
Original URL: https://www.azrvservices.com
Prompt: Create a JavaScript function that calculates the estimated cost of various RV repair services, including awning repair and electrical repairs, based on user input.
Generated: DETERMINISTIC_be19fff7d4684041
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the estimated cost of RV repair services based on user input.
 * @param {Object} services - An object containing the services required and their details.
 * @param {boolean} [services.awningRepair=false] - Whether awning repair is needed.
 * @param {number} [services.awningSize=0] - Size of the awning in square feet.
 * @param {boolean} [services.electricalRepair=false] - Whether electrical repair is needed.
 * @param {number} [services.electricalHours=0] - Hours of electrical work needed.
 * @param {number} [services.laborRate=75] - Hourly labor rate in dollars.
 * @param {number} [services.materialCost=0] - Cost of materials in dollars.
 * @returns {number} The total estimated cost of the repairs.
 * @throws {Error} If input values are invalid.
 */
function calculateRVCost(services) {
    // Default values
    const {
        awningRepair = false,
        awningSize = 0,
        electricalRepair = false,
        electricalHours = 0,
        laborRate = 75,
        materialCost = 0
    } = services;

    // Validate inputs
    if (awningSize < 0 || electricalHours < 0 || laborRate < 0 || materialCost < 0) {
        throw new Error('Negative values are not allowed for size, hours, labor rate, or material cost.');
    }

    if (typeof awningRepair !== 'boolean' || typeof electricalRepair !== 'boolean') {
        throw new Error('Awning and electrical repair flags must be boolean values.');
    }

    // Calculate costs
    let totalCost = 0;

    // Awning repair cost: $5 per square foot + labor
    if (awningRepair) {
        if (awningSize === 0) {
            throw new Error('Awning size must be specified if awning repair is needed.');
        }
        totalCost += (awningSize * 5) + (2 * laborRate); // 2 hours estimated labor
    }

    // Electrical repair cost: labor hours * rate
    if (electricalRepair) {
        if (electricalHours === 0) {
            throw new Error('Electrical hours must be specified if electrical repair is needed.');
        }
        totalCost += electricalHours * laborRate;
    }

    // Add material cost
    totalCost += materialCost;

    return totalCost;
}

// Example usage:
try {
    const repairEstimate = calculateRVCost({
        awningRepair: true,
        awningSize: 50,
        electricalRepair: true,
        electricalHours: 3,
        materialCost: 200
    });
    console.log(`Total estimated cost: $${repairEstimate}`);
} catch (error) {
    console.error(`Error calculating cost: ${error.message}`);
}
```
