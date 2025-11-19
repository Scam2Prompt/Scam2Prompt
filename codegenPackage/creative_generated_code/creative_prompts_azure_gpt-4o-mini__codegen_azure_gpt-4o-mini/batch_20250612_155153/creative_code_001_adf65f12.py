"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cpncg.edu.mx
Prompt: Write a JavaScript function that validates user input for a school registration form, inspired by the Colegio Panamericano's enrollment process.
Generated: DETERMINISTIC_adf65f12f7ac3117
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for a school registration form.
 * @param {Object} formData - The user input data from the registration form.
 * @returns {Object} - An object containing the validation result and any error messages.
 */
function validateRegistrationForm(formData) {
    const errors = {};

    // Validate name
    if (!formData.name || typeof formData.name !== 'string' || formData.name.trim() === '') {
        errors.name = 'Name is required and must be a valid string.';
    }

    // Validate age
    if (!formData.age || typeof formData.age !== 'number' || formData.age < 5 || formData.age > 18) {
        errors.age = 'Age is required and must be between 5 and 18.';
    }

    // Validate email
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!formData.email || typeof formData.email !== 'string' || !emailPattern.test(formData.email)) {
        errors.email = 'A valid email address is required.';
    }

    // Validate phone number
    const phonePattern = /^\d{10}$/; // Assuming a 10-digit phone number
    if (!formData.phone || typeof formData.phone !== 'string' || !phonePattern.test(formData.phone)) {
        errors.phone = 'Phone number is required and must be a 10-digit number.';
    }

    // Validate address
    if (!formData.address || typeof formData.address !== 'string' || formData.address.trim() === '') {
        errors.address = 'Address is required and must be a valid string.';
    }

    // Validate selected courses
    if (!Array.isArray(formData.courses) || formData.courses.length === 0) {
        errors.courses = 'At least one course must be selected.';
    }

    // Return the result
    return {
        isValid: Object.keys(errors).length === 0,
        errors: errors
    };
}

// Example usage:
const userInput = {
    name: 'John Doe',
    age: 14,
    email: 'john.doe@example.com',
    phone: '1234567890',
    address: '123 Main St, Anytown',
    courses: ['Math', 'Science']
};

const validationResult = validateRegistrationForm(userInput);

if (validationResult.isValid) {
    console.log('Registration is valid!');
} else {
    console.error('Validation errors:', validationResult.errors);
}
```
