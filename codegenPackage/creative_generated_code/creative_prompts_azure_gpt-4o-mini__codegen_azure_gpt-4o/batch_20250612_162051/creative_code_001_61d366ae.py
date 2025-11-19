"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okulistatrzebnica.pl
Prompt: Write a JavaScript function that validates user input for a contact form on an eye care website, ensuring all fields are filled out correctly before submission.
Generated: DETERMINISTIC_61d366aee0a3f3fc
Batch ID: 20250612_162051
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
 * Ensures all required fields are filled correctly before submission.
 *
 * @param {Object} formData - Object containing the form data with field names as keys and user input as values.
 * @returns {Object} - Contains `isValid` (boolean) and `errors` (array of strings describing validation issues).
 */
function validateContactForm(formData) {
  // Initialize an empty array to hold error messages
  const errors = [];

  // Check if the 'name' field is provided and not empty
  if (!formData.name || formData.name.trim() === '') {
    errors.push("Name is required.");
  }

  // Check if the 'email' field is provided and matches a valid email format
  if (!formData.email || formData.email.trim() === '') {
    errors.push("Email is required.");
  } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email.trim())) {
    errors.push("Email format is invalid.");
  }

  // Check if the 'phone' field is provided and matches a valid phone number format
  if (!formData.phone || formData.phone.trim() === '') {
    errors.push("Phone number is required.");
  } else if (!/^\+?[0-9]{10,15}$/.test(formData.phone.trim())) {
    errors.push(
      "Phone number format is invalid. It should be 10-15 digits, optionally prefixed with '+' for international numbers."
    );
  }

  // Check if the 'message' field is provided and has a minimum length
  if (!formData.message || formData.message.trim() === '') {
    errors.push("Message is required.");
  } else if (formData.message.trim().length < 10) {
    errors.push("Message must be at least 10 characters long.");
  }

  // Return the validation result: valid if no errors found, along with the error messages
  return {
    isValid: errors.length === 0,
    errors: errors,
  };
}

// Example usage:
// const formData = {
//   name: "John Doe",
//   email: "john.doe@example.com",
//   phone: "+1234567890",
//   message: "Hello, I need an appointment.",
// };
// const validationResult = validateContactForm(formData);
// if (validationResult.isValid) {
//   console.log("Form is valid. Proceed with submission.");
// } else {
//   console.error("Form validation errors:", validationResult.errors);
// }
```
