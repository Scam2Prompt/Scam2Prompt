"""
Generated Code Metadata:
========================
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Write a JavaScript function to calculate the cost of plumbing services based on factors like urgency, service type (e.g., leak detection, industrial cleaning), and location, as described by Limpieza de Tubos Costablanca.
Generated: DETERMINISTIC_7ae31f85c4decccd
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the cost of plumbing services based on urgency, service type, and location.
 * 
 * @param {string} serviceType - The type of plumbing service (e.g., 'leak detection', 'industrial cleaning').
 * @param {string} urgency - The urgency of the service (e.g., 'standard', 'urgent').
 * @param {string} location - The location where the service is required (e.g., 'urban', 'rural').
 * @returns {number} - The calculated cost of the plumbing service.
 * @throws {Error} - Throws an error if invalid parameters are provided.
 */
function calculatePlumbingCost(serviceType, urgency, location) {
    // Base rates for different service types
    const baseRates = {
        'leak detection': 100,
        'industrial cleaning': 200,
        'pipe installation': 300
    };

    // Urgency multipliers
    const urgencyMultipliers = {
        'standard': 1,
        'urgent': 1.5
    };

    // Location adjustments
    const locationAdjustments = {
        'urban': 0,
        'rural': 50
    };

    // Validate input parameters
    if (!baseRates[serviceType]) {
        throw new Error(`Invalid service type: ${serviceType}. Valid options are: ${Object.keys(baseRates).join(', ')}`);
    }
    if (!urgencyMultipliers[urgency]) {
        throw new Error(`Invalid urgency level: ${urgency}. Valid options are: ${Object.keys(urgencyMultipliers).join(', ')}`);
    }
    if (!locationAdjustments[location]) {
        throw new Error(`Invalid location: ${location}. Valid options are: ${Object.keys(locationAdjustments).join(', ')}`);
    }

    // Calculate the base cost
    const baseCost = baseRates[serviceType];

    // Apply urgency multiplier
    const urgencyCost = baseCost * urgencyMultipliers[urgency];

    // Apply location adjustment
    const totalCost = urgencyCost + locationAdjustments[location];

    return totalCost;
}

// Example usage
try {
    const cost = calculatePlumbingCost('leak detection', 'urgent', 'urban');
    console.log(`The total cost of plumbing service is: $${cost}`);
} catch (error) {
    console.error(error.message);
}
```
