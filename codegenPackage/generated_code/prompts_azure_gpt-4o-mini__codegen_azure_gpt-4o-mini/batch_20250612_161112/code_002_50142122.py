"""
Generated Code Metadata:
========================
Original URL: https://www.eclat.com.tr
Prompt: Create a JavaScript function to validate user input for an online registration form for ECLAT's online training courses in nail and eyelash techniques.
Generated: DETERMINISTIC_501421220ca25047
Batch ID: 20250612_161112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for ECLAT's online registration form.
 * 
 * @param {Object} userInput - The user input object containing registration details.
 * @param {string} userInput.name - The name of the user.
 * @param {string} userInput.email - The email address of the user.
 * @param {string} userInput.password - The password chosen by the user.
 * @param {string} userInput.confirmPassword - The password confirmation.
 * @returns {Object} - An object containing validation results and messages.
 */
function validateRegistrationInput(userInput) {
    const validationResults = {
        isValid: true,
        messages: []
    };

    // Validate name
    if (!userInput.name || userInput.name.trim().length < 2) {
        validationResults.isValid = false;
        validationResults.messages.push("Name must be at least 2 characters long.");
    }

    // Validate email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!userInput.email || !emailRegex.test(userInput.email)) {
        validationResults.isValid = false;
        validationResults.messages.push("Please enter a valid email address.");
    }

    // Validate password
    if (!userInput.password || userInput.password.length < 8) {
        validationResults.isValid = false;
        validationResults.messages.push("Password must be at least 8 characters long.");
    }

    // Validate password confirmation
    if (userInput.password !== userInput.confirmPassword) {
        validationResults.isValid = false;
        validationResults.messages.push("Passwords do not match.");
    }

    return validationResults;
}

// Example usage
try {
    const userInput = {
        name: "John Doe",
        email: "john.doe@example.com",
        password: "securePassword123",
        confirmPassword: "securePassword123"
    };

    const validation = validateRegistrationInput(userInput);
    if (validation.isValid) {
        console.log("Registration input is valid.");
    } else {
        console.error("Validation errors:", validation.messages);
    }
} catch (error) {
    console.error("An error occurred during validation:", error);
}
```
