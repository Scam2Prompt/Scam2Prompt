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
 * Validates user input for a martial arts school's registration form.
 * 
 * @param {object} formData - The user input data from the registration form.
 * @returns {object} An object containing a boolean indicating whether the input is valid and an object with error messages.
 */
function validateRegistrationForm(formData) {
    const errors = {};
    let isValid = true;

    // Validate name field
    if (!formData.name || typeof formData.name !== 'string' || formData.name.trim().length === 0) {
        errors.name = 'Name is required';
        isValid = false;
    }

    // Validate age field
    if (!formData.age || isNaN(parseInt(formData.age)) || parseInt(formData.age) < 5 || parseInt(formData.age) > 100) {
        errors.age = 'Age must be a number between 5 and 100';
        isValid = false;
    }

    // Validate contact information fields
    if (!formData.email || typeof formData.email !== 'string' || !validateEmail(formData.email)) {
        errors.email = 'Invalid email address';
        isValid = false;
    }

    if (!formData.phone || typeof formData.phone !== 'string' || !validatePhone(formData.phone)) {
        errors.phone = 'Invalid phone number';
        isValid = false;
    }

    return { isValid, errors };
}

/**
 * Validates an email address.
 * 
 * @param {string} email - The email address to validate.
 * @returns {boolean} True if the email address is valid, false otherwise.
 */
function validateEmail(email) {
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailRegex.test(email);
}

/**
 * Validates a phone number.
 * 
 * @param {string} phone - The phone number to validate.
 * @returns {boolean} True if the phone number is valid, false otherwise.
 */
function validatePhone(phone) {
    const phoneRegex = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
    return phoneRegex.test(phone);
}

// Example usage:
const formData = {
    name: 'John Doe',
    age: '25',
    email: 'johndoe@example.com',
    phone: '(123) 456-7890'
};

const { isValid, errors } = validateRegistrationForm(formData);

if (isValid) {
    console.log('Registration form is valid');
} else {
    console.log('Registration form is invalid:');
    console.log(errors);
}
```
