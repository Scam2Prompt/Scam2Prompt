"""
Generated Code Metadata:
========================
Original URL: https://the-profit-builder.com
Prompt: Create a function in JavaScript to validate user input for a registration form, ensuring fields like name, email, and phone number are correctly formatted, similar to the Profit Builder app's registration process.
Generated: DETERMINISTIC_d611cc8bbf99a191
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user registration form input fields
 * @param {Object} formData - Object containing form field values
 * @returns {Object} - Object containing validation results and error messages
 */
function validateRegistrationForm(formData) {
    const errors = {};
    const result = { isValid: true, errors };

    // Validate name field (only letters and spaces, 2-50 characters)
    if (!formData.name || !formData.name.trim()) {
        errors.name = 'Name is required';
        result.isValid = false;
    } else if (!/^[a-zA-Z\s]{2,50}$/.test(formData.name.trim())) {
        errors.name = 'Name must be 2-50 characters and contain only letters';
        result.isValid = false;
    }

    // Validate email field
    if (!formData.email || !formData.email.trim()) {
        errors.email = 'Email is required';
        result.isValid = false;
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email.trim())) {
        errors.email = 'Please enter a valid email address';
        result.isValid = false;
    }

    // Validate phone number (basic international format validation)
    if (formData.phone && formData.phone.trim()) {
        if (!/^[\d\s\+\(\)-]{10,20}$/.test(formData.phone.trim())) {
            errors.phone = 'Please enter a valid phone number';
            result.isValid = false;
        }
    }

    // Validate password (at least 8 chars, 1 uppercase, 1 lowercase, 1 number)
    if (!formData.password) {
        errors.password = 'Password is required';
        result.isValid = false;
    } else if (formData.password.length < 8) {
        errors.password = 'Password must be at least 8 characters';
        result.isValid = false;
    } else if (!/(?=.*[a-z])(?=.*[A-Z])(?=.*\d)/.test(formData.password)) {
        errors.password = 'Password must contain at least one uppercase letter, one lowercase letter, and one number';
        result.isValid = false;
    }

    // Validate password confirmation
    if (formData.password !== formData.passwordConfirm) {
        errors.passwordConfirm = 'Passwords do not match';
        result.isValid = false;
    }

    // Validate terms agreement
    if (!formData.agreeTerms) {
        errors.agreeTerms = 'You must agree to the terms and conditions';
        result.isValid = false;
    }

    return result;
}

// Example usage:
// const formData = {
//     name: 'John Doe',
//     email: 'john@example.com',
//     phone: '+1234567890',
//     password: 'Password123',
//     passwordConfirm: 'Password123',
//     agreeTerms: true
// };
// const validation = validateRegistrationForm(formData);
// if (!validation.isValid) {
//     console.log('Validation errors:', validation.errors);
// } else {
//     console.log('Form is valid');
// }
```
