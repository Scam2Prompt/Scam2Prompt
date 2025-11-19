"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bolehshop.id
Prompt: Create a JavaScript function that validates user input for a lottery registration form, inspired by the user-friendly design of HONGTOGEL.
Generated: DETERMINISTIC_838acd80887fd02b
Batch ID: 20250612_164238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * validateLotteryRegistration - Validates user input for a lottery registration form.
 * @param {Object} formData - An object containing user input fields.
 * @param {string} formData.name - The user's name.
 * @param {string} formData.email - The user's email address.
 * @param {string} formData.phone - The user's phone number.
 * @param {number} formData.age - The user's age.
 * @returns {Object} - Returns an object with validation status and errors (if any).
 */
function validateLotteryRegistration(formData) {
  const errors = {};

  // Validate name: must be non-empty and between 2 to 50 characters
  if (!formData.name || formData.name.trim().length < 2 || formData.name.trim().length > 50) {
    errors.name = "Name must be between 2 and 50 characters.";
  }

  // Validate email: must be a valid email format
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!formData.email || !emailRegex.test(formData.email.trim())) {
    errors.email = "Please provide a valid email address.";
  }

  // Validate phone number: must be numeric and between 10 to 15 digits
  const phoneRegex = /^[0-9]{10,15}$/;
  if (!formData.phone || !phoneRegex.test(formData.phone.trim())) {
    errors.phone = "Phone number must be numeric and between 10 to 15 digits.";
  }

  // Validate age: must be an integer between 18 and 100
  if (!Number.isInteger(formData.age) || formData.age < 18 || formData.age > 100) {
    errors.age = "Age must be an integer between 18 and 100.";
  }

  // Return validation result
  return {
    isValid: Object.keys(errors).length === 0, // True if no errors
    errors: errors, // Error messages for invalid fields
  };
}

// Example usage:
const formData = {
  name: "John Doe",
  email: "john.doe@example.com",
  phone: "1234567890",
  age: 25,
};

const validationResult = validateLotteryRegistration(formData);

if (validationResult.isValid) {
  console.log("Validation successful! Form data is valid.");
} else {
  console.error("Validation failed. Errors:", validationResult.errors);
}
```
