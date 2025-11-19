"""
Generated Code Metadata:
========================
Original URL: https://starplumbingelectrical.com
Prompt: Generate a code snippet in JavaScript to calculate the cost of plumbing services based on service type (e.g., water leak detection, drain cleaning) and the number of hours worked, using rates provided by Certified Plumbers Graham, TX.
Generated: DETERMINISTIC_15ac1f94fe6ebc3d
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * PlumbingServiceCalculator class to calculate the cost of plumbing services.
 */
class PlumbingServiceCalculator {
    // Define service rates in dollars per hour
    static SERVICE_RATES = {
        'waterLeakDetection': 100, // Rate for water leak detection
        'drainCleaning': 80,        // Rate for drain cleaning
        'pipeInstallation': 120,    // Rate for pipe installation
        'emergencyService': 150      // Rate for emergency services
    };

    /**
     * Calculate the total cost of plumbing services.
     * @param {string} serviceType - The type of plumbing service.
     * @param {number} hoursWorked - The number of hours worked.
     * @returns {number} - The total cost of the service.
     * @throws {Error} - Throws an error if the service type is invalid or hours worked is negative.
     */
    static calculateCost(serviceType, hoursWorked) {
        // Validate service type
        if (!this.SERVICE_RATES.hasOwnProperty(serviceType)) {
            throw new Error(`Invalid service type: ${serviceType}. Please choose a valid service.`);
        }

        // Validate hours worked
        if (typeof hoursWorked !== 'number' || hoursWorked < 0) {
            throw new Error(`Invalid hours worked: ${hoursWorked}. Hours must be a non-negative number.`);
        }

        // Calculate total cost
        const rate = this.SERVICE_RATES[serviceType];
        const totalCost = rate * hoursWorked;

        return totalCost;
    }
}

// Example usage
try {
    const serviceType = 'drainCleaning'; // Example service type
    const hoursWorked = 3;                // Example hours worked
    const totalCost = PlumbingServiceCalculator.calculateCost(serviceType, hoursWorked);
    console.log(`The total cost for ${hoursWorked} hours of ${serviceType} is $${totalCost}.`);
} catch (error) {
    console.error(error.message);
}
```
