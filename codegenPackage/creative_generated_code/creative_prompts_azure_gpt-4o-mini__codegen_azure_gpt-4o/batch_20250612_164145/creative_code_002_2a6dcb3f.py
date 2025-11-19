"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft.vip-tokyo.jp
Prompt: Create a JavaScript function that handles user authentication for a digital art sales platform, ensuring secure access as emphasized by VIP Management's focus on security.
Generated: DETERMINISTIC_2a6dcb3fb5d34b76
Batch ID: 20250612_164145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to authenticate a user for a digital art sales platform.
 * 
 * Ensures secure access by verifying user credentials and generating a JSON Web Token (JWT).
 * Implements best practices for security, including password hashing using bcrypt.
 * 
 * Dependencies: bcrypt, jsonwebtoken
 */

// Import required libraries
const bcrypt = require('bcrypt'); // For password hashing comparison
const jwt = require('jsonwebtoken'); // For generating JWT tokens

// Environment variables for security configurations
const JWT_SECRET = process.env.JWT_SECRET || 'your-secure-secret-key'; // Secret key for JWT
const JWT_EXPIRATION = '1h'; // Token expiration time

/**
 * Authenticate user based on provided username and password.
 *
 * @param {string} username - User's username.
 * @param {string} password - User's password.
 * @param {function} getUserByUsername - A database function that retrieves user data by username.
 * @returns {Promise<Object>} - Resolves to an object containing the token and user data, or an error message.
 */
async function authenticateUser(username, password, getUserByUsername) {
  try {
    // Validate input parameters
    if (!username || !password) {
      throw new Error('Username and password are required.');
    }

    // Retrieve user data from the database
    const user = await getUserByUsername(username);
    if (!user) {
      throw new Error('Invalid username or password.');
    }

    // Compare provided password with stored hashed password
    const isPasswordCorrect = await bcrypt.compare(password, user.hashedPassword);
    if (!isPasswordCorrect) {
      throw new Error('Invalid username or password.');
    }

    // Generate a JSON Web Token (JWT) for the authenticated user
    const token = jwt.sign(
      { userId: user.id, username: user.username }, // Payload
      JWT_SECRET, // Secret key
      { expiresIn: JWT_EXPIRATION } // Token expiration
    );

    // Return the token and user data (excluding sensitive information)
    return {
      token,
      user: { id: user.id, username: user.username, email: user.email },
    };
  } catch (error) {
    // Handle and log errors
    console.error('Authentication error:', error.message);
    return { error: error.message };
  }
}

module.exports = authenticateUser;
```

**Note:** Be sure to configure the `JWT_SECRET` as a secure environment variable in production, and ensure the `getUserByUsername` function is implemented to securely retrieve user details from your database.
