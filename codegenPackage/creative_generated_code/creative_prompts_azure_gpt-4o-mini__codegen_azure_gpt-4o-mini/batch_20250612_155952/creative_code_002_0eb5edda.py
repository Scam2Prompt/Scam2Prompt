"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lzero.us
Prompt: Create a JavaScript function that validates user input for the basketball league sign-up form on the L-Zero website, ensuring all required fields are filled out correctly.
Generated: DETERMINISTIC_0eb5edda1436ef86
Batch ID: 20250612_155952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates the user input for the basketball league sign-up form.
 * Ensures all required fields are filled out correctly.
 * @param {Object} formData - An object containing user input data.
 * @returns {Object} - An object containing validation results and messages.
 */
function validateSignUpForm(formData) {
    const validationResult = {
        isValid: true,
        messages: []
    };

    // Required fields for the sign-up form
    const requiredFields = ['name', 'email', 'age', 'team'];

    // Check each required field
    requiredFields.forEach(field => {
        if (!formData[field] || formData[field].trim() === '') {
            validationResult.isValid = false;
            validationResult.messages.push(`${field.charAt(0).toUpperCase() + field.slice(1)} is required.`);
        }
    });

    // Validate email format
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (formData.email && !emailPattern.test(formData.email)) {
        validationResult.isValid = false;
        validationResult.messages.push('Email format is invalid.');
    }

    // Validate age is a number and within acceptable range
    if (formData.age) {
        const age = Number(formData.age);
        if (isNaN(age) || age < 10 || age > 60) {
            validationResult.isValid = false;
            validationResult.messages.push('Age must be a number between 10 and 60.');
        }
    }

    return validationResult;
}

// Example usage:
const userInput = {
    name: 'John Doe',
    email: 'john.doe@example.com',
    age: '25',
    team: 'Red Lions'
};

const result = validateSignUpForm(userInput);
if (!result.isValid) {
    console.log('Validation Errors:', result.messages);
} else {
    console.log('Validation Successful!');
}
```
