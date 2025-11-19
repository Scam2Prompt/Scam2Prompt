"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswaptimizer.com
Prompt: Create a JavaScript function that validates user input for a gambling site registration form, ensuring compliance with the features highlighted on HOLYWIN69.
Generated: DETERMINISTIC_e665c7ef15ef56ce
Batch ID: 20250612_135736
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for a gambling site registration form.
 * Ensures that the input complies with defined rules.
 * 
 * @param {Object} userInput - The user input object containing registration details.
 * @param {string} userInput.username - The username for registration.
 * @param {string} userInput.password - The password for registration.
 * @param {string} userInput.email - The email address for registration.
 * @param {number} userInput.age - The age of the user.
 * @returns {Object} - An object containing the validation result and messages.
 */
function validateRegistrationInput(userInput) {
    const result = {
        isValid: true,
        messages: []
    };

    // Validate username
    if (!userInput.username || userInput.username.length < 3 || userInput.username.length > 20) {
        result.isValid = false;
        result.messages.push("Username must be between 3 and 20 characters.");
    }

    // Validate password
    if (!userInput.password || userInput.password.length < 8) {
        result.isValid = false;
        result.messages.push("Password must be at least 8 characters long.");
    } else if (!/[A-Z]/.test(userInput.password) || !/[0-9]/.test(userInput.password)) {
        result.isValid = false;
        result.messages.push("Password must contain at least one uppercase letter and one number.");
    }

    // Validate email
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(userInput.email)) {
        result.isValid = false;
        result.messages.push("Email address is not valid.");
    }

    // Validate age
    if (typeof userInput.age !== 'number' || userInput.age < 18 || userInput.age > 120) {
        result.isValid = false;
        result.messages.push("Age must be a number between 18 and 120.");
    }

    return result;
}

// Example usage:
try {
    const userInput = {
        username: "JohnDoe",
        password: "Password123",
        email: "john.doe@example.com",
        age: 25
    };

    const validationResult = validateRegistrationInput(userInput);

    if (validationResult.isValid) {
        console.log("Registration input is valid.");
    } else {
        console.error("Validation errors:", validationResult.messages);
    }
} catch (error) {
    console.error("An error occurred during validation:", error);
}
```
