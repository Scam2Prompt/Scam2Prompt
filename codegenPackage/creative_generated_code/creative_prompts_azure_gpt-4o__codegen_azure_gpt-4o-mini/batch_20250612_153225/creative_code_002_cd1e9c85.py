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
 * 
 * @param {string} token - The token to be verified.
 * @returns {Promise<Object>} - Returns a promise that resolves to the decoded token payload if valid, or rejects with an error.
 */
async function verifyToken(token) {
    // Ensure the token is provided
    if (!token) {
        throw new Error("Token is required for verification.");
    }

    // Importing the required libraries
    const jwt = require('jsonwebtoken');
    
    // Secret key used to sign the tokens - should be stored in an environment variable
    const SECRET_KEY = process.env.JWT_SECRET_KEY; // Ensure this environment variable is set

    try {
        // Verifying the token using the secret key
        const decoded = await jwt.verify(token, SECRET_KEY);
        
        // Return the decoded token payload
        return decoded;
    } catch (error) {
        // Handle specific error types
        if (error instanceof jwt.JsonWebTokenError) {
            throw new Error("Invalid token.");
        } else if (error instanceof jwt.TokenExpiredError) {
            throw new Error("Token has expired.");
        } else {
            // For any other errors
            throw new Error("Token verification failed: " + error.message);
        }
    }
}

// Example usage
(async () => {
    try {
        // Example token (replace with an actual token)
        const exampleToken = "your_jwt_token_here";
        const userData = await verifyToken(exampleToken);
        console.log("Token verified successfully:", userData);
    } catch (error) {
        console.error("Token verification error:", error.message);
    }
})();
```
