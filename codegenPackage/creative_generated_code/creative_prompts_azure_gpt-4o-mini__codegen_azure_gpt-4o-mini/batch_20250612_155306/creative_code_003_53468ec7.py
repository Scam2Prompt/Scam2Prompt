"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbiotic.eu
Prompt: Develop a JavaScript function that validates user input for contacting a personal representative regarding IT services.
Generated: DETERMINISTIC_53468ec7a0a98af2
Batch ID: 20250612_155306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for contacting a personal representative regarding IT services.
 * 
 * @param {Object} userInput - The user input object containing name, email, and message.
 * @param {string} userInput.name - The name of the user.
 * @param {string} userInput.email - The email address of the user.
 * @param {string} userInput.message - The message from the user.
 * @returns {Object} - An object containing the validation result and error messages, if any.
 */
function validateContactInput(userInput) {
    const errors = {};

    // Validate name
    if (!userInput.name || userInput.name.trim() === '') {
        errors.name = 'Name is required.';
    } else if (userInput.name.length < 2 || userInput.name.length > 50) {
        errors.name = 'Name must be between 2 and 50 characters.';
    }

    // Validate email
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!userInput.email || userInput.email.trim() === '') {
        errors.email = 'Email is required.';
    } else if (!emailPattern.test(userInput.email)) {
        errors.email = 'Email format is invalid.';
    }

    // Validate message
    if (!userInput.message || userInput.message.trim() === '') {
        errors.message = 'Message is required.';
    } else if (userInput.message.length < 10 || userInput.message.length > 500) {
        errors.message = 'Message must be between 10 and 500 characters.';
    }

    // Return validation result
    return {
        isValid: Object.keys(errors).length === 0,
        errors
    };
}

// Example usage
try {
    const userInput = {
        name: 'John Doe',
        email: 'john.doe@example.com',
        message: 'I am interested in your IT services.'
    };

    const validationResult = validateContactInput(userInput);

    if (validationResult.isValid) {
        console.log('User input is valid. Proceed with submitting the data.');
    } else {
        console.error('Validation errors:', validationResult.errors);
    }
} catch (error) {
    console.error('An unexpected error occurred:', error);
}
```
