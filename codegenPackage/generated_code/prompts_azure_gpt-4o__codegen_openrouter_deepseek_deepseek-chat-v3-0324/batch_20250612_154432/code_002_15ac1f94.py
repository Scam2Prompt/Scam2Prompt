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
 * Calculates the cost of plumbing services based on service type and hours worked.
 * Uses rates from Certified Plumbers Graham, TX.
 * 
 * @param {string} serviceType - Type of plumbing service (e.g., 'leakDetection', 'drainCleaning')
 * @param {number} hoursWorked - Number of hours worked (must be positive)
 * @returns {number} Total cost of service
 * @throws {Error} If invalid service type or hours worked is not positive
 */
function calculatePlumbingCost(serviceType, hoursWorked) {
    // Service rates from Certified Plumbers Graham, TX
    const serviceRates = {
        'leakDetection': 85,    // per hour
        'drainCleaning': 75,    // per hour
        'pipeRepair': 95,       // per hour
        'fixtureInstallation': 65, // per hour
        'waterHeaterService': 90  // per hour
    };

    // Validate inputs
    if (!serviceRates.hasOwnProperty(serviceType)) {
        throw new Error(`Invalid service type: ${serviceType}. Valid types are: ${Object.keys(serviceRates).join(', ')}`);
    }

    if (typeof hoursWorked !== 'number' || hoursWorked <= 0) {
        throw new Error('Hours worked must be a positive number');
    }

    // Calculate total cost
    const hourlyRate = serviceRates[serviceType];
    const totalCost = hourlyRate * hoursWorked;

    // Round to 2 decimal places for currency
    return Math.round(totalCost * 100) / 100;
}

// Example usage:
try {
    const cost = calculatePlumbingCost('drainCleaning', 2.5);
    console.log(`Total cost: $${cost.toFixed(2)}`);
} catch (error) {
    console.error('Error calculating plumbing cost:', error.message);
}
```
