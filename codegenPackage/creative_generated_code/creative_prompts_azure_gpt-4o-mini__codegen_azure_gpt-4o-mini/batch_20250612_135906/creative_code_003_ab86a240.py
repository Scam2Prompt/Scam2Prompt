"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perrigo-claims.info
Prompt: Develop a JavaScript function that validates user input for a contact form, ensuring all fields are filled out correctly, inspired by the contact information layout on the Perrigo Claims site.
Generated: DETERMINISTIC_ab86a240225bbcfa
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates the user input for a contact form.
 * Ensures all required fields are filled out correctly.
 * 
 * @param {Object} formData - An object containing the form data.
 * @returns {Object} - An object containing validation results and messages.
 */
function validateContactForm(formData) {
    const validationResults = {
        isValid: true,
        messages: []
    };

    // Define required fields
    const requiredFields = ['name', 'email', 'phone', 'message'];

    // Check for empty required fields
    requiredFields.forEach(field => {
        if (!formData[field] || formData[field].trim() === '') {
            validationResults.isValid = false;
            validationResults.messages.push(`${field.charAt(0).toUpperCase() + field.slice(1)} is required.`);
        }
    });

    // Validate email format
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (formData.email && !emailPattern.test(formData.email)) {
        validationResults.isValid = false;
        validationResults.messages.push('Email format is invalid.');
    }

    // Validate phone number format (simple check, can be improved)
    const phonePattern = /^\+?[0-9]{10,15}$/;
    if (formData.phone && !phonePattern.test(formData.phone)) {
        validationResults.isValid = false;
        validationResults.messages.push('Phone number must be between 10 to 15 digits, including country code if necessary.');
    }

    // Validate message length
    if (formData.message && formData.message.length < 10) {
        validationResults.isValid = false;
        validationResults.messages.push('Message must be at least 10 characters long.');
    }

    return validationResults;
}

// Example usage:
const userInput = {
    name: 'John Doe',
    email: 'john.doe@example.com',
    phone: '+12345678901',
    message: 'Hello, I would like to inquire about...'
};

const validation = validateContactForm(userInput);
if (!validation.isValid) {
    console.error('Validation Errors:', validation.messages);
} else {
    console.log('Validation Successful! Form is ready to be submitted.');
}
```
