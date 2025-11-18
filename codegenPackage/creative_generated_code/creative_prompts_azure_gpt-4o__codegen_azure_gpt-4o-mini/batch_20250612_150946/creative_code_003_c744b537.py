"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://b8fffc7f.smart-token-tool-7er.pages.dev
Prompt: Recommend libraries or APIs similar to the Smart Token Tool (SMT) for managing tokens in JavaScript-based applications.
Generated: DETERMINISTIC_c744b5378a97256d
Batch ID: 20250612_150946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * TokenManager - A simple class to manage tokens in a JavaScript-based application.
 * This class provides methods for generating, validating, and managing tokens.
 */

class TokenManager {
    constructor(secretKey) {
        if (!secretKey) {
            throw new Error("A secret key is required for token management.");
        }
        this.secretKey = secretKey;
    }

    /**
     * Generates a token with an optional payload.
     * @param {Object} payload - The data to embed in the token.
     * @returns {string} - The generated token.
     */
    generateToken(payload) {
        const header = {
            alg: 'HS256',
            typ: 'JWT'
        };
        
        const encodedHeader = this._base64UrlEncode(JSON.stringify(header));
        const encodedPayload = this._base64UrlEncode(JSON.stringify(payload));
        
        const signature = this._sign(`${encodedHeader}.${encodedPayload}`);
        
        return `${encodedHeader}.${encodedPayload}.${signature}`;
    }

    /**
     * Validates a token and returns the payload if valid.
     * @param {string} token - The token to validate.
     * @returns {Object|null} - The decoded payload or null if invalid.
     */
    validateToken(token) {
        const parts = token.split('.');
        
        if (parts.length !== 3) {
            throw new Error("Invalid token format.");
        }
        
        const [header, payload, signature] = parts;
        
        if (this._sign(`${header}.${payload}`) !== signature) {
            return null; // Token is invalid
        }
        
        return JSON.parse(this._base64UrlDecode(payload));
    }

    /**
     * Signs a message with the secret key using HMAC SHA256.
     * @param {string} message - The message to sign.
     * @returns {string} - The generated signature.
     * @private
     */
    _sign(message) {
        const crypto = require('crypto');
        return crypto.createHmac('sha256', this.secretKey)
                     .update(message)
                     .digest('base64url'); // Using base64url encoding for JWT
    }

    /**
     * Base64 URL encodes a string.
     * @param {string} str - The string to encode.
     * @returns {string} - The base64url encoded string.
     * @private
     */
    _base64UrlEncode(str) {
        return Buffer.from(str)
                     .toString('base64url');
    }

    /**
     * Base64 URL decodes a string.
     * @param {string} str - The string to decode.
     * @returns {string} - The decoded string.
     * @private
     */
    _base64UrlDecode(str) {
        const padding = '='.repeat((4 - str.length % 4) % 4);
        return Buffer.from((str + padding).replace(/-/g, '+').replace(/_/g, '/'), 'base64').toString();
    }
}

// Example usage
try {
    const tokenManager = new TokenManager('your-secret-key');
    const token = tokenManager.generateToken({ userId: 123 });
    console.log("Generated Token:", token);

    const payload = tokenManager.validateToken(token);
    console.log("Decoded Payload:", payload);
} catch (error) {
    console.error("Error:", error.message);
}
```
