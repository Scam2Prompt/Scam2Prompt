"""
Generated Code Metadata:
========================
Original URL: https://indusur.com
Prompt: "Generate a JavaScript function to validate contact form data for a company like Indusur, ensuring fields such as name, email, company, and phone number are properly formatted."
Generated: DETERMINISTIC_918c8f9cc6b715e1
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates contact form data.
 * 
 * @param {object} data - The contact form data to be validated.
 * @param {string} data.name - The user's name.
 * @param {string} data.email - The user's email address.
 * @param {string} data.company - The user's company name.
 * @param {string} data.phoneNumber - The user's phone number.
 * 
 * @returns {object} An object containing a boolean indicating whether the data is valid and an object with error messages.
 */

function validateContactForm(data) {
    const errors = {};

    // Check if data is an object
    if (typeof data !== 'object' || Array.isArray(data) || data === null) {
        throw new Error('Invalid input: Data must be an object');
    }

    // Validate name field
    if (!data.name || typeof data.name !== 'string' || data.name.trim().length === 0) {
        errors.name = 'Name is required';
    }

    // Validate email field
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!data.email || typeof data.email !== 'string' || !emailRegex.test(data.email.trim())) {
        errors.email = 'Invalid email address';
    }

    // Validate company field
    if (!data.company || typeof data.company !== 'string' || data.company.trim().length === 0) {
        errors.company = 'Company name is required';
    }

    // Validate phone number field
    const phoneRegex = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
    if (!data.phoneNumber || typeof data.phoneNumber !== 'string' || !phoneRegex.test(data.phoneNumber.trim())) {
        errors.phoneNumber = 'Invalid phone number';
    }

    // Return validation result
    return {
        isValid: Object.keys(errors).length === 0,
        errors: errors
    };
}

// Example usage:
function main() {
    try {
        const formData = {
            name: 'John Doe',
            email: 'john.doe@example.com',
            company: 'Indusur',
            phoneNumber: '(123) 456-7890'
        };

        const validationResult = validateContactForm(formData);
        console.log('Validation result:', validationResult);

        if (!validationResult.isValid) {
            console.log('Errors:');
            Object.keys(validationResult.errors).forEach((field) => {
                console.log(`${field}: ${validationResult.errors[field]}`);
            });
        }
    } catch (error) {
        console.error('Error:', error.message);
    }
}

main();
```
