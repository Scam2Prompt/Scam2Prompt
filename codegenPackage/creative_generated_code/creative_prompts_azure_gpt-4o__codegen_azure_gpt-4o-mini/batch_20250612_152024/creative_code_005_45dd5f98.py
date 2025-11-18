"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aicryptoexm.com
Prompt: Develop a JavaScript-based authentication system for a crypto derivatives exchange, ensuring secure login and session management.
Generated: DETERMINISTIC_45dd5f98ba0b87e2
Batch ID: 20250612_152024
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
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const cookieParser = require('cookie-parser');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

// Initialize express app
const app = express();

// Middleware setup
app.use(bodyParser.json());
app.use(cookieParser());

// MongoDB connection (replace 'your_mongo_uri' with your actual MongoDB URI)
mongoose.connect('your_mongo_uri', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// User schema definition
const userSchema = new mongoose.Schema({
    username: { type: String, required: true, unique: true },
    password: { type: String, required: true }
});

// User model
const User = mongoose.model('User', userSchema);

// JWT secret key (should be stored in environment variables for production)
const JWT_SECRET = 'your_jwt_secret'; // Change this to a secure secret

// Register a new user
app.post('/register', async (req, res) => {
    const { username, password } = req.body;

    // Basic validation
    if (!username || !password) {
        return res.status(400).json({ message: 'Username and password are required.' });
    }

    try {
        // Hash the password before saving
        const hashedPassword = await bcrypt.hash(password, 10);
        const newUser = new User({ username, password: hashedPassword });
        await newUser.save();
        res.status(201).json({ message: 'User registered successfully.' });
    } catch (error) {
        console.error('Error registering user:', error);
        res.status(500).json({ message: 'Internal server error.' });
    }
});

// User login
app.post('/login', async (req, res) => {
    const { username, password } = req.body;

    // Basic validation
    if (!username || !password) {
        return res.status(400).json({ message: 'Username and password are required.' });
    }

    try {
        const user = await User.findOne({ username });
        if (!user) {
            return res.status(401).json({ message: 'Invalid credentials.' });
        }

        // Compare provided password with stored hashed password
        const isPasswordValid = await bcrypt.compare(password, user.password);
        if (!isPasswordValid) {
            return res.status(401).json({ message: 'Invalid credentials.' });
        }

        // Generate JWT token
        const token = jwt.sign({ userId: user._id }, JWT_SECRET, { expiresIn: '1h' });

        // Set token as an HTTP-only cookie
        res.cookie('token', token, { httpOnly: true, secure: true, sameSite: 'strict' });
        res.status(200).json({ message: 'Login successful.' });
    } catch (error) {
        console.error('Error during login:', error);
        res.status(500).json({ message: 'Internal server error.' });
    }
});

// Middleware to authenticate JWT token
const authenticateJWT = (req, res, next) => {
    const token = req.cookies.token;
    if (!token) {
        return res.sendStatus(403);
    }

    jwt.verify(token, JWT_SECRET, (err, user) => {
        if (err) {
            return res.sendStatus(403);
        }
        req.user = user;
        next();
    });
};

// Example protected route
app.get('/protected', authenticateJWT, (req, res) => {
    res.json({ message: 'This is a protected route.', user: req.user });
});

// Logout user
app.post('/logout', (req, res) => {
    res.clearCookie('token');
    res.status(200).json({ message: 'Logged out successfully.' });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
