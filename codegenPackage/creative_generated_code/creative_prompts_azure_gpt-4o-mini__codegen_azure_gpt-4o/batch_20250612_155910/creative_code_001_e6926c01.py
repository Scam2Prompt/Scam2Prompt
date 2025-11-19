"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinrush.bet
Prompt: Write a JavaScript function that allows users to register on the Coin Rush platform and receive a welcome bonus.
Generated: DETERMINISTIC_e6926c011b4e4b10
Batch ID: 20250612_155910
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * A function to register a user on the Coin Rush platform and provide a welcome bonus.
 * 
 * This function accepts user details, validates the data, and stores it in the system.
 * Upon successful registration, the user receives a welcome bonus.
 * 
 * @param {Object} userDetails - The details of the user to be registered.
 * @param {string} userDetails.username - The username of the user.
 * @param {string} userDetails.email - The email of the user.
 * @param {string} userDetails.password - The password of the user.
 * @returns {Object} Response object containing registration status and welcome bonus details.
 */
function registerUser(userDetails) {
    // Constants
    const WELCOME_BONUS = 100; // Welcome bonus amount
    const MIN_PASSWORD_LENGTH = 8; // Minimum password length

    // Simulated database for user storage
    const userDatabase = [];

    try {
        // Validate input
        if (!userDetails || typeof userDetails !== 'object') {
            throw new Error("Invalid input: userDetails must be an object.");
        }

        const { username, email, password } = userDetails;

        if (!username || username.trim() === '') {
            throw new Error("Invalid input: username is required.");
        }

        if (!email || !email.match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/)) {
            throw new Error("Invalid input: a valid email is required.");
        }

        if (!password || password.length < MIN_PASSWORD_LENGTH) {
            throw new Error(`Invalid input: password must be at least ${MIN_PASSWORD_LENGTH} characters long.`);
        }

        // Check if email is already registered
        const isEmailRegistered = userDatabase.some(user => user.email === email);

        if (isEmailRegistered) {
            throw new Error("Email is already registered.");
        }

        // Register user
        const newUser = {
            id: Date.now(), // Unique ID
            username,
            email,
            passwordHash: hashPassword(password), // Hash the password before storing
            welcomeBonus: WELCOME_BONUS,
        };

        userDatabase.push(newUser);

        // Return success response
        return {
            success: true,
            message: `Welcome, ${username}! You have been awarded a bonus of ${WELCOME_BONUS} coins.`,
            userId: newUser.id,
            bonus: WELCOME_BONUS,
        };
    } catch (error) {
        // Handle errors and return error response
        return {
            success: false,
            message: error.message,
        };
    }

    /**
     * A helper function to hash the password.
     * 
     * @param {string} password - The plain text password.
     * @returns {string} The hashed password.
     */
    function hashPassword(password) {
        // Note: This is a placeholder. In a real application, use a secure hashing library like bcrypt.
        return `hashed_${password}`;
    }
}
```
