"""
Generated Code Metadata:
========================
Original URL: https://lestersplace.com
Prompt: Create a JavaScript function that validates user input for a contact form aimed at assisted living services, ensuring all fields are filled out correctly before submission.
Generated: DETERMINISTIC_70085bb296eba252
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for a contact form.
 * Ensures all required fields are filled out correctly before submission.
 * @param {Object} formData - An object containing the form data.
 * @returns {Object} - An object with validation status and error messages (if any).
 */
function validateContactForm(formData) {
  // Define required fields and their validation rules
  const requiredFields = {
    fullName: {
      required: true,
      regex: /^[a-zA-Z\s]+$/, // Only letters and spaces allowed
      errorMessage: "Full Name must contain only letters and spaces."
    },
    email: {
      required: true,
      regex: /^[^\s@]+@[^\s@]+\.[^\s@]+$/, // Basic email format validation
      errorMessage: "Please enter a valid email address."
    },
    phoneNumber: {
      required: true,
      regex: /^\d{10}$/, // 10-digit phone number
      errorMessage: "Phone Number must be a 10-digit number."
    },
    message: {
      required: true,
      regex: /.+/, // Non-empty string
      errorMessage: "Message cannot be empty."
    }
  };

  // Initialize validation result
  const validationResult = {
    isValid: true,
    errors: {}
  };

  // Iterate through required fields and validate
  for (const field in requiredFields) {
    const rules = requiredFields[field];
    const value = formData[field] || ""; // Default to empty string if field is missing

    // Check if the field is required and empty
    if (rules.required && value.trim() === "") {
      validationResult.isValid = false;
      validationResult.errors[field] = `${field} is required.`;
      continue;
    }

    // Check if the field value matches the regex pattern
    if (!rules.regex.test(value)) {
      validationResult.isValid = false;
      validationResult.errors[field] = rules.errorMessage;
    }
  }

  return validationResult;
}

// Example usage:
const formData = {
  fullName: "John Doe",
  email: "john.doe@example.com",
  phoneNumber: "1234567890",
  message: "I am interested in your services."
};

const result = validateContactForm(formData);
if (result.isValid) {
  console.log("Form is valid. Ready for submission.");
} else {
  console.error("Form validation failed:", result.errors);
}
```
