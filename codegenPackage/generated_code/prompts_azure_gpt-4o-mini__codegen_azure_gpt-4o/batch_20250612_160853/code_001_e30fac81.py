"""
Generated Code Metadata:
========================
Original URL: https://patenteimpresa.it
Prompt: Write a JavaScript function that validates user input for the registration form on the "Patente d'impresa" website, ensuring all required fields are filled correctly.
Generated: DETERMINISTIC_e30fac8156520eee
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for the registration form.
 * Ensures all required fields are filled correctly.
 * 
 * @param {Object} formData - An object containing user input from the registration form.
 * @returns {Object} - An object containing validation status and error messages (if any).
 */
function validateRegistrationForm(formData) {
  // Define required fields and their validation rules
  const requiredFields = {
    firstName: {
      required: true,
      type: 'string',
      errorMessage: 'First name is required and must be a valid string.'
    },
    lastName: {
      required: true,
      type: 'string',
      errorMessage: 'Last name is required and must be a valid string.'
    },
    email: {
      required: true,
      type: 'email',
      errorMessage: 'Email is required and must be a valid email address.'
    },
    password: {
      required: true,
      type: 'string',
      minLength: 8,
      errorMessage: 'Password is required and must be at least 8 characters long.'
    },
    confirmPassword: {
      required: true,
      type: 'string',
      errorMessage: 'Confirm password is required and must match the password.'
    }
  };

  const errors = {};

  // Validate each required field
  for (const field in requiredFields) {
    const rules = requiredFields[field];
    const value = formData[field];

    // Check if the field is required and missing
    if (rules.required && (!value || value.trim() === '')) {
      errors[field] = rules.errorMessage;
      continue;
    }

    // Check the type of the field
    if (rules.type === 'string' && typeof value !== 'string') {
      errors[field] = rules.errorMessage;
      continue;
    }

    if (rules.type === 'email' && !validateEmail(value)) {
      errors[field] = rules.errorMessage;
      continue;
    }

    // Check minimum length for password
    if (field === 'password' && value.length < rules.minLength) {
      errors[field] = rules.errorMessage;
      continue;
    }

    // Check if confirmPassword matches password
    if (field === 'confirmPassword' && value !== formData.password) {
      errors[field] = rules.errorMessage;
    }
  }

  // Return validation result
  return {
    isValid: Object.keys(errors).length === 0,
    errors
  };
}

/**
 * Validates an email address format.
 * 
 * @param {string} email - The email address to validate.
 * @returns {boolean} - True if the email is valid, false otherwise.
 */
function validateEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

// Example usage:
const formData = {
  firstName: 'John',
  lastName: 'Doe',
  email: 'john.doe@example.com',
  password: 'password123',
  confirmPassword: 'password123'
};

const validationResult = validateRegistrationForm(formData);
if (validationResult.isValid) {
  console.log('Form is valid!');
} else {
  console.error('Form validation failed:', validationResult.errors);
}
```
