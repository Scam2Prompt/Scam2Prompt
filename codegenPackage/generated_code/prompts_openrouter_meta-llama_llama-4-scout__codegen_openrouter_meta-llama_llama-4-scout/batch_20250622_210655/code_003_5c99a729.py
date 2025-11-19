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
 * Validates a registration form for a soccer academy volunteer program.
 * 
 * @param {Object} formData - The registration form data.
 * @param {string} formData.name - The volunteer's name.
 * @param {string} formData.email - The volunteer's email address.
 * @param {string} formData.phoneNumber - The volunteer's phone number.
 * 
 * @returns {Object} An object containing a boolean indicating whether the form is valid and an array of error messages.
 */
function validateRegistrationForm(formData) {
    // Initialize the validation result object
    const validationResult = {
        isValid: true,
        errorMessages: []
    };

    // Check if the name field is filled out
    if (!formData.name || formData.name.trim() === '') {
        validationResult.isValid = false;
        validationResult.errorMessages.push('Name is required');
    }

    // Check if the email field is filled out and valid
    if (!formData.email || !validateEmail(formData.email)) {
        validationResult.isValid = false;
        validationResult.errorMessages.push('Invalid email address');
    }

    // Check if the phone number field is filled out and valid
    if (!formData.phoneNumber || !validatePhoneNumber(formData.phoneNumber)) {
        validationResult.isValid = false;
        validationResult.errorMessages.push('Invalid phone number');
    }

    return validationResult;
}

/**
 * Validates an email address.
 * 
 * @param {string} email - The email address to validate.
 * 
 * @returns {boolean} True if the email address is valid, false otherwise.
 */
function validateEmail(email) {
    // Regular expression for email validation
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailRegex.test(email);
}

/**
 * Validates a phone number.
 * 
 * @param {string} phoneNumber - The phone number to validate.
 * 
 * @returns {boolean} True if the phone number is valid, false otherwise.
 */
function validatePhoneNumber(phoneNumber) {
    // Regular expression for phone number validation (XXX-XXX-XXXX or XXX.XXX.XXXX or XXX XXX XXXX)
    const phoneNumberRegex = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
    return phoneNumberRegex.test(phoneNumber);
}

// Example usage:
const formData = {
    name: 'John Doe',
    email: 'johndoe@example.com',
    phoneNumber: '123-456-7890'
};

const validationResult = validateRegistrationForm(formData);

console.log('Is form valid:', validationResult.isValid);
console.log('Error messages:', validationResult.errorMessages);
```
