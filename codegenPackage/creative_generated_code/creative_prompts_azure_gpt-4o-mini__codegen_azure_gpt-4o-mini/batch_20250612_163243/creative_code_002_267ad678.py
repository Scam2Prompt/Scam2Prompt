"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://8147f917.carbon-app-csq.pages.dev
Prompt: What are the steps to set up a login code feature for a web app using Cloudflare Pages?
Generated: DETERMINISTIC_267ad678a5e39b8b
Batch ID: 20250612_163243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import express from 'express'; // Web framework for Node.js
import bcrypt from 'bcrypt'; // Library for hashing passwords
import jwt from 'jsonwebtoken'; // Library for creating JSON Web Tokens
import dotenv from 'dotenv'; // Library for environment variable management

// Load environment variables from .env file
dotenv.config();

// Initialize Express app
const app = express();
app.use(express.json()); // Middleware to parse JSON requests

// Mock user database (for demonstration purposes, replace with real database in production)
let users = [];

// User registration endpoint
app.post('/register', async (req, res) => {
    const { username, password } = req.body;

    // Validate input
    if (!username || !password) {
        return res.status(400).json({ message: 'Username and password are required.' });
    }

    // Check if user already exists
    const existingUser = users.find(user => user.username === username);
    if (existingUser) {
        return res.status(409).json({ message: 'Username already taken.' });
    }

    // Hash the password
    const hashedPassword = await bcrypt.hash(password, 10);

    // Save user to "database"
    users.push({ username, password: hashedPassword });

    // Respond with success
    res.status(201).json({ message: 'User registered successfully.' });
});

// User login endpoint
app.post('/login', async (req, res) => {
    const { username, password } = req.body;

    // Validate input
    if (!username || !password) {
        return res.status(400).json({ message: 'Username and password are required.' });
    }

    // Find user in "database"
    const user = users.find(user => user.username === username);
    if (!user) {
        return res.status(401).json({ message: 'Invalid username or password.' });
    }

    // Compare hashed password with the provided password
    const isMatch = await bcrypt.compare(password, user.password);
    if (!isMatch) {
        return res.status(401).json({ message: 'Invalid username or password.' });
    }

    // Generate JWT token
    const token = jwt.sign({ username }, process.env.JWT_SECRET, { expiresIn: '1h' });

    // Respond with token
    res.status(200).json({ message: 'Login successful.', token });
});

// Middleware to protect routes
const authenticateToken = (req, res, next) => {
    const token = req.headers['authorization']?.split(' ')[1];
    if (!token) return res.sendStatus(401); // No token

    jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
        if (err) return res.sendStatus(403); // Invalid token
        req.user = user; // Store user info in request object
        next(); // Proceed to next middleware/route handler
    });
};

// Protected route example
app.get('/profile', authenticateToken, (req, res) => {
    res.json({ message: 'Profile data', user: req.user });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
