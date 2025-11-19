"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cliniquerobinpaul.com
Prompt: Develop a JavaScript function that calculates the cost of various treatments (chiropractic, osteopathy, massage therapy) based on the services listed at Clinique Robin Paul & Fils.
Generated: DETERMINISTIC_528e7231620aef12
Batch ID: 20250612_162311
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total cost of treatments based on the services selected.
 * 
 * @param {Object} services - An object where keys are treatment names and values are quantities.
 * @returns {number} - The total cost of the selected treatments.
 * @throws {Error} - Throws an error if an invalid service is provided.
 */
function calculateTreatmentCost(services) {
  // Define the cost per treatment type
  const treatmentRates = {
    chiropractic: 60, // Cost per session in dollars
    osteopathy: 75,   // Cost per session in dollars
    massageTherapy: 50 // Cost per session in dollars
  };

  // Input validation: Ensure services is an object
  if (typeof services !== 'object' || services === null) {
    throw new Error("Invalid input: services must be an object.");
  }

  let totalCost = 0;

  // Iterate through each service in the input object
  for (const [treatment, quantity] of Object.entries(services)) {
    // Check if the treatment exists in the predefined rates
    if (!treatmentRates.hasOwnProperty(treatment)) {
      throw new Error(`Invalid service: "${treatment}" is not offered.`);
    }

    // Validate that the quantity is a positive integer
    if (!Number.isInteger(quantity) || quantity < 0) {
      throw new Error(
        `Invalid quantity for "${treatment}": must be a positive integer.`
      );
    }

    // Calculate cost for the current treatment and add to the total cost
    totalCost += treatmentRates[treatment] * quantity;
  }

  return totalCost;
}

// Example usage:

try {
  // Define the services selected by the user
  const selectedServices = {
    chiropractic: 2, // 2 sessions
    osteopathy: 1,   // 1 session
    massageTherapy: 3 // 3 sessions
  };

  // Calculate the total cost
  const totalCost = calculateTreatmentCost(selectedServices);
  console.log(`Total Cost: $${totalCost}`);
} catch (error) {
  // Handle errors gracefully
  console.error(error.message);
}
```
