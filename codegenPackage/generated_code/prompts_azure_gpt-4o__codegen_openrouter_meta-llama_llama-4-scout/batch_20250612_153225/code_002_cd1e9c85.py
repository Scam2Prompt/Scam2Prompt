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
 * @param {string} token - The authentication token to verify.
 * @param {string} secretKey - The secret key used to generate the token.
 * @returns {boolean} True if the token is valid, false otherwise.
 */
function verifyToken(token, secretKey) {
    // Check if token and secretKey are provided
    if (!token || !secretKey) {
        throw new Error('Token and secret key are required');
    }

    // Define the token expiration time in seconds (e.g., 1 hour)
    const tokenExpirationTime = 3600;

    try {
        // Decode the token
        const decodedToken = jwt.verify(token, secretKey);

        // Check if the token has expired
        const currentTime = Math.floor(Date.now() / 1000);
        if (decodedToken.exp < currentTime) {
            return false;
        }

        // Check if the token has the required properties
        if (!decodedToken.userId || !decodedToken.surveyId) {
            return false;
        }

        return true;
    } catch (error) {
        // Handle token verification errors
        if (error.name === 'TokenExpiredError') {
            return false;
        } else if (error.name === 'JsonWebTokenError') {
            return false;
        } else {
            throw error;
        }
    }
}

// Import the jsonwebtoken library
const jwt = require('jsonwebtoken');

/**
 * Generates a token for a user to access a survey.
 * 
 * @param {string} userId - The ID of the user.
 * @param {string} surveyId - The ID of the survey.
 * @param {string} secretKey - The secret key used to generate the token.
 * @returns {string} The generated token.
 */
function generateToken(userId, surveyId, secretKey) {
    // Define the token expiration time in seconds (e.g., 1 hour)
    const tokenExpirationTime = 3600;

    // Generate the token
    const token = jwt.sign({
        userId,
        surveyId,
        exp: Math.floor(Date.now() / 1000) + tokenExpirationTime,
    }, secretKey, {
        algorithm: 'HS256',
    });

    return token;
}

// Example usage:
const secretKey = 'your-secret-key';
const userId = 'user-123';
const surveyId = 'survey-123';

// Generate a token
const token = generateToken(userId, surveyId, secretKey);
console.log(`Generated token: ${token}`);

// Verify the token
const isValid = verifyToken(token, secretKey);
console.log(`Is token valid? ${isValid}`);
```
