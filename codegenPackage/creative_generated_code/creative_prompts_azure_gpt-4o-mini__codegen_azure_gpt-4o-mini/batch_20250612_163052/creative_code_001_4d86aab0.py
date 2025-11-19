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
 * Validates user registration input for Immediate Orbirex.
 * 
 * @param {Object} userInput - The user registration input containing name and email.
 * @param {string} userInput.name - The user's name.
 * @param {string} userInput.email - The user's email address.
 * @returns {Object} - An object containing validation results and messages.
 */
function validateRegistrationInput(userInput) {
    const validationResults = {
        isValid: true,
        messages: []
    };

    // Validate name
    if (!userInput.name || userInput.name.length < 2) {
        validationResults.isValid = false;
        validationResults.messages.push('Name must be at least 2 characters long.');
    }

    // Validate email using a regular expression
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!userInput.email || !emailRegex.test(userInput.email)) {
        validationResults.isValid = false;
        validationResults.messages.push('Invalid email format.');
    }

    return validationResults;
}

// Example usage:
try {
    const userInput = {
        name: 'John',
        email: 'john.doe@example.com'
    };

    const result = validateRegistrationInput(userInput);
    if (result.isValid) {
        console.log('Registration input is valid.');
    } else {
        console.log('Validation errors:', result.messages.join(' '));
    }
} catch (error) {
    console.error('An error occurred during validation:', error.message);
}
```
