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
 * @param {number} buildingSize - The size of the building in square feet.
 * @param {Array<string>} serviceRequests - An array of specific service requests.
 * @returns {number} - The estimated cost for the disinfection service.
 * @throws {Error} - Throws an error if buildingSize is not a positive number or if serviceRequests is not an array.
 */
function calculateDisinfectionCost(buildingSize, serviceRequests) {
    // Validate input parameters
    if (typeof buildingSize !== 'number' || buildingSize <= 0) {
        throw new Error('Invalid building size. It must be a positive number.');
    }
    
    if (!Array.isArray(serviceRequests)) {
        throw new Error('Invalid service requests. It must be an array of strings.');
    }

    // Base cost per square foot
    const baseCostPerSqFt = 0.10; // Example cost per square foot
    let totalCost = buildingSize * baseCostPerSqFt;

    // Additional costs based on specific service requests
    const serviceCosts = {
        'deepCleaning': 200, // Flat fee for deep cleaning
        'chemicalTreatment': 150, // Flat fee for chemical treatment
        'fumigation': 300 // Flat fee for fumigation
    };

    // Calculate additional costs based on user requests
    serviceRequests.forEach(service => {
        if (serviceCosts[service]) {
            totalCost += serviceCosts[service];
        } else {
            console.warn(`Service request "${service}" is not recognized and will be ignored.`);
        }
    });

    return totalCost;
}

// Example usage
try {
    const buildingSize = 5000; // Size in square feet
    const serviceRequests = ['deepCleaning', 'fumigation']; // User service requests
    const estimatedCost = calculateDisinfectionCost(buildingSize, serviceRequests);
    console.log(`The estimated cost for disinfecting the building is: $${estimatedCost.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating cost: ${error.message}`);
}
```
