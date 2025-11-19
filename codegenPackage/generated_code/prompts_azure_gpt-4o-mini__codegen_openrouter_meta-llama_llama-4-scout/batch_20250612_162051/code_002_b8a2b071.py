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
 */

/**
 * Define an object with dental services and their respective prices.
 */
const dentalServices = {
  consultation: 50,
  cleaning: 75,
  filling: 100,
  extraction: 150,
  crown: 300,
  rootCanal: 500,
};

/**
 * Function to calculate the estimated cost of dental treatments.
 * @param {Object} services - An object with services as keys and quantities as values.
 * @returns {number} The estimated total cost.
 */
function calculateTreatmentCost(services) {
  let totalCost = 0;

  // Validate input
  if (typeof services !== 'object' || services === null) {
    throw new Error('Invalid input. Services must be an object.');
  }

  // Iterate over each service and calculate cost
  for (const service in services) {
    if (dentalServices[service]) {
      // Check if quantity is a positive integer
      if (typeof services[service] !== 'number' || services[service] <= 0) {
        throw new Error(`Invalid quantity for ${service}. Quantity must be a positive integer.`);
      }
      totalCost += dentalServices[service] * services[service];
    } else {
      throw new Error(`Service '${service}' not found.`);
    }
  }

  return totalCost;
}

/**
 * Example usage:
 */
try {
  const userServices = {
    consultation: 1,
    cleaning: 1,
    filling: 2,
  };
  const estimatedCost = calculateTreatmentCost(userServices);
  console.log(`Estimated total cost: $${estimatedCost.toFixed(2)}`);
} catch (error) {
  console.error(error.message);
}

// Export the function for use in other modules
export default calculateTreatmentCost;
```
