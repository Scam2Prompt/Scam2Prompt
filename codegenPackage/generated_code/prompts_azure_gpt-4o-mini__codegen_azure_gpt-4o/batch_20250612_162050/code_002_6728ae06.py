"""
Generated Code Metadata:
========================
Original URL: https://birlikjenerator.com
Prompt: Create a JavaScript function that validates user inputs for selecting portable diesel generators, incorporating the unique features highlighted on the Birlik Jeneratör site.
Generated: DETERMINISTIC_6728ae06d15b36f7
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user inputs for selecting portable diesel generators.
 * The validation is based on common features highlighted on the Birlik Jeneratör site.
 * 
 * @param {Object} userInput - The user input object containing generator preferences.
 * @param {number} userInput.powerOutput - Desired power output in kW.
 * @param {string} userInput.fuelEfficiency - Desired fuel efficiency rating (e.g., "high", "medium", "low").
 * @param {boolean} userInput.isSilent - Whether the generator should be silent (true/false).
 * @param {number} userInput.weight - Maximum acceptable weight in kg.
 * @returns {Object} - Validation result with a boolean `isValid` and an array of `errors`.
 */
function validateGeneratorInput(userInput) {
  const errors = [];

  // Validate power output (must be a positive number)
  if (typeof userInput.powerOutput !== 'number' || userInput.powerOutput <= 0) {
    errors.push("Power output must be a positive number.");
  }

  // Validate fuel efficiency (must be one of the predefined options)
  const validFuelEfficiencyOptions = ["high", "medium", "low"];
  if (!validFuelEfficiencyOptions.includes(userInput.fuelEfficiency)) {
    errors.push(`Fuel efficiency must be one of the following: ${validFuelEfficiencyOptions.join(", ")}.`);
  }

  // Validate silent mode (must be a boolean)
  if (typeof userInput.isSilent !== 'boolean') {
    errors.push("Silent mode must be a boolean value (true or false).");
  }

  // Validate weight (must be a positive number)
  if (typeof userInput.weight !== 'number' || userInput.weight <= 0) {
    errors.push("Weight must be a positive number.");
  }

  // Return validation result
  return {
    isValid: errors.length === 0,
    errors: errors
  };
}

// Example usage:
const userInput = {
  powerOutput: 5,          // in kW
  fuelEfficiency: "high",  // "high", "medium", or "low"
  isSilent: true,          // true or false
  weight: 50               // in kg
};

const validationResult = validateGeneratorInput(userInput);
if (validationResult.isValid) {
  console.log("User input is valid.");
} else {
  console.error("Validation errors:", validationResult.errors);
}
```
