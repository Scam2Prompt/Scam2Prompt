"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ponet.pro
Prompt: Write a JavaScript function that validates user input during a presale registration process and provides error messages for incorrect entries.
Generated: DETERMINISTIC_2cb718d5d13e9058
Batch ID: 20250612_153700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input during a presale registration process.
 * Checks for valid email, non-empty full name, and age within a specified range.
 * Provides error messages for incorrect entries.
 * 
 * @param {Object} userInput - An object containing user input fields.
 * @param {string} userInput.email - The user's email address.
 * @param {string} userInput.fullName - The user's full name.
 * @param {number} userInput.age - The user's age.
 * @returns {Object} - An object containing `isValid` (boolean) and `errors` (array of error messages).
 */
function validatePresaleRegistration(userInput) {
    const errors = [];

    // Validate email format using regex
    if (!userInput.email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(userInput.email)) {
        errors.push("Invalid email format.");
    }

    // Validate full name (must not be empty and should contain at least two words)
    if (!userInput.fullName || userInput.fullName.trim().split(' ').length < 2) {
        errors.push("Full name must contain at least first and last name.");
    }

    // Validate age (must be between 18 and 120)
    if (typeof userInput.age !== 'number' || userInput.age < 18 || userInput.age > 120) {
        errors.push("Age must be a number between 18 and 120.");
    }

    // Return validation result
    return {
        isValid: errors.length === 0,
        errors: errors
    };
}

// Example usage:
const input = {
    email: "example@domain.com",
    fullName: "John Doe",
    age: 25
};

const result = validatePresaleRegistration(input);
if (result.isValid) {
    console.log("Registration is valid.");
} else {
    console.log("Registration has errors:", result.errors);
}
```
