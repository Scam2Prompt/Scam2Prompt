"""
Generated Code Metadata:
========================
Original URL: https://jaraesconstruction.com
Prompt: "Create a JavaScript function to validate user input for a free roof inspection request form, ensuring that all required fields (e.g., name, email, phone number) are filled in correctly, as seen on JaraEs Construction LLC's website."
Generated: DETERMINISTIC_7e3a720bfd236f6d
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for a free roof inspection request form.
 * Ensures that all required fields (name, email, phone number) are filled in correctly.
 * 
 * @param {Object} formData - The user input data from the form.
 * @param {string} formData.name - The name of the user.
 * @param {string} formData.email - The email address of the user.
 * @param {string} formData.phone - The phone number of the user.
 * @returns {Object} - An object containing validation results and messages.
 */
function validateRoofInspectionRequest(formData) {
    const validationResults = {
        isValid: true,
        messages: []
    };

    // Validate name
    if (!formData.name || formData.name.trim() === '') {
        validationResults.isValid = false;
        validationResults.messages.push('Name is required.');
    }

    // Validate email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!formData.email || !emailRegex.test(formData.email)) {
        validationResults.isValid = false;
        validationResults.messages.push('A valid email address is required.');
    }

    // Validate phone number
    const phoneRegex = /^\+?[1-9]\d{1,14}$/; // E.164 format
    if (!formData.phone || !phoneRegex.test(formData.phone)) {
        validationResults.isValid = false;
        validationResults.messages.push('A valid phone number is required.');
    }

    return validationResults;
}

// Example usage:
const userInput = {
    name: 'John Doe',
    email: 'john.doe@example.com',
    phone: '+1234567890'
};

const validation = validateRoofInspectionRequest(userInput);
if (!validation.isValid) {
    console.error('Validation errors:', validation.messages);
} else {
    console.log('Validation successful! Proceed with the request.');
}
```
