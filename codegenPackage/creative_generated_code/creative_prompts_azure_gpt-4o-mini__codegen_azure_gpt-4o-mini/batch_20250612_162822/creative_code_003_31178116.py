"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ledgerreclaim.com
Prompt: Develop a JavaScript function that validates user input for a construction service request form, ensuring all required fields are filled out, based on the structure used by ExpertStroy.
Generated: DETERMINISTIC_31178116c5152bdf
Batch ID: 20250612_162822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for a construction service request form.
 * 
 * @param {Object} formData - The data object containing user input.
 * @returns {Object} - An object containing validation results and messages.
 */
function validateConstructionServiceForm(formData) {
    // Initialize an object to hold validation results
    const validationResult = {
        isValid: true,
        messages: []
    };

    // Check required fields
    const requiredFields = ['name', 'email', 'phone', 'serviceType', 'address', 'description'];

    requiredFields.forEach(field => {
        if (!formData[field] || formData[field].trim() === '') {
            validationResult.isValid = false;
            validationResult.messages.push(`${field.replace(/([A-Z])/g, ' $1')} is required.`);
        }
    });

    // Validate email format
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (formData.email && !emailRegex.test(formData.email)) {
        validationResult.isValid = false;
        validationResult.messages.push('Email format is invalid.');
    }

    // Validate phone number format (simple example: allows digits and dashes)
    const phoneRegex = /^\d{3}-\d{3}-\d{4}$/;
    if (formData.phone && !phoneRegex.test(formData.phone)) {
        validationResult.isValid = false;
        validationResult.messages.push('Phone number must be in the format XXX-XXX-XXXX.');
    }

    // Return the validation result
    return validationResult;
}

// Example usage:
const formData = {
    name: 'John Doe',
    email: 'john.doe@example.com',
    phone: '123-456-7890',
    serviceType: 'Renovation',
    address: '123 Main St',
    description: 'Need help with kitchen remodeling.'
};

const result = validateConstructionServiceForm(formData);
if (!result.isValid) {
    console.error('Validation Errors:', result.messages);
} else {
    console.log('Form is valid. Proceeding with submission.');
}
```
