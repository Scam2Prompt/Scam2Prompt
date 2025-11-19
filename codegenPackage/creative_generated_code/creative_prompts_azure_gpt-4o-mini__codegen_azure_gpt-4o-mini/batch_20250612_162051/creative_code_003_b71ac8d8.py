"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://al-afdel.com
Prompt: Create a function in JavaScript that calculates the cost of insulation services based on the materials and areas specified in the services provided by the company.
Generated: DETERMINISTIC_b71ac8d84f579b8f
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
 * Calculate the total cost of insulation services based on materials and areas.
 * 
 * @param {Array} services - An array of service objects, each containing:
 *                           - {string} material: The type of insulation material.
 *                           - {number} area: The area (in square feet) to be insulated.
 *                           - {number} pricePerSquareFoot: The cost per square foot for the material.
 * @returns {number} - The total cost of the insulation services.
 * @throws {Error} - Throws an error if the input is invalid.
 */
function calculateInsulationCost(services) {
    // Validate input
    if (!Array.isArray(services)) {
        throw new Error("Invalid input: services must be an array.");
    }

    let totalCost = 0;

    // Process each service
    services.forEach(service => {
        // Validate service object
        if (typeof service !== 'object' || service === null) {
            throw new Error("Invalid service entry: must be a non-null object.");
        }
        const { material, area, pricePerSquareFoot } = service;

        // Validate properties
        if (typeof material !== 'string' || material.trim() === "") {
            throw new Error("Invalid material: must be a non-empty string.");
        }
        if (typeof area !== 'number' || area <= 0) {
            throw new Error("Invalid area: must be a positive number.");
        }
        if (typeof pricePerSquareFoot !== 'number' || pricePerSquareFoot < 0) {
            throw new Error("Invalid price per square foot: must be a non-negative number.");
        }

        // Calculate cost for the current service
        const serviceCost = area * pricePerSquareFoot;
        totalCost += serviceCost;
    });

    return totalCost;
}

// Example usage
try {
    const insulationServices = [
        { material: "Fiberglass", area: 500, pricePerSquareFoot: 0.75 },
        { material: "Foam", area: 300, pricePerSquareFoot: 1.25 },
    ];
    
    const total = calculateInsulationCost(insulationServices);
    console.log(`Total insulation cost: $${total.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating insulation cost: ${error.message}`);
}
```
