"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multandesigns.com
Prompt: Write code in Node.js to implement a "Login/Register" system for an e-commerce website, ensuring secure storage of user credentials and session management.
Generated: DETERMINISTIC_d7ede1d6a4553d7d
Batch ID: 20250612_152924
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
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');
const session = require('express-session');
const bodyParser = require('body-parser');
const { body, validationResult } = require('express-validator');

// Initialize express app
const app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Configure session management
app.use(session({
    secret: 'supersecretkey', // Change this to a strong secret in production
    resave: false,
    saveUninitialized: true,
    cookie: { secure: false } // Set to true if using HTTPS
}));

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/ecommerce', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// User schema and model
const userSchema = new mongoose.Schema({
    username: { type: String, required: true, unique: true },
    password: { type: String, required: true }
});

const User = mongoose.model('User', userSchema);

// Register route
app.post('/register', [
    body('username').isString().notEmpty(),
    body('password').isLength({ min: 6 })
], async (req, res) => {
    // Validate request
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
        return res.status(400).json({ errors: errors.array() });
    }

    const { username, password } = req.body;

    // Check if user already exists
    const existingUser = await User.findOne({ username });
    if (existingUser) {
        return res.status(400).json({ message: 'Username already exists' });
    }

    // Hash the password
    const hashedPassword = await bcrypt.hash(password, 10);

    // Create a new user
    const user = new User({ username, password: hashedPassword });
    try {
        await user.save();
        res.status(201).json({ message: 'User registered successfully' });
    } catch (err) {
        res.status(500).json({ message: 'Error registering user', error: err });
    }
});

// Login route
app.post('/login', [
    body('username').isString().notEmpty(),
    body('password').notEmpty()
], async (req, res) => {
    // Validate request
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
        return res.status(400).json({ errors: errors.array() });
    }

    const { username, password } = req.body;

    // Find user by username
    const user = await User.findOne({ username });
    if (!user) {
        return res.status(401).json({ message: 'Invalid credentials' });
    }

    // Check password
    const match = await bcrypt.compare(password, user.password);
    if (!match) {
        return res.status(401).json({ message: 'Invalid credentials' });
    }

    // Save user session
    req.session.userId = user._id;
    res.status(200).json({ message: 'Login successful' });
});

// Logout route
app.post('/logout', (req, res) => {
    req.session.destroy(err => {
        if (err) {
            return res.status(500).json({ message: 'Error logging out', error: err });
        }
        res.status(200).json({ message: 'Logout successful' });
    });
});

// Middleware to verify session
const isAuthenticated = (req, res, next) => {
    if (req.session.userId) {
        return next();
    }
    res.status(401).json({ message: 'Unauthorized access' });
};

// Protected route example
app.get('/profile', isAuthenticated, async (req, res) => {
    const user = await User.findById(req.session.userId).select('-password'); // Exclude password
    res.status(200).json(user);
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
```
