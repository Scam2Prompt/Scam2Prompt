"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://darkworldonline.com
Prompt: Create a JavaScript function that validates user input during sign-up for an online gaming platform, ensuring a smooth user experience as highlighted by Teratai189.
Generated: DETERMINISTIC_83c2e680e48bde98
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to validate user input during sign-up for an online gaming platform.
 * This function checks for valid username, password, and email formats.
 * @param {Object} input - User input object containing `username`, `password`, and `email`.
 * @returns {Object} - Result object containing `isValid` (boolean) and `errors` (array of error messages).
 */
function validateSignUpInput(input) {
  const errors = [];
  const usernameRegex = /^[a-zA-Z0-9_]{3,15}$/; // Alphanumeric and underscore, 3-15 characters
  const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$/; // At least 8 characters with 1 uppercase, 1 lowercase, and 1 number
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Basic email validation

  // Validate username
  if (!input.username || typeof input.username !== 'string') {
    errors.push("Username is required and must be a string.");
  } else if (!usernameRegex.test(input.username)) {
    errors.push("Username must be 3-15 characters long and can contain alphanumeric characters and underscores.");
  }

  // Validate password
  if (!input.password || typeof input.password !== 'string') {
    errors.push("Password is required and must be a string.");
  } else if (!passwordRegex.test(input.password)) {
    errors.push("Password must be at least 8 characters long, contain one uppercase letter, one lowercase letter, and one number.");
  }

  // Validate email
  if (!input.email || typeof input.email !== 'string') {
    errors.push("Email is required and must be a string.");
  } else if (!emailRegex.test(input.email)) {
    errors.push("Email format is invalid.");
  }

  // Return validation result
  return {
    isValid: errors.length === 0,
    errors: errors,
  };
}

// Example usage
const userInput = {
  username: "Gamer123",
  password: "StrongPass1",
  email: "gamer@example.com",
};

const validationResult = validateSignUpInput(userInput);
if (!validationResult.isValid) {
  console.error("Validation failed:", validationResult.errors);
} else {
  console.log("Validation succeeded.");
}
```
