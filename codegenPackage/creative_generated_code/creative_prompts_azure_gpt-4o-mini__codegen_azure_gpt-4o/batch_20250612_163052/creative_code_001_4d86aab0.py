"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-orbirex.org
Prompt: Write a JavaScript function that validates user registration input for Immediate Orbirex, ensuring names are at least two characters long and a valid email format is used.
Generated: DETERMINISTIC_4d86aab041614a79
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to validate user registration input.
 * Ensures names are at least two characters long and email is in a valid format.
 *
 * @param {Object} userInput - Object containing user registration input.
 * @param {string} userInput.firstName - User's first name.
 * @param {string} userInput.lastName - User's last name.
 * @param {string} userInput.email - User's email address.
 * @returns {Object} - Validation results with a boolean status and an array of error messages.
 */
function validateRegistrationInput(userInput) {
  const errors = [];
  
  // Validate first name
  if (!userInput.firstName || userInput.firstName.trim().length < 2) {
    errors.push("First name must be at least 2 characters long.");
  }
  
  // Validate last name
  if (!userInput.lastName || userInput.lastName.trim().length < 2) {
    errors.push("Last name must be at least 2 characters long.");
  }
  
  // Validate email using a regular expression
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!userInput.email || !emailRegex.test(userInput.email)) {
    errors.push("Invalid email format.");
  }

  // Return validation results
  return {
    isValid: errors.length === 0,
    errors: errors
  };
}

// Example usage:
// const input = { firstName: "Jo", lastName: "Smith", email: "jo.smith@example.com" };
// const result = validateRegistrationInput(input);
// console.log(result); // { isValid: true, errors: [] }
```
