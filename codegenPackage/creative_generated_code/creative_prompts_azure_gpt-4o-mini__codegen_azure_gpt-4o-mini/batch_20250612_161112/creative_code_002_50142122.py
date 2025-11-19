"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.eclat.com.tr
Prompt: Create a JavaScript function to validate user input for an online registration form for ECLAT's online training courses in nail and eyelash techniques.
Generated: DETERMINISTIC_501421220ca25047
Batch ID: 20250612_161112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for ECLAT's online registration form.
 * 
 * The function checks for the following:
 * - Valid email format
 * - Non-empty first name and last name
 * - Password strength
 * - Valid phone number format
 * 
 * @param {Object} userInput - An object containing user registration information.
 * @param {string} userInput.firstName - The user's first name.
 * @param {string} userInput.lastName - The user's last name.
 * @param {string} userInput.email - The user's email address.
 * @param {string} userInput.password - The user's password.
 * @param {string} userInput.phone - The user's phone number.
 * @returns {Object} - An object containing validation results and messages.
 */
function validateRegistrationInput(userInput) {
    const validationResults = {
        isValid: true,
        errors: []
    };

    // Regular expressions for validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d@$!%*?&]{8,}$/; // At least 8 characters, 1 uppercase, 1 lowercase, 1 number
    const phoneRegex = /^\+?[\d\s]{7,15}$/; // Valid phone number format

    // Validate first name
    if (!userInput.firstName || userInput.firstName.trim() === "") {
        validationResults.isValid = false;
        validationResults.errors.push("First name is required.");
    }

    // Validate last name
    if (!userInput.lastName || userInput.lastName.trim() === "") {
        validationResults.isValid = false;
        validationResults.errors.push("Last name is required.");
    }

    // Validate email
    if (!emailRegex.test(userInput.email)) {
        validationResults.isValid = false;
        validationResults.errors.push("Please enter a valid email address.");
    }

    // Validate password
    if (!passwordRegex.test(userInput.password)) {
        validationResults.isValid = false;
        validationResults.errors.push("Password must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, and one number.");
    }

    // Validate phone number
    if (!phoneRegex.test(userInput.phone)) {
        validationResults.isValid = false;
        validationResults.errors.push("Please enter a valid phone number.");
    }

    return validationResults;
}

// Example usage:
const userInput = {
    firstName: "John",
    lastName: "Doe",
    email: "john.doe@example.com",
    password: "Password123",
    phone: "+1234567890"
};

const validation = validateRegistrationInput(userInput);
if (!validation.isValid) {
    console.error("Validation errors:", validation.errors);
} else {
    console.log("Registration input is valid.");
}
```
