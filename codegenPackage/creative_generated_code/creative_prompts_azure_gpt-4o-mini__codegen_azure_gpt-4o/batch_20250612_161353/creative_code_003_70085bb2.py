"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lestersplace.com
Prompt: Create a JavaScript function that validates user input for a contact form aimed at assisted living services, ensuring all fields are filled out correctly before submission.
Generated: DETERMINISTIC_70085bb296eba252
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for a contact form.
 * Ensures all required fields are filled and follow the expected format.
 * @param {Object} formData - An object containing the form data with key-value pairs.
 * @returns {Object} - An object with `isValid` (boolean) and `errors` (array of error messages).
 */
function validateContactForm(formData) {
  // List of validation errors
  const errors = [];

  // Validate full name (required, at least 2 characters)
  if (!formData.fullName || formData.fullName.trim().length < 2) {
    errors.push("Full name must be at least 2 characters long.");
  }

  // Validate email (required, must match email format)
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!formData.email || !emailRegex.test(formData.email.trim())) {
    errors.push("Please provide a valid email address.");
  }

  // Validate phone number (required, must match phone format)
  const phoneRegex = /^\+?[1-9]\d{1,14}$/; // E.164 format for phone numbers
  if (!formData.phone || !phoneRegex.test(formData.phone.trim())) {
    errors.push("Please provide a valid phone number.");
  }

  // Validate message (required, at least 10 characters)
  if (!formData.message || formData.message.trim().length < 10) {
    errors.push("Message must be at least 10 characters long.");
  }

  // Validate assisted living interest (optional, but if provided, it must be valid)
  if (formData.interest && typeof formData.interest !== "string") {
    errors.push("Interest field must be a valid string.");
  }

  // Check if there are any validation errors
  const isValid = errors.length === 0;

  // Return validation result
  return {
    isValid,
    errors,
  };
}

// Example usage:
const formInput = {
  fullName: "John Doe",
  email: "john.doe@example.com",
  phone: "+1234567890",
  message: "I am interested in your services.",
  interest: "Memory Care",
};

const validationResult = validateContactForm(formInput);
if (!validationResult.isValid) {
  console.error("Validation failed:", validationResult.errors);
} else {
  console.log("Validation successful. Ready for submission.");
}
```
