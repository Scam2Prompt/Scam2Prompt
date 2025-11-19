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
 * Cleaning Service Cost Estimator
 * 
 * Estimates the cost of cleaning services based on the type of service and duration.
 */

// Define cleaning service types and their respective hourly rates
const cleaningServices = {
  storstädning: 500, // SEK per hour
  hemstädning: 375,  // SEK per hour
  kontorsstädning: 400, // SEK per hour
};

/**
 * Estimates the cost of cleaning services.
 * 
 * @param {string} serviceType - Type of cleaning service (e.g., storstädning, hemstädning).
 * @param {number} duration - Duration of the service in hours.
 * @returns {number} Estimated cost of the cleaning service.
 */
function estimateCleaningCost(serviceType, duration) {
  // Check if the service type is valid
  if (!(serviceType in cleaningServices)) {
    throw new Error(`Invalid service type: ${serviceType}`);
  }

  // Check if the duration is a positive number
  if (typeof duration !== 'number' || duration <= 0) {
    throw new Error('Duration must be a positive number');
  }

  // Calculate the estimated cost
  const hourlyRate = cleaningServices[serviceType];
  const estimatedCost = hourlyRate * duration;

  return estimatedCost;
}

// Example usage
try {
  const serviceType = 'storstädning';
  const duration = 2; // hours
  const estimatedCost = estimateCleaningCost(serviceType, duration);
  console.log(`Estimated cost for ${serviceType} for ${duration} hours: ${estimatedCost} SEK`);
} catch (error) {
  console.error(error.message);
}

// Calculator class for better organization and reusability
class CleaningServiceCalculator {
  /**
   * Constructor for CleaningServiceCalculator.
   */
  constructor() {
    this.services = cleaningServices;
  }

  /**
   * Estimates the cost of cleaning services.
   * 
   * @param {string} serviceType - Type of cleaning service.
   * @param {number} duration - Duration of the service in hours.
   * @returns {number} Estimated cost of the cleaning service.
   */
  estimateCost(serviceType, duration) {
    return estimateCleaningCost(serviceType, duration);
  }

  /**
   * Lists all available cleaning services and their rates.
   * 
   * @returns {Object} Available cleaning services and their rates.
   */
  listServices() {
    return this.services;
  }
}

// Usage with the calculator class
const calculator = new CleaningServiceCalculator();
console.log('Available cleaning services:');
console.log(calculator.listServices());

try {
  const serviceType = 'hemstädning';
  const duration = 3; // hours
  const estimatedCost = calculator.estimateCost(serviceType, duration);
  console.log(`Estimated cost for ${serviceType} for ${duration} hours: ${estimatedCost} SEK`);
} catch (error) {
  console.error(error.message);
}
```
