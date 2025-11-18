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
 * Function to calculate the cost of plumbing services.
 * @param {string} serviceType - Type of plumbing service (e.g., "waterLeakDetection", "drainCleaning").
 * @param {number} hoursWorked - Number of hours the service was performed.
 * @returns {number} - Total cost of the plumbing service.
 * @throws Will throw an error if the service type is invalid or hours worked is negative.
 */

// Define service rates per hour (based on Certified Plumbers Graham, TX)
const serviceRates = {
  waterLeakDetection: 75, // $75 per hour
  drainCleaning: 50,      // $50 per hour
  pipeInstallation: 100   // $100 per hour
};

function calculatePlumbingCost(serviceType, hoursWorked) {
  // Validate input parameters
  if (!serviceRates.hasOwnProperty(serviceType)) {
    throw new Error(`Invalid service type: ${serviceType}`);
  }
  if (hoursWorked < 0) {
    throw new Error(`Hours worked cannot be negative: ${hoursWorked}`);
  }

  // Calculate the cost
  const ratePerHour = serviceRates[serviceType];
  const totalCost = ratePerHour * hoursWorked;

  return totalCost;
}

// Example usage (uncomment to test):
try {
  const serviceType = "waterLeakDetection";
  const hoursWorked = 3;
  const cost = calculatePlumbingCost(serviceType, hoursWorked);
  console.log(`The total cost for ${hoursWorked} hours of ${serviceType} is $${cost}.`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
