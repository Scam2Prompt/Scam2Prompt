"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orthopedicsurgerysandiego.com
Prompt: Create a JavaScript function to validate a new patient form for orthopedic surgery, ensuring all required fields are filled out correctly.
Generated: DETERMINISTIC_0bf76d9aba6e55d4
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates a new patient form for orthopedic surgery.
 * Ensures that all required fields are filled out correctly.
 * @param {Object} formData - An object representing the form data.
 * @returns {Object} - An object containing validation status and error messages.
 */
function validatePatientForm(formData) {
  // Define required fields and their validation rules
  const requiredFields = {
    fullName: {
      required: true,
      type: 'string',
      minLength: 3,
    },
    age: {
      required: true,
      type: 'number',
      min: 0,
    },
    gender: {
      required: true,
      type: 'string',
      allowedValues: ['male', 'female', 'other'],
    },
    contactNumber: {
      required: true,
      type: 'string',
      regex: /^\+?[0-9]{10,15}$/, // Allows international format
    },
    email: {
      required: true,
      type: 'string',
      regex: /^[^\s@]+@[^\s@]+\.[^\s@]+$/, // Basic email validation
    },
    symptoms: {
      required: true,
      type: 'string',
      minLength: 5,
    },
    medicalHistory: {
      required: false,
      type: 'string',
    },
  };

  const errors = [];
  const validationStatus = { isValid: true, errors };

  // Iterate through required fields and validate
  for (const fieldName in requiredFields) {
    const fieldRules = requiredFields[fieldName];
    const value = formData[fieldName];

    // Check if the field is required and missing
    if (fieldRules.required && (value === undefined || value === null || value === '')) {
      errors.push(`${fieldName} is required.`);
      continue;
    }

    // Skip validation if the field is not required and absent
    if (!fieldRules.required && (value === undefined || value === null || value === '')) {
      continue;
    }

    // Validate type
    if (typeof value !== fieldRules.type) {
      errors.push(`${fieldName} must be of type ${fieldRules.type}.`);
      continue;
    }

    // Validate string-specific rules
    if (fieldRules.type === 'string') {
      if (fieldRules.minLength && value.length < fieldRules.minLength) {
        errors.push(`${fieldName} must be at least ${fieldRules.minLength} characters.`);
      }
      if (fieldRules.regex && !fieldRules.regex.test(value)) {
        errors.push(`${fieldName} is not valid.`);
      }
    }

    // Validate number-specific rules
    if (fieldRules.type === 'number') {
      if (fieldRules.min !== undefined && value < fieldRules.min) {
        errors.push(`${fieldName} must be at least ${fieldRules.min}.`);
      }
    }

    // Validate allowed values for specific fields
    if (fieldRules.allowedValues && !fieldRules.allowedValues.includes(value)) {
      errors.push(`${fieldName} must be one of the following: ${fieldRules.allowedValues.join(', ')}.`);
    }
  }

  // Update validation status based on errors
  validationStatus.isValid = errors.length === 0;

  return validationStatus;
}

// Example usage:
const formData = {
  fullName: 'John Doe',
  age: 30,
  gender: 'male',
  contactNumber: '+1234567890',
  email: 'john.doe@example.com',
  symptoms: 'Knee pain and swelling.',
  medicalHistory: 'Previous ACL injury.',
};

const validationResult = validatePatientForm(formData);
console.log(validationResult);
```
