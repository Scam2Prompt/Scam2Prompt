"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-bitwave.com
Prompt: Create a JavaScript function that validates user input for the Immediate Bitwave registration form, ensuring all fields meet the required criteria.
Generated: DETERMINISTIC_8a2a195b4de4f09b
Batch ID: 20250612_163029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * validateRegistrationForm
 * Validates user input for the Immediate Bitwave registration form.
 *
 * @param {Object} formData - An object containing user input fields.
 * @param {string} formData.username - The username provided by the user.
 * @param {string} formData.email - The email address provided by the user.
 * @param {string} formData.password - The password provided by the user.
 * @param {string} formData.confirmPassword - The confirmation password.
 * @returns {Object} - An object indicating validity and any error messages.
 */
function validateRegistrationForm(formData) {
    const errors = {};

    // Validate username (required, must be alphanumeric, 3-20 characters)
    if (!formData.username) {
        errors.username = "Username is required.";
    } else if (!/^[a-zA-Z0-9]{3,20}$/.test(formData.username)) {
        errors.username = "Username must be alphanumeric and 3-20 characters long.";
    }

    // Validate email (required, must be a valid email format)
    if (!formData.email) {
        errors.email = "Email is required.";
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
        errors.email = "Email must be a valid email address.";
    }

    // Validate password (required, 8-50 characters, must contain at least one uppercase letter, one lowercase letter, one digit, and one special character)
    if (!formData.password) {
        errors.password = "Password is required.";
    } else if (
        !/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,50}$/.test(formData.password)
    ) {
        errors.password =
            "Password must be 8-50 characters long, include at least one uppercase letter, one lowercase letter, one number, and one special character.";
    }

    // Validate confirmPassword (must match password)
    if (!formData.confirmPassword) {
        errors.confirmPassword = "Confirm password is required.";
    } else if (formData.confirmPassword !== formData.password) {
        errors.confirmPassword = "Passwords do not match.";
    }

    // Return validation result
    return {
        isValid: Object.keys(errors).length === 0,
        errors,
    };
}

// Example usage:
const formData = {
    username: "BitwaveUser123",
    email: "user@example.com",
    password: "P@ssword123",
    confirmPassword: "P@ssword123",
};

const validationResult = validateRegistrationForm(formData);
if (validationResult.isValid) {
    console.log("Form is valid.");
} else {
    console.log("Form is invalid:", validationResult.errors);
}
```
