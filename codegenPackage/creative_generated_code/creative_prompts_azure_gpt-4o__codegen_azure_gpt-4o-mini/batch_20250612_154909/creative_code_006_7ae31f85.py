"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Write a JavaScript function to calculate the cost of plumbing services based on factors like urgency, service type (e.g., leak detection, industrial cleaning), and location, as described by Limpieza de Tubos Costablanca.
Generated: DETERMINISTIC_7ae31f85c4decccd
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the cost of plumbing services based on urgency, service type, and location.
 * 
 * @param {string} serviceType - The type of plumbing service (e.g., 'leak detection', 'industrial cleaning').
 * @param {string} urgency - The urgency of the service ('standard', 'urgent', 'emergency').
 * @param {string} location - The location where the service is required (e.g., 'urban', 'suburban', 'rural').
 * @returns {number} - The calculated cost of the service.
 * @throws {Error} - Throws an error if the input parameters are invalid.
 */
function calculatePlumbingCost(serviceType, urgency, location) {
    // Base costs for different service types
    const baseCosts = {
        'leak detection': 100,
        'industrial cleaning': 250,
        'drain cleaning': 150
    };

    // Urgency modifiers
    const urgencyModifiers = {
        'standard': 1.0,
        'urgent': 1.5,
        'emergency': 2.0
    };

    // Location modifiers
    const locationModifiers = {
        'urban': 1.0,
        'suburban': 1.2,
        'rural': 1.5
    };

    // Validate input parameters
    if (!baseCosts[serviceType]) {
        throw new Error(`Invalid service type: ${serviceType}. Valid options are: ${Object.keys(baseCosts).join(', ')}`);
    }
    if (!urgencyModifiers[urgency]) {
        throw new Error(`Invalid urgency level: ${urgency}. Valid options are: ${Object.keys(urgencyModifiers).join(', ')}`);
    }
    if (!locationModifiers[location]) {
        throw new Error(`Invalid location: ${location}. Valid options are: ${Object.keys(locationModifiers).join(', ')}`);
    }

    // Calculate the base cost based on service type
    const baseCost = baseCosts[serviceType];

    // Calculate the total cost by applying urgency and location modifiers
    const totalCost = baseCost * urgencyModifiers[urgency] * locationModifiers[location];

    return totalCost;
}

// Example usage
try {
    const cost = calculatePlumbingCost('leak detection', 'urgent', 'urban');
    console.log(`The calculated cost is: $${cost}`);
} catch (error) {
    console.error(error.message);
}
```
