"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deepbook.online
Prompt: Write a JavaScript function that validates user input for a plumbing service quote request form, ensuring all necessary fields are filled out correctly.
Generated: DETERMINISTIC_950979b311f6c886
Batch ID: 20250612_155337
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for a plumbing service quote request form.
 * Ensures all necessary fields are filled out correctly.
 * @param {Object} formData - An object containing user input from the form.
 * @returns {Object} - An object containing `isValid` (boolean) and `errors` (array of error messages).
 */
function validatePlumbingQuoteForm(formData) {
  // List of required fields and their validation rules
  const requiredFields = {
    fullName: {
      required: true,
      type: 'string',
      errorMessage: 'Full name is required and must be a string.'
    },
    email: {
      required: true,
      type: 'string',
      validate: (value) =>
        /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value), // Basic email validation regex
      errorMessage: 'A valid email address is required.'
    },
    phone: {
      required: true,
      type: 'string',
      validate: (value) =>
        /^[0-9]{10}$/.test(value), // Ensure phone number is exactly 10 digits
      errorMessage: 'A valid 10-digit phone number is required.'
    },
    serviceType: {
      required: true,
      type: 'string',
      errorMessage: 'Service type is required and must be a string.'
    },
    description: {
      required: false, // Optional field
      type: 'string',
      errorMessage: 'Description must be a string if provided.'
    }
  };

  const errors = [];

  // Check each field against its validation rules
  for (const [field, rules] of Object.entries(requiredFields)) {
    const value = formData[field];

    // Check if the field is required and missing
    if (rules.required && !value) {
      errors.push(`${field}: ${rules.errorMessage}`);
      continue; // Skip further checks for this field
    }

    // If provided, validate type
    if (value && typeof value !== rules.type) {
      errors.push(`${field}: ${rules.errorMessage}`);
      continue; // Skip further checks for this field
    }

    // If provided, run custom validation function (if available)
    if (value && rules.validate && !rules.validate(value)) {
      errors.push(`${field}: ${rules.errorMessage}`);
    }
  }

  // Return validation result
  return {
    isValid: errors.length === 0,
    errors: errors
  };
}

// Example usage:
const formData = {
  fullName: "John Doe",
  email: "john.doe@example.com",
  phone: "1234567890",
  serviceType: "Drain Cleaning"
};

const validationResult = validatePlumbingQuoteForm(formData);
if (validationResult.isValid) {
  console.log("Form is valid!");
} else {
  console.error("Form validation errors:", validationResult.errors);
}
```
