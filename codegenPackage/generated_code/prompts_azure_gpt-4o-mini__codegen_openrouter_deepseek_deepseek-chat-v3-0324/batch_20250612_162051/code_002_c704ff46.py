"""
Generated Code Metadata:
========================
Original URL: https://spanglerroofingllc.com
Prompt: Create a JavaScript function that validates user input for a roofing service request form, ensuring all required fields are filled out correctly.
Generated: DETERMINISTIC_c704ff46a9125644
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
 * Validates user input for a roofing service request form.
 * @param {Object} formData - The form data to validate.
 * @param {string} formData.name - Customer's full name.
 * @param {string} formData.email - Customer's email address.
 * @param {string} formData.phone - Customer's phone number.
 * @param {string} formData.address - Service address.
 * @param {string} formData.roofType - Type of roof.
 * @param {string} formData.serviceNeeded - Type of service needed.
 * @param {string} formData.description - Problem description.
 * @returns {Object} - Validation result with success status and error messages.
 */
function validateRoofingForm(formData) {
    const errors = {};
    let isValid = true;

    // Helper function to check if a string is empty or contains only whitespace
    const isBlank = (str) => !str || !str.trim();

    // Validate name
    if (isBlank(formData.name)) {
        errors.name = 'Full name is required';
        isValid = false;
    }

    // Validate email
    if (isBlank(formData.email)) {
        errors.email = 'Email is required';
        isValid = false;
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
        errors.email = 'Please enter a valid email address';
        isValid = false;
    }

    // Validate phone
    if (isBlank(formData.phone)) {
        errors.phone = 'Phone number is required';
        isValid = false;
    } else if (!/^[\d\s\-()+]{10,20}$/.test(formData.phone)) {
        errors.phone = 'Please enter a valid phone number';
        isValid = false;
    }

    // Validate address
    if (isBlank(formData.address)) {
        errors.address = 'Service address is required';
        isValid = false;
    }

    // Validate roof type
    if (isBlank(formData.roofType)) {
        errors.roofType = 'Roof type is required';
        isValid = false;
    }

    // Validate service needed
    if (isBlank(formData.serviceNeeded)) {
        errors.serviceNeeded = 'Service type is required';
        isValid = false;
    }

    // Validate description
    if (isBlank(formData.description)) {
        errors.description = 'Problem description is required';
        isValid = false;
    } else if (formData.description.length < 20) {
        errors.description = 'Description must be at least 20 characters';
        isValid = false;
    }

    return {
        isValid,
        errors: isValid ? null : errors
    };
}

// Example usage:
// const formData = {
//     name: 'John Doe',
//     email: 'john@example.com',
//     phone: '123-456-7890',
//     address: '123 Main St',
//     roofType: 'Asphalt',
//     serviceNeeded: 'Repair',
//     description: 'My roof has several leaks that need to be fixed.'
// };
// const validationResult = validateRoofingForm(formData);
```
