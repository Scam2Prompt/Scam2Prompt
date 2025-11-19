"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lestersplace.com
Prompt: Create a JavaScript function that validates user input for a contact form aimed at assisted living services, ensuring all fields are filled out correctly before submission.
Generated: DETERMINISTIC_70085bb296eba252
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for a contact form aimed at assisted living services.
 * Ensures that all required fields are filled out correctly before submission.
 * 
 * @param {Object} formData - An object containing the form input values.
 * @returns {Object} - An object containing validation results and error messages if any.
 */
function validateContactForm(formData) {
    const errors = {};
    const requiredFields = ['name', 'email', 'phone', 'message'];

    // Check for required fields
    requiredFields.forEach(field => {
        if (!formData[field] || formData[field].trim() === '') {
            errors[field] = `${field.charAt(0).toUpperCase() + field.slice(1)} is required.`;
        }
    });

    // Validate email format
    if (formData.email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
        errors.email = 'Please enter a valid email address.';
    }

    // Validate phone format (assuming US phone numbers)
    if (formData.phone && !/^\+?(\d{1,3})?[-. ]?\(?(0\d{2})\)?[-. ]?(\d{3})[-. ]?(\d{4})$/.test(formData.phone)) {
        errors.phone = 'Please enter a valid phone number.';
    }

    // Check message length
    if (formData.message && formData.message.length < 10) {
        errors.message = 'Message must be at least 10 characters long.';
    }

    // Return validation results
    return {
        isValid: Object.keys(errors).length === 0,
        errors: errors
    };
}

// Example usage:
const formData = {
    name: 'John Doe',
    email: 'john.doe@example.com',
    phone: '+1234567890',
    message: 'Looking for information.'
};

const validationResult = validateContactForm(formData);

if (!validationResult.isValid) {
    console.error('Validation errors:', validationResult.errors);
} else {
    console.log('Form is valid. Proceed with submission.');
}
```
