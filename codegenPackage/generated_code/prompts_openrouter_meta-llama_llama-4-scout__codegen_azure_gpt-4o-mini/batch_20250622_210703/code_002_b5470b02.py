"""
Generated Code Metadata:
========================
Original URL: https://www.aspuddensstad.se
Prompt: Generate a JavaScript code snippet for a simple calculator that estimates the cost of städning (cleaning) services based on the type of service (e.g., storstädning, hemstädning) and duration.
Generated: DETERMINISTIC_b5470b02eca7818d
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple Calculator for Cleaning Services Cost Estimation
 * This calculator estimates the cost of cleaning services based on the type of service
 * and the duration in hours.
 */

// Define a class for the CleaningServiceCalculator
class CleaningServiceCalculator {
    // Define the rates for different types of cleaning services
    static rates = {
        storstädning: 200, // Rate per hour for deep cleaning
        hemstädning: 150,  // Rate per hour for regular cleaning
    };

    /**
     * Calculate the estimated cost of cleaning services.
     * @param {string} serviceType - The type of cleaning service (storstädning or hemstädning).
     * @param {number} duration - The duration of the service in hours.
     * @returns {number} - The estimated cost of the service.
     * @throws {Error} - Throws an error if the service type is invalid or duration is not a positive number.
     */
    static calculateCost(serviceType, duration) {
        // Validate the service type
        if (!CleaningServiceCalculator.rates[serviceType]) {
            throw new Error(`Invalid service type: ${serviceType}. Please choose either 'storstädning' or 'hemstädning'.`);
        }

        // Validate the duration
        if (typeof duration !== 'number' || duration <= 0) {
            throw new Error(`Invalid duration: ${duration}. Duration must be a positive number.`);
        }

        // Calculate the estimated cost
        const rate = CleaningServiceCalculator.rates[serviceType];
        return rate * duration;
    }
}

// Example usage
try {
    const serviceType = 'storstädning'; // Change to 'hemstädning' for regular cleaning
    const duration = 3; // Duration in hours

    // Calculate the cost
    const estimatedCost = CleaningServiceCalculator.calculateCost(serviceType, duration);
    console.log(`The estimated cost for ${duration} hours of ${serviceType} is: ${estimatedCost} SEK`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
