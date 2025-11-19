"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rayatrecruitment.com
Prompt: Write a JavaScript function to validate the application form fields for Rayat Shikshan Sanstha's online application, ensuring all required information is correctly filled.
Generated: DETERMINISTIC_b721f522da17fa61
Batch ID: 20250612_160742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates the application form fields for Rayat Shikshan Sanstha's online application.
 * @param {Object} formData - An object containing form field values.
 * @returns {Object} - An object containing validation results and messages.
 */
function validateApplicationForm(formData) {
    // Initialize an object to hold validation results
    const validationResults = {
        isValid: true,
        messages: []
    };

    // Required fields
    const requiredFields = ['name', 'email', 'phone', 'address', 'course'];

    // Check for missing required fields
    requiredFields.forEach(field => {
        if (!formData[field]) {
            validationResults.isValid = false;
            validationResults.messages.push(`${field} is required.`);
        }
    });

    // Validate email format
    if (formData.email && !isValidEmail(formData.email)) {
        validationResults.isValid = false;
        validationResults.messages.push('Email is not valid.');
    }

    // Validate phone number format (example format: 123-456-7890)
    if (formData.phone && !isValidPhone(formData.phone)) {
        validationResults.isValid = false;
        validationResults.messages.push('Phone number is not valid.');
    }

    return validationResults;
}

/**
 * Validates the format of an email address.
 * @param {string} email - The email address to validate.
 * @returns {boolean} - True if valid, otherwise false.
 */
function isValidEmail(email) {
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailPattern.test(email);
}

/**
 * Validates the format of a phone number.
 * @param {string} phone - The phone number to validate.
 * @returns {boolean} - True if valid, otherwise false.
 */
function isValidPhone(phone) {
    const phonePattern = /^\d{3}-\d{3}-\d{4}$/;
    return phonePattern.test(phone);
}

// Example usage:
const formData = {
    name: "John Doe",
    email: "johndoe@example.com",
    phone: "123-456-7890",
    address: "123 Main St",
    course: "Computer Science"
};

const validation = validateApplicationForm(formData);

if (!validation.isValid) {
    console.error("Validation Errors:", validation.messages);
} else {
    console.log("Form is valid.");
}
```
