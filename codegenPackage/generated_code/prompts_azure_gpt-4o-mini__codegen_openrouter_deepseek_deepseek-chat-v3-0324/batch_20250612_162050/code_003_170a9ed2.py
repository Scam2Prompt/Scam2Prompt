"""
Generated Code Metadata:
========================
Original URL: https://moonbirds-9g2.pages.dev
Prompt: Generate a JavaScript function that checks for token validity before allowing access to a survey, based on the Moonbirds Q1 '24 Holder Survey.
Generated: DETERMINISTIC_170a9ed24c0ef401
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Checks if a given token is valid for accessing the Moonbirds Q1 '24 Holder Survey.
 * @param {string} token - The token to validate.
 * @param {string[]} validTokens - An array of valid tokens.
 * @returns {Object} An object with `isValid` (boolean) and `message` (string) properties.
 */
function checkTokenValidity(token, validTokens) {
    // Validate input parameters
    if (typeof token !== 'string' || !Array.isArray(validTokens)) {
        return {
            isValid: false,
            message: 'Invalid input parameters'
        };
    }

    // Check if token is empty
    if (!token.trim()) {
        return {
            isValid: false,
            message: 'Token cannot be empty'
        };
    }

    // Check if token is in the list of valid tokens
    const isValid = validTokens.includes(token.trim());
    
    return {
        isValid,
        message: isValid ? 'Token is valid' : 'Invalid token'
    };
}

/**
 * Middleware function to validate token before allowing survey access.
 * @param {string[]} validTokens - Array of valid tokens.
 * @returns {Function} Express middleware function.
 */
function surveyAccessMiddleware(validTokens) {
    return (req, res, next) => {
        try {
            // Get token from Authorization header
            const authHeader = req.headers.authorization;
            if (!authHeader) {
                return res.status(401).json({ error: 'Authorization header missing' });
            }

            // Check if header is in correct format (Bearer <token>)
            const parts = authHeader.split(' ');
            if (parts.length !== 2 || parts[0] !== 'Bearer') {
                return res.status(401).json({ error: 'Invalid authorization format' });
            }

            const token = parts[1];
            const { isValid, message } = checkTokenValidity(token, validTokens);

            if (!isValid) {
                return res.status(403).json({ error: message });
            }

            // Token is valid, proceed to survey
            next();
        } catch (error) {
            console.error('Error in survey access middleware:', error);
            res.status(500).json({ error: 'Internal server error' });
        }
    };
}

// Example usage:
// const validTokens = ['token1', 'token2', 'token3'];
// app.get('/survey', surveyAccessMiddleware(validTokens), (req, res) => {
//     res.json({ message: 'Welcome to the Moonbirds Q1 2024 Holder Survey' });
// });
```
