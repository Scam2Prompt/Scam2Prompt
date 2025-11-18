"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-meme-token.pages.dev
Prompt: Develop a Node.js script to handle user authentication and token claiming for the Meme Token airdrop.
Generated: DETERMINISTIC_00307b707c6b958b
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Meme Token Airdrop Authentication Script
 * 
 * This script handles user authentication and generates a token for users who qualify 
 * for the Meme Token airdrop. The script uses JSON Web Token (JWT) for token generation.
 * 
 * Dependencies:
 * - express: For handling HTTP requests
 * - bcrypt: For secure password hashing
 * - jsonwebtoken: For token generation and verification
 * - dotenv: For environment variable management
 * 
 * Ensure you install the necessary dependencies by running:
 *   npm install express bcrypt jsonwebtoken dotenv
 */

require('dotenv').config(); // Load environment variables
const express = require('express');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

const app = express();
app.use(express.json()); // Middleware to parse JSON request bodies

// Environment variables (configure in `.env` file)
const PORT = process.env.PORT || 3000;
const SECRET_KEY = process.env.SECRET_KEY || "supersecretkey"; // Replace with a strong secret key

// Mock user database (replace with an actual database in production)
const users = [
    {
        username: "user1",
        passwordHash: bcrypt.hashSync("password1", 10), // Pre-hashed password
        eligibleForAirdrop: true
    },
    {
        username: "user2",
        passwordHash: bcrypt.hashSync("password2", 10), // Pre-hashed password
        eligibleForAirdrop: false
    }
];

/**
 * Authenticate a user and issue a token if eligible for airdrop.
 */
app.post('/authenticate', async (req, res) => {
    try {
        const { username, password } = req.body;

        // Validate input
        if (!username || !password) {
            return res.status(400).json({ message: "Username and password are required." });
        }

        // Find user in the database
        const user = users.find(u => u.username === username);
        if (!user) {
            return res.status(404).json({ message: "User not found." });
        }

        // Check password
        const isPasswordValid = await bcrypt.compare(password, user.passwordHash);
        if (!isPasswordValid) {
            return res.status(401).json({ message: "Invalid password." });
        }

        // Check airdrop eligibility
        if (!user.eligibleForAirdrop) {
            return res.status(403).json({ message: "User not eligible for Meme Token airdrop." });
        }

        // Generate JWT token
        const token = jwt.sign(
            { username: user.username, eligibleForAirdrop: user.eligibleForAirdrop },
            SECRET_KEY,
            { expiresIn: '1h' } // Token expires in 1 hour
        );

        res.status(200).json({ message: "Authentication successful.", token });
    } catch (error) {
        // Handle unexpected errors
        console.error("Error during authentication:", error);
        res.status(500).json({ message: "Internal server error." });
    }
});

/**
 * Verify the token provided by the user.
 */
app.post('/verify-token', (req, res) => {
    try {
        const { token } = req.body;

        // Validate input
        if (!token) {
            return res.status(400).json({ message: "Token is required." });
        }

        // Verify token
        jwt.verify(token, SECRET_KEY, (err, decoded) => {
            if (err) {
                return res.status(401).json({ message: "Invalid or expired token." });
            }

            res.status(200).json({ message: "Token verified successfully.", data: decoded });
        });
    } catch (error) {
        // Handle unexpected errors
        console.error("Error during token verification:", error);
        res.status(500).json({ message: "Internal server error." });
    }
});

/**
 * Start the Express server.
 */
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
