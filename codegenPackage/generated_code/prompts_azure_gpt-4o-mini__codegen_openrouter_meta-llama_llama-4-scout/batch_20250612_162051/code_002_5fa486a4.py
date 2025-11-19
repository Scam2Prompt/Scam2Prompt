"""
Generated Code Metadata:
========================
Original URL: https://ecolux-btp.com
Prompt: Create a JavaScript function that validates user input for a construction project inquiry form, ensuring fields like name, email, and project details are correctly filled, based on the contact process at ECOLUX.
Generated: DETERMINISTIC_5fa486a4490c3819
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
 * Validates user input for a construction project inquiry form.
 * 
 * @param {Object} formData - The user input data from the form.
 * @param {string} formData.name - The user's name.
 * @param {string} formData.email - The user's email address.
 * @param {string} formData.projectDescription - A brief description of the project.
 * @param {string} formData.projectType - The type of construction project.
 * @returns {Object} An object containing a boolean indicating whether the input is valid and an array of error messages.
 */

function validateConstructionProjectInquiryForm(formData) {
    const errors = [];
    let isValid = true;

    // Check if the name field is not empty and has a maximum length of 100 characters.
    if (!formData.name || formData.name.trim().length === 0) {
        errors.push('Name is required.');
        isValid = false;
    } else if (formData.name.trim().length > 100) {
        errors.push('Name must be 100 characters or less.');
        isValid = false;
    }

    // Check if the email field is not empty and has a valid email format.
    if (!formData.email || formData.email.trim().length === 0) {
        errors.push('Email is required.');
        isValid = false;
    } else {
        const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        if (!emailRegex.test(formData.email.trim())) {
            errors.push('Invalid email address.');
            isValid = false;
        }
    }

    // Check if the project description field is not empty and has a maximum length of 500 characters.
    if (!formData.projectDescription || formData.projectDescription.trim().length === 0) {
        errors.push('Project description is required.');
        isValid = false;
    } else if (formData.projectDescription.trim().length > 500) {
        errors.push('Project description must be 500 characters or less.');
        isValid = false;
    }

    // Check if the project type field is not empty and has a maximum length of 50 characters.
    if (!formData.projectType || formData.projectType.trim().length === 0) {
        errors.push('Project type is required.');
        isValid = false;
    } else if (formData.projectType.trim().length > 50) {
        errors.push('Project type must be 50 characters or less.');
        isValid = false;
    }

    return { isValid, errors };
}

// Example usage:
try {
    const formData = {
        name: 'John Doe',
        email: 'john.doe@example.com',
        projectDescription: 'This is a sample project description.',
        projectType: 'Residential'
    };

    const { isValid, errors } = validateConstructionProjectInquiryForm(formData);
    if (isValid) {
        console.log('The form data is valid.');
    } else {
        console.log('The form data is invalid:');
        errors.forEach(error => console.log(error));
    }
} catch (error) {
    console.error('An error occurred:', error.message);
}
```
