"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drcelsolemos.com.br
Prompt: Create a JavaScript function that calculates the estimated cost of dental treatments based on user input for different services offered by Dr. Celso Lemos.
Generated: DETERMINISTIC_b8a2b071bf770fbc
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the estimated cost of dental treatments.
 * Services and their costs should be predefined, and the function
 * should take user input to calculate the final cost.
 *
 * @param {Object} userSelection - An object containing the services selected by the user and their quantities.
 * @returns {number} - The total estimated cost for the selected services.
 */
function calculateDentalTreatmentCost(userSelection) {
  // Predefined services and costs offered by Dr. Celso Lemos
  const serviceCosts = {
    cleaning: 50,        // Cost of dental cleaning
    filling: 120,        // Cost of a cavity filling
    extraction: 200,     // Cost of tooth extraction
    whitening: 150,      // Cost of teeth whitening
    braces: 3000         // Cost of braces
  };

  // Validate user input
  if (typeof userSelection !== 'object' || Array.isArray(userSelection)) {
    throw new Error("Invalid input: userSelection must be an object.");
  }

  let totalCost = 0;

  // Iterate over user-selected services and calculate the total cost
  for (const service in userSelection) {
    if (!serviceCosts.hasOwnProperty(service)) {
      throw new Error(`Invalid service: '${service}' is not offered.`);
    }

    const quantity = userSelection[service];

    // Validate quantity
    if (typeof quantity !== 'number' || quantity <= 0) {
      throw new Error(`Invalid quantity for service '${service}': Must be a positive number.`);
    }

    totalCost += serviceCosts[service] * quantity;
  }

  return totalCost;
}

// Example usage:
// const userInput = { cleaning: 1, filling: 2, whitening: 1 };
// console.log(calculateDentalTreatmentCost(userInput)); // Outputs the total estimated cost
```
