"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sparkarabia.net
Prompt: Develop a JavaScript function that validates user input for a contact form to inquire about Spark Arabia's industrial services.
Generated: DETERMINISTIC_f14480e4d5304f4b
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for a contact form.
 * 
 * @param {Object} formData - The data from the contact form.
 * @param {string} formData.name - The name of the user.
 * @param {string} formData.email - The email address of the user.
 * @param {string} formData.phone - The phone number of the user.
 * @param {string} formData.message - The message from the user.
 * @returns {Object} - An object containing validation results.
 * @throws {Error} - Throws error if formData is not an object.
 */
function validateContactForm(formData) {
    // Check if formData is an object
    if (typeof formData !== 'object' || formData === null) {
        throw new Error('Invalid input: formData must be an object');
    }

    const validationResults = {
        isValid: true,
        errors: {}
    };

    // Validate name
    if (!formData.name || formData.name.trim() === '') {
        validationResults.isValid = false;
        validationResults.errors.name = 'Name is required.';
    }

    // Validate email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!formData.email || !emailRegex.test(formData.email)) {
        validationResults.isValid = false;
        validationResults.errors.email = 'A valid email address is required.';
    }

    // Validate phone number (optional)
    if (formData.phone && !/^\+?[1-9]\d{1,14}$/.test(formData.phone)) {
        validationResults.isValid = false;
        validationResults.errors.phone = 'A valid phone number is required.';
    }

    // Validate message
    if (!formData.message || formData.message.trim().length < 10) {
        validationResults.isValid = false;
        validationResults.errors.message = 'Message must be at least 10 characters long.';
    }

    return validationResults;
}

// Example usage
try {
    const formData = {
        name: 'John Doe',
        email: 'john@example.com',
        phone: '+1234567890',
        message: 'I would like to inquire about your services.'
    };

    const validation = validateContactForm(formData);
    if (validation.isValid) {
        console.log('Form is valid. Proceed with submission.');
    } else {
        console.error('Validation errors:', validation.errors);
    }
} catch (error) {
    console.error('Error during form validation:', error.message);
}
```
