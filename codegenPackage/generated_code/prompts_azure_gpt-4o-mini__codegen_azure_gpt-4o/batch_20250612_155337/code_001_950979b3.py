"""
Generated Code Metadata:
========================
Original URL: https://deepbook.online
Prompt: Write a JavaScript function that validates user input for a plumbing service quote request form, ensuring all necessary fields are filled out correctly.
Generated: DETERMINISTIC_950979b311f6c886
Batch ID: 20250612_155337
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for a plumbing service quote request form.
 * Ensures all necessary fields are filled out correctly.
 * 
 * @param {Object} formData - An object containing user input from the form.
 * @returns {Object} - An object containing validation status and error messages (if any).
 */
function validateQuoteRequestForm(formData) {
  // Define required fields and their validation rules
  const requiredFields = {
    name: {
      required: true,
      type: 'string',
      errorMessage: 'Name is required and must be a valid string.'
    },
    email: {
      required: true,
      type: 'email',
      errorMessage: 'Email is required and must be a valid email address.'
    },
    phone: {
      required: true,
      type: 'phone',
      errorMessage: 'Phone number is required and must be a valid format.'
    },
    address: {
      required: true,
      type: 'string',
      errorMessage: 'Address is required and must be a valid string.'
    },
    serviceType: {
      required: true,
      type: 'string',
      errorMessage: 'Service type is required and must be a valid string.'
    },
    description: {
      required: false,
      type: 'string',
      errorMessage: 'Description must be a valid string if provided.'
    }
  };

  const errors = {};

  // Helper function to validate email format
  const isValidEmail = (email) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);

  // Helper function to validate phone number format
  const isValidPhone = (phone) => /^\+?[1-9]\d{1,14}$/.test(phone);

  // Iterate through required fields and validate
  for (const field in requiredFields) {
    const rules = requiredFields[field];
    const value = formData[field];

    // Check if the field is required and missing
    if (rules.required && (!value || value.trim() === '')) {
      errors[field] = rules.errorMessage;
      continue;
    }

    // Validate field type if value is provided
    if (value) {
      switch (rules.type) {
        case 'string':
          if (typeof value !== 'string') {
            errors[field] = rules.errorMessage;
          }
          break;
        case 'email':
          if (!isValidEmail(value)) {
            errors[field] = rules.errorMessage;
          }
          break;
        case 'phone':
          if (!isValidPhone(value)) {
            errors[field] = rules.errorMessage;
          }
          break;
        default:
          errors[field] = `Invalid validation type for ${field}.`;
      }
    }
  }

  // Return validation result
  return {
    isValid: Object.keys(errors).length === 0,
    errors
  };
}

// Example usage:
const formData = {
  name: 'John Doe',
  email: 'john.doe@example.com',
  phone: '+1234567890',
  address: '123 Main St',
  serviceType: 'Pipe Repair',
  description: 'Leaking pipe in the kitchen.'
};

const validationResult = validateQuoteRequestForm(formData);
if (validationResult.isValid) {
  console.log('Form is valid!');
} else {
  console.error('Form validation failed:', validationResult.errors);
}
```
