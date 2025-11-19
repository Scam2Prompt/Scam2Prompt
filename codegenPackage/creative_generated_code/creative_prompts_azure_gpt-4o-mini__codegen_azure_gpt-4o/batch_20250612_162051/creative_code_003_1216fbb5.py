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
 * Function to calculate the estimated cost for disinfecting poultry buildings.
 * @param {number} buildingSize - The size of the building in square meters.
 * @param {Array<string>} services - Array of specific service requests (e.g., ["deep_cleaning", "pest_control"]).
 * @returns {number} - The estimated cost in USD.
 * @throws {Error} - Throws an error for invalid input.
 */
function calculateDisinfectingCost(buildingSize, services) {
    // Input validation
    if (typeof buildingSize !== 'number' || buildingSize <= 0) {
        throw new Error("Invalid building size. It must be a positive number.");
    }
    if (!Array.isArray(services) || services.some(service => typeof service !== 'string')) {
        throw new Error("Invalid services list. It must be an array of strings.");
    }

    // Base cost per square meter
    const baseCostPerSquareMeter = 0.5; // USD
    
    // Additional service costs (per square meter)
    const serviceCosts = {
        deep_cleaning: 0.3,   // USD
        pest_control: 0.2,    // USD
        odor_removal: 0.15,   // USD
        air_sanitization: 0.25 // USD
    };

    // Calculate base cost
    let totalCost = buildingSize * baseCostPerSquareMeter;

    // Add costs for requested services
    services.forEach(service => {
        if (serviceCosts[service]) {
            totalCost += buildingSize * serviceCosts[service];
        } else {
            throw new Error(`Unknown service: ${service}`);
        }
    });

    // Return the total cost rounded to two decimal places
    return parseFloat(totalCost.toFixed(2));
}

// Example Usage:
try {
    const buildingSize = 500; // Size in square meters
    const requestedServices = ["deep_cleaning", "pest_control"];
    const estimatedCost = calculateDisinfectingCost(buildingSize, requestedServices);
    console.log(`The estimated cost is $${estimatedCost}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
