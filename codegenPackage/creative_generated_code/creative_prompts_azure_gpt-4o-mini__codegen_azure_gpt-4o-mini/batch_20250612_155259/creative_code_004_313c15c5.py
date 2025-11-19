"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.smarti.edu.pk
Prompt: Create a JavaScript function that validates user input for the admission query form at SMA Rizvi Textile Institute, ensuring all required fields are filled out correctly.
Generated: DETERMINISTIC_313c15c5657f3c26
Batch ID: 20250612_155259
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates the user input for the admission query form at SMA Rizvi Textile Institute.
 * Ensures all required fields are filled out correctly.
 * 
 * @param {Object} formData - The input data from the form.
 * @returns {Object} - An object containing the validation status and error messages, if any.
 */
function validateAdmissionForm(formData) {
    // Initialize an object to store validation results
    const validationResult = {
        isValid: true,
        errors: []
    };

    // Validate the name field
    if (!formData.name || formData.name.trim() === "") {
        validationResult.isValid = false;
        validationResult.errors.push("Name is required.");
    }

    // Validate the email field
    if (!formData.email || formData.email.trim() === "") {
        validationResult.isValid = false;
        validationResult.errors.push("Email is required.");
    } else if (!validateEmail(formData.email)) {
        validationResult.isValid = false;
        validationResult.errors.push("Email format is invalid.");
    }

    // Validate the phone number field
    if (!formData.phone || formData.phone.trim() === "") {
        validationResult.isValid = false;
        validationResult.errors.push("Phone number is required.");
    } else if (!validatePhoneNumber(formData.phone)) {
        validationResult.isValid = false;
        validationResult.errors.push("Phone number format is invalid. It should contain only digits.");
    }

    // Validate the message field
    if (!formData.message || formData.message.trim() === "") {
        validationResult.isValid = false;
        validationResult.errors.push("Message is required.");
    }

    return validationResult;
}

/**
 * Validates the email format using a regular expression.
 * 
 * @param {string} email - The email string to validate.
 * @returns {boolean} - Returns true if the email is valid, otherwise false.
 */
function validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

/**
 * Validates the phone number format to ensure it contains only digits.
 * 
 * @param {string} phone - The phone number string to validate.
 * @returns {boolean} - Returns true if the phone number is valid, otherwise false.
 */
function validatePhoneNumber(phone) {
    const phoneRegex = /^\d+$/;
    return phoneRegex.test(phone);
}

// Example usage:
const formData = {
    name: "John Doe",
    email: "john.doe@example.com",
    phone: "1234567890",
    message: "I would like more information about the admission process."
};

const result = validateAdmissionForm(formData);
if (!result.isValid) {
    console.error("Validation failed:", result.errors);
} else {
    console.log("Validation succeeded.");
}
```
