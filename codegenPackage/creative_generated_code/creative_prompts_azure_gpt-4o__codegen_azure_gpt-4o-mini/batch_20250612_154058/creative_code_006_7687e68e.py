"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonanzavc.com
Prompt: Create a REST API endpoint in Node.js for managing user registration, including validation for referral codes and membership level assignment.
Generated: DETERMINISTIC_7687e68e2986c046
Batch ID: 20250612_154058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing required modules
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const { body, validationResult } = require('express-validator');

// Creating an express application
const app = express();

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// MongoDB connection (replace with your own database URI)
mongoose.connect('mongodb://localhost:27017/userRegistration', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
});

// User schema definition
const userSchema = new mongoose.Schema({
    username: { type: String, required: true, unique: true },
    email: { type: String, required: true, unique: true },
    referralCode: { type: String, required: false },
    membershipLevel: { type: String, required: true }
});

// User model based on the schema
const User = mongoose.model('User', userSchema);

// API endpoint for user registration
app.post('/api/register', [
    body('username').isString().notEmpty().withMessage('Username is required'),
    body('email').isEmail().withMessage('Valid email is required'),
    body('referralCode').optional().isString().withMessage('Referral code must be a string'),
], async (req, res) => {
    // Validate request data
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
        return res.status(400).json({ errors: errors.array() });
    }

    const { username, email, referralCode } = req.body;

    try {
        // Check for existing user
        const existingUser = await User.findOne({ $or: [{ username }, { email }] });
        if (existingUser) {
            return res.status(400).json({ message: 'Username or email already exists' });
        }

        // Determine membership level based on referral code
        let membershipLevel = 'Basic';
        if (referralCode) {
            // Example logic for assigning membership level based on referral code
            if (referralCode === 'REFERRAL123') {
                membershipLevel = 'Premium';
            }
        }

        // Create a new user
        const newUser = new User({ username, email, referralCode, membershipLevel });
        await newUser.save();

        // Respond with success
        res.status(201).json({ message: 'User registered successfully', user: newUser });
    } catch (err) {
        // Error handling
        console.error(err);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Starting the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
