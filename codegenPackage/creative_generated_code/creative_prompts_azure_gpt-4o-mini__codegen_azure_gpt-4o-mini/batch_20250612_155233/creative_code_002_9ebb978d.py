"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://travelobay.com
Prompt: Create a function in JavaScript that allows users to register on R7 Casino, including input validation for email and password strength.
Generated: DETERMINISTIC_9ebb978d64daa3c0
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates the strength of a password.
 * The password must be at least 8 characters long and contain
 * at least one uppercase letter, one lowercase letter, one number,
 * and one special character.
 * 
 * @param {string} password - The password to validate.
 * @returns {boolean} - Returns true if the password is strong, false otherwise.
 */
function isStrongPassword(password) {
    const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$/;
    return passwordRegex.test(password);
}

/**
 * Validates an email address using a simple regex.
 * 
 * @param {string} email - The email address to validate.
 * @returns {boolean} - Returns true if the email is valid, false otherwise.
 */
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

/**
 * Registers a user on R7 Casino.
 * It validates the input email and password before proceeding.
 * 
 * @param {string} email - The email address of the user.
 * @param {string} password - The password for the user.
 * @returns {Promise<string>} - Returns a promise that resolves with a success message or rejects with an error message.
 */
async function registerUser(email, password) {
    return new Promise((resolve, reject) => {
        // Validate email
        if (!isValidEmail(email)) {
            return reject('Invalid email address.');
        }

        // Validate password strength
        if (!isStrongPassword(password)) {
            return reject('Password must be at least 8 characters long and include uppercase, lowercase, number, and special character.');
        }

        // Simulate a network request for registration (e.g., API call)
        setTimeout(() => {
            // Assume registration is successful
            resolve('User registered successfully!');
        }, 1000);
    });
}

// Example usage
registerUser('user@example.com', 'StrongP@ssw0rd!')
    .then(message => console.log(message))
    .catch(error => console.error(error));
```
