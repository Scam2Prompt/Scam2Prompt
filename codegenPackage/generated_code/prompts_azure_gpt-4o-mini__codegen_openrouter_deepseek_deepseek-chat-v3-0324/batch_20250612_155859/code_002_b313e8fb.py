"""
Generated Code Metadata:
========================
Original URL: https://cohencues.com
Prompt: Create a JavaScript function that validates user input for a custom cue order form, ensuring all required fields are filled out as described on the Cohen Cues website.
Generated: DETERMINISTIC_b313e8fbb0bf808c
Batch ID: 20250612_155859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for a custom cue order form.
 * @param {Object} formData - The form data object containing user inputs.
 * @param {Object} requiredFields - The required fields configuration.
 * @returns {Object} An object containing validation results (isValid, errors).
 */
function validateCustomCueOrder(formData, requiredFields) {
    const errors = {};
    let isValid = true;

    // Validate required fields
    for (const field in requiredFields) {
        if (requiredFields.hasOwnProperty(field)) {
            const fieldConfig = requiredFields[field];
            const value = formData[field];

            // Check if field is required and empty
            if (fieldConfig.required && (!value || value.trim() === '')) {
                errors[field] = fieldConfig.errorMessage || `${field} is required`;
                isValid = false;
                continue;
            }

            // Validate field type if specified
            if (fieldConfig.type) {
                switch (fieldConfig.type) {
                    case 'email':
                        if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)) {
                            errors[field] = fieldConfig.errorMessage || 'Invalid email format';
                            isValid = false;
                        }
                        break;
                    case 'number':
                        if (isNaN(value) || value < (fieldConfig.min || -Infinity) || value > (fieldConfig.max || Infinity)) {
                            errors[field] = fieldConfig.errorMessage || 
                                `Must be a number between ${fieldConfig.min || 'any'} and ${fieldConfig.max || 'any'}`;
                            isValid = false;
                        }
                        break;
                    case 'phone':
                        if (!/^[\d\s\-()+]{10,20}$/.test(value)) {
                            errors[field] = fieldConfig.errorMessage || 'Invalid phone number format';
                            isValid = false;
                        }
                        break;
                }
            }

            // Validate custom regex if specified
            if (fieldConfig.pattern && !new RegExp(fieldConfig.pattern).test(value)) {
                errors[field] = fieldConfig.errorMessage || `Invalid ${field} format`;
                isValid = false;
            }

            // Validate length constraints if specified
            if (fieldConfig.minLength && value.length < fieldConfig.minLength) {
                errors[field] = fieldConfig.errorMessage || 
                    `Must be at least ${fieldConfig.minLength} characters`;
                isValid = false;
            }

            if (fieldConfig.maxLength && value.length > fieldConfig.maxLength) {
                errors[field] = fieldConfig.errorMessage || 
                    `Must be no more than ${fieldConfig.maxLength} characters`;
                isValid = false;
            }
        }
    }

    return {
        isValid,
        errors
    };
}

// Example usage:
/*
const requiredFields = {
    name: {
        required: true,
        minLength: 2,
        errorMessage: 'Please enter your full name'
    },
    email: {
        required: true,
        type: 'email',
        errorMessage: 'Please enter a valid email address'
    },
    phone: {
        required: true,
        type: 'phone',
        errorMessage: 'Please enter a valid phone number'
    },
    cueLength: {
        required: true,
        type: 'number',
        min: 48,
        max: 60,
        errorMessage: 'Cue length must be between 48 and 60 inches'
    },
    woodType: {
        required: true,
        errorMessage: 'Please select a wood type'
    }
};

const formData = {
    name: 'John Doe',
    email: 'john@example.com',
    phone: '555-123-4567',
    cueLength: '58',
    woodType: 'maple'
};

const validation = validateCustomCueOrder(formData, requiredFields);
if (!validation.isValid) {
    console.error('Validation errors:', validation.errors);
} else {
    console.log('Form is valid');
}
*/
```
