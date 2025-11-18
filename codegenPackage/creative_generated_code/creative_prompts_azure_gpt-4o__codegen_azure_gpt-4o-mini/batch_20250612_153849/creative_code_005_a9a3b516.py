"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zeebu-governance.azurewebsites.net
Prompt: Create a JavaScript-based implementation to handle user authentication and permissions within the Zeebu Protocol governance framework.
Generated: DETERMINISTIC_a9a3b5160601b1b4
Batch ID: 20250612_153849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// User Authentication and Permissions Management for Zeebu Protocol Governance Framework

// Import necessary libraries
const jwt = require('jsonwebtoken'); // For token-based authentication
const bcrypt = require('bcrypt');     // For password hashing
const express = require('express');    // For creating the server
const bodyParser = require('body-parser'); // For parsing request bodies
const mongoose = require('mongoose');  // For MongoDB interaction

// Initialize Express app
const app = express();
app.use(bodyParser.json());

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/zeebu', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// User schema definition
const userSchema = new mongoose.Schema({
    username: { type: String, required: true, unique: true },
    password: { type: String, required: true },
    roles: { type: [String], default: ['user'] } // Default role is user
});

// Create User model
const User = mongoose.model('User', userSchema);

// Middleware for authentication
const authenticateToken = (req, res, next) => {
    const token = req.headers['authorization']?.split(' ')[1];
    if (!token) return res.sendStatus(401); // Unauthorized

    jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
        if (err) return res.sendStatus(403); // Forbidden
        req.user = user;
        next();
    });
};

// Route to register a new user
app.post('/register', async (req, res) => {
    try {
        const { username, password } = req.body;

        // Check if user already exists
        const existingUser = await User.findOne({ username });
        if (existingUser) return res.status(400).send('User already exists');

        // Hash the password
        const hashedPassword = await bcrypt.hash(password, 10);

        // Create a new user
        const user = new User({ username, password: hashedPassword });
        await user.save();

        res.status(201).send('User registered successfully');
    } catch (error) {
        console.error('Error during registration:', error);
        res.status(500).send('Internal Server Error');
    }
});

// Route to login a user
app.post('/login', async (req, res) => {
    try {
        const { username, password } = req.body;

        const user = await User.findOne({ username });
        if (!user) return res.status(400).send('Invalid username or password');

        // Validate password
        const isValidPassword = await bcrypt.compare(password, user.password);
        if (!isValidPassword) return res.status(400).send('Invalid username or password');

        // Generate JWT token
        const token = jwt.sign({ username: user.username, roles: user.roles }, process.env.JWT_SECRET, { expiresIn: '1h' });
        res.json({ token });
    } catch (error) {
        console.error('Error during login:', error);
        res.status(500).send('Internal Server Error');
    }
});

// Route to get user info
app.get('/me', authenticateToken, (req, res) => {
    res.json({ username: req.user.username, roles: req.user.roles });
});

// Middleware to check user permissions
const checkPermissions = (requiredRoles) => {
    return (req, res, next) => {
        const userRoles = req.user.roles;
        const hasPermission = requiredRoles.some(role => userRoles.includes(role));
        if (!hasPermission) return res.sendStatus(403); // Forbidden
        next();
    };
};

// Example route that requires admin permissions
app.get('/admin', authenticateToken, checkPermissions(['admin']), (req, res) => {
    res.send('Welcome to the admin panel');
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

Make sure to set the `JWT_SECRET` environment variable for the application to work correctly.
