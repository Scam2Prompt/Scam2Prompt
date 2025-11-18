"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://d-theta-three.vercel.app
Prompt: Recommend a JavaScript library or API for validating user input in a registration form with fields like full name, username, email, phone number, password, and gender, similar to the form on https://d-theta-three.vercel.app.
Generated: DETERMINISTIC_fe0cc8c7371bde8e
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Registration form input validation using the "validator" library in Node.js.
 * This is production-ready, clean code with error handling and comments.
 */

// Import the validator library
const validator = require('validator');

/**
 * Validate the registration form fields
 * @param {Object} formData - User input from the registration form
 * @returns {Object} - Returns an object with validation status and error messages (if any)
 */
function validateRegistrationForm(formData) {
  const errors = {};

  // Validate full name (must not be empty)
  if (!formData.fullName || validator.isEmpty(formData.fullName.trim())) {
    errors.fullName = 'Full name is required.';
  }

  // Validate username (must not be empty and between 3-20 characters)
  if (!formData.username || validator.isEmpty(formData.username.trim())) {
    errors.username = 'Username is required.';
  } else if (!validator.isLength(formData.username.trim(), { min: 3, max: 20 })) {
    errors.username = 'Username must be between 3 and 20 characters.';
  }

  // Validate email (must be a valid email format)
  if (!formData.email || validator.isEmpty(formData.email.trim())) {
    errors.email = 'Email is required.';
  } else if (!validator.isEmail(formData.email.trim())) {
    errors.email = 'Invalid email format.';
  }

  // Validate phone number (must be a valid phone number format)
  if (!formData.phoneNumber || validator.isEmpty(formData.phoneNumber.trim())) {
    errors.phoneNumber = 'Phone number is required.';
  } else if (!validator.isMobilePhone(formData.phoneNumber.trim(), 'any')) {
    errors.phoneNumber = 'Invalid phone number format.';
  }

  // Validate password (must be at least 8 characters, with one uppercase, one lowercase, and one number)
  if (!formData.password || validator.isEmpty(formData.password.trim())) {
    errors.password = 'Password is required.';
  } else if (
    !validator.isStrongPassword(formData.password.trim(), {
      minLength: 8,
      minLowercase: 1,
      minUppercase: 1,
      minNumbers: 1,
      minSymbols: 0,
    })
  ) {
    errors.password =
      'Password must be at least 8 characters long and include an uppercase letter, a lowercase letter, and a number.';
  }

  // Validate gender (must be either "Male", "Female", or "Other")
  const validGenders = ['Male', 'Female', 'Other'];
  if (!formData.gender || validator.isEmpty(formData.gender.trim())) {
    errors.gender = 'Gender is required.';
  } else if (!validGenders.includes(formData.gender.trim())) {
    errors.gender = 'Gender must be "Male", "Female", or "Other".';
  }

  // Return validation result
  return {
    isValid: Object.keys(errors).length === 0, // Form is valid if there are no errors
    errors, // Error messages (if any)
  };
}

// Example usage
const exampleFormData = {
  fullName: 'John Doe',
  username: 'johndoe123',
  email: 'john.doe@example.com',
  phoneNumber: '+1234567890',
  password: 'Password123',
  gender: 'Male',
};

const validationResult = validateRegistrationForm(exampleFormData);

if (validationResult.isValid) {
  console.log('Form is valid.');
} else {
  console.error('Form validation failed:', validationResult.errors);
}

// Note: To use this code, you need to install the "validator" package:
// Run `npm install validator` in your project directory.
```
