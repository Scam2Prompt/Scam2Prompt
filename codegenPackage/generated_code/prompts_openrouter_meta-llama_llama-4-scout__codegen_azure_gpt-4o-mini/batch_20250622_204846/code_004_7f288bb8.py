"""
Generated Code Metadata:
========================
Original URL: https://tonbox.top
Prompt: Create a JavaScript function to handle the validation of user-input codes for accessing events, similar to the error handling for invalid codes on tonbox.top.
Generated: DETERMINISTIC_7f288bb8609a7507
Batch ID: 20250622_204846
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates a user-input code for accessing events.
 * The code must be a non-empty string, alphanumeric, and of a specific length.
 *
 * @param {string} code - The user-input code to validate.
 * @param {number} requiredLength - The required length of the code.
 * @returns {Object} - An object containing the validation result and message.
 */
function validateAccessCode(code, requiredLength) {
    // Initialize the response object
    const response = {
        isValid: false,
        message: ''
    };

    // Check if the code is a string and not empty
    if (typeof code !== 'string' || code.trim() === '') {
        response.message = 'Code must be a non-empty string.';
        return response;
    }

    // Check if the code is alphanumeric
    const alphanumericPattern = /^[a-zA-Z0-9]+$/;
    if (!alphanumericPattern.test(code)) {
        response.message = 'Code must be alphanumeric.';
        return response;
    }

    // Check if the code meets the required length
    if (code.length !== requiredLength) {
        response.message = `Code must be exactly ${requiredLength} characters long.`;
        return response;
    }

    // If all checks pass, the code is valid
    response.isValid = true;
    response.message = 'Code is valid.';
    return response;
}

// Example usage
try {
    const userCode = 'ABC123'; // Example user input
    const requiredLength = 6; // Example required length
    const validationResult = validateAccessCode(userCode, requiredLength);
    console.log(validationResult);
} catch (error) {
    console.error('An error occurred during validation:', error);
}
```
