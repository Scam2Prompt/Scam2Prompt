"""
Generated Code Metadata:
========================
Original URL: https://cpncg.edu.mx
Prompt: Write a JavaScript function that validates user input for a school registration form, inspired by the Colegio Panamericano's enrollment process.
Generated: DETERMINISTIC_adf65f12f7ac3117
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for a school registration form.
 * 
 * @param {Object} formData - The data from the registration form.
 * @param {string} formData.name - The name of the student.
 * @param {string} formData.email - The email address of the student.
 * @param {string} formData.phone - The phone number of the student.
 * @param {number} formData.age - The age of the student.
 * @returns {Object} - An object containing validation results.
 */
function validateRegistrationForm(formData) {
    const errors = {};

    // Validate name
    if (!formData.name || formData.name.trim() === '') {
        errors.name = 'Name is required.';
    } else if (formData.name.length < 2) {
        errors.name = 'Name must be at least 2 characters long.';
    }

    // Validate email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!formData.email || formData.email.trim() === '') {
        errors.email = 'Email is required.';
    } else if (!emailRegex.test(formData.email)) {
        errors.email = 'Email is not valid.';
    }

    // Validate phone
    const phoneRegex = /^\d{10}$/; // Assuming a 10-digit phone number
    if (!formData.phone || formData.phone.trim() === '') {
        errors.phone = 'Phone number is required.';
    } else if (!phoneRegex.test(formData.phone)) {
        errors.phone = 'Phone number must be 10 digits.';
    }

    // Validate age
    if (formData.age === undefined || formData.age === null) {
        errors.age = 'Age is required.';
    } else if (formData.age < 5 || formData.age > 18) {
        errors.age = 'Age must be between 5 and 18.';
    }

    // Return validation results
    return {
        isValid: Object.keys(errors).length === 0,
        errors: errors
    };
}

// Example usage
const registrationData = {
    name: 'John Doe',
    email: 'john.doe@example.com',
    phone: '1234567890',
    age: 15
};

const validationResult = validateRegistrationForm(registrationData);
if (!validationResult.isValid) {
    console.error('Validation errors:', validationResult.errors);
} else {
    console.log('Registration data is valid.');
}
```
