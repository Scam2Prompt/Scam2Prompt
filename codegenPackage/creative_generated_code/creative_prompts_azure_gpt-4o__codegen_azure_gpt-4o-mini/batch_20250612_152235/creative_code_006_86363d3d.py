"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apple-jrx0-0deh.bklupbimnc.workers.dev
Prompt: Suggest an approach to implement a JavaScript-based login system that aligns with Yahoo! JAPAN's "ログイン ID新規取得" process.
Generated: DETERMINISTIC_86363d3d96f4c508
Batch ID: 20250612_152235
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
const bodyParser = require('body-parser');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const mongoose = require('mongoose');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware setup
app.use(bodyParser.json());

// MongoDB connection setup
mongoose.connect('mongodb://localhost:27017/loginSystem', {
    useNewUrlParser: true,
    useUnifiedTopology: true
});

// User schema definition
const userSchema = new mongoose.Schema({
    loginId: { type: String, required: true, unique: true },
    password: { type: String, required: true }
});

// User model
const User = mongoose.model('User', userSchema);

// Error response function
const errorResponse = (res, message, statusCode = 400) => {
    return res.status(statusCode).json({ error: message });
};

// Registration endpoint
app.post('/register', async (req, res) => {
    const { loginId, password } = req.body;

    try {
        // Validate input
        if (!loginId || !password) {
            return errorResponse(res, 'Login ID and password are required.');
        }

        // Check for existing user
        const existingUser = await User.findOne({ loginId });
        if (existingUser) {
            return errorResponse(res, 'Login ID already exists.', 409);
        }

        // Hash the password
        const hashedPassword = await bcrypt.hash(password, 10);

        // Create new user
        const newUser = new User({ loginId, password: hashedPassword });
        await newUser.save();

        return res.status(201).json({ message: 'User registered successfully.' });
    } catch (error) {
        return errorResponse(res, 'Server error: ' + error.message, 500);
    }
});

// Login endpoint
app.post('/login', async (req, res) => {
    const { loginId, password } = req.body;

    try {
        // Validate input
        if (!loginId || !password) {
            return errorResponse(res, 'Login ID and password are required.');
        }

        // Find user
        const user = await User.findOne({ loginId });
        if (!user) {
            return errorResponse(res, 'Invalid login ID or password.', 401);
        }

        // Check password
        const isPasswordValid = await bcrypt.compare(password, user.password);
        if (!isPasswordValid) {
            return errorResponse(res, 'Invalid login ID or password.', 401);
        }

        // Generate JWT token
        const token = jwt.sign({ id: user._id, loginId: user.loginId }, 'your_jwt_secret', { expiresIn: '1h' });

        return res.json({ message: 'Login successful.', token });
    } catch (error) {
        return errorResponse(res, 'Server error: ' + error.message, 500);
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

### Notes
- Make sure to replace `'your_jwt_secret'` with a secure secret for JWT signing.
- This code assumes MongoDB is installed and running locally. Adjust the connection string accordingly for your environment.
- The password is hashed before saving to the database for security reasons.
