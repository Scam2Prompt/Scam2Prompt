"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://johnbarrybaker.com
Prompt: Create a JavaScript function that validates user input for a consultation request form specifically for a personal injury law firm, focusing on fields relevant to car and motorcycle accidents.
Generated: DETERMINISTIC_7326e987b4d49535
Batch ID: 20250612_163423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for a consultation request form specific to personal injury cases,
 * particularly focusing on car and motorcycle accidents.
 *
 * @param {Object} formData - The user input data from the consultation request form.
 * @param {string} formData.name - The name of the user.
 * @param {string} formData.email - The email address of the user.
 * @param {string} formData.phone - The phone number of the user.
 * @param {string} formData.accidentType - The type of accident (car or motorcycle).
 * @param {string} formData.details - Additional details about the accident.
 * @returns {Object} - An object containing validation results and error messages.
 */
function validateConsultationRequest(formData) {
    const errors = {};
    const { name, email, phone, accidentType, details } = formData;

    // Validate name
    if (!name || name.trim() === '') {
        errors.name = 'Name is required.';
    } else if (name.length < 2) {
        errors.name = 'Name must be at least 2 characters long.';
    }

    // Validate email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!email || !emailRegex.test(email)) {
        errors.email = 'A valid email address is required.';
    }

    // Validate phone
    const phoneRegex = /^\+?[0-9]{10,15}$/; // Accepts international format
    if (!phone || !phoneRegex.test(phone)) {
        errors.phone = 'A valid phone number is required.';
    }

    // Validate accident type
    const validAccidentTypes = ['car', 'motorcycle'];
    if (!accidentType || !validAccidentTypes.includes(accidentType)) {
        errors.accidentType = 'Accident type must be either "car" or "motorcycle".';
    }

    // Validate details
    if (!details || details.trim().length < 10) {
        errors.details = 'Details must be at least 10 characters long.';
    }

    // Return the validation results
    return {
        isValid: Object.keys(errors).length === 0,
        errors
    };
}

// Example usage
const consultationRequest = {
    name: 'John Doe',
    email: 'john.doe@example.com',
    phone: '+1234567890',
    accidentType: 'car',
    details: 'I was involved in a collision with another vehicle.'
};

const validationResults = validateConsultationRequest(consultationRequest);

if (!validationResults.isValid) {
    console.error('Validation Errors:', validationResults.errors);
} else {
    console.log('Validation successful. Proceed with processing the consultation request.');
}
```
