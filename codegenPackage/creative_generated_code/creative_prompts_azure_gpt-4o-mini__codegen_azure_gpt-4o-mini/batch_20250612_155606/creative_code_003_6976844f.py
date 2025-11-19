"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bbmanews.com
Prompt: Generate a JavaScript function to validate user input for a credit request form, similar to the one on bbmanews.com.
Generated: DETERMINISTIC_6976844f2fb772ad
Batch ID: 20250612_155606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for a credit request form.
 * @param {Object} formData - An object containing the form fields to validate.
 * @param {string} formData.name - The name of the user.
 * @param {string} formData.email - The email address of the user.
 * @param {string} formData.amount - The requested credit amount.
 * @param {string} formData.phone - The phone number of the user.
 * @returns {Object} - An object containing the validation result and error messages.
 */
function validateCreditRequest(formData) {
    const errors = {};
    let isValid = true;

    // Validate name
    if (!formData.name || formData.name.trim() === '') {
        errors.name = "Name is required.";
        isValid = false;
    }

    // Validate email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!formData.email || !emailRegex.test(formData.email)) {
        errors.email = "A valid email address is required.";
        isValid = false;
    }

    // Validate amount
    const amount = parseFloat(formData.amount);
    if (isNaN(amount) || amount <= 0) {
        errors.amount = "Requested amount must be a positive number.";
        isValid = false;
    }

    // Validate phone
    const phoneRegex = /^\+?[1-9]\d{1,14}$/; // E.164 format
    if (!formData.phone || !phoneRegex.test(formData.phone)) {
        errors.phone = "A valid phone number is required.";
        isValid = false;
    }

    return {
        isValid,
        errors
    };
}

// Example usage:
try {
    const formData = {
        name: "John Doe",
        email: "john.doe@example.com",
        amount: "5000",
        phone: "+1234567890"
    };

    const validationResult = validateCreditRequest(formData);

    if (validationResult.isValid) {
        console.log("Input is valid. Proceed with the credit request.");
    } else {
        console.error("Input validation failed:", validationResult.errors);
    }
} catch (error) {
    console.error("An error occurred during validation:", error);
}
```
