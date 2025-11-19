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
 * @param {Object} formData - The form data to validate
 * @param {string} formData.name - Client's full name
 * @param {string} formData.email - Client's email address
 * @param {string} formData.phone - Client's phone number
 * @param {string} formData.projectType - Type of cabinetry project
 * @param {string} formData.budget - Project budget range
 * @param {string} formData.timeline - Project timeline
 * @param {string} formData.message - Additional message
 * @returns {Object} - Validation result with isValid boolean and errors object
 */
function validateConsultationForm(formData) {
    const errors = {};
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const phoneRegex = /^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/;

    // Validate name
    if (!formData.name || formData.name.trim().length < 2) {
        errors.name = 'Please enter your full name (min 2 characters)';
    }

    // Validate email
    if (!formData.email || !emailRegex.test(formData.email)) {
        errors.email = 'Please enter a valid email address';
    }

    // Validate phone
    if (!formData.phone || !phoneRegex.test(formData.phone)) {
        errors.phone = 'Please enter a valid phone number';
    }

    // Validate project type
    if (!formData.projectType || formData.projectType === 'Select') {
        errors.projectType = 'Please select a project type';
    }

    // Validate budget
    if (!formData.budget || formData.budget === 'Select') {
        errors.budget = 'Please select a budget range';
    }

    // Validate timeline
    if (!formData.timeline || formData.timeline.trim().length < 5) {
        errors.timeline = 'Please provide a timeline (min 5 characters)';
    }

    // Validate message (optional field but recommended)
    if (formData.message && formData.message.trim().length > 500) {
        errors.message = 'Message must be less than 500 characters';
    }

    return {
        isValid: Object.keys(errors).length === 0,
        errors
    };
}

// Example usage:
// const formData = {
//     name: 'John Doe',
//     email: 'john@example.com',
//     phone: '555-123-4567',
//     projectType: 'Kitchen Remodel',
//     budget: '$10,000 - $20,000',
//     timeline: 'Within 3 months',
//     message: 'Looking for custom cabinetry for my kitchen remodel.'
// };
// const validation = validateConsultationForm(formData);
// if (!validation.isValid) {
//     console.log('Validation errors:', validation.errors);
// }
```
