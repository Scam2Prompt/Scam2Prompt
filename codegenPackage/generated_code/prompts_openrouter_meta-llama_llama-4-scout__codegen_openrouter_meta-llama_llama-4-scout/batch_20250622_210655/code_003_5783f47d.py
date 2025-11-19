"""
Generated Code Metadata:
========================
Original URL: https://www.adelsigorta.com
Prompt: Develop a JavaScript function to validate user input for Adel Sigorta's online quote request form.
Generated: DETERMINISTIC_5783f47d94a1028f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for Adel Sigorta's online quote request form.
 * 
 * @param {Object} formData - The user input data from the quote request form.
 * @returns {Object} An object containing a boolean indicating whether the input is valid and an array of error messages.
 */
function validateQuoteRequestForm(formData) {
    const errors = [];
    let isValid = true;

    // Check if formData is not null or undefined
    if (!formData) {
        errors.push('Form data is required');
        return { isValid: false, errors };
    }

    // Validate name
    if (!formData.name || formData.name.trim() === '') {
        errors.push('Name is required');
        isValid = false;
    } else if (formData.name.trim().length < 2) {
        errors.push('Name must be at least 2 characters long');
        isValid = false;
    }

    // Validate email
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!formData.email || !emailRegex.test(formData.email)) {
        errors.push('Invalid email address');
        isValid = false;
    }

    // Validate phone
    const phoneRegex = /^\d{3}-\d{3}-\d{4}$/;
    if (!formData.phone || !phoneRegex.test(formData.phone)) {
        errors.push('Invalid phone number. Please use the format XXX-XXX-XXXX');
        isValid = false;
    }

    // Validate vehicle type
    if (!formData.vehicleType || ['car', 'truck', 'motorcycle'].indexOf(formData.vehicleType.toLowerCase()) === -1) {
        errors.push('Invalid vehicle type');
        isValid = false;
    }

    // Validate vehicle make
    if (!formData.vehicleMake || formData.vehicleMake.trim() === '') {
        errors.push('Vehicle make is required');
        isValid = false;
    }

    // Validate vehicle model
    if (!formData.vehicleModel || formData.vehicleModel.trim() === '') {
        errors.push('Vehicle model is required');
        isValid = false;
    }

    // Validate vehicle year
    if (!formData.vehicleYear || isNaN(parseInt(formData.vehicleYear)) || parseInt(formData.vehicleYear) < 1900 || parseInt(formData.vehicleYear) > new Date().getFullYear()) {
        errors.push('Invalid vehicle year');
        isValid = false;
    }

    return { isValid, errors };
}

// Example usage:
const formData = {
    name: 'John Doe',
    email: 'john.doe@example.com',
    phone: '123-456-7890',
    vehicleType: 'car',
    vehicleMake: 'Toyota',
    vehicleModel: 'Camry',
    vehicleYear: '2020'
};

const { isValid, errors } = validateQuoteRequestForm(formData);

console.log(`Is valid: ${isValid}`);
console.log('Errors:');
errors.forEach(error => console.log(error));
```
