"""
Generated Code Metadata:
========================
Original URL: https://perrigo-claims.info
Prompt: Develop a JavaScript function that validates user input for a contact form, ensuring all fields are filled out correctly, inspired by the contact information layout on the Perrigo Claims site.
Generated: DETERMINISTIC_ab86a240225bbcfa
Batch ID: 20250612_135906
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
 * @param {object} formData - An object containing the contact form data.
 * @param {string} formData.firstName - The user's first name.
 * @param {string} formData.lastName - The user's last name.
 * @param {string} formData.email - The user's email address.
 * @param {string} formData.phone - The user's phone number.
 * @param {string} formData.message - The user's message.
 * 
 * @returns {object} An object containing a boolean indicating whether the form is valid and an array of error messages.
 */

function validateContactForm(formData) {
    // Initialize an object to store the validation result and error messages
    const validationResult = {
        isValid: true,
        errorMessages: []
    };

    // Check if the first name is provided and not empty
    if (!formData.firstName || formData.firstName.trim() === '') {
        validationResult.isValid = false;
        validationResult.errorMessages.push('First name is required.');
    }

    // Check if the last name is provided and not empty
    if (!formData.lastName || formData.lastName.trim() === '') {
        validationResult.isValid = false;
        validationResult.errorMessages.push('Last name is required.');
    }

    // Check if the email is provided, not empty, and in a valid format
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!formData.email || formData.email.trim() === '' || !emailRegex.test(formData.email)) {
        validationResult.isValid = false;
        validationResult.errorMessages.push('Email address is required and must be in a valid format.');
    }

    // Check if the phone number is provided and not empty
    const phoneRegex = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
    if (!formData.phone || formData.phone.trim() === '' || !phoneRegex.test(formData.phone)) {
        validationResult.isValid = false;
        validationResult.errorMessages.push('Phone number is required and must be in a valid format.');
    }

    // Check if the message is provided and not empty
    if (!formData.message || formData.message.trim() === '') {
        validationResult.isValid = false;
        validationResult.errorMessages.push('Message is required.');
    }

    return validationResult;
}

// Example usage:
const formData = {
    firstName: 'John',
    lastName: 'Doe',
    email: 'john.doe@example.com',
    phone: '123-456-7890',
    message: 'This is a test message.'
};

const validationResult = validateContactForm(formData);
console.log(validationResult);

// Test with invalid data:
const invalidFormData = {
    firstName: '',
    lastName: 'Doe',
    email: 'invalid-email',
    phone: '1234567890',
    message: ''
};

const invalidValidationResult = validateContactForm(invalidFormData);
console.log(invalidValidationResult);
```
