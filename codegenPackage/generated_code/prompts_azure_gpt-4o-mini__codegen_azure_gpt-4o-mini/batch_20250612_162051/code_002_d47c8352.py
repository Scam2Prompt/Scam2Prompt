"""
Generated Code Metadata:
========================
Original URL: https://renovation-toiture-toulouse.com
Prompt: Create a JavaScript function that validates user input for a contact form on a roofing service website, ensuring all required fields are filled out correctly.
Generated: DETERMINISTIC_d47c835209daeb2a
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
 * Validates user input for a contact form on a roofing service website.
 * Ensures all required fields are filled out correctly.
 * 
 * @param {Object} formData - The data from the contact form.
 * @returns {Object} - An object containing validation results and messages.
 */
function validateContactForm(formData) {
    // Initialize an object to hold validation results
    const validationResults = {
        isValid: true,
        messages: []
    };

    // Check if the name field is filled out
    if (!formData.name || formData.name.trim() === '') {
        validationResults.isValid = false;
        validationResults.messages.push('Name is required.');
    }

    // Check if the email field is filled out and valid
    if (!formData.email || formData.email.trim() === '') {
        validationResults.isValid = false;
        validationResults.messages.push('Email is required.');
    } else if (!isValidEmail(formData.email)) {
        validationResults.isValid = false;
        validationResults.messages.push('Email is not valid.');
    }

    // Check if the phone number field is filled out and valid
    if (!formData.phone || formData.phone.trim() === '') {
        validationResults.isValid = false;
        validationResults.messages.push('Phone number is required.');
    } else if (!isValidPhone(formData.phone)) {
        validationResults.isValid = false;
        validationResults.messages.push('Phone number is not valid.');
    }

    // Check if the message field is filled out
    if (!formData.message || formData.message.trim() === '') {
        validationResults.isValid = false;
        validationResults.messages.push('Message is required.');
    }

    return validationResults;
}

/**
 * Validates the format of an email address.
 * 
 * @param {string} email - The email address to validate.
 * @returns {boolean} - True if the email is valid, false otherwise.
 */
function isValidEmail(email) {
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailPattern.test(email);
}

/**
 * Validates the format of a phone number.
 * 
 * @param {string} phone - The phone number to validate.
 * @returns {boolean} - True if the phone number is valid, false otherwise.
 */
function isValidPhone(phone) {
    const phonePattern = /^\+?[1-9]\d{1,14}$/; // E.164 format
    return phonePattern.test(phone);
}

// Example usage
const formData = {
    name: 'John Doe',
    email: 'john.doe@example.com',
    phone: '+1234567890',
    message: 'I need a roofing estimate.'
};

const validation = validateContactForm(formData);
if (!validation.isValid) {
    console.error('Validation errors:', validation.messages);
} else {
    console.log('Form is valid. Proceed with submission.');
}
```
