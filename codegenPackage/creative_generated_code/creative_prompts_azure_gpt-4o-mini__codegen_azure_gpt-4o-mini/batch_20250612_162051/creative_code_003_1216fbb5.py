"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Develop a JavaScript function that calculates the estimated cost for disinfecting poultry buildings based on user input for building size and specific service requests.
Generated: DETERMINISTIC_1216fbb5998a361d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the estimated cost for disinfecting poultry buildings.
 *
 * @param {number} buildingSize - The size of the building in square feet.
 * @param {Array} serviceRequests - An array of service requests, each represented by an object
 *                                  containing 'serviceType' and 'costMultiplier'.
 * @returns {number} - The estimated cost for disinfecting the building.
 * @throws {Error} - Throws an error if buildingSize is not a positive number or if serviceRequests is not an array.
 */
function calculateDisinfectionCost(buildingSize, serviceRequests) {
    // Validate input parameters
    if (typeof buildingSize !== 'number' || buildingSize <= 0) {
        throw new Error('Building size must be a positive number.');
    }
    
    if (!Array.isArray(serviceRequests)) {
        throw new Error('Service requests must be an array.');
    }

    // Initialize base cost per square foot (this can vary based on your pricing model)
    const baseCostPerSquareFoot = 0.10; // Example cost per square foot

    // Calculate the base cost for disinfecting the building
    let estimatedCost = buildingSize * baseCostPerSquareFoot;

    // Iterate over each service request to calculate additional costs
    serviceRequests.forEach(request => {
        if (typeof request.serviceType !== 'string' || typeof request.costMultiplier !== 'number') {
            throw new Error('Each service request must have a valid serviceType and costMultiplier.');
        }

        // Add the cost of the service request based on the building size
        estimatedCost += buildingSize * request.costMultiplier;
    });

    // Return the final estimated cost, ensuring it has at least 2 decimal places
    return parseFloat(estimatedCost.toFixed(2));
}

// Example Usage:
try {
    const buildingSize = 5000; // in square feet
    const serviceRequests = [
        { serviceType: 'Deep Cleaning', costMultiplier: 0.05 },
        { serviceType: 'Pest Control', costMultiplier: 0.03 }
    ];

    const totalCost = calculateDisinfectionCost(buildingSize, serviceRequests);
    console.log(`Estimated Cost for Disinfection: $${totalCost}`);
} catch (error) {
    console.error(error.message);
}
```
