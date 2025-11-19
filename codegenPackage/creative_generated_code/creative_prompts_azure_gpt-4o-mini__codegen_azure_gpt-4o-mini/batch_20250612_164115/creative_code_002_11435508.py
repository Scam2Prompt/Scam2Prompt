"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unitedcabinetry.com.au
Prompt: Create a JavaScript function that validates user input for a cabinetry consultation request form, ensuring all required fields are filled out correctly.
Generated: DETERMINISTIC_11435508d7fabacc
Batch ID: 20250612_164115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for a cabinetry consultation request form.
 * Ensures all required fields are filled out correctly.
 *
 * @param {Object} formData - The data from the form to validate.
 * @param {string} formData.name - The name of the user.
 * @param {string} formData.email - The user's email address.
 * @param {string} formData.phone - The user's phone number.
 * @param {string} formData.projectDetails - Details about the cabinetry project.
 * @returns {Object} - An object containing the validation result and messages.
 */
function validateCabinetryConsultation(formData) {
    const errors = {}; // Object to hold error messages

    // Check if name is provided
    if (!formData.name || formData.name.trim() === '') {
        errors.name = 'Name is required.';
    }

    // Check if email is provided and is valid
    if (!formData.email || formData.email.trim() === '') {
        errors.email = 'Email is required.';
    } else if (!isValidEmail(formData.email)) {
        errors.email = 'Invalid email format.';
    }

    // Check if phone number is provided
    if (!formData.phone || formData.phone.trim() === '') {
        errors.phone = 'Phone number is required.';
    }

    // Check if project details are provided
    if (!formData.projectDetails || formData.projectDetails.trim() === '') {
        errors.projectDetails = 'Project details are required.';
    }

    // Return validation result
    return {
        isValid: Object.keys(errors).length === 0,
        errors: errors
    };
}

/**
 * Validates the format of an email address.
 *
 * @param {string} email - The email address to validate.
 * @returns {boolean} - True if the email format is valid, otherwise false.
 */
function isValidEmail(email) {
    // Simple regex for email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Example usage:
const userInput = {
    name: 'John Doe',
    email: 'john.doe@example.com',
    phone: '1234567890',
    projectDetails: 'I need custom cabinets for my kitchen.'
};

const validationResult = validateCabinetryConsultation(userInput);
if (!validationResult.isValid) {
    console.error('Validation errors:', validationResult.errors);
} else {
    console.log('Validation successful. Form is ready to be submitted.');
}
```
