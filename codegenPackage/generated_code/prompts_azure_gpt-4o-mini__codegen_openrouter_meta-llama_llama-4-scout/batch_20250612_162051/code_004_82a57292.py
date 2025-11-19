"""
Generated Code Metadata:
========================
Original URL: https://www.albertozofrea.it
Prompt: Construct a JavaScript function that validates user input for a contact form based on the details provided on the Alberto Zofrea site.
Generated: DETERMINISTIC_82a57292a4e49156
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for a contact form.
 * 
 * @param {object} formData - An object containing the user's input data.
 * @param {string} formData.name - The user's name.
 * @param {string} formData.email - The user's email address.
 * @param {string} formData.message - The user's message.
 * @returns {object} An object containing a boolean indicating whether the input is valid and an array of error messages.
 */
function validateContactForm(formData) {
    // Initialize an object to store the validation result and error messages
    const validationResult = {
        isValid: true,
        errorMessages: []
    };

    // Check if the name field is not empty and has a minimum length of 2 characters
    if (!formData.name || formData.name.length < 2) {
        validationResult.isValid = false;
        validationResult.errorMessages.push('Name must be at least 2 characters long.');
    }

    // Check if the email field is not empty and has a valid email format
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!formData.email || !emailRegex.test(formData.email)) {
        validationResult.isValid = false;
        validationResult.errorMessages.push('Invalid email address.');
    }

    // Check if the message field is not empty and has a minimum length of 10 characters
    if (!formData.message || formData.message.length < 10) {
        validationResult.isValid = false;
        validationResult.errorMessages.push('Message must be at least 10 characters long.');
    }

    return validationResult;
}

// Example usage:
try {
    const formData = {
        name: 'John Doe',
        email: 'johndoe@example.com',
        message: 'This is a test message.'
    };

    const validationResult = validateContactForm(formData);
    console.log(validationResult);

    if (!validationResult.isValid) {
        throw new Error('Invalid form data.');
    }
} catch (error) {
    console.error(error.message);
}
```
