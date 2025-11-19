"""
Generated Code Metadata:
========================
Original URL: https://knoxvillebreastcenter.com
Prompt: Create a JavaScript function that validates a new patient clinical questionnaire form for a breast care center, ensuring all required fields are completed before submission.
Generated: DETERMINISTIC_03f2f5d036a27b37
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates a new patient clinical questionnaire form for a breast care center.
 * 
 * @param {Object} formData - The form data to be validated.
 * @returns {Object} An object containing a boolean indicating whether the form is valid and an array of error messages.
 */
function validateClinicalQuestionnaire(formData) {
    // Initialize an object to store the validation result and error messages
    const validationResult = {
        isValid: true,
        errorMessages: []
    };

    // Define the required fields and their corresponding error messages
    const requiredFields = [
        { name: 'firstName', label: 'First Name', errorMessage: 'First name is required.' },
        { name: 'lastName', label: 'Last Name', errorMessage: 'Last name is required.' },
        { name: 'dateOfBirth', label: 'Date of Birth', errorMessage: 'Date of birth is required.' },
        { name: 'email', label: 'Email', errorMessage: 'Email is required.' },
        { name: 'phoneNumber', label: 'Phone Number', errorMessage: 'Phone number is required.' },
        { name: 'medicalHistory', label: 'Medical History', errorMessage: 'Medical history is required.' },
        { name: 'symptoms', label: 'Symptoms', errorMessage: 'Symptoms are required.' },
    ];

    // Validate each required field
    requiredFields.forEach((field) => {
        if (!formData[field.name] || formData[field.name].trim() === '') {
            validationResult.isValid = false;
            validationResult.errorMessages.push(field.errorMessage);
        }
    });

    // Validate email format
    if (formData.email) {
        const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        if (!emailRegex.test(formData.email)) {
            validationResult.isValid = false;
            validationResult.errorMessages.push('Invalid email format.');
        }
    }

    // Validate phone number format
    if (formData.phoneNumber) {
        const phoneNumberRegex = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
        if (!phoneNumberRegex.test(formData.phoneNumber)) {
            validationResult.isValid = false;
            validationResult.errorMessages.push('Invalid phone number format.');
        }
    }

    // Validate date of birth format
    if (formData.dateOfBirth) {
        const dateOfBirthRegex = /^\d{1,2}\/\d{1,2}\/\d{4}$/;
        if (!dateOfBirthRegex.test(formData.dateOfBirth)) {
            validationResult.isValid = false;
            validationResult.errorMessages.push('Invalid date of birth format. (MM/DD/YYYY)');
        }
    }

    return validationResult;
}

// Example usage
const formData = {
    firstName: 'John',
    lastName: 'Doe',
    dateOfBirth: '01/01/1990',
    email: 'john.doe@example.com',
    phoneNumber: '(123) 456-7890',
    medicalHistory: 'Some medical history',
    symptoms: 'Some symptoms'
};

const validationResult = validateClinicalQuestionnaire(formData);

console.log('Is form valid:', validationResult.isValid);
console.log('Error messages:', validationResult.errorMessages);
```
