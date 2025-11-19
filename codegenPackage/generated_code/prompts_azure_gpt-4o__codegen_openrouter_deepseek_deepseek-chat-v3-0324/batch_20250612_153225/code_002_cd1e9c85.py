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
 * Verifies a JWT token for authentication in a secure survey platform.
 * @param {string} token - The JWT token to verify.
 * @param {string} secret - The secret key used to verify the token.
 * @param {string} requiredRole - The required role for access (optional).
 * @returns {Promise<Object>} - Resolves with decoded token if valid, rejects with error if invalid.
 */
async function verifySurveyToken(token, secret, requiredRole = null) {
    const jwt = require('jsonwebtoken');
    
    if (!token) {
        throw new Error('No token provided');
    }

    try {
        // Verify and decode the token
        const decoded = await new Promise((resolve, reject) => {
            jwt.verify(token, secret, (err, decoded) => {
                if (err) {
                    reject(err);
                } else {
                    resolve(decoded);
                }
            });
        });

        // Check token expiration
        if (decoded.exp && Date.now() >= decoded.exp * 1000) {
            throw new Error('Token expired');
        }

        // Check required role if specified
        if (requiredRole && decoded.role !== requiredRole) {
            throw new Error('Insufficient permissions');
        }

        // Additional checks for survey-specific requirements
        if (!decoded.surveyId || !decoded.userId) {
            throw new Error('Invalid token payload');
        }

        return decoded;
    } catch (error) {
        console.error('Token verification failed:', error.message);
        throw error;
    }
}

/**
 * Middleware function for Express.js to verify survey tokens.
 * @param {string} secret - The secret key used to verify tokens.
 * @param {string} requiredRole - The required role for access (optional).
 * @returns {Function} - Express middleware function.
 */
function surveyAuthMiddleware(secret, requiredRole = null) {
    return async (req, res, next) => {
        try {
            const authHeader = req.headers.authorization;
            if (!authHeader || !authHeader.startsWith('Bearer ')) {
                return res.status(401).json({ error: 'Unauthorized - No token provided' });
            }

            const token = authHeader.split(' ')[1];
            const decoded = await verifySurveyToken(token, secret, requiredRole);
            
            // Attach user information to the request
            req.user = {
                id: decoded.userId,
                role: decoded.role,
                surveyId: decoded.surveyId
            };

            next();
        } catch (error) {
            res.status(403).json({ error: `Forbidden - ${error.message}` });
        }
    };
}

module.exports = {
    verifySurveyToken,
    surveyAuthMiddleware
};
```
