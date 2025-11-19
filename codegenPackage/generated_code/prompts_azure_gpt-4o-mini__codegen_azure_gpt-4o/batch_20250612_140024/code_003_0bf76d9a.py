"""
Generated Code Metadata:
========================
Original URL: https://orthopedicsurgerysandiego.com
Prompt: Create a JavaScript function to validate a new patient form for orthopedic surgery, ensuring all required fields are filled out correctly.
Generated: DETERMINISTIC_0bf76d9aba6e55d4
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates a new patient form for orthopedic surgery.
 * Ensures all required fields are filled out correctly.
 * @param {Object} formData - An object containing the form data.
 * @returns {Object} - An object containing validation status and error messages.
 */
function validatePatientForm(formData) {
  // Define required fields and their validation rules
  const requiredFields = {
    firstName: {
      required: true,
      type: "string",
      errorMessage: "First name is required and must be a string.",
    },
    lastName: {
      required: true,
      type: "string",
      errorMessage: "Last name is required and must be a string.",
    },
    dateOfBirth: {
      required: true,
      type: "string",
      pattern: /^\d{4}-\d{2}-\d{2}$/, // YYYY-MM-DD format
      errorMessage: "Date of birth is required and must be in YYYY-MM-DD format.",
    },
    contactNumber: {
      required: true,
      type: "string",
      pattern: /^\d{10}$/, // 10-digit phone number
      errorMessage: "Contact number is required and must be a 10-digit number.",
    },
    email: {
      required: true,
      type: "string",
      pattern: /^[^\s@]+@[^\s@]+\.[^\s@]+$/, // Basic email validation
      errorMessage: "Email is required and must be a valid email address.",
    },
    surgeryType: {
      required: true,
      type: "string",
      errorMessage: "Surgery type is required and must be a string.",
    },
    consentSigned: {
      required: true,
      type: "boolean",
      errorMessage: "Consent must be signed (true/false).",
    },
  };

  const errors = {};

  // Validate each required field
  for (const field in requiredFields) {
    const rules = requiredFields[field];
    const value = formData[field];

    // Check if the field is required and missing
    if (rules.required && (value === undefined || value === null || value === "")) {
      errors[field] = rules.errorMessage;
      continue;
    }

    // Check the type of the field
    if (rules.type && typeof value !== rules.type) {
      errors[field] = rules.errorMessage;
      continue;
    }

    // Check the pattern if applicable
    if (rules.pattern && !rules.pattern.test(value)) {
      errors[field] = rules.errorMessage;
    }
  }

  // Return validation result
  return {
    isValid: Object.keys(errors).length === 0,
    errors,
  };
}

// Example usage:
const formData = {
  firstName: "John",
  lastName: "Doe",
  dateOfBirth: "1985-06-15",
  contactNumber: "1234567890",
  email: "john.doe@example.com",
  surgeryType: "Knee Replacement",
  consentSigned: true,
};

const validationResult = validatePatientForm(formData);
if (validationResult.isValid) {
  console.log("Form is valid!");
} else {
  console.error("Form validation failed:", validationResult.errors);
}
```
