"""
Generated Code Metadata:
========================
Original URL: https://lestersplace.com
Prompt: Create a JavaScript function that validates user input for a contact form aimed at assisted living services, ensuring all fields are filled out correctly before submission.
Generated: DETERMINISTIC_70085bb296eba252
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for a contact form aimed at assisted living services.
 * 
 * @param {object} formData - An object containing the form data.
 * @param {string} formData.name - The user's name.
 * @param {string} formData.email - The user's email address.
 * @param {string} formData.phone - The user's phone number.
 * @param {string} formData.message - The user's message.
 * @param {string} formData.service - The user's requested service.
 * 
 * @returns {object} An object containing a boolean indicating whether the form is valid and an object with error messages.
 */

function validateContactForm(formData) {
    // Initialize an object to store error messages
    const errors = {};

    // Check if the form data is not empty
    if (!formData) {
        throw new Error('Form data is required');
    }

    // Validate name field
    if (!formData.name || formData.name.trim() === '') {
        errors.name = 'Name is required';
    }

    // Validate email field
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!formData.email || !emailRegex.test(formData.email)) {
        errors.email = 'Invalid email address';
    }

    // Validate phone field
    const phoneRegex = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
    if (!formData.phone || !phoneRegex.test(formData.phone)) {
        errors.phone = 'Invalid phone number';
    }

    // Validate message field
    if (!formData.message || formData.message.trim() === '') {
        errors.message = 'Message is required';
    }

    // Validate service field
    if (!formData.service || formData.service.trim() === '') {
        errors.service = 'Service is required';
    }

    // Return an object with a boolean indicating whether the form is valid and the error messages
    return {
        isValid: Object.keys(errors).length === 0,
        errors,
    };
}

// Example usage:
const formData = {
    name: 'John Doe',
    email: 'john.doe@example.com',
    phone: '123-456-7890',
    message: 'Hello, I am interested in your assisted living services.',
    service: 'Assisted Living',
};

const validationResult = validateContactForm(formData);
console.log(validationResult);

// Test with invalid data
const invalidFormData = {
    name: '',
    email: 'invalid-email',
    phone: 'invalid-phone',
    message: '',
    service: '',
};

const invalidValidationResult = validateContactForm(invalidFormData);
console.log(invalidValidationResult);
```
