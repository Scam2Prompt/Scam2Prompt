"""
Generated Code Metadata:
========================
Original URL: https://unitedcabinetry.com.au
Prompt: Create a JavaScript function that validates user input for a cabinetry consultation request form, ensuring all required fields are filled out correctly.
Generated: DETERMINISTIC_11435508d7fabacc
Batch ID: 20250612_164115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for a cabinetry consultation request form.
 * 
 * @param {Object} formData - The user input data from the form.
 * @returns {Object} An object containing a boolean indicating whether the form is valid and an object of error messages.
 */
function validateCabinetryConsultationForm(formData) {
    // Initialize an object to store error messages
    const errors = {};

    // Check if formData is null or undefined
    if (!formData) {
        throw new Error('Form data is required');
    }

    // Define required fields
    const requiredFields = [
        'name',
        'email',
        'phone',
        'address',
        'city',
        'state',
        'zip',
        'cabinetType',
        'consultationDate'
    ];

    // Check for required fields
    requiredFields.forEach((field) => {
        if (!formData[field] || formData[field].trim() === '') {
            errors[field] = `${field.charAt(0).toUpperCase() + field.slice(1)} is required`;
        }
    });

    // Validate email format
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (formData.email && !emailRegex.test(formData.email)) {
        errors.email = 'Invalid email address';
    }

    // Validate phone number format
    const phoneRegex = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
    if (formData.phone && !phoneRegex.test(formData.phone)) {
        errors.phone = 'Invalid phone number';
    }

    // Check if consultation date is in the future
    const consultationDate = new Date(formData.consultationDate);
    if (consultationDate && consultationDate <= new Date()) {
        errors.consultationDate = 'Consultation date must be in the future';
    }

    // Return an object with a boolean indicating form validity and error messages
    return {
        isValid: Object.keys(errors).length === 0,
        errors
    };
}

// Example usage:
const formData = {
    name: 'John Doe',
    email: 'johndoe@example.com',
    phone: '123-456-7890',
    address: '123 Main St',
    city: 'Anytown',
    state: 'CA',
    zip: '12345',
    cabinetType: 'custom',
    consultationDate: '2024-09-20T14:00:00.000Z'
};

const { isValid, errors } = validateCabinetryConsultationForm(formData);
console.log(isValid); // true
console.log(errors); // {}

const invalidFormData = {
    name: '',
    email: 'invalid',
    phone: '123',
    address: '123 Main St',
    city: 'Anytown',
    state: 'CA',
    zip: '12345',
    cabinetType: 'custom',
    consultationDate: '2024-09-20T14:00:00.000Z'
};

const { isValid: isInvalidValid, errors: invalidErrors } = validateCabinetryConsultationForm(invalidFormData);
console.log(isInvalidValid); // false
console.log(invalidErrors);
// {
//   name: 'Name is required',
//   email: 'Invalid email address',
//   phone: 'Invalid phone number'
// }
```
