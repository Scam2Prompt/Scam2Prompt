"""
Generated Code Metadata:
========================
Original URL: https://b8fffc7f.smart-token-tool-7er.pages.dev
Prompt: Enable JavaScript to run the Smart Token Tool application.
Generated: DETERMINISTIC_c459f005d8f7898b
Batch ID: 20250622_211350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Smart Token Tool Application
// This application allows users to generate and manage smart tokens securely.

// Import necessary libraries
const express = require('express'); // Web framework for Node.js
const bodyParser = require('body-parser'); // Middleware for parsing request bodies
const jwt = require('jsonwebtoken'); // Library for creating JSON Web Tokens
const dotenv = require('dotenv'); // Library for loading environment variables

// Load environment variables from .env file
dotenv.config();

// Initialize the Express application
const app = express();

// Middleware to parse JSON request bodies
app.use(bodyParser.json());

// Secret key for JWT signing and verification
const SECRET_KEY = process.env.SECRET_KEY || 'your-secret-key';

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack); // Log the error stack
    res.status(500).send('Something broke!'); // Send a generic error response
});

// Route to generate a smart token
app.post('/generate-token', (req, res) => {
    const { userId } = req.body; // Extract userId from request body

    // Validate input
    if (!userId) {
        return res.status(400).json({ error: 'User ID is required' });
    }

    // Create a token with userId as payload
    const token = jwt.sign({ userId }, SECRET_KEY, { expiresIn: '1h' });

    // Send the generated token as response
    res.json({ token });
});

// Route to verify a smart token
app.post('/verify-token', (req, res) => {
    const { token } = req.body; // Extract token from request body

    // Validate input
    if (!token) {
        return res.status(400).json({ error: 'Token is required' });
    }

    // Verify the token
    jwt.verify(token, SECRET_KEY, (err, decoded) => {
        if (err) {
            return res.status(401).json({ error: 'Invalid token' });
        }
        // Token is valid, return decoded payload
        res.json({ valid: true, decoded });
    });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Smart Token Tool application is running on port ${PORT}`);
});
```
