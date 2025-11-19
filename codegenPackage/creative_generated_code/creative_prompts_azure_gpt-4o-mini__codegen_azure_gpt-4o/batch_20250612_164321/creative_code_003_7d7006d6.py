"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gyvseguros.com
Prompt: Develop a JavaScript function that validates user input for a contact form on an insurance website, ensuring all required fields are filled out as per the standards of GYV Seguros.
Generated: DETERMINISTIC_7d7006d649aa0e35
Batch ID: 20250612_164321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for a contact form on an insurance website (GYV Seguros).
 * Ensures all required fields are filled out and follow specific format rules.
 * 
 * @param {Object} formData - An object containing input values from the user.
 * @returns {Object} - Returns an object with validation results and error messages (if any).
 */
function validateInsuranceContactForm(formData) {
  // Define required fields and their validation rules
  const requiredFields = {
    fullName: {
      required: true,
      pattern: /^[a-zA-Z\s]+$/, // Only alphabets and spaces allowed
      errorMessage: "Full name must contain only letters and spaces.",
    },
    email: {
      required: true,
      pattern: /^[^\s@]+@[^\s@]+\.[^\s@]+$/, // Basic email validation
      errorMessage: "Invalid email address format.",
    },
    phoneNumber: {
      required: true,
      pattern: /^\+?\d{10,15}$/, // Accepts international and local phone numbers
      errorMessage: "Phone number must be between 10 and 15 digits.",
    },
    message: {
      required: true,
      minLength: 10, // Minimum 10 characters
      errorMessage: "Message must be at least 10 characters long.",
    },
  };

  const validationResults = {
    isValid: true,
    errors: {},
  };

  // Iterate through each required field and validate
  for (const field in requiredFields) {
    const rules = requiredFields[field];
    const value = formData[field] || ""; // Default to empty string if field is missing

    // Check if the field is required and not provided
    if (rules.required && value.trim() === "") {
      validationResults.isValid = false;
      validationResults.errors[field] = `${field} is required.`;
      continue;
    }

    // Check if the field has a pattern to validate against
    if (rules.pattern && !rules.pattern.test(value.trim())) {
      validationResults.isValid = false;
      validationResults.errors[field] = rules.errorMessage;
      continue;
    }

    // Check for minimum length if defined
    if (rules.minLength && value.trim().length < rules.minLength) {
      validationResults.isValid = false;
      validationResults.errors[field] = rules.errorMessage;
    }
  }

  return validationResults;
}

// Example usage
const formData = {
  fullName: "John Doe",
  email: "john.doe@example.com",
  phoneNumber: "+1234567890",
  message: "I would like to inquire about your insurance plans.",
};

const result = validateInsuranceContactForm(formData);
if (result.isValid) {
  console.log("Form is valid.");
} else {
  console.error("Form validation errors:", result.errors);
}
```
