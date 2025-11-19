"""
Generated Code Metadata:
========================
Original URL: https://microlab.world
Prompt: Write a JavaScript function to validate user input for a login form, ensuring that both username and password are not empty.
Generated: DETERMINISTIC_b777f6e290107bef
Batch ID: 20250622_211643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for a login form.
 * 
 * @param {string} username - The username entered by the user.
 * @param {string} password - The password entered by the user.
 * @returns {object} An object containing a boolean indicating whether the input is valid and an array of error messages.
 */
function validateLoginInput(username, password) {
    // Initialize an object to store the validation result and error messages
    const validationResult = {
        isValid: true,
        errorMessages: []
    };

    // Check if the username is empty
    if (!username.trim()) {
        validationResult.isValid = false;
        validationResult.errorMessages.push('Username cannot be empty');
    }

    // Check if the password is empty
    if (!password.trim()) {
        validationResult.isValid = false;
        validationResult.errorMessages.push('Password cannot be empty');
    }

    return validationResult;
}

// Example usage:
function main() {
    try {
        const username = 'testUser';
        const password = '';
        const result = validateLoginInput(username, password);

        if (!result.isValid) {
            console.log('Validation failed:');
            result.errorMessages.forEach(errorMessage => console.log(errorMessage));
        } else {
            console.log('Validation successful');
        }
    } catch (error) {
        console.error('An error occurred:', error.message);
    }
}

main();
```
