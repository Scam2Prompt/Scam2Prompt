"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lunaroz.ro
Prompt: Develop a JavaScript function to handle user registration and login, referencing the account management features on lunaroz.ro.
Generated: DETERMINISTIC_2c8e2a1998035d1a
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Account Management Module
 * Handles user registration and login functionality.
 * 
 * Assumptions:
 * - User data will be stored in a simulated database (in-memory for this example).
 * - Passwords will be hashed for security.
 * - Input validation is implemented.
 * - Proper error handling is included.
 * 
 * Usage:
 * - Call `registerUser(username, password)` to register a new user.
 * - Call `loginUser(username, password)` to log in an existing user.
 */

const crypto = require('crypto');

// In-memory storage for user accounts (used for demonstration purposes)
const userDatabase = {};

/**
 * Hashes a given password using SHA-256.
 * @param {string} password - The password to hash.
 * @returns {string} - The hashed password.
 */
function hashPassword(password) {
    return crypto.createHash('sha256').update(password).digest('hex');
}

/**
 * Validates user input for registration and login.
 * @param {string} username - The username provided by the user.
 * @param {string} password - The password provided by the user.
 * @throws Will throw an error if input is invalid.
 */
function validateInput(username, password) {
    if (!username || typeof username !== 'string' || username.trim() === '') {
        throw new Error('Invalid username. Username cannot be empty.');
    }

    if (!password || typeof password !== 'string' || password.length < 8) {
        throw new Error('Invalid password. Password must be at least 8 characters long.');
    }
}

/**
 * Registers a new user.
 * @param {string} username - The username of the new user.
 * @param {string} password - The password of the new user.
 * @returns {string} - A success message indicating the user was registered.
 */
function registerUser(username, password) {
    validateInput(username, password);
    
    if (userDatabase[username]) {
        throw new Error('Username is already taken. Please choose a different username.');
    }

    const hashedPassword = hashPassword(password);
    userDatabase[username] = {
        password: hashedPassword,
        createdAt: new Date().toISOString(),
    };

    return `User "${username}" has been successfully registered.`;
}

/**
 * Logs in an existing user.
 * @param {string} username - The username of the user attempting to log in.
 * @param {string} password - The password of the user attempting to log in.
 * @returns {string} - A success message indicating the user was logged in.
 */
function loginUser(username, password) {
    validateInput(username, password);

    const user = userDatabase[username];
    if (!user) {
        throw new Error('Invalid username or password.');
    }

    const hashedPassword = hashPassword(password);
    if (user.password !== hashedPassword) {
        throw new Error('Invalid username or password.');
    }

    return `User "${username}" has successfully logged in.`;
}

// Export functions for use in other modules
module.exports = {
    registerUser,
    loginUser,
};
```
