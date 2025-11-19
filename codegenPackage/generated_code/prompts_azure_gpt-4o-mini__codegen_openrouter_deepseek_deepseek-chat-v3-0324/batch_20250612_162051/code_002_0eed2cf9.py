"""
Generated Code Metadata:
========================
Original URL: https://www.getaconsulenze.it
Prompt: Create a code snippet in JavaScript that validates user input for the Certificazione di alfabetizzazione digitale (CIAD) registration form mentioned on Geta Consulenze's site.
Generated: DETERMINISTIC_0eed2cf9f68a82b7
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates the CIAD registration form input fields.
 * @param {Object} formData - The form data object containing user input.
 * @returns {Object} An object containing validation results and error messages.
 */
function validateCIADForm(formData) {
    const errors = {};
    const requiredFields = [
        'firstName', 'lastName', 'email', 'phone', 'address',
        'city', 'postalCode', 'country', 'birthDate', 'idNumber'
    ];

    // Check required fields
    requiredFields.forEach(field => {
        if (!formData[field] || formData[field].trim() === '') {
            errors[field] = 'This field is required';
        }
    });

    // Validate email format
    if (formData.email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
        errors.email = 'Please enter a valid email address';
    }

    // Validate phone number (basic international format)
    if (formData.phone && !/^\+?[\d\s-]{6,}$/.test(formData.phone)) {
        errors.phone = 'Please enter a valid phone number';
    }

    // Validate postal code (basic numeric check)
    if (formData.postalCode && !/^\d+$/.test(formData.postalCode)) {
        errors.postalCode = 'Postal code must contain only numbers';
    }

    // Validate birth date (format: YYYY-MM-DD)
    if (formData.birthDate) {
        const dateRegex = /^\d{4}-\d{2}-\d{2}$/;
        if (!dateRegex.test(formData.birthDate)) {
            errors.birthDate = 'Date must be in YYYY-MM-DD format';
        } else {
            const birthDate = new Date(formData.birthDate);
            const currentDate = new Date();
            if (birthDate >= currentDate) {
                errors.birthDate = 'Birth date must be in the past';
            }
        }
    }

    // Validate ID number (alphanumeric)
    if (formData.idNumber && !/^[a-zA-Z0-9]+$/.test(formData.idNumber)) {
        errors.idNumber = 'ID number must be alphanumeric';
    }

    return {
        isValid: Object.keys(errors).length === 0,
        errors
    };
}

// Example usage:
/*
const formData = {
    firstName: 'John',
    lastName: 'Doe',
    email: 'john.doe@example.com',
    phone: '+39 123 456789',
    address: '123 Main St',
    city: 'Rome',
    postalCode: '00100',
    country: 'Italy',
    birthDate: '1990-01-01',
    idNumber: 'AB123456'
};

const validationResult = validateCIADForm(formData);
if (!validationResult.isValid) {
    console.log('Validation errors:', validationResult.errors);
} else {
    console.log('Form is valid');
}
*/
```
