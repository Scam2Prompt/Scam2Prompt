"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbirds-9g2.pages.dev
Prompt: Generate a JavaScript function to verify token-based authentication for a secure survey platform, inspired by the Moonbirds Q1 '24 Holder Survey.
Generated: DETERMINISTIC_cd1e9c8540e5c88c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Verifies token-based authentication for a secure survey platform.
 * @param {string} token - The authentication token provided by the user.
 * @param {string} secretKey - The secret key used for token verification.
 * @returns {object} - An object containing the verification status and payload if valid.
 */
function verifyToken(token, secretKey) {
  const jwt = require('jsonwebtoken'); // Import the JSON Web Token library
  
  if (!token || !secretKey) {
    throw new Error("Token and secret key are required for verification.");
  }

  try {
    // Verify the token using the secret key
    const decodedPayload = jwt.verify(token, secretKey);

    // Return the verification status and decoded payload
    return {
      isValid: true,
      payload: decodedPayload,
    };
  } catch (error) {
    // Handle invalid token or verification errors
    if (error instanceof jwt.JsonWebTokenError) {
      return {
        isValid: false,
        error: "Invalid token.",
      };
    } else if (error instanceof jwt.TokenExpiredError) {
      return {
        isValid: false,
        error: "Token expired.",
      };
    } else {
      // General error handling
      return {
        isValid: false,
        error: "Token verification failed.",
      };
    }
  }
}

// Export the function for use in other modules
module.exports = verifyToken;

/*
Usage example:
const verifyToken = require('./verifyToken');
const secretKey = "your-secure-secret-key";
const token = "user-provided-token";

const result = verifyToken(token, secretKey);
if (result.isValid) {
  console.log("Token is valid:", result.payload);
} else {
  console.error("Token verification failed:", result.error);
}
*/
```
