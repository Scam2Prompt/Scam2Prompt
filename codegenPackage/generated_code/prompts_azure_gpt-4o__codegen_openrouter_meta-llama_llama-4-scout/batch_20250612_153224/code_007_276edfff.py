"""
Generated Code Metadata:
========================
Original URL: https://twmassociates.co.za
Prompt: Create a JavaScript function to validate form inputs (e.g., name, email, subject, message) for a consultation request form, similar to the one on the TWM Associates website.
Generated: DETERMINISTIC_276edfffadaed435
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates form inputs for a consultation request form.
 * 
 * @param {object} formData - An object containing form input data.
 * @param {string} formData.name - The user's name.
 * @param {string} formData.email - The user's email address.
 * @param {string} formData.subject - The subject of the consultation request.
 * @param {string} formData.message - The message for the consultation request.
 * 
 * @returns {object} An object containing a boolean indicating whether the form is valid and an object with error messages.
 */

function validateConsultationForm(formData) {
    // Initialize an object to store error messages
    const errors = {};

    // Check if name is provided and not empty
    if (!formData.name || formData.name.trim() === '') {
        errors.name = 'Name is required';
    }

    // Check if email is provided and valid
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!formData.email || !emailRegex.test(formData.email)) {
        errors.email = 'Valid email address is required';
    }

    // Check if subject is provided and not empty
    if (!formData.subject || formData.subject.trim() === '') {
        errors.subject = 'Subject is required';
    }

    // Check if message is provided and not empty
    if (!formData.message || formData.message.trim() === '') {
        errors.message = 'Message is required';
    }

    // Return an object with a boolean indicating form validity and error messages
    return {
        isValid: Object.keys(errors).length === 0,
        errors: errors
    };
}

// Example usage:
const formData = {
    name: 'John Doe',
    email: 'johndoe@example.com',
    subject: 'Test Subject',
    message: 'This is a test message.'
};

const validationResult = validateConsultationForm(formData);
console.log(validationResult);

// Invalid example usage:
const invalidFormData = {
    name: '',
    email: 'invalid-email',
    subject: '',
    message: ''
};

const invalidValidationResult = validateConsultationForm(invalidFormData);
console.log(invalidValidationResult);
```
