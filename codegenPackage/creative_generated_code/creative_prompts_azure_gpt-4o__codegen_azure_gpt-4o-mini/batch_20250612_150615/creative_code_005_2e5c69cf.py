"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scburnet.okta.acmecorp.name
Prompt: What are the best practices for handling cookies in a custom Okta sign-in implementation?
Generated: DETERMINISTIC_2e5c69cfb48e4604
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express');
const cookieParser = require('cookie-parser');
const jwt = require('jsonwebtoken');
const app = express();

// Middleware for parsing cookies
app.use(cookieParser());

// Secret key for signing tokens (in production, use environment variables)
const JWT_SECRET = 'your_jwt_secret'; // Replace with a secure secret

// Function to set a secure cookie
function setSecureCookie(res, name, value, options = {}) {
    // Default cookie options
    const cookieOptions = {
        httpOnly: true, // Prevents client-side JavaScript access
        secure: process.env.NODE_ENV === 'production', // Use secure cookies in production
        sameSite: 'Strict', // CSRF protection
        ...options, // Spread custom options
    };
    
    res.cookie(name, value, cookieOptions);
}

// Function to handle login
app.post('/login', async (req, res) => {
    try {
        const { username, password } = req.body;

        // Here you would validate the user with Okta
        // This is a placeholder for actual authentication logic
        const user = await authenticateWithOkta(username, password);

        if (!user) {
            return res.status(401).json({ error: 'Invalid credentials' });
        }

        // Generate JWT token
        const token = jwt.sign({ userId: user.id }, JWT_SECRET, { expiresIn: '1h' });

        // Set the token in a secure cookie
        setSecureCookie(res, 'auth_token', token);

        // Respond with success
        return res.status(200).json({ message: 'Login successful' });
    } catch (error) {
        console.error('Login error:', error);
        return res.status(500).json({ error: 'Internal Server Error' });
    }
});

// Middleware to protect routes
function authenticateUser(req, res, next) {
    const token = req.cookies.auth_token;

    if (!token) {
        return res.status(401).json({ error: 'Unauthorized' });
    }

    // Verify the JWT token
    jwt.verify(token, JWT_SECRET, (err, decoded) => {
        if (err) {
            return res.status(403).json({ error: 'Forbidden' });
        }
        // Attach user information to request object
        req.user = decoded;
        next(); // Proceed to the next middleware or route
    });
}

// Protected route example
app.get('/protected', authenticateUser, (req, res) => {
    return res.status(200).json({ message: `Welcome, user ${req.user.userId}` });
});

// Function to handle logout
app.post('/logout', (req, res) => {
    // Clear the cookie
    res.clearCookie('auth_token');
    return res.status(200).json({ message: 'Logout successful' });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

// Placeholder for Okta authentication function
async function authenticateWithOkta(username, password) {
    // Implement actual authentication logic with Okta API
    // Return user object if successful, else return null
    return { id: 1, username }; // Mock user for demonstration
}
```
