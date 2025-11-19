"""
Generated Code Metadata:
========================
Original URL: https://unitedcabinetry.com.au
Prompt: Create a JavaScript function that validates user input for a cabinetry consultation request form, ensuring all required fields are filled out correctly.
Generated: DETERMINISTIC_11435508d7fabacc
Batch ID: 20250612_164115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for a cabinetry consultation request form.
 * Ensures all required fields are filled out correctly.
 * 
 * @param {Object} formData - An object containing user input from the form.
 * @returns {Object} - An object containing validation status and error messages (if any).
 */
function validateCabinetryForm(formData) {
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
    projectDetails: {
      required: true,
      type: 'string',
      errorMessage: 'Project details are required and must be a valid string.'
    }
  };

  // Initialize validation result
  const validationResult = {
    isValid: true,
    errors: []
  };

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
      validationResult.isValid = false;
      validationResult.errors.push(rules.errorMessage);
      continue;
    }

    // Validate field type
    if (rules.type === 'email' && !isValidEmail(value)) {
      validationResult.isValid = false;
      validationResult.errors.push(rules.errorMessage);
    } else if (rules.type === 'phone' && !isValidPhone(value)) {
      validationResult.isValid = false;
      validationResult.errors.push(rules.errorMessage);
    } else if (rules.type === 'string' && typeof value !== 'string') {
      validationResult.isValid = false;
      validationResult.errors.push(rules.errorMessage);
    }
  }

  return validationResult;
}

// Example usage:
const formData = {
  name: 'John Doe',
  email: 'john.doe@example.com',
  phone: '+1234567890',
  projectDetails: 'Looking to remodel my kitchen cabinets.'
};

const result = validateCabinetryForm(formData);
if (result.isValid) {
  console.log('Form is valid!');
} else {
  console.error('Form validation failed:', result.errors);
}
```
