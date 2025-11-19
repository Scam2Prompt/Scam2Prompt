"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://as-media.rs
Prompt: Create a JavaScript function that allows users to register and log in to a music streaming service similar to Radio S, focusing on user experience and security.
Generated: DETERMINISTIC_b07eae2d5a3d2a3d
Batch ID: 20250612_164316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * A simple implementation of user registration and login functionality for a music streaming service.
 * This example uses bcrypt for hashing passwords and a mock database object.
 * 
 * Note: In a production environment, you should replace the mock database with a real database.
 * Also, ensure the code is executed in a secure server environment with HTTPS enabled.
 */

const bcrypt = require('bcrypt'); // For hashing passwords
const crypto = require("crypto"); // For generating a secure session token

// Mock database for simplicity
const mockDB = {
    users: {}, // Stores user data in the format {username: {passwordHash, sessionToken}}
};

/**
 * Registers a new user.
 * @param {string} username - The username of the new user.
 * @param {string} password - The password of the new user.
 * @returns {string} - Success message or error message.
 */
async function registerUser(username, password) {
    try {
        // Input validation
        if (!username || !password) {
            return "Username and password are required.";
        }
        if (mockDB.users[username]) {
            return "Username is already taken.";
        }

        // Hash the password using bcrypt
        const saltRounds = 10;
        const passwordHash = await bcrypt.hash(password, saltRounds);

        // Save the user in the mock database
        mockDB.users[username] = { passwordHash, sessionToken: null };

        return "User registered successfully.";
    } catch (error) {
        console.error("Error during registration:", error);
        return "An error occurred during registration. Please try again.";
    }
}

/**
 * Logs in an existing user.
 * @param {string} username - The username of the user.
 * @param {string} password - The password of the user.
 * @returns {string} - Success message with session token or error message.
 */
async function loginUser(username, password) {
    try {
        // Input validation
        if (!username || !password) {
            return "Username and password are required.";
        }
        const user = mockDB.users[username];
        if (!user) {
            return "Invalid username or password.";
        }

        // Verify the password hash using bcrypt
        const isPasswordMatch = await bcrypt.compare(password, user.passwordHash);
        if (!isPasswordMatch) {
            return "Invalid username or password.";
        }

        // Generate a secure session token using crypto
        const sessionToken = crypto.randomBytes(32).toString("hex");
        user.sessionToken = sessionToken;

        return `Login successful. Your session token: ${sessionToken}`;
    } catch (error) {
        console.error("Error during login:", error);
        return "An error occurred during login. Please try again.";
    }
}

/**
 * Example usage of the registration and login functionality.
 */
(async () => {
    console.log(await registerUser("musicLover", "securePassword123")); // Register a user
    console.log(await loginUser("musicLover", "securePassword123")); // Log in the user
    console.log(await loginUser("musicLover", "wrongPassword")); // Attempt login with incorrect password
})();
```

**Dependencies**:  
Install `bcrypt` using `npm install bcrypt`.
