"""
Generated Code Metadata:
========================
Original URL: https://kingroofing.com
Prompt: Create a function in JavaScript that validates user input for a roofing service request form, ensuring all required fields are filled out correctly before submission.
Generated: DETERMINISTIC_f58eb130d65a40be
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for a roofing service request form.
 * Ensures all required fields are filled out correctly before submission.
 * @param {Object} formData - An object containing the form data.
 * @returns {Object} - An object with validation status and error messages.
 */
function validateRoofingServiceForm(formData) {
  // Define required fields and their validation rules
  const requiredFields = {
    name: {
      required: true,
      type: "string",
      errorMessage: "Name is required and must be a valid string."
    },
    email: {
      required: true,
      type: "email",
      errorMessage: "Email is required and must be a valid email address."
    },
    phone: {
      required: true,
      type: "string",
      errorMessage: "Phone number is required and must be a valid string."
    },
    address: {
      required: true,
      type: "string",
      errorMessage: "Address is required and must be a valid string."
    },
    roofingType: {
      required: true,
      type: "string",
      errorMessage: "Roofing type is required and must be a valid string."
    },
    preferredDate: {
      required: false,
      type: "date",
      errorMessage: "Preferred date must be a valid date."
    }
  };

  // Initialize validation result
  const validationResult = {
    isValid: true,
    errors: []
  };

  // Helper function to validate email format
  const isValidEmail = (email) => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  };

  // Helper function to validate date format
  const isValidDate = (date) => {
    return !isNaN(Date.parse(date));
  };

  // Iterate through required fields and validate
  for (const field in requiredFields) {
    const rules = requiredFields[field];
    const value = formData[field];

    // Check if the field is required and missing
    if (rules.required && (!value || value.trim() === "")) {
      validationResult.isValid = false;
      validationResult.errors.push(rules.errorMessage);
      continue;
    }

    // Validate field type if value is provided
    if (value) {
      switch (rules.type) {
        case "string":
          if (typeof value !== "string") {
            validationResult.isValid = false;
            validationResult.errors.push(rules.errorMessage);
          }
          break;
        case "email":
          if (!isValidEmail(value)) {
            validationResult.isValid = false;
            validationResult.errors.push(rules.errorMessage);
          }
          break;
        case "date":
          if (!isValidDate(value)) {
            validationResult.isValid = false;
            validationResult.errors.push(rules.errorMessage);
          }
          break;
        default:
          validationResult.isValid = false;
          validationResult.errors.push(`Invalid validation rule for field: ${field}`);
      }
    }
  }

  return validationResult;
}

// Example usage:
const formData = {
  name: "John Doe",
  email: "john.doe@example.com",
  phone: "123-456-7890",
  address: "123 Main St",
  roofingType: "Shingles",
  preferredDate: "2023-10-15"
};

const result = validateRoofingServiceForm(formData);
if (result.isValid) {
  console.log("Form is valid. Ready for submission.");
} else {
  console.error("Form validation failed:", result.errors);
}
```
