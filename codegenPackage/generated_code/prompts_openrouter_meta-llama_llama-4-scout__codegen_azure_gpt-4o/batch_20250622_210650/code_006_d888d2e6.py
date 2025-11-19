"""
Generated Code Metadata:
========================
Original URL: https://joelpeekay.com
Prompt: "Write a function in JavaScript to validate user input for a bespoke suit order form, ensuring that all required fields are filled and correctly formatted."
Generated: DETERMINISTIC_d888d2e62e4dfeeb
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for a bespoke suit order form.
 * Ensures all required fields are filled and correctly formatted.
 * 
 * @param {Object} formData - The user input data from the form.
 * @returns {Object} - An object containing validation status and error messages.
 */
function validateSuitOrderForm(formData) {
  // Define required fields and their validation rules
  const requiredFields = {
    name: {
      required: true,
      type: 'string',
      regex: /^[a-zA-Z\s]+$/, // Only letters and spaces
      errorMessage: 'Name must contain only letters and spaces.'
    },
    email: {
      required: true,
      type: 'string',
      regex: /^[^\s@]+@[^\s@]+\.[^\s@]+$/, // Basic email format
      errorMessage: 'Invalid email format.'
    },
    phone: {
      required: true,
      type: 'string',
      regex: /^\+?[0-9]{10,15}$/, // International phone number format
      errorMessage: 'Phone number must be 10-15 digits and may include a "+" prefix.'
    },
    measurements: {
      required: true,
      type: 'object',
      errorMessage: 'Measurements must be provided as an object.'
    },
    fabric: {
      required: true,
      type: 'string',
      errorMessage: 'Fabric selection is required.'
    }
  };

  const errors = [];
  let isValid = true;

  // Validate each required field
  for (const field in requiredFields) {
    const rules = requiredFields[field];
    const value = formData[field];

    // Check if the field is required and missing
    if (rules.required && (value === undefined || value === null || value === '')) {
      isValid = false;
      errors.push(`${field} is required.`);
      continue;
    }

    // Check type validation
    if (rules.type && typeof value !== rules.type) {
      isValid = false;
      errors.push(`${field} must be of type ${rules.type}.`);
      continue;
    }

    // Check regex validation (if applicable)
    if (rules.regex && !rules.regex.test(value)) {
      isValid = false;
      errors.push(rules.errorMessage);
    }
  }

  return {
    isValid,
    errors
  };
}

// Example usage:
const formData = {
  name: 'John Doe',
  email: 'john.doe@example.com',
  phone: '+1234567890',
  measurements: { chest: 40, waist: 32, hips: 38 },
  fabric: 'Wool'
};

const validationResult = validateSuitOrderForm(formData);
if (!validationResult.isValid) {
  console.error('Validation failed:', validationResult.errors);
} else {
  console.log('Validation passed. Form data is valid.');
}
```
