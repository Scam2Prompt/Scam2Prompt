"""
Generated Code Metadata:
========================
Original URL: https://spanglerroofingllc.com
Prompt: Create a JavaScript function that validates user input for a roofing service request form, ensuring all required fields are filled out correctly.
Generated: DETERMINISTIC_c704ff46a9125644
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for a roofing service request form.
 * Ensures all required fields are filled out correctly.
 * 
 * @param {Object} formData - The data from the roofing service request form.
 * @returns {Object} - An object containing validation results and messages.
 */
function validateRoofingServiceRequest(formData) {
    // Initialize an object to hold validation results
    const validationResults = {
        isValid: true,
        messages: []
    };

    // Check if the name field is filled out
    if (!formData.name || formData.name.trim() === '') {
        validationResults.isValid = false;
        validationResults.messages.push('Name is required.');
    }

    // Check if the email field is filled out and valid
    if (!formData.email || !isValidEmail(formData.email)) {
        validationResults.isValid = false;
        validationResults.messages.push('A valid email is required.');
    }

    // Check if the phone number field is filled out and valid
    if (!formData.phone || !isValidPhone(formData.phone)) {
        validationResults.isValid = false;
        validationResults.messages.push('A valid phone number is required.');
    }

    // Check if the address field is filled out
    if (!formData.address || formData.address.trim() === '') {
        validationResults.isValid = false;
        validationResults.messages.push('Address is required.');
    }

    // Check if the service type is selected
    if (!formData.serviceType || formData.serviceType === 'none') {
        validationResults.isValid = false;
        validationResults.messages.push('Please select a service type.');
    }

    return validationResults;
}

/**
 * Validates the email format using a regular expression.
 * 
 * @param {string} email - The email address to validate.
 * @returns {boolean} - True if the email is valid, false otherwise.
 */
function isValidEmail(email) {
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailPattern.test(email);
}

/**
 * Validates the phone number format using a regular expression.
 * 
 * @param {string} phone - The phone number to validate.
 * @returns {boolean} - True if the phone number is valid, false otherwise.
 */
function isValidPhone(phone) {
    const phonePattern = /^\+?[1-9]\d{1,14}$/; // E.164 format
    return phonePattern.test(phone);
}

// Example usage
const formData = {
    name: 'John Doe',
    email: 'john.doe@example.com',
    phone: '+1234567890',
    address: '123 Main St, Anytown, USA',
    serviceType: 'roofRepair'
};

const validation = validateRoofingServiceRequest(formData);
if (!validation.isValid) {
    console.error('Validation errors:', validation.messages);
} else {
    console.log('Form is valid. Proceed with submission.');
}
```
