"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daddys-universitys.com
Prompt: Create a JavaScript function that validates user input for a contact form on the Inaka Revive Solutions website, ensuring all required fields are filled out correctly.
Generated: DETERMINISTIC_4d5e249e700255b8
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for a contact form.
 * 
 * This function checks whether all required fields are filled out correctly.
 * Fields include name, email, phone, and message. 
 * - Name should not be empty.
 * - Email should be a valid email format.
 * - Phone should be a valid format (optional).
 * - Message should not be empty.
 * 
 * @param {Object} formData - An object containing the form fields to validate.
 * @returns {Object} - An object containing validation results and error messages.
 */
function validateContactForm(formData) {
    // Initialize an object to hold error messages and a validation status
    const validationResults = {
        isValid: true,
        errors: {}
    };

    // Validate name
    if (!formData.name || formData.name.trim() === '') {
        validationResults.isValid = false;
        validationResults.errors.name = 'Name is required.';
    }

    // Validate email using a regular expression
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!formData.email || !emailRegex.test(formData.email)) {
        validationResults.isValid = false;
        validationResults.errors.email = 'A valid email is required.';
    }

    // Validate phone (optional, can be left empty)
    if (formData.phone && !/^\+?([0-9]{1,3})?[-. ]?\(?([0-9]{1,4})?\)?[-. ]?([0-9]{1,4})[-. ]?([0-9]{1,9})?$/.test(formData.phone)) {
        validationResults.isValid = false;
        validationResults.errors.phone = 'Phone number is invalid.';
    }

    // Validate message
    if (!formData.message || formData.message.trim() === '') {
        validationResults.isValid = false;
        validationResults.errors.message = 'Message cannot be empty.';
    }

    return validationResults;
}

// Example usage:
const formData = {
    name: 'John Doe',
    email: 'john.doe@example.com',
    phone: '+1234567890',
    message: 'Hello, I would like to know more about your services.'
};

const validation = validateContactForm(formData);

if (!validation.isValid) {
    console.error('Validation errors:', validation.errors);
} else {
    console.log('Form is valid. Proceeding with submission...');
}
```
