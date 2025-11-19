"""
Generated Code Metadata:
========================
Original URL: https://jobbo.com.au
Prompt: "Generate a code snippet in JavaScript for a simple calculator that determines the cost of moving sleds to different pull centers in Australia, considering factors mentioned on jobbo.com.au."
Generated: DETERMINISTIC_475e9fed9b906dae
Batch ID: 20250622_205138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the cost of moving sleds to different pull centers in Australia.
 * Based on factors from jobbo.com.au including distance, weight, and service type.
 * 
 * @param {Object} params - Parameters for the calculation
 * @param {number} params.distance - Distance in kilometers
 * @param {number} params.weight - Weight of sleds in kilograms
 * @param {string} params.serviceType - Type of service ('standard', 'express', 'premium')
 * @param {string} params.destination - Destination city in Australia
 * @returns {Object} - Result containing cost and any additional information
 * @throws {Error} - If invalid parameters are provided
 */
function calculateMovingCost(params) {
    // Validate input parameters
    if (!params || typeof params !== 'object') {
        throw new Error('Invalid parameters: must provide an object');
    }

    const { distance, weight, serviceType, destination } = params;

    if (typeof distance !== 'number' || distance <= 0) {
        throw new Error('Invalid distance: must be a positive number');
    }

    if (typeof weight !== 'number' || weight <= 0) {
        throw new Error('Invalid weight: must be a positive number');
    }

    if (!['standard', 'express', 'premium'].includes(serviceType)) {
        throw new Error('Invalid service type: must be standard, express, or premium');
    }

    if (!destination || typeof destination !== 'string') {
        throw new Error('Invalid destination: must be a non-empty string');
    }

    // Base cost per kilometer (AUD)
    const baseRatePerKm = 0.50;
    
    // Weight multiplier factors
    const weightMultipliers = {
        standard: 1.0,
        express: 1.2,
        premium: 1.5
    };

    // Regional multipliers for different Australian cities
    const regionalMultipliers = {
        'Sydney': 1.0,
        'Melbourne': 1.0,
        'Brisbane': 1.1,
        'Perth': 1.3,
        'Adelaide': 1.2,
        'Canberra': 1.1,
        'Hobart': 1.4,
        'Darwin': 1.5
    };

    // Get regional multiplier (default to 1.5 if city not found)
    const regionalMultiplier = regionalMultipliers[destination] || 1.5;

    // Calculate total cost
    const baseCost = distance * baseRatePerKm;
    const weightAdjustedCost = baseCost * weight * 0.001; // Convert kg to metric tons factor
    const serviceAdjustedCost = weightAdjustedCost * weightMultipliers[serviceType];
    const totalCost = serviceAdjustedCost * regionalMultiplier;

    // Round to 2 decimal places for currency
    const roundedCost = Math.round(totalCost * 100) / 100;

    return {
        cost: roundedCost,
        currency: 'AUD',
        distance: distance,
        weight: weight,
        serviceType: serviceType,
        destination: destination,
        calculationDetails: {
            baseRatePerKm,
            weightMultiplier: weightMultipliers[serviceType],
            regionalMultiplier
        }
    };
}

// Example usage:
// try {
//     const result = calculateMovingCost({
//         distance: 200,
//         weight: 500,
//         serviceType: 'express',
//         destination: 'Perth'
//     });
//     console.log(result);
// } catch (error) {
//     console.error('Error:', error.message);
// }
```
