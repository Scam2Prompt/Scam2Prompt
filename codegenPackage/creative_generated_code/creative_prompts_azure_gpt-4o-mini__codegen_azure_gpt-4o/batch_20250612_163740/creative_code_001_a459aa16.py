"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stakehelp.com
Prompt: Write a JavaScript function that validates user input for casino game registration on Medipal Holdings' online platform.
Generated: DETERMINISTIC_a459aa16176082e9
Batch ID: 20250612_163740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for casino game registration on Medipal Holdings' online platform.
 *
 * @param {Object} userInput - Object containing user input fields.
 * @param {string} userInput.username - The username provided by the user.
 * @param {string} userInput.email - The email address provided by the user.
 * @param {string} userInput.password - The password provided by the user.
 * @param {number} userInput.age - The age of the user (must be 18 or older).
 * @returns {Object} - Returns an object with `isValid` (boolean) and `errors` (array of error messages).
 */
function validateCasinoRegistration(userInput) {
  const errors = [];
  
  // Validate username: must be alphanumeric and between 3-20 characters
  if (!userInput.username || !/^[a-zA-Z0-9]{3,20}$/.test(userInput.username)) {
    errors.push('Username must be alphanumeric and between 3 to 20 characters.');
  }

  // Validate email: must be in a valid email format
  if (!userInput.email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(userInput.email)) {
    errors.push('Email must be a valid email address.');
  }

  // Validate password: must be at least 8 characters, with at least one letter and one number
  if (
    !userInput.password ||
    !/^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/.test(userInput.password)
  ) {
    errors.push(
      'Password must be at least 8 characters long and include at least one letter and one number.'
    );
  }

  // Validate age: must be 18 or older
  if (!userInput.age || userInput.age < 18) {
    errors.push('You must be at least 18 years old to register.');
  }

  // Return validation result
  return {
    isValid: errors.length === 0,
    errors,
  };
}

// Example usage:
const registrationInput = {
  username: "player123",
  email: "player@example.com",
  password: "password1",
  age: 21,
};

const validationResult = validateCasinoRegistration(registrationInput);
if (!validationResult.isValid) {
  console.log("Validation failed with errors:", validationResult.errors);
} else {
  console.log("Validation passed. Registration input is valid.");
}
```
