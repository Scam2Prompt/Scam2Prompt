"""
Generated Code Metadata:
========================
Original URL: https://sherafight.nl
Prompt: Create a code snippet in JavaScript to validate user input for a martial arts school's registration form, including fields for name, age, and contact information.
Generated: DETERMINISTIC_6d93db92a997e9a2
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for a martial arts school registration form.
 * @param {Object} formData - The form data to validate.
 * @param {string} formData.name - The student's name.
 * @param {number} formData.age - The student's age.
 * @param {string} formData.email - The student's email.
 * @param {string} formData.phone - The student's phone number.
 * @returns {Object} An object containing validation results.
 */
function validateRegistrationForm(formData) {
    const errors = {};
    const { name, age, email, phone } = formData;

    // Name validation: must be at least 2 characters and only letters/spaces
    if (!name || typeof name !== 'string' || name.trim().length < 2) {
        errors.name = 'Name must be at least 2 characters long';
    } else if (!/^[a-zA-Z\s]+$/.test(name)) {
        errors.name = 'Name can only contain letters and spaces';
    }

    // Age validation: must be between 5 and 100
    if (!age || typeof age !== 'number' || isNaN(age)) {
        errors.age = 'Age must be a valid number';
    } else if (age < 5 || age > 100) {
        errors.age = 'Age must be between 5 and 100';
    }

    // Email validation: must be a valid email format
    if (!email || typeof email !== 'string') {
        errors.email = 'Email is required';
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        errors.email = 'Please enter a valid email address';
    }

    // Phone validation: must be at least 10 digits (simple validation)
    if (!phone || typeof phone !== 'string') {
        errors.phone = 'Phone number is required';
    } else if (!/^\d{10,}$/.test(phone.replace(/\D/g, ''))) {
        errors.phone = 'Please enter a valid phone number (at least 10 digits)';
    }

    return {
        isValid: Object.keys(errors).length === 0,
        errors
    };
}

// Example usage:
/*
const formData = {
    name: 'John Doe',
    age: 25,
    email: 'john@example.com',
    phone: '1234567890'
};

const validationResult = validateRegistrationForm(formData);
if (!validationResult.isValid) {
    console.log('Validation errors:', validationResult.errors);
} else {
    console.log('Form is valid');
}
*/
```
