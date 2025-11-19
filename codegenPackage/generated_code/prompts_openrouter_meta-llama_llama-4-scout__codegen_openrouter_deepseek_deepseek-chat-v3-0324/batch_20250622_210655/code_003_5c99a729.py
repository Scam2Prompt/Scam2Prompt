"""
Generated Code Metadata:
========================
Original URL: https://jsa.academy
Prompt: "Create a JavaScript function to validate a registration form for a soccer academy volunteer program, ensuring that fields such as name, email, and phone number are properly filled out."
Generated: DETERMINISTIC_5c99a729936fca7b
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates a soccer academy volunteer registration form.
 * @param {Object} formData - The form data object containing volunteer information
 * @param {string} formData.name - Volunteer's full name
 * @param {string} formData.email - Volunteer's email address
 * @param {string} formData.phone - Volunteer's phone number
 * @param {string} [formData.age] - Volunteer's age (optional)
 * @param {string} [formData.experience] - Volunteer's soccer experience (optional)
 * @returns {Object} An object containing validation results: { isValid: boolean, errors: Object }
 */
function validateVolunteerForm(formData) {
    const errors = {};
    const { name, email, phone, age, experience } = formData;

    // Name validation: required, at least 2 characters
    if (!name || name.trim().length < 2) {
        errors.name = 'Please enter a valid name (at least 2 characters)';
    }

    // Email validation: required, valid format
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!email || !emailRegex.test(email)) {
        errors.email = 'Please enter a valid email address';
    }

    // Phone validation: required, at least 10 digits (allowing various formats)
    const phoneDigits = phone ? phone.replace(/\D/g, '') : '';
    if (!phone || phoneDigits.length < 10) {
        errors.phone = 'Please enter a valid phone number (at least 10 digits)';
    }

    // Age validation: optional, but must be a positive number if provided
    if (age && (isNaN(age) || parseInt(age) <= 0)) {
        errors.age = 'Please enter a valid age';
    }

    // Experience validation: optional, but must not be empty if provided
    if (experience && experience.trim().length === 0) {
        errors.experience = 'Please provide valid experience information';
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
    email: 'john@example.com',
    phone: '(123) 456-7890',
    age: '25',
    experience: 'Played soccer in high school'
};

const validationResult = validateVolunteerForm(formData);
if (!validationResult.isValid) {
    console.log('Validation errors:', validationResult.errors);
} else {
    console.log('Form is valid');
}
*/
```
