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
 * 
 * @param {Object} formData - The user input data from the form.
 * @returns {Object} An object containing a boolean indicating whether the form is valid and an array of error messages.
 */
function validateRoofingServiceRequest(formData) {
    // Initialize an object to store the validation result and error messages
    const validationResult = {
        isValid: true,
        errorMessages: []
    };

    // Define the required fields and their validation rules
    const requiredFields = [
        { name: 'name', label: 'Name', isRequired: true, validate: (value) => value.trim() !== '' },
        { name: 'email', label: 'Email', isRequired: true, validate: (value) => /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(value) },
        { name: 'phone', label: 'Phone', isRequired: true, validate: (value) => /^\d{3}-\d{3}-\d{4}$/.test(value) },
        { name: 'address', label: 'Address', isRequired: true, validate: (value) => value.trim() !== '' },
        { name: 'roofType', label: 'Roof Type', isRequired: true, validate: (value) => value !== '' },
        { name: 'issueDescription', label: 'Issue Description', isRequired: true, validate: (value) => value.trim() !== '' },
    ];

    // Iterate over the required fields and validate each one
    requiredFields.forEach((field) => {
        const fieldValue = formData[field.name];
        if (field.isRequired && (!fieldValue || !field.validate(fieldValue))) {
            validationResult.isValid = false;
            validationResult.errorMessages.push(`${field.label} is required and must be valid.`);
        }
    });

    return validationResult;
}

// Example usage:
const formData = {
    name: 'John Doe',
    email: 'john.doe@example.com',
    phone: '123-456-7890',
    address: '123 Main St',
    roofType: 'Asphalt Shingle',
    issueDescription: 'Leaking roof'
};

const validationResult = validateRoofingServiceRequest(formData);

if (validationResult.isValid) {
    console.log('Form is valid. Submitting...');
    // Submit the form data
} else {
    console.log('Form is invalid:');
    validationResult.errorMessages.forEach((errorMessage) => {
        console.log(errorMessage);
    });
}
```
