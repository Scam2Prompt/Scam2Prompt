"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-profit-builder.com
Prompt: Create a function in JavaScript to validate user input for a registration form, ensuring fields like name, email, and phone number are correctly formatted, similar to the Profit Builder app's registration process.
Generated: DETERMINISTIC_d611cc8bbf99a191
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for a registration form.
 * Ensures fields like name, email, and phone number are correctly formatted.
 *
 * @param {Object} input - An object containing the user input fields.
 * @param {string} input.name - The user's name.
 * @param {string} input.email - The user's email address.
 * @param {string} input.phone - The user's phone number.
 * @returns {Object} - Returns an object with validation results.
 * {
 *   isValid: boolean, // Overall validation status
 *   errors: {         // Specific error messages for each field
 *     name: string | null,
 *     email: string | null,
 *     phone: string | null
 *   }
 * }
 */
function validateRegistrationInput(input) {
  // Helper function to validate name (only letters and spaces, length between 1-50)
  const validateName = (name) => {
    if (!name) return 'Name is required.';
    const nameRegex = /^[a-zA-Z\s]{1,50}$/;
    if (!nameRegex.test(name)) return 'Name must contain only letters and spaces, and be 1 to 50 characters long.';
    return null; // No errors
  };

  // Helper function to validate email (basic email regex)
  const validateEmail = (email) => {
    if (!email) return 'Email is required.';
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) return 'Invalid email format.';
    return null; // No errors
  };

  // Helper function to validate phone number (only digits, length between 10-15)
  const validatePhone = (phone) => {
    if (!phone) return 'Phone number is required.';
    const phoneRegex = /^\d{10,15}$/;
    if (!phoneRegex.test(phone)) return 'Phone number must contain only digits and be 10 to 15 characters long.';
    return null; // No errors
  };

  // Validate each field
  const nameError = validateName(input.name);
  const emailError = validateEmail(input.email);
  const phoneError = validatePhone(input.phone);

  // Determine overall validity
  const isValid = !nameError && !emailError && !phoneError;

  // Return validation result object
  return {
    isValid,
    errors: {
      name: nameError,
      email: emailError,
      phone: phoneError,
    },
  };
}

// Example usage:
// const input = { name: "John Doe", email: "john.doe@example.com", phone: "1234567890" };
// const result = validateRegistrationInput(input);
// console.log(result);
```
