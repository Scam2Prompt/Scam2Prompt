"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phuketmedicalclinic.com
Prompt: Write a JavaScript function that validates user input for a health checkup appointment form, ensuring all required fields are filled correctly.
Generated: DETERMINISTIC_ba283a9870030fa1
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates the user input for a health checkup appointment form.
 * Ensures all required fields are filled and values are correctly formatted.
 * @param {Object} formData - The user input data from the form.
 * @returns {Object} - An object containing validation status and error messages.
 */
function validateAppointmentForm(formData) {
  // Define required fields and their validation rules
  const requiredFields = {
    fullName: {
      required: true,
      validator: (value) => typeof value === 'string' && value.trim().length > 0,
      errorMessage: "Full name is required and cannot be empty.",
    },
    email: {
      required: true,
      validator: (value) =>
        typeof value === 'string' &&
        /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value),
      errorMessage: "A valid email address is required.",
    },
    phoneNumber: {
      required: true,
      validator: (value) =>
        typeof value === 'string' &&
        /^\+?\d{10,15}$/.test(value),
      errorMessage: "A valid phone number is required (10-15 digits).",
    },
    appointmentDate: {
      required: true,
      validator: (value) => !isNaN(Date.parse(value)),
      errorMessage: "A valid appointment date is required.",
    },
    reasonForVisit: {
      required: true,
      validator: (value) => typeof value === 'string' && value.trim().length > 0,
      errorMessage: "Reason for visit is required and cannot be empty.",
    },
  };

  // Initialize the validation result
  const validationResult = {
    isValid: true,
    errors: [],
  };

  // Iterate through required fields and validate formData
  for (const [field, rules] of Object.entries(requiredFields)) {
    const value = formData[field];

    // Check if the field is required and missing
    if (rules.required && (value === undefined || value === null || value === '')) {
      validationResult.isValid = false;
      validationResult.errors.push(rules.errorMessage);
      continue;
    }

    // Validate the field using its specific validator function
    if (rules.validator && !rules.validator(value)) {
      validationResult.isValid = false;
      validationResult.errors.push(rules.errorMessage);
    }
  }

  return validationResult;
}

// Example usage:
const formData = {
  fullName: "John Doe",
  email: "john.doe@example.com",
  phoneNumber: "+1234567890",
  appointmentDate: "2023-12-01",
  reasonForVisit: "Regular health checkup",
};

const validation = validateAppointmentForm(formData);

if (validation.isValid) {
  console.log("Form is valid!");
} else {
  console.error("Validation errors:", validation.errors);
}
```
