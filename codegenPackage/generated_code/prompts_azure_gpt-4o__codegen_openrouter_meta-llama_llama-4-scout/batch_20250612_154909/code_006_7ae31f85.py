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
 * @param {Object} serviceRequest - Request object containing service details.
 * @param {String} serviceRequest.serviceType - Type of plumbing service (e.g., leak detection, industrial cleaning).
 * @param {String} serviceRequest.urgency - Level of urgency (e.g., emergency, routine).
 * @param {String} serviceRequest.location - Location of service (e.g., residential, commercial).
 * @param {Number} [serviceRequest.distance=0] - Distance to service location in miles.
 * 
 * @returns {Number} The calculated cost of the plumbing service.
 */
function calculatePlumbingCost(serviceRequest) {
    // Define base costs for service types
    const serviceTypeCosts = {
        'leak detection': 100,
        'industrial cleaning': 200,
        'drain cleaning': 150,
        'pipe repair': 120,
        'default': 100 // Default cost for unknown service types
    };

    // Define urgency multipliers
    const urgencyMultipliers = {
        'emergency': 1.5,
        'routine': 1,
        'default': 1 // Default multiplier for unknown urgency levels
    };

    // Define location multipliers
    const locationMultipliers = {
        'residential': 1,
        'commercial': 1.2,
        'industrial': 1.5,
        'default': 1 // Default multiplier for unknown locations
    };

    // Define distance rate
    const distanceRate = 50; // $50 per mile

    // Validate service request
    if (!serviceRequest || !serviceRequest.serviceType || !serviceRequest.urgency || !serviceRequest.location) {
        throw new Error('Invalid service request. Please provide service type, urgency, and location.');
    }

    // Get service type cost
    const serviceTypeCost = serviceTypeCosts[serviceRequest.serviceType.toLowerCase()] || serviceTypeCosts['default'];

    // Get urgency multiplier
    const urgencyMultiplier = urgencyMultipliers[serviceRequest.urgency.toLowerCase()] || urgencyMultipliers['default'];

    // Get location multiplier
    const locationMultiplier = locationMultipliers[serviceRequest.location.toLowerCase()] || locationMultipliers['default'];

    // Calculate base cost
    let baseCost = serviceTypeCost * urgencyMultiplier * locationMultiplier;

    // Calculate distance cost
    const distanceCost = (serviceRequest.distance || 0) * distanceRate;

    // Calculate total cost
    const totalCost = baseCost + distanceCost;

    return totalCost;
}

// Example usage:
try {
    const serviceRequest = {
        serviceType: 'leak detection',
        urgency: 'emergency',
        location: 'residential',
        distance: 10 // miles
    };

    const cost = calculatePlumbingCost(serviceRequest);
    console.log(`The calculated cost of the plumbing service is: $${cost.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
