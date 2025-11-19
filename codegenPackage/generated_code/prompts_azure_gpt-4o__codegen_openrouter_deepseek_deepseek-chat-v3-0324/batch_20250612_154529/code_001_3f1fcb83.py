"""
Generated Code Metadata:
========================
Original URL: https://panchapakesan.com
Prompt: Create a validation script in JavaScript for a ticket booking form that ensures the "Email Address" is properly formatted, the "Phone Number" contains only digits, and at least one "Preferred Method of Communication" is selected.
Generated: DETERMINISTIC_3f1fcb838e673f27
Batch ID: 20250612_154529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates a ticket booking form.
 * @param {Object} formData - The form data to validate.
 * @param {string} formData.email - The email address to validate.
 * @param {string} formData.phone - The phone number to validate.
 * @param {Array} formData.preferredCommunication - Array of selected communication methods.
 * @returns {Object} An object containing validation results.
 */
function validateBookingForm(formData) {
    const errors = {};
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const phoneRegex = /^\d+$/;

    // Validate email
    if (!formData.email) {
        errors.email = 'Email is required';
    } else if (!emailRegex.test(formData.email)) {
        errors.email = 'Please enter a valid email address';
    }

    // Validate phone number
    if (!formData.phone) {
        errors.phone = 'Phone number is required';
    } else if (!phoneRegex.test(formData.phone)) {
        errors.phone = 'Phone number should contain only digits';
    }

    // Validate preferred communication method
    if (!formData.preferredCommunication || formData.preferredCommunication.length === 0) {
        errors.preferredCommunication = 'Please select at least one preferred method of communication';
    }

    return {
        isValid: Object.keys(errors).length === 0,
        errors
    };
}

// Example usage:
/*
const formData = {
    email: 'test@example.com',
    phone: '1234567890',
    preferredCommunication: ['email', 'sms']
};

const validationResult = validateBookingForm(formData);
if (!validationResult.isValid) {
    console.log('Validation errors:', validationResult.errors);
} else {
    console.log('Form is valid');
}
*/
```
