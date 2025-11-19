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
 * @param {Object} formData - The form data object containing user input
 * @param {string} formData.name - User's full name
 * @param {string} formData.email - User's email address
 * @param {string} formData.phone - User's phone number
 * @param {string} [formData.address] - User's address (optional)
 * @param {string} [formData.message] - Additional message (optional)
 * @returns {Object} An object containing validation results: { isValid: boolean, errors: Object }
 */
function validateRoofInspectionForm(formData) {
    const errors = {};
    let isValid = true;

    // Validate name (required, at least 2 characters)
    if (!formData.name || formData.name.trim().length < 2) {
        errors.name = 'Please enter your full name (at least 2 characters)';
        isValid = false;
    }

    // Validate email (required, valid format)
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!formData.email || !emailRegex.test(formData.email)) {
        errors.email = 'Please enter a valid email address';
        isValid = false;
    }

    // Validate phone number (required, at least 10 digits)
    const phoneRegex = /^[\d\s\-().+]{10,}$/;
    const digitsOnly = formData.phone ? formData.phone.replace(/\D/g, '') : '';
    if (!formData.phone || digitsOnly.length < 10 || !phoneRegex.test(formData.phone)) {
        errors.phone = 'Please enter a valid phone number (at least 10 digits)';
        isValid = false;
    }

    // Optional address validation (if provided)
    if (formData.address && formData.address.trim().length > 0 && formData.address.trim().length < 5) {
        errors.address = 'Address must be at least 5 characters if provided';
        isValid = false;
    }

    // Optional message validation (if provided)
    if (formData.message && formData.message.trim().length > 500) {
        errors.message = 'Message must be less than 500 characters';
        isValid = false;
    }

    return {
        isValid,
        errors
    };
}

// Example usage:
// const formData = {
//     name: 'John Doe',
//     email: 'john@example.com',
//     phone: '(123) 456-7890',
//     address: '123 Main St',
//     message: 'I need a roof inspection'
// };
// const validationResult = validateRoofInspectionForm(formData);
// if (!validationResult.isValid) {
//     console.log('Validation errors:', validationResult.errors);
// }
```
