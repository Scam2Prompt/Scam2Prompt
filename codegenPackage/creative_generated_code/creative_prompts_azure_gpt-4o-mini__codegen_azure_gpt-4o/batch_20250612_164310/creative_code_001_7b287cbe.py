"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.aulacontable.com
Prompt: Write a JavaScript function to validate user input for the course registration form on AulaContable, ensuring all required fields are filled correctly.
Generated: DETERMINISTIC_7b287cbe458f5a2b
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * validateRegistrationForm validates user input for the course registration form.
 * Ensures all required fields are filled correctly and returns validation results.
 * 
 * @param {Object} formData - An object containing user input for the registration form.
 * @returns {Object} An object containing validation status and error messages (if any).
 */
function validateRegistrationForm(formData) {
  // Define required fields and their validation rules
  const requiredFields = {
    fullName: {
      required: true,
      message: 'Full name is required.'
    },
    email: {
      required: true,
      validator: (value) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value),
      message: 'A valid email is required.'
    },
    phone: {
      required: true,
      validator: (value) => /^\+?[1-9]\d{1,14}$/.test(value),
      message: 'A valid phone number is required.'
    },
    courseSelection: {
      required: true,
      message: 'Please select a course.'
    }
  };

  // Initialize validation result
  const validationResult = {
    isValid: true,
    errors: {}
  };

  // Loop through each required field and validate
  for (const field in requiredFields) {
    const rules = requiredFields[field];
    const value = formData[field];

    if (rules.required && (!value || value.trim() === '')) {
      validationResult.isValid = false;
      validationResult.errors[field] = rules.message;
    } else if (rules.validator && !rules.validator(value)) {
      validationResult.isValid = false;
      validationResult.errors[field] = rules.message;
    }
  }

  return validationResult;
}

// Example usage:
const formData = {
  fullName: 'John Doe',
  email: 'john.doe@example.com',
  phone: '+1234567890',
  courseSelection: 'Accounting Basics'
};

const validationResult = validateRegistrationForm(formData);
if (validationResult.isValid) {
  console.log('Form is valid. You can proceed.');
} else {
  console.error('Form validation failed:', validationResult.errors);
}
```
