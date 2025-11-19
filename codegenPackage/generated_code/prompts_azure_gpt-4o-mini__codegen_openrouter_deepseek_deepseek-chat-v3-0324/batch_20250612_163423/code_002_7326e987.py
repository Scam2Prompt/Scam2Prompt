"""
Generated Code Metadata:
========================
Original URL: https://johnbarrybaker.com
Prompt: Create a JavaScript function that validates user input for a consultation request form specifically for a personal injury law firm, focusing on fields relevant to car and motorcycle accidents.
Generated: DETERMINISTIC_7326e987b4d49535
Batch ID: 20250612_163423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for a personal injury law firm consultation request form.
 * Focuses on fields relevant to car and motorcycle accidents.
 * 
 * @param {Object} formData - The form data to validate
 * @param {string} formData.name - Full name of the client
 * @param {string} formData.email - Email address
 * @param {string} formData.phone - Phone number
 * @param {string} formData.accidentType - Type of accident (car/motorcycle)
 * @param {string} formData.accidentDate - Date of accident
 * @param {string} formData.description - Description of the accident
 * @param {string} [formData.injuries] - Description of injuries (optional)
 * @returns {Object} - Validation result { isValid: boolean, errors: Object }
 */
function validateConsultationForm(formData) {
    const errors = {};
    const currentDate = new Date();
    const maxPastDate = new Date();
    maxPastDate.setFullYear(currentDate.getFullYear() - 1); // Allow accidents up to 1 year old

    // Validate name (required, at least 2 words)
    if (!formData.name || formData.name.trim().length < 3) {
        errors.name = 'Full name is required';
    } else {
        const nameParts = formData.name.trim().split(/\s+/);
        if (nameParts.length < 2) {
            errors.name = 'Please enter your full name (first and last)';
        }
    }

    // Validate email (required, valid format)
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!formData.email) {
        errors.email = 'Email is required';
    } else if (!emailRegex.test(formData.email)) {
        errors.email = 'Please enter a valid email address';
    }

    // Validate phone (required, at least 10 digits)
    const phoneDigits = formData.phone ? formData.phone.replace(/\D/g, '') : '';
    if (!formData.phone) {
        errors.phone = 'Phone number is required';
    } else if (phoneDigits.length < 10) {
        errors.phone = 'Please enter a valid phone number (at least 10 digits)';
    }

    // Validate accident type (required, must be car or motorcycle)
    const validAccidentTypes = ['car', 'motorcycle'];
    if (!formData.accidentType) {
        errors.accidentType = 'Accident type is required';
    } else if (!validAccidentTypes.includes(formData.accidentType.toLowerCase())) {
        errors.accidentType = 'Please select either car or motorcycle accident';
    }

    // Validate accident date (required, valid date, not in future, not too old)
    if (!formData.accidentDate) {
        errors.accidentDate = 'Accident date is required';
    } else {
        const accidentDate = new Date(formData.accidentDate);
        if (isNaN(accidentDate.getTime())) {
            errors.accidentDate = 'Please enter a valid date';
        } else if (accidentDate > currentDate) {
            errors.accidentDate = 'Accident date cannot be in the future';
        } else if (accidentDate < maxPastDate) {
            errors.accidentDate = 'Accident date cannot be more than one year old';
        }
    }

    // Validate description (required, minimum length)
    if (!formData.description || formData.description.trim().length < 20) {
        errors.description = 'Please provide a detailed description (at least 20 characters)';
    }

    // Validate injuries if provided (minimum length)
    if (formData.injuries && formData.injuries.trim().length < 10) {
        errors.injuries = 'Please provide more details about injuries (at least 10 characters)';
    }

    return {
        isValid: Object.keys(errors).length === 0,
        errors: errors
    };
}

// Example usage:
// const formData = {
//     name: 'John Doe',
//     email: 'john@example.com',
//     phone: '(123) 456-7890',
//     accidentType: 'car',
//     accidentDate: '2023-05-15',
//     description: 'I was rear-ended at a stop light by a speeding vehicle.',
//     injuries: 'Whiplash and back pain'
// };
// const validation = validateConsultationForm(formData);
```
