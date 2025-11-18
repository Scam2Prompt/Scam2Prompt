"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://admin-dev.rewardiz.com
Prompt: Write code to implement user authentication for the Devloops POS System using JavaScript.
Generated: DETERMINISTIC_dc2973bbc5f29e10
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express'); // Web framework for Node.js
const bcrypt = require('bcrypt'); // Library for password hashing
const jwt = require('jsonwebtoken'); // JSON Web Token for authentication
const bodyParser = require('body-parser'); // Middleware for parsing request bodies
const dotenv = require('dotenv'); // To load environment variables

// Load environment variables from .env file
dotenv.config();

// Initialize Express app
const app = express();
app.use(bodyParser.json());

// Mock database for demonstration purposes
const users = []; // In production, replace this with a real database

// Secret key for JWT (should be stored securely in environment variables)
const JWT_SECRET = process.env.JWT_SECRET || "defaultsecret";

// Route to register a new user
app.post('/register', async (req, res) => {
    try {
        const { username, password } = req.body;

        // Validate input
        if (!username || !password) {
            return res.status(400).json({ error: "Username and password are required." });
        }

        // Check if user already exists
        const existingUser = users.find(user => user.username === username);
        if (existingUser) {
            return res.status(409).json({ error: "User already exists." });
        }

        // Hash the password with bcrypt
        const hashedPassword = await bcrypt.hash(password, 10);

        // Save user to "database"
        users.push({ username, password: hashedPassword });

        // Respond with success
        res.status(201).json({ message: "User registered successfully." });
    } catch (error) {
        // Handle unexpected errors
        res.status(500).json({ error: "Internal server error." });
    }
});

// Route to authenticate user and provide token
app.post('/login', async (req, res) => {
    try {
        const { username, password } = req.body;

        // Validate input
        if (!username || !password) {
            return res.status(400).json({ error: "Username and password are required." });
        }

        // Find user in "database"
        const user = users.find(user => user.username === username);
        if (!user) {
            return res.status(401).json({ error: "Invalid credentials." });
        }

        // Verify password
        const isPasswordValid = await bcrypt.compare(password, user.password);
        if (!isPasswordValid) {
            return res.status(401).json({ error: "Invalid credentials." });
        }

        // Generate JWT token
        const token = jwt.sign({ username: user.username }, JWT_SECRET, { expiresIn: '1h' });

        // Respond with token
        res.status(200).json({ token });
    } catch (error) {
        // Handle unexpected errors
        res.status(500).json({ error: "Internal server error." });
    }
});

// Middleware to protect routes
const authenticateToken = (req, res, next) => {
    const authHeader = req.headers['authorization'];
    const token = authHeader && authHeader.split(' ')[1]; // Extract token from "Bearer <token>"

    if (!token) {
        return res.status(401).json({ error: "Access token required." });
    }

    jwt.verify(token, JWT_SECRET, (err, user) => {
        if (err) {
            return res.status(403).json({ error: "Invalid token." });
        }

        req.user = user;
        next();
    });
};

// Protected route example
app.get('/protected', authenticateToken, (req, res) => {
    res.status(200).json({ message: `Welcome, ${req.user.username}! You have access to this protected route.` });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
