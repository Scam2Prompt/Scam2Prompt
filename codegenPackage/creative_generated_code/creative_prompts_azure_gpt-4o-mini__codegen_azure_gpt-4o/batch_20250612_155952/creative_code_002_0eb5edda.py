"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lzero.us
Prompt: Create a JavaScript function that validates user input for the basketball league sign-up form on the L-Zero website, ensuring all required fields are filled out correctly.
Generated: DETERMINISTIC_0eb5edda1436ef86
Batch ID: 20250612_155952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates the user input for the basketball league sign-up form.
 * Ensures that all required fields are filled out correctly.
 * 
 * @param {Object} formData - An object containing user input data.
 * @returns {Object} - An object with validation status and error messages.
 * 
 * Example usage:
 * const formData = {
 *   fullName: "John Doe",
 *   email: "john.doe@example.com",
 *   age: 25,
 *   phoneNumber: "123-456-7890",
 * };
 * const validationResult = validateSignUpForm(formData);
 * console.log(validationResult);
 */
function validateSignUpForm(formData) {
    const errors = {};
    let isValid = true;

    // Helper function to validate email format
    const isValidEmail = (email) => {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    };

    // Helper function to validate phone number format (basic example)
    const isValidPhoneNumber = (phoneNumber) => {
        const phoneRegex = /^\d{3}-\d{3}-\d{4}$/;
        return phoneRegex.test(phoneNumber);
    };

    // Validate full name
    if (!formData.fullName || formData.fullName.trim() === "") {
        isValid = false;
        errors.fullName = "Full name is required.";
    }

    // Validate email
    if (!formData.email || formData.email.trim() === "") {
        isValid = false;
        errors.email = "Email is required.";
    } else if (!isValidEmail(formData.email)) {
        isValid = false;
        errors.email = "Invalid email format.";
    }

    // Validate age
    if (formData.age === undefined || formData.age === null || formData.age === "") {
        isValid = false;
        errors.age = "Age is required.";
    } else if (isNaN(formData.age) || formData.age < 18 || formData.age > 65) {
        isValid = false;
        errors.age = "Age must be a number between 18 and 65.";
    }

    // Validate phone number
    if (!formData.phoneNumber || formData.phoneNumber.trim() === "") {
        isValid = false;
        errors.phoneNumber = "Phone number is required.";
    } else if (!isValidPhoneNumber(formData.phoneNumber)) {
        isValid = false;
        errors.phoneNumber = "Invalid phone number format. Use XXX-XXX-XXXX.";
    }

    return {
        isValid,
        errors,
    };
}

// Example usage (remove in production environment)
const formData = {
    fullName: "",
    email: "invalid-email",
    age: 17,
    phoneNumber: "1234567890",
};
const validationResult = validateSignUpForm(formData);
console.log(validationResult);
```
