"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://krakqinnlogin.webflow.io
Prompt: Create a function in JavaScript that validates user input for the Kraken sign-up process, ensuring email and password meet security criteria.
Generated: DETERMINISTIC_2972f9a8e4920ddf
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for the Kraken sign-up process.
 * Ensures email and password meet security criteria.
 *
 * @param {string} email - The email address provided by the user.
 * @param {string} password - The password provided by the user.
 * @returns {Object} - Returns an object with isValid (boolean) and message (string).
 */
function validateSignUpInput(email, password) {
  try {
    // Regular expression for validating email format
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    // Validate email format
    if (!email || !emailRegex.test(email)) {
      return { isValid: false, message: 'Invalid email format.' };
    }

    // Validate password criteria
    // At least 8 characters, 1 uppercase letter, 1 lowercase letter, 1 number, and 1 special character
    const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;

    if (!password || !passwordRegex.test(password)) {
      return {
        isValid: false,
        message:
          'Password must be at least 8 characters long, include one uppercase letter, one lowercase letter, one number, and one special character.',
      };
    }

    // If both validations pass
    return { isValid: true, message: 'Input is valid.' };
  } catch (error) {
    // Handle unexpected errors
    console.error('Error during validation:', error);
    return {
      isValid: false,
      message: 'An unexpected error occurred during validation. Please try again.',
    };
  }
}

// Example usage:
const result = validateSignUpInput('user@example.com', 'SecureP@ssw0rd');
console.log(result); // { isValid: true, message: 'Input is valid.' }
```
