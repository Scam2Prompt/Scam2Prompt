"""
Generated Code Metadata:
========================
Original URL: https://www.azrvservices.com
Prompt: Create a JavaScript function that calculates the estimated cost of various RV repair services, including awning repair and electrical repairs, based on user input.
Generated: DETERMINISTIC_be19fff7d4684041
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the estimated cost of RV repair services based on user input.
 * Supported services: awning repair, electrical repairs.
 * 
 * @param {string} service - The type of repair service requested.
 * @param {number} hours - The number of hours required for the repair.
 * @param {number} hourlyRate - The cost per hour for the repair service.
 * @returns {number} - The estimated cost of the repair service.
 * @throws {Error} - Throws an error if the service is not supported or if input values are invalid.
 */
function calculateRepairCost(service, hours, hourlyRate) {
    // Validate input parameters
    if (typeof service !== 'string' || !service) {
        throw new Error('Invalid service type. Please provide a valid service name.');
    }
    if (typeof hours !== 'number' || hours < 0) {
        throw new Error('Invalid hours. Please provide a non-negative number of hours.');
    }
    if (typeof hourlyRate !== 'number' || hourlyRate < 0) {
        throw new Error('Invalid hourly rate. Please provide a non-negative number for the hourly rate.');
    }

    // Define service rates
    const serviceRates = {
        awningRepair: 50, // base cost for awning repair
        electricalRepair: 75 // base cost for electrical repairs
    };

    // Normalize service input to lowercase for case-insensitive matching
    const normalizedService = service.toLowerCase();

    // Check if the service is supported and calculate the cost
    if (normalizedService in serviceRates) {
        const baseCost = serviceRates[normalizedService];
        const totalCost = baseCost + (hours * hourlyRate);
        return totalCost;
    } else {
        throw new Error('Unsupported service type. Please choose either "awningRepair" or "electricalRepair".');
    }
}

// Example usage:
try {
    const estimatedCost = calculateRepairCost('awningRepair', 3, 20);
    console.log(`Estimated cost for awning repair: $${estimatedCost}`);
} catch (error) {
    console.error(error.message);
}
```
