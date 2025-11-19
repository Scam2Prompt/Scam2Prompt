"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ayushmancollege.com
Prompt: Write a JavaScript function that validates user input for the online application form for the Bachelor of Physiotherapy (BPTh) course at Ayushman College.
Generated: DETERMINISTIC_848f2a928a1757be
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for the Bachelor of Physiotherapy (BPTh) course application form.
 * 
 * @param {Object} formData - The user input data from the application form.
 * @param {string} formData.fullName - The full name of the applicant.
 * @param {string} formData.email - The email address of the applicant.
 * @param {string} formData.phone - The phone number of the applicant.
 * @param {number} formData.age - The age of the applicant.
 * @returns {Object} - An object containing validation results and messages.
 */
function validateApplicationForm(formData) {
    const validationResults = {
        isValid: true,
        messages: []
    };

    // Validate full name
    if (!formData.fullName || typeof formData.fullName !== 'string' || formData.fullName.trim().length < 2) {
        validationResults.isValid = false;
        validationResults.messages.push('Full name is required and must be at least 2 characters long.');
    }

    // Validate email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!formData.email || !emailRegex.test(formData.email)) {
        validationResults.isValid = false;
        validationResults.messages.push('A valid email address is required.');
    }

    // Validate phone number
    const phoneRegex = /^\d{10}$/; // Assuming a 10-digit phone number without formatting
    if (!formData.phone || !phoneRegex.test(formData.phone)) {
        validationResults.isValid = false;
        validationResults.messages.push('Phone number must be a 10-digit number.');
    }

    // Validate age
    if (typeof formData.age !== 'number' || formData.age < 18 || formData.age > 35) {
        validationResults.isValid = false;
        validationResults.messages.push('Age must be a number between 18 and 35.');
    }

    return validationResults;
}

// Example usage:
try {
    const applicantData = {
        fullName: 'John Doe',
        email: 'john.doe@example.com',
        phone: '1234567890',
        age: 25
    };

    const validation = validateApplicationForm(applicantData);
    if (!validation.isValid) {
        console.error('Validation Errors:', validation.messages);
    } else {
        console.log('Application is valid. Proceed with submission.');
    }
} catch (error) {
    console.error('An error occurred during validation:', error.message);
}
```
