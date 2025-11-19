"""
Generated Code Metadata:
========================
Original URL: https://aibaoinsurance.com
Prompt: Develop a JavaScript function that validates user input for an insurance quote request form, ensuring all necessary fields are filled out correctly.
Generated: DETERMINISTIC_c4dd2c66057520ea
Batch ID: 20250612_161209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for an insurance quote request form.
 * 
 * @param {Object} formData - The user input data from the form.
 * @returns {Object} An object containing a boolean indicating whether the form is valid and an object with error messages.
 */
function validateInsuranceQuoteForm(formData) {
    const requiredFields = ['firstName', 'lastName', 'email', 'phone', 'address', 'city', 'state', 'zip', 'coverageAmount'];
    const errorMessages = {};

    // Check if all required fields are present
    if (typeof formData !== 'object' || Object.keys(formData).length === 0) {
        errorMessages.formData = 'Form data is required';
        return { isValid: false, errors: errorMessages };
    }

    // Validate each required field
    requiredFields.forEach((field) => {
        if (!formData[field] || formData[field].trim() === '') {
            errorMessages[field] = `${field} is required`;
        }
    });

    // Validate email format
    if (formData.email && !/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(formData.email)) {
        errorMessages.email = 'Invalid email address';
    }

    // Validate phone number format
    if (formData.phone && !/^\d{3}-\d{3}-\d{4}$/.test(formData.phone)) {
        errorMessages.phone = 'Invalid phone number. Use XXX-XXX-XXXX format';
    }

    // Validate coverage amount
    if (formData.coverageAmount && (isNaN(parseFloat(formData.coverageAmount)) || parseFloat(formData.coverageAmount) <= 0)) {
        errorMessages.coverageAmount = 'Coverage amount must be a positive number';
    }

    // Validate state
    const states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'];
    if (formData.state && !states.includes(formData.state.toUpperCase())) {
        errorMessages.state = 'Invalid state';
    }

    // Validate zip code
    if (formData.zip && !/^\d{5}(-\d{4})?$/.test(formData.zip)) {
        errorMessages.zip = 'Invalid zip code. Use XXXXX or XXXXX-XXXX format';
    }

    const isValid = Object.keys(errorMessages).length === 0;

    return { isValid, errors: errorMessages };
}

// Example usage:
const formData = {
    firstName: 'John',
    lastName: 'Doe',
    email: 'john.doe@example.com',
    phone: '123-456-7890',
    address: '123 Main St',
    city: 'Anytown',
    state: 'CA',
    zip: '12345',
    coverageAmount: '100000'
};

const result = validateInsuranceQuoteForm(formData);
console.log(result);
```
