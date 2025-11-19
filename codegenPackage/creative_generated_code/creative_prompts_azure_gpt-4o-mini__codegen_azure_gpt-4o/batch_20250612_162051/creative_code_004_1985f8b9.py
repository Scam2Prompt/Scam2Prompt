"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://superiortitlemontana.com
Prompt: Develop a JavaScript function that validates user input in the property information request form on the Superior Title Montana website.
Generated: DETERMINISTIC_1985f8b9f2fd5379
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
 * Validates user input for the property information request form on Superior Title Montana website.
 * This function checks if required fields are filled, validates email format, and ensures no invalid characters.
 * @param {Object} formData - An object containing user input data. Example: { fullName: 'John Doe', email: 'john@example.com', propertyAddress: '123 Main St' }
 * @returns {Object} - An object containing validation status and error messages, if any. Example: { isValid: true, errors: [] }
 */
function validateFormInput(formData) {
    // Initialize validation result
    const validationResult = {
        isValid: true,
        errors: []
    };

    // Regular expression for email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    // Regular expression for invalid characters (used for checking names and addresses)
    const invalidCharRegex = /[^a-zA-Z0-9\s,.-]/;

    // Check if required fields are present and not empty
    if (!formData.fullName || formData.fullName.trim() === '') {
        validationResult.isValid = false;
        validationResult.errors.push('Full Name is required.');
    }

    if (!formData.email || formData.email.trim() === '') {
        validationResult.isValid = false;
        validationResult.errors.push('Email is required.');
    }

    if (!formData.propertyAddress || formData.propertyAddress.trim() === '') {
        validationResult.isValid = false;
        validationResult.errors.push('Property Address is required.');
    }

    // Validate email format
    if (formData.email && !emailRegex.test(formData.email)) {
        validationResult.isValid = false;
        validationResult.errors.push('Invalid email format.');
    }

    // Check for invalid characters in Full Name
    if (formData.fullName && invalidCharRegex.test(formData.fullName)) {
        validationResult.isValid = false;
        validationResult.errors.push('Full Name contains invalid characters.');
    }

    // Check for invalid characters in Property Address
    if (formData.propertyAddress && invalidCharRegex.test(formData.propertyAddress)) {
        validationResult.isValid = false;
        validationResult.errors.push('Property Address contains invalid characters.');
    }

    return validationResult;
}

// Example usage:
const formInput = {
    fullName: 'John Doe',
    email: 'john.doe@example.com',
    propertyAddress: '123 Main St'
};

const result = validateFormInput(formInput);
if (result.isValid) {
    console.log('Form input is valid.');
} else {
    console.log('Form input is invalid:', result.errors);
}
```
