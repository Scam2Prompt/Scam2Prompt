"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deepbook.online
Prompt: Write a JavaScript function that validates user input for a plumbing service quote request form, ensuring all necessary fields are filled out correctly.
Generated: DETERMINISTIC_950979b311f6c886
Batch ID: 20250612_155337
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates the user input from the plumbing service quote request form.
 * Ensures that all necessary fields are filled out correctly.
 * 
 * @param {Object} formData - The user's input data from the form.
 * @returns {Object} - An object containing validation results.
 */
function validateQuoteRequest(formData) {
    const errors = {};

    // Check if the name field is filled
    if (!formData.name || formData.name.trim() === '') {
        errors.name = 'Name is required.';
    }

    // Check if the email field is filled and valid
    if (!formData.email || formData.email.trim() === '') {
        errors.email = 'Email is required.';
    } else if (!isValidEmail(formData.email)) {
        errors.email = 'Email is invalid.';
    }

    // Check if the phone number field is filled
    if (!formData.phone || formData.phone.trim() === '') {
        errors.phone = 'Phone number is required.';
    } else if (!isValidPhoneNumber(formData.phone)) {
        errors.phone = 'Phone number is invalid.';
    }

    // Check if the service type is selected
    if (!formData.serviceType || formData.serviceType.trim() === '') {
        errors.serviceType = 'Service type is required.';
    }

    // Check if the description field is filled
    if (!formData.description || formData.description.trim() === '') {
        errors.description = 'Description is required.';
    }

    return {
        isValid: Object.keys(errors).length === 0,
        errors
    };
}

/**
 * Validates the format of the email address.
 *
 * @param {string} email - The email address to validate.
 * @returns {boolean} - Returns true if the email format is valid, otherwise false.
 */
function isValidEmail(email) {
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailPattern.test(email);
}

/**
 * Validates the format of the phone number.
 *
 * @param {string} phone - The phone number to validate.
 * @returns {boolean} - Returns true if the phone number format is valid, otherwise false.
 */
function isValidPhoneNumber(phone) {
    const phonePattern = /^\+?[1-9]\d{1,14}$/; // E.164 format
    return phonePattern.test(phone);
}

// Example usage:
const formData = {
    name: "John Doe",
    email: "john.doe@example.com",
    phone: "+1234567890",
    serviceType: "Leak Repair",
    description: "There is a leak under the kitchen sink."
};

const validationResults = validateQuoteRequest(formData);

if (!validationResults.isValid) {
    console.error('Validation errors:', validationResults.errors);
} else {
    console.log('Form is valid. Proceed with the quote request.');
}
```
