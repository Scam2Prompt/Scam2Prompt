"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mwxoq1840.ukit.me
Prompt: What are the best practices for managing user authentication in uKit?
Generated: DETERMINISTIC_fa0035fdbfc55080
Batch ID: 20250612_164213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express'); // Web framework
const bcrypt = require('bcrypt'); // Library for hashing passwords
const jwt = require('jsonwebtoken'); // Library for creating JSON Web Tokens
const mongoose = require('mongoose'); // MongoDB object modeling tool
const User = require('./models/User'); // User model
const app = express(); // Create an Express application

// Middleware to parse JSON bodies
app.use(express.json());

// MongoDB connection
mongoose.connect('mongodb://localhost:27017/ukit_auth', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
}).then(() => {
    console.log('Connected to MongoDB');
}).catch(err => {
    console.error('MongoDB connection error:', err);
});

// User registration endpoint
app.post('/register', async (req, res) => {
    const { username, password } = req.body;
    try {
        // Check if user already exists
        const existingUser = await User.findOne({ username });
        if (existingUser) {
            return res.status(400).json({ message: 'User already exists' });
        }

        // Hash the password
        const hashedPassword = await bcrypt.hash(password, 10);

        // Create new user
        const user = new User({ username, password: hashedPassword });
        await user.save();

        // Respond with success
        res.status(201).json({ message: 'User registered successfully' });
    } catch (err) {
        console.error('Error during registration:', err);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// User login endpoint
app.post('/login', async (req, res) => {
    const { username, password } = req.body;
    try {
        // Find the user by username
        const user = await User.findOne({ username });
        if (!user) {
            return res.status(401).json({ message: 'Invalid credentials' });
        }

        // Compare passwords
        const isPasswordValid = await bcrypt.compare(password, user.password);
        if (!isPasswordValid) {
            return res.status(401).json({ message: 'Invalid credentials' });
        }

        // Create JWT token
        const token = jwt.sign({ id: user._id }, 'your_jwt_secret', { expiresIn: '1h' });
        
        // Respond with token
        res.json({ token });
    } catch (err) {
        console.error('Error during login:', err);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Middleware to authenticate JWT tokens
const authenticateToken = (req, res, next) => {
    const token = req.headers['authorization']?.split(' ')[1]; // Bearer token format
    if (!token) return res.sendStatus(401); // Unauthorized

    jwt.verify(token, 'your_jwt_secret', (err, user) => {
        if (err) return res.sendStatus(403); // Forbidden
        req.user = user; // Save user info in request object
        next(); // Proceed to the next middleware or route handler
    });
};

// Protected endpoint example
app.get('/profile', authenticateToken, (req, res) => {
    res.json({ message: 'This is a protected route', user: req.user });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

**User Model (models/User.js)**:
```javascript
const mongoose = require('mongoose');

// Define User schema
const userSchema = new mongoose.Schema({
    username: {
        type: String,
        required: true,
        unique: true
    },
    password: {
        type: String,
        required: true
    }
});

// Create User model
const User = mongoose.model('User', userSchema);

module.exports = User;
```
