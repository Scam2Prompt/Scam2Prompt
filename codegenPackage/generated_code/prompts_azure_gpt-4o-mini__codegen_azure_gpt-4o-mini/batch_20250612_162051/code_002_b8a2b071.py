"""
Generated Code Metadata:
========================
Original URL: https://drcelsolemos.com.br
Prompt: Create a JavaScript function that calculates the estimated cost of dental treatments based on user input for different services offered by Dr. Celso Lemos.
Generated: DETERMINISTIC_b8a2b071bf770fbc
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
 * Calculates the estimated cost of dental treatments based on user input.
 * 
 * @param {Object} services - An object containing the services and their respective costs.
 * @param {Array} selectedServices - An array of strings representing the selected services.
 * @returns {number} - The total estimated cost of the selected dental treatments.
 * @throws {Error} - Throws an error if a selected service is not found in the services list.
 */
function calculateDentalCost(services, selectedServices) {
    // Validate input types
    if (typeof services !== 'object' || !Array.isArray(selectedServices)) {
        throw new Error('Invalid input: services must be an object and selectedServices must be an array.');
    }

    let totalCost = 0;

    // Iterate through the selected services to calculate the total cost
    selectedServices.forEach(service => {
        // Check if the service exists in the services object
        if (services.hasOwnProperty(service)) {
            totalCost += services[service];
        } else {
            throw new Error(`Service "${service}" not found in the services list.`);
        }
    });

    return totalCost;
}

// Example usage
try {
    const dentalServices = {
        'Cleaning': 75,
        'Filling': 150,
        'Root Canal': 300,
        'Crown': 800,
        'Extraction': 200
    };

    const selected = ['Cleaning', 'Filling', 'Crown'];
    const estimatedCost = calculateDentalCost(dentalServices, selected);
    console.log(`The estimated cost of the selected dental treatments is: $${estimatedCost}`);
} catch (error) {
    console.error(`Error calculating dental cost: ${error.message}`);
}
```
