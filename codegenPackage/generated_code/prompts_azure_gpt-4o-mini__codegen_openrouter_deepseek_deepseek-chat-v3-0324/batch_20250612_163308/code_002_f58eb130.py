"""
Generated Code Metadata:
========================
Original URL: https://kingroofing.com
Prompt: Create a function in JavaScript that validates user input for a roofing service request form, ensuring all required fields are filled out correctly before submission.
Generated: DETERMINISTIC_f58eb130d65a40be
Batch ID: 20250612_163308
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
 * @param {string} formData.name - Customer's name.
 * @param {string} formData.email - Customer's email.
 * @param {string} formData.phone - Customer's phone number.
 * @param {string} formData.address - Service address.
 * @param {string} formData.roofType - Type of roof.
 * @param {string} formData.serviceNeeded - Service requested.
 * @param {string} formData.preferredDate - Preferred service date.
 * @returns {Object} An object with validation results: { isValid: boolean, errors: Object }.
 */
function validateRoofingServiceForm(formData) {
    const errors = {};

    // Helper function to check if a string is empty or whitespace
    const isBlank = (str) => !str || !str.trim();

    // Validate name
    if (isBlank(formData.name)) {
        errors.name = 'Name is required';
    }

    // Validate email
    if (isBlank(formData.email)) {
        errors.email = 'Email is required';
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
        errors.email = 'Please enter a valid email address';
    }

    // Validate phone
    if (isBlank(formData.phone)) {
        errors.phone = 'Phone number is required';
    } else if (!/^[\d\s\-()]+$/.test(formData.phone)) {
        errors.phone = 'Please enter a valid phone number';
    }

    // Validate address
    if (isBlank(formData.address)) {
        errors.address = 'Address is required';
    }

    // Validate roof type
    if (isBlank(formData.roofType)) {
        errors.roofType = 'Roof type is required';
    }

    // Validate service needed
    if (isBlank(formData.serviceNeeded)) {
        errors.serviceNeeded = 'Service needed is required';
    }

    // Validate preferred date
    if (isBlank(formData.preferredDate)) {
        errors.preferredDate = 'Preferred date is required';
    } else {
        const selectedDate = new Date(formData.preferredDate);
        const currentDate = new Date();
        currentDate.setHours(0, 0, 0, 0);
        
        if (selectedDate < currentDate) {
            errors.preferredDate = 'Preferred date cannot be in the past';
        }
    }

    return {
        isValid: Object.keys(errors).length === 0,
        errors: errors
    };
}

module.exports = validateRoofingServiceForm;
```
