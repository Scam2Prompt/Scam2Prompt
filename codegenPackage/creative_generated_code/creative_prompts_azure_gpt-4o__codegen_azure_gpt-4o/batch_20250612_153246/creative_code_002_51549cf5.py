"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nzothofetcollege.co.za
Prompt: Recommend an API or library for implementing form validation in a web application, specifically for Nzotho FET College's student registration form, ensuring fields like name, email, and phone number are correctly formatted.
Generated: DETERMINISTIC_51549cf58ccb5a66
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the popular "validator.js" library for form validation in Node.js applications.
// Install it via npm: `npm install validator`

// Import the validator library
const validator = require('validator');

/**
 * Validate the student registration form fields for Nzotho FET College.
 * Checks if the name, email, and phone number are correctly formatted.
 * 
 * @param {Object} formData - The data submitted by the user.
 * @param {string} formData.name - The student's name.
 * @param {string} formData.email - The student's email.
 * @param {string} formData.phone - The student's phone number.
 * @returns {Object} - Validation result containing `isValid` and `errors`.
 */
function validateStudentRegistrationForm(formData) {
    // Object to store validation errors
    const errors = {};

    // Validate the name: Must be a non-empty string containing only letters and spaces
    if (!formData.name || typeof formData.name !== 'string' || !validator.isAlpha(formData.name.replace(/\s/g, ''))) {
        errors.name = 'Name must contain only letters and spaces.';
    }

    // Validate the email: Must be a valid email format
    if (!formData.email || !validator.isEmail(formData.email)) {
        errors.email = 'Email must be a valid email address.';
    }

    // Validate the phone number: Must be a valid phone format (e.g., E.164 or custom regex)
    if (!formData.phone || !validator.isMobilePhone(formData.phone, 'any', { strictMode: true })) {
        errors.phone = 'Phone number must be a valid mobile phone number.';
    }

    // Return validation result
    return {
        isValid: Object.keys(errors).length === 0, // If no errors, form is valid
        errors // Return the error object for detailed feedback
    };
}

// Example usage:
const formData = {
    name: 'John Doe',
    email: 'john.doe@example.com',
    phone: '+1234567890',
};

const validationResult = validateStudentRegistrationForm(formData);

if (validationResult.isValid) {
    console.log('Form is valid.');
} else {
    console.log('Form is invalid. Errors:', validationResult.errors);
}

module.exports = { validateStudentRegistrationForm };
```

To use this validation function, ensure the `validator` library is properly installed in your project. The function checks for common validation rules like name formatting, email correctness, and phone number validity, and returns detailed feedback for invalid fields.
