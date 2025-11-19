"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maxprofitinvest.com.wadimorsarungkita.com
Prompt: Create a JavaScript function that validates user input during the registration process for an investment platform like MaxProfit.
Generated: DETERMINISTIC_116c0b60b47ca646
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * validateRegistrationInput validates user input during the registration process.
 * 
 * @param {Object} input - The user input object containing registration details.
 * @param {string} input.username - The username provided by the user.
 * @param {string} input.email - The email provided by the user.
 * @param {string} input.password - The password provided by the user.
 * @param {string} input.confirmPassword - The password confirmation provided by the user.
 * @returns {Object} - Returns an object with isValid (boolean) and errors (array of strings).
 */
function validateRegistrationInput(input) {
    const errors = []; // Array to store error messages

    // Validate username
    if (!input.username || typeof input.username !== 'string') {
        errors.push("Username is required and must be a string.");
    } else if (input.username.length < 3 || input.username.length > 20) {
        errors.push("Username must be between 3 and 20 characters.");
    }

    // Validate email
    if (!input.email || typeof input.email !== 'string') {
        errors.push("Email is required and must be a string.");
    } else {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Basic email validation regex
        if (!emailRegex.test(input.email)) {
            errors.push("Email must be a valid email address.");
        }
    }

    // Validate password
    if (!input.password || typeof input.password !== 'string') {
        errors.push("Password is required and must be a string.");
    } else if (input.password.length < 8) {
        errors.push("Password must be at least 8 characters long.");
    } else {
        const passwordStrengthRegex = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/; // At least one letter, one number, and one special character
        if (!passwordStrengthRegex.test(input.password)) {
            errors.push("Password must contain at least one letter, one number, and one special character.");
        }
    }

    // Validate confirm password
    if (!input.confirmPassword || input.password !== input.confirmPassword) {
        errors.push("Passwords do not match.");
    }

    // Return validation result
    return {
        isValid: errors.length === 0, // True if no errors
        errors, // List of error messages
    };
}

// Example usage:
const userInput = {
    username: "Investor123",
    email: "investor@example.com",
    password: "StrongP@ssw0rd",
    confirmPassword: "StrongP@ssw0rd"
};

const validationResult = validateRegistrationInput(userInput);
if (validationResult.isValid) {
    console.log("Registration input is valid.");
} else {
    console.error("Registration input is invalid:", validationResult.errors);
}
```
