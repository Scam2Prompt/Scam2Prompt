"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://renovation-toiture-toulouse.com
Prompt: Create a JavaScript function that validates user input for a contact form on a roofing service website, ensuring all required fields are filled out correctly.
Generated: DETERMINISTIC_d47c835209daeb2a
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for a contact form on a roofing service website.
 * 
 * @param {Object} formData - An object containing the form input values.
 * @returns {Object} - An object containing validation results including a success flag and error messages.
 */
function validateContactForm(formData) {
    const errors = {};
    let isValid = true;

    // Define required fields
    const requiredFields = ['name', 'email', 'phone', 'message'];

    // Check for required fields
    requiredFields.forEach(field => {
        if (!formData[field] || formData[field].trim() === '') {
            errors[field] = `${field.charAt(0).toUpperCase() + field.slice(1)} is required.`;
            isValid = false;
        }
    });

    // Validate email format
    if (formData.email && !validateEmail(formData.email)) {
        errors.email = 'Please enter a valid email address.';
        isValid = false;
    }

    // Validate phone number format (simple regex for demonstration)
    if (formData.phone && !validatePhone(formData.phone)) {
        errors.phone = 'Please enter a valid phone number.';
        isValid = false;
    }

    return {
        isValid,
        errors
    };
}

/**
 * Validates email format using a regular expression.
 * 
 * @param {string} email - The email address to validate.
 * @returns {boolean} - True if the email is valid, otherwise false.
 */
function validateEmail(email) {
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailPattern.test(email);
}

/**
 * Validates phone number format using a simple regex.
 * 
 * @param {string} phone - The phone number to validate.
 * @returns {boolean} - True if the phone number is valid, otherwise false.
 */
function validatePhone(phone) {
    const phonePattern = /^\+?[1-9]\d{1,14}$/; // E.164 format
    return phonePattern.test(phone);
}

// Example usage:
const formData = {
    name: 'John Doe',
    email: 'john.doe@example.com',
    phone: '+1234567890',
    message: 'I would like a roofing quote.'
};

const validationResult = validateContactForm(formData);
if (!validationResult.isValid) {
    console.log('Validation failed:', validationResult.errors);
} else {
    console.log('Validation successful!');
}
```
