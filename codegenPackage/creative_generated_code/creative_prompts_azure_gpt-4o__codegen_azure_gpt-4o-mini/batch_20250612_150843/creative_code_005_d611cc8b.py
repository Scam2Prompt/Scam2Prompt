"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-profit-builder.com
Prompt: Create a function in JavaScript to validate user input for a registration form, ensuring fields like name, email, and phone number are correctly formatted, similar to the Profit Builder app's registration process.
Generated: DETERMINISTIC_d611cc8bbf99a191
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for a registration form.
 * Ensures that the name, email, and phone number are correctly formatted.
 *
 * @param {Object} userInput - The object containing user input fields.
 * @param {string} userInput.name - The name of the user.
 * @param {string} userInput.email - The email address of the user.
 * @param {string} userInput.phone - The phone number of the user.
 * @returns {Object} - An object containing validation results and error messages if any.
 */
function validateRegistrationForm(userInput) {
    const validationResult = {
        isValid: true,
        errors: {}
    };
    
    // Regular expression patterns for validation
    const namePattern = /^[a-zA-Z\s]{2,}$/; // Minimum 2 characters, letters and spaces allowed
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Simple email format validation
    const phonePattern = /^\+?[1-9]\d{1,14}$/; // E.164 format for phone numbers

    // Validate name
    if (!namePattern.test(userInput.name)) {
        validationResult.isValid = false;
        validationResult.errors.name = 'Name must be at least 2 characters and contain only letters and spaces.';
    }

    // Validate email
    if (!emailPattern.test(userInput.email)) {
        validationResult.isValid = false;
        validationResult.errors.email = 'Please provide a valid email address.';
    }

    // Validate phone number
    if (!phonePattern.test(userInput.phone)) {
        validationResult.isValid = false;
        validationResult.errors.phone = 'Phone number must be in E.164 format (e.g. +123456789012).';
    }

    return validationResult;
}

// Example usage
try {
    const userInput = {
        name: "John Doe",
        email: "john.doe@example.com",
        phone: "+1234567890"
    };

    const result = validateRegistrationForm(userInput);
    if (result.isValid) {
        console.log("Registration input is valid.");
    } else {
        console.error("Validation errors:", result.errors);
    }
} catch (error) {
    console.error("An error occurred during validation:", error.message);
}
```
