"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.albertozofrea.it
Prompt: Construct a JavaScript function that validates user input for a contact form based on the details provided on the Alberto Zofrea site.
Generated: DETERMINISTIC_82a57292a4e49156
Batch ID: 20250612_162051
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
 * @param {Object} formData - The contact form data containing name, email, and message.
 * @returns {Object} - An object containing validation results and messages.
 */
function validateContactForm(formData) {
    const validationResults = {
        isValid: true,
        errors: []
    };

    // Validate Name
    if (!formData.name || typeof formData.name !== 'string' || formData.name.trim().length < 2) {
        validationResults.isValid = false;
        validationResults.errors.push('Name is required and must be at least 2 characters long.');
    }

    // Validate Email
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Basic email regex
    if (!formData.email || !emailPattern.test(formData.email)) {
        validationResults.isValid = false;
        validationResults.errors.push('A valid email address is required.');
    }

    // Validate Message
    if (!formData.message || typeof formData.message !== 'string' || formData.message.trim().length < 10) {
        validationResults.isValid = false;
        validationResults.errors.push('Message is required and must be at least 10 characters long.');
    }

    return validationResults;
}

// Example usage
try {
    const formData = {
        name: 'John Doe',
        email: 'john.doe@example.com',
        message: 'Hello, I would like to inquire about your services.'
    };

    const validationResponse = validateContactForm(formData);
    if (validationResponse.isValid) {
        console.log('Form is valid. Proceed with submission.');
    } else {
        console.error('Validation errors:', validationResponse.errors);
    }
} catch (error) {
    console.error('An error occurred during validation:', error);
}
```
