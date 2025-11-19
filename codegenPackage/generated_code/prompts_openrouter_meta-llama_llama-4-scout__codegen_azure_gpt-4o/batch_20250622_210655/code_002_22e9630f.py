"""
Generated Code Metadata:
========================
Original URL: https://capetownplasticsurgeon.co.za
Prompt: Create a JavaScript function to calculate the cost of a surgical procedure based on individual patient needs and procedure details.
Generated: DETERMINISTIC_22e9630fb5886033
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate the cost of a surgical procedure based on patient needs and procedure details.
 * @param {Object} patientDetails - An object containing patient-specific details.
 * @param {Object} procedureDetails - An object containing procedure-specific details.
 * @returns {number} - The total cost of the surgical procedure.
 * @throws {Error} - Throws an error if input data is invalid.
 */
function calculateSurgicalCost(patientDetails, procedureDetails) {
  // Validate input parameters
  if (!patientDetails || typeof patientDetails !== 'object') {
    throw new Error("Invalid patient details provided.");
  }
  if (!procedureDetails || typeof procedureDetails !== 'object') {
    throw new Error("Invalid procedure details provided.");
  }

  // Extract patient-specific details
  const { age, insuranceCoverage, additionalNeeds } = patientDetails;
  if (typeof age !== 'number' || age <= 0) {
    throw new Error("Invalid age provided in patient details.");
  }
  if (typeof insuranceCoverage !== 'number' || insuranceCoverage < 0 || insuranceCoverage > 100) {
    throw new Error("Invalid insurance coverage percentage provided.");
  }
  if (!Array.isArray(additionalNeeds)) {
    throw new Error("Additional needs must be an array.");
  }

  // Extract procedure-specific details
  const { baseCost, complexityFactor, additionalCosts } = procedureDetails;
  if (typeof baseCost !== 'number' || baseCost <= 0) {
    throw new Error("Invalid base cost provided in procedure details.");
  }
  if (typeof complexityFactor !== 'number' || complexityFactor <= 0) {
    throw new Error("Invalid complexity factor provided.");
  }
  if (!Array.isArray(additionalCosts)) {
    throw new Error("Additional costs must be an array.");
  }

  // Calculate the base procedure cost
  let totalCost = baseCost * complexityFactor;

  // Add additional costs for the procedure
  additionalCosts.forEach((cost) => {
    if (typeof cost !== 'number' || cost < 0) {
      throw new Error("Invalid value in additional costs.");
    }
    totalCost += cost;
  });

  // Add costs for patient-specific additional needs
  additionalNeeds.forEach((needCost) => {
    if (typeof needCost !== 'number' || needCost < 0) {
      throw new Error("Invalid value in additional needs.");
    }
    totalCost += needCost;
  });

  // Apply insurance coverage discount
  const insuranceDiscount = (insuranceCoverage / 100) * totalCost;
  totalCost -= insuranceDiscount;

  // Ensure the total cost is rounded to two decimal places
  return parseFloat(totalCost.toFixed(2));
}

// Example usage:
try {
  const patientDetails = {
    age: 45,
    insuranceCoverage: 80, // 80% coverage
    additionalNeeds: [200, 150], // Additional costs for patient-specific needs
  };

  const procedureDetails = {
    baseCost: 5000, // Base cost of the procedure
    complexityFactor: 1.2, // Complexity multiplier
    additionalCosts: [300, 400], // Additional costs for the procedure
  };

  const totalCost = calculateSurgicalCost(patientDetails, procedureDetails);
  console.log(`The total cost of the surgical procedure is: $${totalCost}`);
} catch (error) {
  console.error(`Error calculating surgical cost: ${error.message}`);
}
```
