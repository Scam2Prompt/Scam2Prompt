"""
Generated Code Metadata:
========================
Original URL: https://sherafight.nl
Prompt: Create a code snippet in JavaScript to validate user input for a martial arts school's registration form, including fields for name, age, and contact information.
Generated: DETERMINISTIC_6d93db92a997e9a2
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for a martial arts school's registration form.
 * @param {Object} formData - The data from the registration form.
 * @param {string} formData.name - The name of the user.
 * @param {number} formData.age - The age of the user.
 * @param {string} formData.contact - The contact information of the user.
 * @returns {Object} - An object containing validation results and messages.
 */
function validateRegistrationForm(formData) {
    const validationResults = {
        isValid: true,
        messages: []
    };

    // Validate name
    if (!formData.name || typeof formData.name !== 'string' || formData.name.trim().length === 0) {
        validationResults.isValid = false;
        validationResults.messages.push('Name is required and must be a valid string.');
    }

    // Validate age
    if (!formData.age || typeof formData.age !== 'number' || formData.age < 0 || formData.age > 120) {
        validationResults.isValid = false;
        validationResults.messages.push('Age is required and must be a number between 0 and 120.');
    }

    // Validate contact information
    const contactRegex = /^[\+]?[(]?[0-9]{1,4}[)]?[-\s\.]?[0-9]{1,4}[-\s\.]?[0-9]{1,4}[-\s\.]?[0-9]{1,9}$/;
    if (!formData.contact || typeof formData.contact !== 'string' || !contactRegex.test(formData.contact)) {
        validationResults.isValid = false;
        validationResults.messages.push('Contact information is required and must be a valid phone number.');
    }

    return validationResults;
}

// Example usage
const registrationData = {
    name: 'John Doe',
    age: 25,
    contact: '+1234567890'
};

const validation = validateRegistrationForm(registrationData);

if (validation.isValid) {
    console.log('Registration is valid.');
} else {
    console.error('Validation errors:', validation.messages);
}
```
