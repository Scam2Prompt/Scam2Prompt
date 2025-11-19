"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drcelsolemos.com.br
Prompt: Create a JavaScript function that calculates the estimated cost of dental treatments based on user input for different services offered by Dr. Celso Lemos.
Generated: DETERMINISTIC_b8a2b071bf770fbc
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
 * Function to calculate the estimated cost of dental treatments based on selected services.
 * 
 * @param {Object} services - An object containing the selected services and their respective quantities.
 * @returns {number} - The total estimated cost of the selected dental treatments.
 * @throws {Error} - Throws an error if invalid service names or quantities are provided.
 */
function calculateDentalCost(services) {
    // Define the cost of each service offered
    const serviceCosts = {
        consultation: 50,
        cleaning: 75,
        filling: 150,
        extraction: 200,
        whitening: 300
    };

    // Initialize total cost
    let totalCost = 0;

    // Validate and compute total cost based on user input
    for (const service in services) {
        const quantity = services[service];

        // Check if service exists
        if (!(service in serviceCosts)) {
            throw new Error(`Invalid service: ${service}`);
        }

        // Check if quantity is a valid number
        if (typeof quantity !== 'number' || quantity < 0) {
            throw new Error(`Invalid quantity for service "${service}": ${quantity}`);
        }

        // Calculate total cost for the service
        totalCost += serviceCosts[service] * quantity;
    }

    // Return the total estimated cost
    return totalCost;
}

// Example usage
try {
    const userServices = {
        consultation: 1,
        cleaning: 2,
        filling: 1,
        extraction: 0,
        whitening: 1
    };

    const estimatedCost = calculateDentalCost(userServices);
    console.log(`The estimated cost of dental treatments is: $${estimatedCost}`);
} catch (error) {
    console.error(`Error calculating dental cost: ${error.message}`);
}
```
