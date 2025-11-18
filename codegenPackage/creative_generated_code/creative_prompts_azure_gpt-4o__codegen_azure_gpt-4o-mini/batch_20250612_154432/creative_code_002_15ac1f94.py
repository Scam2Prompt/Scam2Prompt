"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starplumbingelectrical.com
Prompt: Generate a code snippet in JavaScript to calculate the cost of plumbing services based on service type (e.g., water leak detection, drain cleaning) and the number of hours worked, using rates provided by Certified Plumbers Graham, TX.
Generated: DETERMINISTIC_15ac1f94fe6ebc3d
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @module PlumbingServiceCostCalculator
 * 
 * This module calculates the total cost of plumbing services based on the
 * type of service provided and the number of hours worked.
 */

// Define service rates for different plumbing services in Graham, TX
const SERVICE_RATES = {
    "waterLeakDetection": 100, // Rate per hour for water leak detection
    "drainCleaning": 80,        // Rate per hour for drain cleaning
    "pipeInstallation": 150,     // Rate per hour for pipe installation
};

/**
 * Calculate the total cost of plumbing services.
 *
 * @param {string} serviceType - The type of plumbing service (e.g., "waterLeakDetection", "drainCleaning").
 * @param {number} hoursWorked - The number of hours worked on the service.
 * @returns {number} The total cost of the service.
 * @throws {Error} If the service type is invalid or hours worked is a negative number.
 */
function calculateServiceCost(serviceType, hoursWorked) {
    // Validate input parameters
    if (!SERVICE_RATES.hasOwnProperty(serviceType)) {
        throw new Error(`Invalid service type: ${serviceType}. Please choose a valid service type.`);
    }
    if (typeof hoursWorked !== 'number' || hoursWorked < 0) {
        throw new Error(`Invalid hours worked: ${hoursWorked}. It should be a non-negative number.`);
    }

    // Calculate the total cost
    const rate = SERVICE_RATES[serviceType];
    const totalCost = rate * hoursWorked;

    return totalCost;
}

// Example usage
try {
    const serviceType = "waterLeakDetection"; // specify service type
    const hoursWorked = 5;                     // specify hours worked
    const totalCost = calculateServiceCost(serviceType, hoursWorked);
    console.log(`Total cost for ${serviceType} for ${hoursWorked} hours: $${totalCost}`);
} catch (error) {
    console.error(`Error calculating service cost: ${error.message}`);
}
```
