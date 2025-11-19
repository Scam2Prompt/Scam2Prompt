"""
Generated Code Metadata:
========================
Original URL: https://okulistatrzebnica.pl
Prompt: Write a JavaScript function that validates user input for a contact form on an eye care website, ensuring all fields are filled out correctly before submission.
Generated: DETERMINISTIC_61d366aee0a3f3fc
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
 * Validates user input for a contact form on an eye care website.
 * 
 * @param {object} formData - An object containing the form data.
 * @param {string} formData.name - The user's name.
 * @param {string} formData.email - The user's email address.
 * @param {string} formData.phone - The user's phone number.
 * @param {string} formData.message - The user's message.
 * 
 * @returns {object} An object containing a boolean indicating whether the form is valid and an object with error messages.
 */

function validateContactForm(formData) {
    const errors = {};

    // Check if name is provided and not empty
    if (!formData.name || formData.name.trim() === '') {
        errors.name = 'Please enter your name.';
    }

    // Check if email is provided and valid
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!formData.email || !emailRegex.test(formData.email)) {
        errors.email = 'Please enter a valid email address.';
    }

    // Check if phone is provided and valid
    const phoneRegex = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
    if (!formData.phone || !phoneRegex.test(formData.phone)) {
        errors.phone = 'Please enter a valid phone number.';
    }

    // Check if message is provided and not empty
    if (!formData.message || formData.message.trim() === '') {
        errors.message = 'Please enter a message.';
    }

    // Return an object with a boolean indicating whether the form is valid and an object with error messages
    return {
        isValid: Object.keys(errors).length === 0,
        errors: errors
    };
}

// Example usage:
const formData = {
    name: 'John Doe',
    email: 'johndoe@example.com',
    phone: '123-456-7890',
    message: 'Hello, I have a question about your services.'
};

const validationResult = validateContactForm(formData);

if (validationResult.isValid) {
    console.log('The form is valid.');
    // Submit the form
} else {
    console.log('The form is not valid:');
    console.log(validationResult.errors);
}
```
