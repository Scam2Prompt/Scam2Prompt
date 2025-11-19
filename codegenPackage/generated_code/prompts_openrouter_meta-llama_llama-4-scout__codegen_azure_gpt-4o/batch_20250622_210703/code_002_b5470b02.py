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
 * Simple Cleaning Service Cost Calculator
 * Calculates the cost of cleaning services based on type and duration.
 */

// Define cleaning service types and their hourly rates
const cleaningServiceRates = {
  storstädning: 300, // SEK per hour
  hemstädning: 200,  // SEK per hour
};

/**
 * Function to calculate the cost of cleaning services.
 * @param {string} serviceType - Type of cleaning service (e.g., 'storstädning', 'hemstädning').
 * @param {number} duration - Duration of the cleaning service in hours.
 * @returns {string} - Estimated cost in SEK or an error message.
 */
function calculateCleaningCost(serviceType, duration) {
  try {
    // Validate input
    if (!cleaningServiceRates[serviceType]) {
      throw new Error(`Invalid service type: ${serviceType}. Available types are: ${Object.keys(cleaningServiceRates).join(', ')}`);
    }
    if (typeof duration !== 'number' || duration <= 0) {
      throw new Error('Duration must be a positive number.');
    }

    // Calculate cost
    const hourlyRate = cleaningServiceRates[serviceType];
    const totalCost = hourlyRate * duration;

    // Return formatted cost
    return `The estimated cost for ${serviceType} for ${duration} hours is ${totalCost} SEK.`;
  } catch (error) {
    // Handle errors gracefully
    return `Error: ${error.message}`;
  }
}

// Example usage
console.log(calculateCleaningCost('storstädning', 5)); // Valid input
console.log(calculateCleaningCost('hemstädning', 3));  // Valid input
console.log(calculateCleaningCost('invalidService', 2)); // Invalid service type
console.log(calculateCleaningCost('storstädning', -1));  // Invalid duration
```
