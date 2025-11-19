"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://melikataheri.com
Prompt: Create a JavaScript function that validates user input for a registration form for the "Elusive Self-Love" webinar, ensuring it captures necessary details as outlined on Melika Taheri's site.
Generated: DETERMINISTIC_a24616136ba0c683
Batch ID: 20250612_163851
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * validateRegistrationForm - Validates user input for the "Elusive Self-Love" webinar registration form.
 * Ensures all necessary details are captured and adhere to specified validation rules.
 * 
 * @param {Object} formData - The user input data from the registration form.
 * @param {string} formData.fullName - The full name of the user (required).
 * @param {string} formData.email - The email address of the user (required, valid format).
 * @param {number} formData.age - The age of the user (optional, must be a positive integer if provided).
 * @param {string} formData.phoneNumber - The phone number of the user (optional, valid format).
 * @returns {Object} - An object indicating whether validation succeeded and any validation errors.
 */
function validateRegistrationForm(formData) {
    const errors = {};

    // Validate full name (required, non-empty)
    if (!formData.fullName || formData.fullName.trim() === "") {
        errors.fullName = "Full name is required.";
    }

    // Validate email (required, valid format)
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!formData.email || formData.email.trim() === "") {
        errors.email = "Email is required.";
    } else if (!emailRegex.test(formData.email)) {
        errors.email = "Invalid email format.";
    }

    // Validate age (optional, positive integer)
    if (formData.age !== undefined) {
        if (!Number.isInteger(formData.age) || formData.age <= 0) {
            errors.age = "Age must be a positive integer.";
        }
    }

    // Validate phone number (optional, valid format: 10-15 digits)
    const phoneRegex = /^\d{10,15}$/;
    if (formData.phoneNumber && !phoneRegex.test(formData.phoneNumber)) {
        errors.phoneNumber = "Phone number must be between 10 and 15 digits.";
    }

    // Final validation result
    const isValid = Object.keys(errors).length === 0;

    return {
        isValid,
        errors,
    };
}

// Example usage:
const formData = {
    fullName: "John Doe",
    email: "john.doe@example.com",
    age: 25,
    phoneNumber: "1234567890",
};

const validationResult = validateRegistrationForm(formData);
if (validationResult.isValid) {
    console.log("Registration form is valid!");
} else {
    console.error("Validation errors:", validationResult.errors);
}
```
