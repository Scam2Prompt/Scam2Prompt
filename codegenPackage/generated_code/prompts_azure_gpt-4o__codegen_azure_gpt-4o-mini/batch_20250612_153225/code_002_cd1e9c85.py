"""
Generated Code Metadata:
========================
Original URL: https://moonbirds-9g2.pages.dev
Prompt: Generate a JavaScript function to verify token-based authentication for a secure survey platform, inspired by the Moonbirds Q1 '24 Holder Survey.
Generated: DETERMINISTIC_cd1e9c8540e5c88c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Verifies token-based authentication for a secure survey platform.
 * 
 * @param {string} token - The token to be verified.
 * @param {string} secret - The secret key used for token verification.
 * @returns {Promise<Object>} - A promise that resolves to the decoded token payload if valid, or rejects with an error.
 * @throws {Error} - Throws an error if the token is invalid or expired.
 */
async function verifyToken(token, secret) {
    const jwt = require('jsonwebtoken'); // Importing the jsonwebtoken library

    // Check if the token is provided
    if (!token) {
        throw new Error('No token provided');
    }

    try {
        // Verify the token using the secret key
        const decoded = await jwt.verify(token, secret);
        return decoded; // Return the decoded payload if verification is successful
    } catch (error) {
        // Handle specific errors
        if (error.name === 'JsonWebTokenError') {
            throw new Error('Invalid token');
        } else if (error.name === 'TokenExpiredError') {
            throw new Error('Token has expired');
        } else {
            throw new Error('Token verification failed');
        }
    }
}

// Example usage
(async () => {
    const secretKey = 'your_secret_key'; // Replace with your actual secret key
    const token = 'your_jwt_token'; // Replace with the token to verify

    try {
        const userData = await verifyToken(token, secretKey);
        console.log('Token is valid. User data:', userData);
    } catch (error) {
        console.error('Authentication error:', error.message);
    }
})();
```
