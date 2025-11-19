"""
Generated Code Metadata:
========================
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Develop a JavaScript function that calculates the estimated cost for disinfecting poultry buildings based on user input for building size and specific service requests.
Generated: DETERMINISTIC_1216fbb5998a361d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the estimated cost for disinfecting poultry buildings.
 * 
 * @param {Object} options - User input options.
 * @param {number} options.buildingSize - The size of the building in square feet.
 * @param {string} options.serviceType - The type of disinfection service requested (e.g., 'standard', 'premium', 'extended').
 * @param {number} [options.additionalServices] - Additional services requested (e.g., number of rooms, special equipment needed).
 * @returns {Object} An object containing the estimated cost and a description of the services included.
 */

function calculateDisinfectionCost(options) {
    try {
        // Validate input options
        if (!options || typeof options !== 'object') {
            throw new Error('Invalid input options');
        }

        const requiredOptions = ['buildingSize', 'serviceType'];
        if (!requiredOptions.every(option => option in options)) {
            throw new Error('Missing required options');
        }

        const { buildingSize, serviceType, additionalServices } = options;

        // Validate building size
        if (typeof buildingSize !== 'number' || buildingSize <= 0) {
            throw new Error('Building size must be a positive number');
        }

        // Define service pricing
        const servicePrices = {
            standard: 0.05,
            premium: 0.10,
            extended: 0.15
        };

        // Validate service type
        if (!(serviceType in servicePrices)) {
            throw new Error(`Invalid service type: ${serviceType}`);
        }

        // Calculate base cost
        const baseCost = buildingSize * servicePrices[serviceType];

        // Calculate additional services cost
        let additionalCost = 0;
        if (additionalServices) {
            if (typeof additionalServices === 'number') {
                // Assume additional cost is $100 per room or equipment
                additionalCost = additionalServices * 100;
            } else {
                throw new Error('Additional services must be a number');
            }
        }

        // Calculate total cost
        const totalCost = baseCost + additionalCost;

        // Return estimated cost and services description
        return {
            estimatedCost: totalCost.toFixed(2),
            services: [
                `Disinfection of ${buildingSize} sq. ft. building at $${servicePrices[serviceType].toFixed(2)} per sq. ft.`,
                additionalServices ? `${additionalServices} additional services` : ''
            ].filter(Boolean)
        };
    } catch (error) {
        // Return error message
        return { error: error.message };
    }
}

// Example usage:
const options = {
    buildingSize: 10000,
    serviceType: 'premium',
    additionalServices: 5
};

const result = calculateDisinfectionCost(options);
console.log(result);
```
