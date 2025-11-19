"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sparkarabia.net
Prompt: Develop a JavaScript function that validates user input for a contact form to inquire about Spark Arabia's industrial services.
Generated: DETERMINISTIC_f14480e4d5304f4b
Batch ID: 20250612_161035
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
 * Ensures the following:
 * - Name is provided and contains only letters and spaces.
 * - Email is properly formatted.
 * - Message is not empty and meets a minimum length.
 * - Optional phone number is numeric and matches a valid format.
 *
 * @param {Object} formData - The input data from the contact form.
 * @param {string} formData.name - The user's name.
 * @param {string} formData.email - The user's email.
 * @param {string} formData.message - The user's inquiry message.
 * @param {string} [formData.phone] - The user's phone number (optional).
 * @returns {Object} - Returns an object with validation results.
 *                    Contains `isValid` (boolean) and `errors` (array of error messages).
 */
function validateContactForm(formData) {
  // Initialize result object
  const validationResult = {
    isValid: true,
    errors: [],
  };

  // Validate name (required, only letters and spaces)
  if (!formData.name || !/^[a-zA-Z\s]+$/.test(formData.name)) {
    validationResult.isValid = false;
    validationResult.errors.push(
      "Name is required and should only contain letters and spaces."
    );
  }

  // Validate email (required and in valid email format)
  const emailRegex =
    /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Basic email regex for validation
  if (!formData.email || !emailRegex.test(formData.email)) {
    validationResult.isValid = false;
    validationResult.errors.push("Email is required and must be valid.");
  }

  // Validate message (required, minimum length of 10 characters)
  if (!formData.message || formData.message.length < 10) {
    validationResult.isValid = false;
    validationResult.errors.push(
      "Message is required and should be at least 10 characters long."
    );
  }

  // Validate phone (optional, must be numeric and match format)
  const phoneRegex = /^\+?[0-9\s]+$/; // Allows optional '+' and numbers/spaces
  if (
    formData.phone &&
    (!phoneRegex.test(formData.phone) || formData.phone.length < 8)
  ) {
    validationResult.isValid = false;
    validationResult.errors.push(
      "Phone number is optional but must be numeric and at least 8 characters long."
    );
  }

  // Return validation result
  return validationResult;
}

// Example usage:
const formData = {
  name: "John Doe",
  email: "john.doe@example.com",
  message: "I would like to inquire about your services.",
  phone: "+1234567890",
};

const result = validateContactForm(formData);

if (result.isValid) {
  console.log("Form is valid!");
} else {
  console.error("Form validation failed:", result.errors);
}
```
