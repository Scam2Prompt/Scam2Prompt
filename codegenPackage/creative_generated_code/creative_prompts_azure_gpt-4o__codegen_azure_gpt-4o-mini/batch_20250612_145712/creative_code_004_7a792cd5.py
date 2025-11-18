"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://microlab.world
Prompt: Write a JavaScript function to validate username and password input fields on a login form, ensuring compatibility with a system like MicroLab.
Generated: DETERMINISTIC_7a792cd59f1ce003
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates the username and password input fields on a login form.
 *
 * @param {string} username - The username input value.
 * @param {string} password - The password input value.
 * @returns {Object} - An object containing a boolean 'isValid' and an 'errorMessage' if invalid.
 */
function validateLoginInput(username, password) {
    // Initialize validation result object
    const result = {
        isValid: true,
        errorMessage: ''
    };

    // Define regex for username: Alphanumeric characters only, length 3-20
    const usernameRegex = /^[a-zA-Z0-9]{3,20}$/;

    // Define regex for password: Minimum 8 characters, at least one uppercase, one lowercase, one digit, one special character
    const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;

    // Validate username
    if (!usernameRegex.test(username)) {
        result.isValid = false;
        result.errorMessage += 'Username must be 3-20 characters long and contain only alphanumeric characters.\n';
    }

    // Validate password
    if (!passwordRegex.test(password)) {
        result.isValid = false;
        result.errorMessage += 'Password must be at least 8 characters long and include at least one uppercase letter, one lowercase letter, one number, and one special character.\n';
    }

    return result;
}

// Example usage
try {
    const username = 'User123';
    const password = 'Password@1';
    const validation = validateLoginInput(username, password);

    if (validation.isValid) {
        console.log('Login input is valid.');
    } else {
        console.error('Validation errors:\n' + validation.errorMessage);
    }
} catch (error) {
    console.error('An unexpected error occurred during validation:', error);
}
```
