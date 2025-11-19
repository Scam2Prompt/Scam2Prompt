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
 * Ensures all fields are filled out correctly.
 * 
 * @param {Object} formData - An object containing the form fields.
 * @returns {Object} - An object containing validation results.
 */
function validateContactForm(formData) {
    // Initialize an object to hold validation results
    const validationResults = {
        isValid: true,
        errors: {}
    };

    // Define required fields
    const requiredFields = ['name', 'email', 'phone', 'message'];

    // Check each required field
    requiredFields.forEach(field => {
        if (!formData[field] || formData[field].trim() === '') {
            validationResults.isValid = false;
            validationResults.errors[field] = `${field.charAt(0).toUpperCase() + field.slice(1)} is required.`;
        }
    });

    // Validate email format
    if (formData.email && !isValidEmail(formData.email)) {
        validationResults.isValid = false;
        validationResults.errors.email = 'Email format is invalid.';
    }

    // Validate phone number format (simple regex for demonstration)
    if (formData.phone && !isValidPhone(formData.phone)) {
        validationResults.isValid = false;
        validationResults.errors.phone = 'Phone number format is invalid.';
    }

    return validationResults;
}

/**
 * Validates the email format using a regular expression.
 * 
 * @param {string} email - The email address to validate.
 * @returns {boolean} - True if valid, false otherwise.
 */
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

/**
 * Validates the phone number format using a simple regex.
 * 
 * @param {string} phone - The phone number to validate.
 * @returns {boolean} - True if valid, false otherwise.
 */
function isValidPhone(phone) {
    const phoneRegex = /^\+?[1-9]\d{1,14}$/; // E.164 format
    return phoneRegex.test(phone);
}

// Example usage
const formData = {
    name: 'John Doe',
    email: 'john.doe@example.com',
    phone: '+1234567890',
    message: 'Hello, I would like to inquire about...'
};

const validation = validateContactForm(formData);
if (!validation.isValid) {
    console.error('Validation errors:', validation.errors);
} else {
    console.log('Form is valid. Proceed with submission.');
}
```
