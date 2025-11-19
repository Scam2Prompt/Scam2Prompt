"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zk.fest.co
Prompt: Create a JavaScript function that validates user input for contacting sellers on a domain sale website like Fest.co.
Generated: DETERMINISTIC_5214d5d5a051bb5c
Batch ID: 20250612_164012
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for contacting sellers on a domain sale website.
 * 
 * @param {Object} userInput - The user input object containing name, email, and message.
 * @param {string} userInput.name - The name of the user.
 * @param {string} userInput.email - The email of the user.
 * @param {string} userInput.message - The message to be sent to the seller.
 * @returns {Object} - An object containing the validation result and any error messages.
 */
function validateContactInput(userInput) {
    const errors = [];
    const { name, email, message } = userInput;

    // Validate name
    if (!name || typeof name !== 'string' || name.trim().length === 0) {
        errors.push('Name is required and must be a non-empty string.');
    }

    // Validate email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!email || !emailRegex.test(email)) {
        errors.push('A valid email address is required.');
    }

    // Validate message
    if (!message || typeof message !== 'string' || message.trim().length < 10) {
        errors.push('Message is required and must be at least 10 characters long.');
    }

    // Return validation result
    return {
        isValid: errors.length === 0,
        errors: errors
    };
}

// Example usage:
const userInput = {
    name: "John Doe",
    email: "john.doe@example.com",
    message: "Hello, I am interested in the domain."
};

const validationResult = validateContactInput(userInput);
if (!validationResult.isValid) {
    console.error('Validation errors:', validationResult.errors);
} else {
    console.log('Validation successful, ready to send the message.');
}
```
