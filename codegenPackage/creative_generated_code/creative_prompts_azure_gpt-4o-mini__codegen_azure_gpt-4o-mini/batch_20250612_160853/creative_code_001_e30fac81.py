"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://patenteimpresa.it
Prompt: Write a JavaScript function that validates user input for the registration form on the "Patente d'impresa" website, ensuring all required fields are filled correctly.
Generated: DETERMINISTIC_e30fac8156520eee
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for the registration form on the "Patente d'impresa" website.
 * @param {Object} formData - An object containing form field values.
 * @returns {Object} - An object containing validation results and error messages.
 */
function validateRegistrationForm(formData) {
    // Initialize an object to hold validation results
    const validationResults = {
        isValid: true,
        errors: {}
    };

    // Check if the required fields are filled
    if (!formData.name || formData.name.trim() === '') {
        validationResults.isValid = false;
        validationResults.errors.name = 'Name is required.';
    }

    if (!formData.email || !isValidEmail(formData.email)) {
        validationResults.isValid = false;
        validationResults.errors.email = 'A valid email is required.';
    }

    if (!formData.password || formData.password.length < 6) {
        validationResults.isValid = false;
        validationResults.errors.password = 'Password must be at least 6 characters long.';
    }

    if (!formData.confirmPassword || formData.confirmPassword !== formData.password) {
        validationResults.isValid = false;
        validationResults.errors.confirmPassword = 'Passwords do not match.';
    }

    // You can add more validation checks as needed

    return validationResults;
}

/**
 * Validates the email format using a regular expression.
 * @param {string} email - The email address to validate.
 * @returns {boolean} - True if the email is valid, otherwise false.
 */
function isValidEmail(email) {
    // Regular expression to validate email format
    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailPattern.test(email);
}

// Example usage:
const userInput = {
    name: 'John Doe',
    email: 'john.doe@example.com',
    password: 'password123',
    confirmPassword: 'password123'
};

const validationResult = validateRegistrationForm(userInput);

if (!validationResult.isValid) {
    console.error('Validation failed:', validationResult.errors);
} else {
    console.log('Validation succeeded. User can be registered.');
}
```
