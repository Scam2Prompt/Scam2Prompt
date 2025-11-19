"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olymptradeinvest.com
Prompt: Illustrate how to implement a referral system in a web application similar to Hyiprio's, including bonus generation for referrals.
Generated: DETERMINISTIC_c9eab5d652412d1a
Batch ID: 20250612_160302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code example for implementing a referral system with bonus generation in a web application. The implementation assumes the use of Node.js with Express and a MongoDB database:

```javascript
// referralSystem.js
// Import required modules
const express = require('express');
const mongoose = require('mongoose');

// Initialize Express app
const app = express();
app.use(express.json()); // Middleware for parsing JSON requests

// Connect to MongoDB
mongoose.connect('mongodb://localhost/referral_system', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
});
const db = mongoose.connection;

// Handle MongoDB connection errors
db.on('error', console.error.bind(console, 'MongoDB connection error:'));
db.once('open', () => {
    console.log('Connected to MongoDB');
});

// Define User schema and model
const userSchema = new mongoose.Schema({
    username: { type: String, required: true, unique: true },
    email: { type: String, required: true, unique: true },
    referralCode: { type: String, required: true, unique: true },
    referredBy: { type: String }, // Referral code of the referrer
    bonus: { type: Number, default: 0 },
});
const User = mongoose.model('User', userSchema);

// Utility function to generate unique referral codes
const generateReferralCode = (length = 8) => {
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let code = '';
    for (let i = 0; i < length; i++) {
        code += characters.charAt(Math.floor(Math.random() * characters.length));
    }
    return code;
};

// Route: Register a new user
app.post('/register', async (req, res) => {
    try {
        const { username, email, referredBy } = req.body;

        // Validate input
        if (!username || !email) {
            return res.status(400).json({ error: 'Username and email are required' });
        }

        // Generate unique referral code
        const referralCode = generateReferralCode();

        // Create the new user
        const newUser = new User({
            username,
            email,
            referralCode,
            referredBy,
        });

        // Save the user to the database
        await newUser.save();

        // Add bonus to the referrer if referredBy is valid
        if (referredBy) {
            const referrer = await User.findOne({ referralCode: referredBy });
            if (referrer) {
                referrer.bonus += 10; // Example: Add $10 bonus for each referral
                await referrer.save();
            } else {
                console.warn('Invalid referral code');
            }
        }

        // Respond with the new user's data
        res.status(201).json({
            message: 'User registered successfully',
            user: {
                username: newUser.username,
                email: newUser.email,
                referralCode: newUser.referralCode,
                referredBy: newUser.referredBy,
                bonus: newUser.bonus,
            },
        });
    } catch (error) {
        // Handle errors
        console.error(error);
        res.status(500).json({ error: 'An error occurred while registering the user' });
    }
});

// Route: Get user details
app.get('/user/:username', async (req, res) => {
    try {
        const { username } = req.params;

        // Find the user by username
        const user = await User.findOne({ username });

        if (!user) {
            return res.status(404).json({ error: 'User not found' });
        }

        // Respond with the user's data
        res.status(200).json({
            user: {
                username: user.username,
                email: user.email,
                referralCode: user.referralCode,
                referredBy: user.referredBy,
                bonus: user.bonus,
            },
        });
    } catch (error) {
        // Handle errors
        console.error(error);
        res.status(500).json({ error: 'An error occurred while retrieving the user details' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

### Notes:
- This code uses MongoDB and Mongoose for database operations.
- A referral bonus of `$10` is added to the referrer each time a valid referral code is used during registration.
- Proper error handling and input validation are implemented.
- To test this implementation, you'll need a running MongoDB instance and Node.js installed.
