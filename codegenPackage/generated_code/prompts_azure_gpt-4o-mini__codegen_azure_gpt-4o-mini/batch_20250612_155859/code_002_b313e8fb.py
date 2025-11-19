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
 * Ensures all required fields are filled out according to the specifications.
 * 
 * @param {Object} formData - The data from the cue order form.
 * @returns {Object} - An object containing validation results and messages.
 */
function validateCueOrderForm(formData) {
    // Initialize an object to hold validation results
    const validationResults = {
        isValid: true,
        messages: []
    };

    // Required fields as per the specifications
    const requiredFields = [
        'name',
        'email',
        'phone',
        'cueType',
        'length',
        'weight',
        'tipSize'
    ];

    // Check for missing required fields
    requiredFields.forEach(field => {
        if (!formData[field] || formData[field].trim() === '') {
            validationResults.isValid = false;
            validationResults.messages.push(`${field} is required.`);
        }
    });

    // Validate email format
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (formData.email && !emailPattern.test(formData.email)) {
        validationResults.isValid = false;
        validationResults.messages.push('Email format is invalid.');
    }

    // Validate phone number format (example: (123) 456-7890)
    const phonePattern = /^\(\d{3}\) \d{3}-\d{4}$/;
    if (formData.phone && !phonePattern.test(formData.phone)) {
        validationResults.isValid = false;
        validationResults.messages.push('Phone number must be in the format (123) 456-7890.');
    }

    // Validate length and weight to be positive numbers
    if (formData.length && (isNaN(formData.length) || formData.length <= 0)) {
        validationResults.isValid = false;
        validationResults.messages.push('Length must be a positive number.');
    }

    if (formData.weight && (isNaN(formData.weight) || formData.weight <= 0)) {
        validationResults.isValid = false;
        validationResults.messages.push('Weight must be a positive number.');
    }

    // Validate tip size (example: must be one of the predefined sizes)
    const validTipSizes = ['12mm', '13mm', '14mm'];
    if (formData.tipSize && !validTipSizes.includes(formData.tipSize)) {
        validationResults.isValid = false;
        validationResults.messages.push(`Tip size must be one of the following: ${validTipSizes.join(', ')}.`);
    }

    return validationResults;
}

// Example usage
const formData = {
    name: 'John Doe',
    email: 'john.doe@example.com',
    phone: '(123) 456-7890',
    cueType: 'Pool Cue',
    length: '58',
    weight: '19',
    tipSize: '13mm'
};

const validation = validateCueOrderForm(formData);
if (!validation.isValid) {
    console.error('Validation errors:', validation.messages);
} else {
    console.log('Form is valid. Proceed with submission.');
}
```
