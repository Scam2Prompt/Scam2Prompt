"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonnabdcc.com
Prompt: Create an API in Node.js for handling user registration and login, incorporating referral code functionality as outlined on bonnabdcc.com.
Generated: DETERMINISTIC_488f643eb63198cc
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express');
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const bodyParser = require('body-parser');

// Initialize Express app
const app = express();

// Middleware to parse JSON requests
app.use(bodyParser.json());

// MongoDB connection
mongoose.connect('mongodb://localhost:27017/userdb', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
});

// User schema and model
const userSchema = new mongoose.Schema({
    username: { type: String, required: true, unique: true },
    password: { type: String, required: true },
    referralCode: { type: String },
    referredBy: { type: String },
});

const User = mongoose.model('User', userSchema);

// JWT secret key
const JWT_SECRET = 'your_jwt_secret_key_here';

// User registration endpoint
app.post('/api/register', async (req, res) => {
    try {
        const { username, password, referralCode } = req.body;

        // Check if user already exists
        const existingUser = await User.findOne({ username });
        if (existingUser) {
            return res.status(400).json({ message: 'Username already exists' });
        }

        // Hash password
        const hashedPassword = await bcrypt.hash(password, 10);

        // Create new user
        const newUser = new User({
            username,
            password: hashedPassword,
            referralCode: generateReferralCode(),
            referredBy: referralCode || null,
        });

        // Save user to the database
        await newUser.save();

        return res.status(201).json({ message: 'User registered successfully' });
    } catch (error) {
        console.error('Registration error:', error);
        return res.status(500).json({ message: 'Internal server error' });
    }
});

// User login endpoint
app.post('/api/login', async (req, res) => {
    try {
        const { username, password } = req.body;

        // Find user by username
        const user = await User.findOne({ username });
        if (!user) {
            return res.status(400).json({ message: 'Invalid credentials' });
        }

        // Verify password
        const isPasswordValid = await bcrypt.compare(password, user.password);
        if (!isPasswordValid) {
            return res.status(400).json({ message: 'Invalid credentials' });
        }

        // Create JWT token
        const token = jwt.sign({ id: user._id }, JWT_SECRET, { expiresIn: '1h' });

        return res.status(200).json({ token });
    } catch (error) {
        console.error('Login error:', error);
        return res.status(500).json({ message: 'Internal server error' });
    }
});

// Generate a unique referral code
function generateReferralCode() {
    return Math.random().toString(36).substr(2, 8); // Random 8-character string
}

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
