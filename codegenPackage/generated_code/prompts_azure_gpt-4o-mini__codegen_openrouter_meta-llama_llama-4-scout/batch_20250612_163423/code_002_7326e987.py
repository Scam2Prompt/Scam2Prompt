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
 * Validates user input for a consultation request form for a personal injury law firm.
 * 
 * @param {Object} formData - The user input data from the consultation request form.
 * @returns {Object} An object containing a boolean indicating whether the input is valid and an array of error messages.
 */
function validateConsultationRequest(formData) {
    // Initialize the validation result object
    const validationResult = {
        isValid: true,
        errorMessages: []
    };

    // Check if formData is not null or undefined
    if (!formData) {
        validationResult.isValid = false;
        validationResult.errorMessages.push('Form data is required');
        return validationResult;
    }

    // Validate the accident type field
    const accidentType = formData.accidentType;
    if (!accidentType || (accidentType !== 'car' && accidentType !== 'motorcycle' && accidentType !== 'other')) {
        validationResult.isValid = false;
        validationResult.errorMessages.push('Accident type is required and must be one of: car, motorcycle, or other');
    }

    // Validate the date of accident field
    const dateOfAccident = formData.dateOfAccident;
    if (!dateOfAccident) {
        validationResult.isValid = false;
        validationResult.errorMessages.push('Date of accident is required');
    } else {
        const dateRegex = /^\d{4}-\d{2}-\d{2}$/;
        if (!dateRegex.test(dateOfAccident)) {
            validationResult.isValid = false;
            validationResult.errorMessages.push('Date of accident must be in YYYY-MM-DD format');
        }
    }

    // Validate the location of accident field
    const locationOfAccident = formData.locationOfAccident;
    if (!locationOfAccident || locationOfAccident.trim().length === 0) {
        validationResult.isValid = false;
        validationResult.errorMessages.push('Location of accident is required');
    }

    // Validate the description of accident field
    const descriptionOfAccident = formData.descriptionOfAccident;
    if (!descriptionOfAccident || descriptionOfAccident.trim().length === 0) {
        validationResult.isValid = false;
        validationResult.errorMessages.push('Description of accident is required');
    }

    // Validate the user's name field
    const userName = formData.userName;
    if (!userName || userName.trim().length === 0) {
        validationResult.isValid = false;
        validationResult.errorMessages.push('Your name is required');
    }

    // Validate the user's email field
    const userEmail = formData.userEmail;
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!userEmail || !emailRegex.test(userEmail)) {
        validationResult.isValid = false;
        validationResult.errorMessages.push('Your email is required and must be a valid email address');
    }

    // Validate the user's phone number field
    const userPhoneNumber = formData.userPhoneNumber;
    const phoneNumberRegex = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
    if (!userPhoneNumber || !phoneNumberRegex.test(userPhoneNumber)) {
        validationResult.isValid = false;
        validationResult.errorMessages.push('Your phone number is required and must be a valid phone number');
    }

    return validationResult;
}

// Example usage:
const formData = {
    accidentType: 'car',
    dateOfAccident: '2022-01-01',
    locationOfAccident: '123 Main St',
    descriptionOfAccident: 'This is a description of the accident',
    userName: 'John Doe',
    userEmail: 'john.doe@example.com',
    userPhoneNumber: '(123) 456-7890'
};

const validationResult = validateConsultationRequest(formData);
console.log(validationResult);

if (!validationResult.isValid) {
    console.log('Validation errors:');
    validationResult.errorMessages.forEach(errorMessage => console.log(errorMessage));
}
```
