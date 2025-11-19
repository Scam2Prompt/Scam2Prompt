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
 * 
 * @param {Object} userInput - User input object containing generator selection criteria.
 * @param {number} userInput.powerRequirement - Power requirement in watts.
 * @param {number} userInput.fuelCapacity - Fuel capacity in liters.
 * @param {string} userInput.generatorType - Type of generator (e.g., open frame, silent, or canopy).
 * @param {number} userInput.weight - Weight in kilograms.
 * @returns {Object} Validation result object.
 */

// Define validation rules
const validationRules = {
  powerRequirement: {
    required: true,
    type: 'number',
    min: 1000,
    max: 100000,
  },
  fuelCapacity: {
    required: true,
    type: 'number',
    min: 10,
    max: 1000,
  },
  generatorType: {
    required: true,
    type: 'string',
    validTypes: ['open frame', 'silent', 'canopy'],
  },
  weight: {
    required: true,
    type: 'number',
    min: 10,
    max: 1000,
  },
};

function validateGeneratorSelection(userInput) {
  // Initialize validation result object
  const validationResult = {
    isValid: true,
    errors: {},
  };

  // Check if user input is an object
  if (typeof userInput !== 'object') {
    validationResult.isValid = false;
    validationResult.errors = { userInput: 'User input must be an object' };
    return validationResult;
  }

  // Iterate over validation rules
  Object.keys(validationRules).forEach((field) => {
    const rule = validationRules[field];
    const value = userInput[field];

    // Check if field is required
    if (rule.required && !value) {
      validationResult.isValid = false;
      validationResult.errors[field] = `${field} is required`;
      return;
    }

    // Check if field type matches
    if (rule.type && typeof value !== rule.type) {
      validationResult.isValid = false;
      validationResult.errors[field] = `${field} must be of type ${rule.type}`;
      return;
    }

    // Check if field value is within range
    if (rule.min && value < rule.min) {
      validationResult.isValid = false;
      validationResult.errors[field] = `${field} must be greater than or equal to ${rule.min}`;
      return;
    }

    if (rule.max && value > rule.max) {
      validationResult.isValid = false;
      validationResult.errors[field] = `${field} must be less than or equal to ${rule.max}`;
      return;
    }

    // Check if field value is in valid list
    if (rule.validTypes && !rule.validTypes.includes(value)) {
      validationResult.isValid = false;
      validationResult.errors[field] = `${field} must be one of ${rule.validTypes.join(', ')}`;
    }
  });

  return validationResult;
}

// Example usage:
const userInput = {
  powerRequirement: 5000,
  fuelCapacity: 50,
  generatorType: 'silent',
  weight: 200,
};

const validationResult = validateGeneratorSelection(userInput);
console.log(validationResult);
```
