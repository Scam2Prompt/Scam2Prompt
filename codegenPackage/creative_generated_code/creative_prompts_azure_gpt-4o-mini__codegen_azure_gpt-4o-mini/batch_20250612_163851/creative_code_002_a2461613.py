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
 * Validates user input for the "Elusive Self-Love" webinar registration form.
 * 
 * @param {Object} formData - The user input data.
 * @param {string} formData.name - The name of the user.
 * @param {string} formData.email - The email address of the user.
 * @param {string} formData.password - The password chosen by the user.
 * @param {string} formData.confirmPassword - Confirmation of the user's password.
 * @returns {Object} - An object containing a success flag and an array of error messages.
 */
function validateRegistrationForm(formData) {
    const errors = [];
    const { name, email, password, confirmPassword } = formData;

    // Check if name is provided and is a valid string
    if (!name || typeof name !== 'string' || name.trim().length === 0) {
        errors.push("Name is required and must be a valid string.");
    }

    // Check if email is provided and is a valid format
    if (!email || typeof email !== 'string' || !validateEmail(email)) {
        errors.push("A valid email address is required.");
    }

    // Check if password is provided and meets the length criteria
    if (!password || typeof password !== 'string' || password.length < 8) {
        errors.push("Password must be at least 8 characters long.");
    }

    // Check if passwords match
    if (password !== confirmPassword) {
        errors.push("Passwords do not match.");
    }
    
    // Return result
    return {
        success: errors.length === 0,
        errors: errors
    };
}

/**
 * Validates the format of an email address.
 * 
 * @param {string} email - The email address to validate.
 * @returns {boolean} - True if the email is valid, otherwise false.
 */
function validateEmail(email) {
    // Basic regex for email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Example usage:
const registrationData = {
    name: "John Doe",
    email: "john.doe@example.com",
    password: "securePassword123",
    confirmPassword: "securePassword123"
};

const validationResult = validateRegistrationForm(registrationData);
if (validationResult.success) {
    console.log("Registration is valid. Proceeding with registration.");
} else {
    console.error("Registration failed with the following errors:");
    validationResult.errors.forEach(error => console.error(`- ${error}`));
}
```
