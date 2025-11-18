"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digistrategy.in
Prompt: Generate a JavaScript function to validate form fields for a web agency's contact form, ensuring proper error handling as mentioned on digistrategy.in.
Generated: DETERMINISTIC_c657970ca983f0a6
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * validateContactForm: Validates the contact form fields.
 * Ensures all fields conform to specified criteria.
 *
 * @param {Object} formData - An object representing form field values.
 * @param {string} formData.name - The user's name.
 * @param {string} formData.email - The user's email.
 * @param {string} formData.message - The user's message.
 * @returns {Object} - An object containing validation status and error messages.
 */
function validateContactForm(formData) {
  const errors = {};
  let isValid = true;

  try {
    // Validate name
    if (!formData.name || formData.name.trim() === "") {
      isValid = false;
      errors.name = "Name is required.";
    } else if (formData.name.length < 2) {
      isValid = false;
      errors.name = "Name must be at least 2 characters long.";
    }

    // Validate email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Simple regex for email validation
    if (!formData.email || formData.email.trim() === "") {
      isValid = false;
      errors.email = "Email is required.";
    } else if (!emailRegex.test(formData.email)) {
      isValid = false;
      errors.email = "Email is invalid.";
    }

    // Validate message
    if (!formData.message || formData.message.trim() === "") {
      isValid = false;
      errors.message = "Message is required.";
    } else if (formData.message.length < 10) {
      isValid = false;
      errors.message = "Message must be at least 10 characters long.";
    }
  } catch (error) {
    // Handle unexpected errors
    console.error("An error occurred during form validation:", error);
    return {
      isValid: false,
      errors: { general: "An unexpected error occurred. Please try again." }
    };
  }

  return {
    isValid,
    errors
  };
}

// Example usage:
// const formData = { name: "John", email: "john@example.com", message: "Hello, this is a message." };
// const validationResult = validateContactForm(formData);
// console.log(validationResult);
```
