"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://d-theta-three.vercel.app
Prompt: Write a JavaScript function to validate user input for a registration form with fields for full name, email, and password.
Generated: DETERMINISTIC_986c07f75e890d86
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
 * Validates user input for a registration form.
 * @param {Object} userInput - Object containing user input fields.
 * @param {string} userInput.fullName - The full name of the user.
 * @param {string} userInput.email - The email address of the user.
 * @param {string} userInput.password - The password provided by the user.
 * @returns {Object} An object containing validation status and error messages (if any).
 */
function validateRegistrationForm(userInput) {
  const errors = {};

  // Validate full name
  if (!userInput.fullName || typeof userInput.fullName !== 'string' || userInput.fullName.trim() === '') {
    errors.fullName = 'Full name is required and cannot be empty.';
  } else if (userInput.fullName.length < 3 || userInput.fullName.length > 50) {
    errors.fullName = 'Full name must be between 3 and 50 characters.';
  }

  // Validate email
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Simple regex for email validation
  if (!userInput.email || typeof userInput.email !== 'string' || userInput.email.trim() === '') {
    errors.email = 'Email is required and cannot be empty.';
  } else if (!emailRegex.test(userInput.email)) {
    errors.email = 'Invalid email format.';
  }

  // Validate password
  if (!userInput.password || typeof userInput.password !== 'string' || userInput.password.trim() === '') {
    errors.password = 'Password is required and cannot be empty.';
  } else if (userInput.password.length < 8) {
    errors.password = 'Password must be at least 8 characters long.';
  } else if (!/[A-Z]/.test(userInput.password)) {
    errors.password = 'Password must contain at least one uppercase letter.';
  } else if (!/[a-z]/.test(userInput.password)) {
    errors.password = 'Password must contain at least one lowercase letter.';
  } else if (!/[0-9]/.test(userInput.password)) {
    errors.password = 'Password must contain at least one numeric digit.';
  } else if (!/[!@#$%^&*(),.?":{}|<>]/.test(userInput.password)) {
    errors.password = 'Password must contain at least one special character.';
  }

  // Return validation results
  return {
    isValid: Object.keys(errors).length === 0,
    errors,
  };
}

// Example usage:
const userInput = {
  fullName: "John Doe",
  email: "john.doe@example.com",
  password: "Password123!",
};

const validationResult = validateRegistrationForm(userInput);

if (validationResult.isValid) {
  console.log("Validation successful!");
} else {
  console.error("Validation failed:", validationResult.errors);
}
```
