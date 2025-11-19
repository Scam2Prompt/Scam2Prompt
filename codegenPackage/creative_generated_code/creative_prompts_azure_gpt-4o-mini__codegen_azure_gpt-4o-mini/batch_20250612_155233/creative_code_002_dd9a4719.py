"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welwitschia-aviation.com
Prompt: Create a function in JavaScript that validates user input for enrollment in the Avsec Supervisor Course at Welwitschia Aviation, ensuring all required fields are completed.
Generated: DETERMINISTIC_dd9a471975448a78
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for enrollment in the Avsec Supervisor Course at Welwitschia Aviation.
 * 
 * @param {Object} userInput - The input object containing user details.
 * @param {string} userInput.name - The name of the user.
 * @param {string} userInput.email - The email of the user.
 * @param {string} userInput.phone - The phone number of the user.
 * @param {string} userInput.age - The age of the user.
 * @returns {Object} - An object containing the validation result and errors, if any.
 */
function validateEnrollment(userInput) {
    // Initialize an empty array to collect validation errors
    const errors = [];
    
    // Check if the name is provided and is a string
    if (!userInput.name || typeof userInput.name !== 'string' || userInput.name.trim() === '') {
        errors.push('Name is required and must be a valid string.');
    }

    // Check if the email is provided and is in valid format
    if (!userInput.email || !isValidEmail(userInput.email)) {
        errors.push('A valid email is required.');
    }

    // Check if the phone number is provided and is a valid format
    if (!userInput.phone || !isValidPhone(userInput.phone)) {
        errors.push('A valid phone number is required.');
    }

    // Check if the age is provided and is a valid number
    if (!userInput.age || isNaN(userInput.age) || userInput.age < 18) {
        errors.push('Age is required and must be a number greater than or equal to 18.');
    }

    // Return validation result
    return {
        isValid: errors.length === 0,
        errors: errors
    };
}

/**
 * Validates the format of an email address.
 * 
 * @param {string} email - The email address to validate.
 * @returns {boolean} - Returns true if the email is in valid format, false otherwise.
 */
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

/**
 * Validates the format of a phone number.
 * 
 * @param {string} phone - The phone number to validate.
 * @returns {boolean} - Returns true if the phone number is in valid format, false otherwise.
 */
function isValidPhone(phone) {
    const phoneRegex = /^\+?[1-9]\d{1,14}$/; // E.164 format
    return phoneRegex.test(phone);
}

// Example Usage
const userInput = {
    name: 'John Doe',
    email: 'john.doe@example.com',
    phone: '+1234567890',
    age: 25
};

const validationResult = validateEnrollment(userInput);

if (validationResult.isValid) {
    console.log('Enrollment is valid. Proceeding with enrollment...');
} else {
    console.error('Enrollment validation failed:', validationResult.errors);
}
```
