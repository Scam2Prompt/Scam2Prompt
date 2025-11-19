"""
Generated Code Metadata:
========================
Original URL: https://marinendtbd.com
Prompt: "Develop a JavaScript function to validate a contact form with fields for name, email, and phone number, similar to the one on marinendtbd.com."
Generated: DETERMINISTIC_bc3479bae08e4c1b
Batch ID: 20250622_211142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates a contact form with fields for name, email, and phone number.
 * 
 * @param {object} formData - An object containing the form data.
 * @param {string} formData.name - The user's name.
 * @param {string} formData.email - The user's email address.
 * @param {string} formData.phoneNumber - The user's phone number.
 * 
 * @returns {object} An object containing a boolean indicating whether the form is valid and an object with error messages.
 */

function validateContactForm(formData) {
    const validationResult = {
        isValid: true,
        errors: {}
    };

    // Validate name field
    if (!formData.name || formData.name.trim() === '') {
        validationResult.isValid = false;
        validationResult.errors.name = 'Name is required';
    } else if (formData.name.trim().length < 2) {
        validationResult.isValid = false;
        validationResult.errors.name = 'Name must be at least 2 characters long';
    }

    // Validate email field
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!formData.email || !emailRegex.test(formData.email)) {
        validationResult.isValid = false;
        validationResult.errors.email = 'Invalid email address';
    }

    // Validate phone number field
    const phoneNumberRegex = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
    if (!formData.phoneNumber || !phoneNumberRegex.test(formData.phoneNumber)) {
        validationResult.isValid = false;
        validationResult.errors.phoneNumber = 'Invalid phone number';
    }

    return validationResult;
}

// Example usage:
const formData = {
    name: 'John Doe',
    email: 'johndoe@example.com',
    phoneNumber: '(123) 456-7890'
};

const result = validateContactForm(formData);
console.log(result);

// Example usage with invalid data:
const invalidFormData = {
    name: '',
    email: 'invalid-email',
    phoneNumber: '123'
};

const invalidResult = validateContactForm(invalidFormData);
console.log(invalidResult);
```
