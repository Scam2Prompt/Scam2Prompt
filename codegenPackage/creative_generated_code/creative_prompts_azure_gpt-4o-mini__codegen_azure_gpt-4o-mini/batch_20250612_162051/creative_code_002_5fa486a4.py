"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecolux-btp.com
Prompt: Create a JavaScript function that validates user input for a construction project inquiry form, ensuring fields like name, email, and project details are correctly filled, based on the contact process at ECOLUX.
Generated: DETERMINISTIC_5fa486a4490c3819
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for a construction project inquiry form.
 * Ensures that the name, email, and project details fields are correctly filled.
 *
 * @param {Object} formData - An object containing form input data.
 * @param {string} formData.name - The name of the user.
 * @param {string} formData.email - The email address of the user.
 * @param {string} formData.projectDetails - The details of the project.
 * @returns {Object} - An object containing validation results and messages.
 */
function validateInquiryForm(formData) {
    // Initialize an object to store validation results
    const validationResults = {
        isValid: true,
        messages: []
    };

    // Validate name
    if (!formData.name || formData.name.trim() === '') {
        validationResults.isValid = false;
        validationResults.messages.push('Name is required.');
    }

    // Validate email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!formData.email || !emailRegex.test(formData.email)) {
        validationResults.isValid = false;
        validationResults.messages.push('A valid email address is required.');
    }

    // Validate project details
    if (!formData.projectDetails || formData.projectDetails.trim() === '') {
        validationResults.isValid = false;
        validationResults.messages.push('Project details are required.');
    }

    return validationResults;
}

// Example usage:
try {
    const formData = {
        name: 'John Doe',
        email: 'john.doe@example.com',
        projectDetails: 'Need a new roof installed.'
    };

    const result = validateInquiryForm(formData);
    if (result.isValid) {
        console.log('Form is valid. Proceed with the inquiry.');
    } else {
        console.error('Form validation errors:', result.messages.join(' '));
    }
} catch (error) {
    console.error('An error occurred during form validation:', error);
}
```
