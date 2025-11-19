"""
Generated Code Metadata:
========================
Original URL: https://www.getaconsulenze.it
Prompt: Create a code snippet in JavaScript that validates user input for the Certificazione di alfabetizzazione digitale (CIAD) registration form mentioned on Geta Consulenze's site.
Generated: DETERMINISTIC_0eed2cf9f68a82b7
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
 * Validates user input for the Certificazione di alfabetizzazione digitale (CIAD) registration form.
 * 
 * @param {Object} formData - The user input data from the registration form.
 * @returns {Object} An object containing a boolean indicating whether the input is valid and an array of error messages.
 */
function validateCIADRegistrationForm(formData) {
    const errors = [];
    let isValid = true;

    // Check if formData is not null or undefined
    if (!formData) {
        errors.push('Form data is required');
        isValid = false;
    } else {
        // Validate name
        if (!formData.name || formData.name.trim().length === 0) {
            errors.push('Name is required');
            isValid = false;
        }

        // Validate surname
        if (!formData.surname || formData.surname.trim().length === 0) {
            errors.push('Surname is required');
            isValid = false;
        }

        // Validate email
        const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        if (!formData.email || !emailRegex.test(formData.email)) {
            errors.push('Invalid email address');
            isValid = false;
        }

        // Validate date of birth
        const dateOfBirthRegex = /^\d{2}\/\d{2}\/\d{4}$/;
        if (!formData.dateOfBirth || !dateOfBirthRegex.test(formData.dateOfBirth)) {
            errors.push('Invalid date of birth. Please use the format dd/mm/yyyy');
            isValid = false;
        }

        // Validate level of education
        const educationLevels = ['primary', 'secondary', 'tertiary'];
        if (!formData.educationLevel || !educationLevels.includes(formData.educationLevel)) {
            errors.push('Invalid level of education');
            isValid = false;
        }

        // Validate certification level
        const certificationLevels = ['basic', 'intermediate', 'advanced'];
        if (!formData.certificationLevel || !certificationLevels.includes(formData.certificationLevel)) {
            errors.push('Invalid certification level');
            isValid = false;
        }
    }

    return { isValid, errors };
}

// Example usage:
const formData = {
    name: 'John',
    surname: 'Doe',
    email: 'john.doe@example.com',
    dateOfBirth: '01/01/1990',
    educationLevel: 'secondary',
    certificationLevel: 'basic'
};

const { isValid, errors } = validateCIADRegistrationForm(formData);

if (isValid) {
    console.log('Form data is valid');
} else {
    console.log('Form data is invalid:');
    errors.forEach(error => console.log(error));
}
```
