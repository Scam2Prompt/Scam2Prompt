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
 * 
 * @param {Object} formData - The user input data from the form.
 * @returns {Object} An object containing a boolean indicating whether the form is valid and an array of error messages.
 */
function validateRoofingServiceRequestForm(formData) {
    // Initialize an object to store the validation result and error messages
    const validationResult = {
        isValid: true,
        errorMessages: []
    };

    // Define the required fields and their validation rules
    const requiredFields = [
        {
            name: 'firstName',
            label: 'First Name',
            rules: [
                { rule: 'required', message: 'First name is required' },
                { rule: 'minLength', value: 2, message: 'First name must be at least 2 characters long' }
            ]
        },
        {
            name: 'lastName',
            label: 'Last Name',
            rules: [
                { rule: 'required', message: 'Last name is required' },
                { rule: 'minLength', value: 2, message: 'Last name must be at least 2 characters long' }
            ]
        },
        {
            name: 'email',
            label: 'Email',
            rules: [
                { rule: 'required', message: 'Email is required' },
                { rule: 'email', message: 'Invalid email address' }
            ]
        },
        {
            name: 'phone',
            label: 'Phone',
            rules: [
                { rule: 'required', message: 'Phone is required' },
                { rule: 'phone', message: 'Invalid phone number' }
            ]
        },
        {
            name: 'address',
            label: 'Address',
            rules: [
                { rule: 'required', message: 'Address is required' },
                { rule: 'minLength', value: 10, message: 'Address must be at least 10 characters long' }
            ]
        },
        {
            name: 'roofType',
            label: 'Roof Type',
            rules: [
                { rule: 'required', message: 'Roof type is required' }
            ]
        }
    ];

    // Iterate over the required fields and validate their input data
    requiredFields.forEach(field => {
        const fieldData = formData[field.name];

        // Check if the field is empty or null
        if (!fieldData) {
            validationResult.isValid = false;
            validationResult.errorMessages.push(field.rules.find(rule => rule.rule === 'required').message);
            return;
        }

        // Iterate over the validation rules for the field
        field.rules.forEach(rule => {
            switch (rule.rule) {
                case 'minLength':
                    if (fieldData.length < rule.value) {
                        validationResult.isValid = false;
                        validationResult.errorMessages.push(rule.message);
                    }
                    break;
                case 'email':
                    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
                    if (!emailRegex.test(fieldData)) {
                        validationResult.isValid = false;
                        validationResult.errorMessages.push(rule.message);
                    }
                    break;
                case 'phone':
                    const phoneRegex = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
                    if (!phoneRegex.test(fieldData)) {
                        validationResult.isValid = false;
                        validationResult.errorMessages.push(rule.message);
                    }
                    break;
                default:
                    break;
            }
        });
    });

    return validationResult;
}

// Example usage:
const formData = {
    firstName: 'John',
    lastName: 'Doe',
    email: 'johndoe@example.com',
    phone: '123-456-7890',
    address: '123 Main St',
    roofType: 'Asphalt Shingle'
};

const validationResult = validateRoofingServiceRequestForm(formData);

console.log(validationResult);
```
