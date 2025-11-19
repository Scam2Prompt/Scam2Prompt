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
 * Function to calculate the estimated cost of RV repair services.
 * @param {Object} services - An object containing the selected services and their quantities.
 * @returns {number} - The total estimated cost of the repair services.
 */
function calculateRVRepairCost(services) {
  // Define the cost per service type
  const serviceRates = {
    awningRepair: 150, // Cost per awning repair
    electricalRepair: 200, // Cost per electrical repair
    plumbingRepair: 180, // Cost per plumbing repair
    tireReplacement: 120, // Cost per tire replacement
  };

  // Validate input
  if (typeof services !== 'object' || services === null) {
    throw new Error("Invalid input: 'services' must be a non-null object.");
  }

  let totalCost = 0;

  // Iterate through the services object to calculate the total cost
  for (const [service, quantity] of Object.entries(services)) {
    if (!serviceRates[service]) {
      throw new Error(`Unknown service: '${service}'.`);
    }
    if (typeof quantity !== 'number' || quantity < 0) {
      throw new Error(`Invalid quantity for service '${service}': Must be a non-negative number.`);
    }

    totalCost += serviceRates[service] * quantity;
  }

  return totalCost;
}

// Example usage:
try {
  const userServices = {
    awningRepair: 2,
    electricalRepair: 1,
    plumbingRepair: 0,
    tireReplacement: 4,
  };

  const estimatedCost = calculateRVRepairCost(userServices);
  console.log(`The estimated cost for the selected services is: $${estimatedCost}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
