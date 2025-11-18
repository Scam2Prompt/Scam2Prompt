"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getinge-torin.com
Prompt: Create a backend API endpoint in Node.js for user authentication, including functionality for "stay logged in" sessions, inspired by the Torin portal.
Generated: DETERMINISTIC_a888db44ec72b4d7
Batch ID: 20250612_154909
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const mongoose = require('mongoose');
const cookieParser = require('cookie-parser');

// Initialize Express application
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware for parsing JSON and cookies
app.use(express.json());
app.use(cookieParser());

// Connect to MongoDB (ensure to replace with your connection string)
mongoose.connect('mongodb://localhost:27017/user_auth', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
});

// User schema definition
const userSchema = new mongoose.Schema({
    username: { type: String, required: true, unique: true },
    password: { type: String, required: true },
});

// User model
const User = mongoose.model('User', userSchema);

// JWT secret key
const JWT_SECRET = process.env.JWT_SECRET || 'your_jwt_secret'; // Use an env variable for production

/**
 * Registers a new user.
 * @route POST /register
 */
app.post('/register', async (req, res) => {
    try {
        const { username, password } = req.body;

        // Hash the password before saving
        const hashedPassword = await bcrypt.hash(password, 10);
        const newUser = new User({ username, password: hashedPassword });

        // Save the user to the database
        await newUser.save();
        res.status(201).json({ message: 'User registered successfully' });
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

/**
 * Authenticates a user and generates a JWT token.
 * @route POST /login
 */
app.post('/login', async (req, res) => {
    try {
        const { username, password, stayLoggedIn } = req.body;

        // Find the user by username
        const user = await User.findOne({ username });
        if (!user) {
            return res.status(401).json({ error: 'Invalid username or password' });
        }

        // Check the password
        const isValidPassword = await bcrypt.compare(password, user.password);
        if (!isValidPassword) {
            return res.status(401).json({ error: 'Invalid username or password' });
        }

        // Generate JWT token
        const token = jwt.sign({ id: user._id }, JWT_SECRET, {
            expiresIn: stayLoggedIn ? '7d' : '1h', // Longer expiry for stay logged in
        });

        // Set cookie with the token
        res.cookie('token', token, {
            httpOnly: true,
            secure: process.env.NODE_ENV === 'production', // Use secure cookies in production
            maxAge: stayLoggedIn ? 7 * 24 * 60 * 60 * 1000 : 60 * 60 * 1000, // 7 days or 1 hour
        });

        res.json({ message: 'Login successful' });
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

/**
 * Middleware to authenticate user using JWT
 */
const authenticateJWT = (req, res, next) => {
    const token = req.cookies.token;

    if (!token) {
        return res.sendStatus(403); // Forbidden
    }

    jwt.verify(token, JWT_SECRET, (err, user) => {
        if (err) {
            return res.sendStatus(403); // Forbidden
        }
        req.user = user;
        next();
    });
};

/**
 * Protected route example
 * @route GET /protected
 */
app.get('/protected', authenticateJWT, (req, res) => {
    res.json({ message: 'This is a protected route', user: req.user });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```
