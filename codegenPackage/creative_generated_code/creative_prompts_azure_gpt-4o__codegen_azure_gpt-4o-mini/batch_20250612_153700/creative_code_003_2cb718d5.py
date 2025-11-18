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
 * 
 * @param {Object} userInput - The user input object containing registration details.
 * @param {string} userInput.name - The name of the user.
 * @param {string} userInput.email - The email of the user.
 * @param {string} userInput.phone - The phone number of the user.
 * @returns {Object} result - An object containing validation status and messages.
 */
function validateRegistrationInput(userInput) {
    const result = {
        isValid: true,
        messages: []
    };

    // Validate name
    if (!userInput.name || typeof userInput.name !== 'string' || userInput.name.trim() === '') {
        result.isValid = false;
        result.messages.push('Name is required and must be a non-empty string.');
    }

    // Validate email using a simple regex pattern
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!userInput.email || !emailPattern.test(userInput.email)) {
        result.isValid = false;
        result.messages.push('A valid email address is required.');
    }

    // Validate phone number (basic check for digits and length)
    const phonePattern = /^\d{10}$/; // Assumes a 10-digit phone number
    if (!userInput.phone || !phonePattern.test(userInput.phone)) {
        result.isValid = false;
        result.messages.push('A valid 10-digit phone number is required.');
    }

    // Return the validation result
    return result;
}

// Example usage:
try {
    const userInput = {
        name: 'John Doe',
        email: 'john.doe@example.com',
        phone: '1234567890'
    };

    const validationResult = validateRegistrationInput(userInput);

    if (!validationResult.isValid) {
        console.error('Validation errors:', validationResult.messages);
    } else {
        console.log('Registration input is valid.');
        // Proceed with registration process
    }
} catch (error) {
    console.error('An unexpected error occurred:', error);
}
```
