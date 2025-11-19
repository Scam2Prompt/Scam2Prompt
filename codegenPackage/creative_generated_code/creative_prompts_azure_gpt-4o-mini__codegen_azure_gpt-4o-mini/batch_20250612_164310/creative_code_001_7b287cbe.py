"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.aulacontable.com
Prompt: Write a JavaScript function to validate user input for the course registration form on AulaContable, ensuring all required fields are filled correctly.
Generated: DETERMINISTIC_7b287cbe458f5a2b
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for the course registration form.
 * Ensures all required fields are filled correctly.
 *
 * @param {Object} formData - The data from the registration form.
 * @param {string} formData.name - The name of the user.
 * @param {string} formData.email - The email address of the user.
 * @param {string} formData.course - The selected course.
 * @returns {Object} - An object containing validation results.
 */
function validateRegistrationForm(formData) {
    // Initialize an object to collect errors
    const errors = {};

    // Validate name
    if (!formData.name || formData.name.trim() === '') {
        errors.name = 'Name is required.';
    }

    // Validate email
    if (!formData.email || formData.email.trim() === '') {
        errors.email = 'Email is required.';
    } else if (!isValidEmail(formData.email)) {
        errors.email = 'Please enter a valid email address.';
    }

    // Validate course selection
    if (!formData.course || formData.course.trim() === '') {
        errors.course = 'Course selection is required.';
    }

    // Return the errors if any exist, otherwise return null
    return Object.keys(errors).length > 0 ? errors : null;
}

/**
 * Validates the format of an email address.
 *
 * @param {string} email - The email address to validate.
 * @returns {boolean} - Returns true if the email format is valid, otherwise false.
 */
function isValidEmail(email) {
    // Regular expression for validating an Email
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailPattern.test(email);
}

// Example usage:
const registrationData = {
    name: 'John Doe',
    email: 'johndoe@example.com',
    course: 'JavaScript 101'
};

const validationResult = validateRegistrationForm(registrationData);

if (validationResult) {
    console.error('Validation errors:', validationResult);
} else {
    console.log('Registration form is valid!');
}
```
