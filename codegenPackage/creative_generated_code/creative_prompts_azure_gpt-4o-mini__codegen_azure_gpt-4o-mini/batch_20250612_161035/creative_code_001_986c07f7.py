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
 * 
 * @param {Object} userInput - The user input object containing fullName, email, and password.
 * @param {string} userInput.fullName - The full name of the user.
 * @param {string} userInput.email - The email of the user.
 * @param {string} userInput.password - The password of the user.
 * @returns {Object} - An object containing the validation status and messages.
 */
function validateRegistrationInput(userInput) {
    // Initialize validation results
    const validationResults = {
        isValid: true,
        messages: []
    };

    // Validate full name
    if (!userInput.fullName || userInput.fullName.trim().length === 0) {
        validationResults.isValid = false;
        validationResults.messages.push('Full name is required.');
    } else if (userInput.fullName.length < 3) {
        validationResults.isValid = false;
        validationResults.messages.push('Full name must be at least 3 characters long.');
    }

    // Validate email using a regular expression
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!userInput.email || !emailRegex.test(userInput.email)) {
        validationResults.isValid = false;
        validationResults.messages.push('A valid email address is required.');
    }

    // Validate password
    if (!userInput.password || userInput.password.length < 6) {
        validationResults.isValid = false;
        validationResults.messages.push('Password must be at least 6 characters long.');
    }

    return validationResults;
}

// Example usage:
try {
    const userInput = {
        fullName: 'John Doe',
        email: 'john.doe@example.com',
        password: '123456'
    };
    
    const validation = validateRegistrationInput(userInput);
    
    if (validation.isValid) {
        console.log('Registration input is valid.');
    } else {
        console.error('Validation errors:', validation.messages);
    }
} catch (error) {
    console.error('An error occurred during validation:', error.message);
}
```
