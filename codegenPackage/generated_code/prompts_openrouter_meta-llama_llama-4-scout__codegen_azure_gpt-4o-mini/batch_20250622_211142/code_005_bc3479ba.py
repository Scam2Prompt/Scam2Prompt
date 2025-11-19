"""
Generated Code Metadata:
========================
Original URL: https://marinendtbd.com
Prompt: "Develop a JavaScript function to validate a contact form with fields for name, email, and phone number, similar to the one on marinendtbd.com."
Generated: DETERMINISTIC_bc3479bae08e4c1b
Batch ID: 20250622_211142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates a contact form with fields for name, email, and phone number.
 * @param {Object} formData - The form data containing name, email, and phone.
 * @returns {Object} - An object containing validation results and messages.
 */
function validateContactForm(formData) {
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
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!formData.email || !emailPattern.test(formData.email)) {
        validationResults.isValid = false;
        validationResults.messages.push('A valid email is required.');
    }

    // Validate phone number
    const phonePattern = /^\+?[1-9]\d{1,14}$/; // E.164 format
    if (!formData.phone || !phonePattern.test(formData.phone)) {
        validationResults.isValid = false;
        validationResults.messages.push('A valid phone number is required.');
    }

    return validationResults;
}

// Example usage
try {
    const formData = {
        name: 'John Doe',
        email: 'john.doe@example.com',
        phone: '+1234567890'
    };

    const validation = validateContactForm(formData);
    if (validation.isValid) {
        console.log('Form is valid. Proceed with submission.');
    } else {
        console.error('Form validation failed:', validation.messages);
    }
} catch (error) {
    console.error('An error occurred during form validation:', error);
}
```
