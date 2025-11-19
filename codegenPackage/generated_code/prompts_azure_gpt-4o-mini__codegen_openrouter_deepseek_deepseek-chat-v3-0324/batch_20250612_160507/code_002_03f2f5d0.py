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
 * @param {Object} formData - The form data object containing patient questionnaire responses
 * @returns {Object} - An object containing validation result and error messages
 */
function validatePatientQuestionnaire(formData) {
    const errors = {};
    let isValid = true;

    // Personal Information Validation
    if (!formData.firstName || formData.firstName.trim() === '') {
        errors.firstName = 'First name is required';
        isValid = false;
    }

    if (!formData.lastName || formData.lastName.trim() === '') {
        errors.lastName = 'Last name is required';
        isValid = false;
    }

    if (!formData.dateOfBirth || !isValidDate(formData.dateOfBirth)) {
        errors.dateOfBirth = 'Valid date of birth is required';
        isValid = false;
    }

    if (!formData.gender || !['male', 'female', 'other'].includes(formData.gender.toLowerCase())) {
        errors.gender = 'Gender is required (male/female/other)';
        isValid = false;
    }

    // Contact Information Validation
    if (!formData.phone || !isValidPhoneNumber(formData.phone)) {
        errors.phone = 'Valid phone number is required';
        isValid = false;
    }

    if (!formData.email || !isValidEmail(formData.email)) {
        errors.email = 'Valid email address is required';
        isValid = false;
    }

    // Medical History Validation
    if (formData.hasPreviousBreastCancer === undefined) {
        errors.hasPreviousBreastCancer = 'Please indicate if you have had breast cancer before';
        isValid = false;
    }

    if (formData.familyHistoryBreastCancer === undefined) {
        errors.familyHistoryBreastCancer = 'Please indicate if you have a family history of breast cancer';
        isValid = false;
    }

    if (formData.lastMammogramDate && !isValidDate(formData.lastMammogramDate)) {
        errors.lastMammogramDate = 'Please enter a valid date for last mammogram';
        isValid = false;
    }

    // Current Symptoms Validation
    if (formData.currentSymptoms && formData.currentSymptoms.length > 0) {
        if (formData.symptomsDuration === undefined) {
            errors.symptomsDuration = 'Please indicate how long you have had these symptoms';
            isValid = false;
        }
    }

    // Consent Validation
    if (!formData.consentToTreatment || formData.consentToTreatment !== true) {
        errors.consentToTreatment = 'Consent to treatment is required';
        isValid = false;
    }

    return {
        isValid,
        errors
    };
}

/**
 * Validates if a string is a valid date in format YYYY-MM-DD
 * @param {string} dateString - The date string to validate
 * @returns {boolean} - True if valid date, false otherwise
 */
function isValidDate(dateString) {
    const regex = /^\d{4}-\d{2}-\d{2}$/;
    if (!dateString.match(regex)) return false;
    
    const date = new Date(dateString);
    const timestamp = date.getTime();
    
    if (typeof timestamp !== 'number' || Number.isNaN(timestamp)) {
        return false;
    }
    
    return date.toISOString().startsWith(dateString);
}

/**
 * Validates if a string is a valid email address
 * @param {string} email - The email string to validate
 * @returns {boolean} - True if valid email, false otherwise
 */
function isValidEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(String(email).toLowerCase());
}

/**
 * Validates if a string is a valid phone number (US format)
 * @param {string} phone - The phone number string to validate
 * @returns {boolean} - True if valid phone number, false otherwise
 */
function isValidPhoneNumber(phone) {
    const re = /^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$/;
    return re.test(String(phone));
}

// Example usage:
// const formData = {
//     firstName: 'Jane',
//     lastName: 'Doe',
//     dateOfBirth: '1980-05-15',
//     gender: 'female',
//     phone: '555-123-4567',
//     email: 'jane.doe@example.com',
//     hasPreviousBreastCancer: false,
//     familyHistoryBreastCancer: true,
//     lastMammogramDate: '2022-01-10',
//     currentSymptoms: ['lump'],
//     symptomsDuration: '2 weeks',
//     consentToTreatment: true
// };

// const validationResult = validatePatientQuestionnaire(formData);
// console.log(validationResult);
```
