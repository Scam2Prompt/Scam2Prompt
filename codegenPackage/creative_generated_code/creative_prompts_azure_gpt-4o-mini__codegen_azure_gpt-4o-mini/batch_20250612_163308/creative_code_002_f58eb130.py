"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kingroofing.com
Prompt: Create a function in JavaScript that validates user input for a roofing service request form, ensuring all required fields are filled out correctly before submission.
Generated: DETERMINISTIC_f58eb130d65a40be
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates the user input for a roofing service request form.
 * Ensures all required fields are filled out correctly before submission.
 *
 * @param {Object} formData - The data object containing form fields.
 * @returns {Object} - An object containing validation results and error messages.
 */
function validateRoofingServiceRequest(formData) {
    // Initialize an object to hold validation results
    const validationResults = {
        isValid: true,
        errors: {}
    };

    // Required fields array
    const requiredFields = ['name', 'email', 'phone', 'address', 'description'];

    // Loop through required fields to check for validity
    requiredFields.forEach(field => {
        if (!formData[field] || formData[field].trim() === '') {
            validationResults.isValid = false;
            validationResults.errors[field] = `${field.charAt(0).toUpperCase() + field.slice(1)} is required.`;
        }
    });

    // Validate email format if provided
    if (formData.email && !isValidEmail(formData.email)) {
        validationResults.isValid = false;
        validationResults.errors.email = "Email format is invalid.";
    }

    // Validate phone number format if provided
    if (formData.phone && !isValidPhone(formData.phone)) {
        validationResults.isValid = false;
        validationResults.errors.phone = "Phone number format is invalid.";
    }

    return validationResults;
}

/**
 * Validates the format of an email address.
 *
 * @param {string} email - The email address to validate.
 * @returns {boolean} - True if the email is valid, false otherwise.
 */
function isValidEmail(email) {
    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailPattern.test(email);
}

/**
 * Validates the format of a phone number.
 *
 * @param {string} phone - The phone number to validate.
 * @returns {boolean} - True if the phone number is valid, false otherwise.
 */
function isValidPhone(phone) {
    const phonePattern = /^\+?[1-9]\d{1,14}$/; // E.164 format
    return phonePattern.test(phone);
}

// Example usage:
const formData = {
    name: 'John Doe',
    email: 'john.doe@example.com',
    phone: '+1234567890',
    address: '123 Main St, Anytown, USA',
    description: 'Need a roof replacement.'
};

const validation = validateRoofingServiceRequest(formData);

if (validation.isValid) {
    console.log("Form is valid. Proceed to submission.");
} else {
    console.error("Form validation failed:", validation.errors);
}
```
