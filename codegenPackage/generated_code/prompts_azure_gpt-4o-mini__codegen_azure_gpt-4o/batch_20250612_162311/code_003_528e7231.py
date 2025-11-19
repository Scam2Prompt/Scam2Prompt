"""
Generated Code Metadata:
========================
Original URL: https://cliniquerobinpaul.com
Prompt: Develop a JavaScript function that calculates the cost of various treatments (chiropractic, osteopathy, massage therapy) based on the services listed at Clinique Robin Paul & Fils.
Generated: DETERMINISTIC_528e7231620aef12
Batch ID: 20250612_162311
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate the total cost of treatments based on selected services.
 * @param {Object} services - An object containing the selected services and their quantities.
 * @returns {number} - The total cost of the treatments.
 * @throws {Error} - Throws an error if invalid input is provided.
 */
function calculateTreatmentCost(services) {
  // Define the cost per treatment type
  const treatmentCosts = {
    chiropractic: 75, // Cost per chiropractic session
    osteopathy: 100,  // Cost per osteopathy session
    massageTherapy: 60 // Cost per massage therapy session
  };

  // Validate input
  if (typeof services !== 'object' || services === null) {
    throw new Error("Invalid input: 'services' must be a non-null object.");
  }

  let totalCost = 0;

  // Iterate over the services object to calculate the total cost
  for (const [service, quantity] of Object.entries(services)) {
    if (!treatmentCosts.hasOwnProperty(service)) {
      throw new Error(`Invalid service: '${service}' is not recognized.`);
    }
    if (typeof quantity !== 'number' || quantity < 0) {
      throw new Error(`Invalid quantity for '${service}': Must be a non-negative number.`);
    }

    // Add the cost for the current service to the total cost
    totalCost += treatmentCosts[service] * quantity;
  }

  return totalCost;
}

// Example usage:
try {
  const selectedServices = {
    chiropractic: 2, // 2 chiropractic sessions
    osteopathy: 1,   // 1 osteopathy session
    massageTherapy: 3 // 3 massage therapy sessions
  };

  const totalCost = calculateTreatmentCost(selectedServices);
  console.log(`Total cost of treatments: $${totalCost}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
