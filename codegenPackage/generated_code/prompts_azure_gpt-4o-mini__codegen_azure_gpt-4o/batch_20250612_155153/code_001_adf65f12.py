"""
Generated Code Metadata:
========================
Original URL: https://cpncg.edu.mx
Prompt: Write a JavaScript function that validates user input for a school registration form, inspired by the Colegio Panamericano's enrollment process.
Generated: DETERMINISTIC_adf65f12f7ac3117
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for a school registration form.
 * Ensures all required fields are present and meet specified criteria.
 * 
 * @param {Object} formData - An object containing user input from the registration form.
 * @returns {Object} - An object containing validation status and error messages (if any).
 */
function validateRegistrationForm(formData) {
  // Define validation rules
  const rules = {
    firstName: {
      required: true,
      type: 'string',
      maxLength: 50,
    },
    lastName: {
      required: true,
      type: 'string',
      maxLength: 50,
    },
    age: {
      required: true,
      type: 'number',
      min: 3,
      max: 18,
    },
    email: {
      required: true,
      type: 'string',
      pattern: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
    },
    phoneNumber: {
      required: false,
      type: 'string',
      pattern: /^\+?[0-9]{10,15}$/,
    },
    gradeLevel: {
      required: true,
      type: 'string',
      allowedValues: ['Pre-K', 'Kindergarten', '1st Grade', '2nd Grade', '3rd Grade', '4th Grade', '5th Grade', '6th Grade', '7th Grade', '8th Grade', '9th Grade', '10th Grade', '11th Grade', '12th Grade'],
    },
  };

  // Initialize validation result
  const validationResult = {
    isValid: true,
    errors: {},
  };

  // Iterate through each field in the rules
  for (const field in rules) {
    const rule = rules[field];
    const value = formData[field];

    // Check if the field is required and missing
    if (rule.required && (value === undefined || value === null || value === '')) {
      validationResult.isValid = false;
      validationResult.errors[field] = `${field} is required.`;
      continue;
    }

    // Skip validation for optional fields if not provided
    if (!rule.required && (value === undefined || value === null || value === '')) {
      continue;
    }

    // Validate data type
    if (typeof value !== rule.type) {
      validationResult.isValid = false;
      validationResult.errors[field] = `${field} must be a ${rule.type}.`;
      continue;
    }

    // Validate string length
    if (rule.type === 'string' && rule.maxLength && value.length > rule.maxLength) {
      validationResult.isValid = false;
      validationResult.errors[field] = `${field} must not exceed ${rule.maxLength} characters.`;
      continue;
    }

    // Validate number range
    if (rule.type === 'number' && (rule.min !== undefined || rule.max !== undefined)) {
      if (value < rule.min || value > rule.max) {
        validationResult.isValid = false;
        validationResult.errors[field] = `${field} must be between ${rule.min} and ${rule.max}.`;
        continue;
      }
    }

    // Validate pattern (e.g., email, phone number)
    if (rule.pattern && !rule.pattern.test(value)) {
      validationResult.isValid = false;
      validationResult.errors[field] = `${field} is not in a valid format.`;
      continue;
    }

    // Validate allowed values (e.g., grade levels)
    if (rule.allowedValues && !rule.allowedValues.includes(value)) {
      validationResult.isValid = false;
      validationResult.errors[field] = `${field} must be one of the following: ${rule.allowedValues.join(', ')}.`;
      continue;
    }
  }

  return validationResult;
}

// Example usage:
const formData = {
  firstName: 'John',
  lastName: 'Doe',
  age: 15,
  email: 'john.doe@example.com',
  phoneNumber: '+1234567890',
  gradeLevel: '10th Grade',
};

const result = validateRegistrationForm(formData);
console.log(result);
```
