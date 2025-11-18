"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonaeac.com
Prompt: Create an API endpoint in Node.js for registering new users with fields for username, phone number, password, and referral code, as specified on bonaeac.com.
Generated: DETERMINISTIC_ac269abf58879d81
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
const express = require('express');
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');
const Joi = require('joi');
const app = express();

// Middleware to parse JSON bodies
app.use(express.json());

// MongoDB connection string
const mongoURI = 'mongodb://localhost:27017/bonaeac'; // Update with your MongoDB URI

// Connect to MongoDB
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// User schema definition
const userSchema = new mongoose.Schema({
    username: { type: String, required: true, unique: true },
    phoneNumber: { type: String, required: true, unique: true },
    password: { type: String, required: true },
    referralCode: { type: String, required: false },
});

// User model
const User = mongoose.model('User', userSchema);

// Validation schema using Joi
const userSchemaValidation = Joi.object({
    username: Joi.string().min(3).max(30).required(),
    phoneNumber: Joi.string().pattern(/^[0-9]{10}$/).required(),
    password: Joi.string().min(6).max(1024).required(),
    referralCode: Joi.string().optional(),
});

// API endpoint for user registration
app.post('/api/register', async (req, res) => {
    // Validate the incoming request body
    const { error } = userSchemaValidation.validate(req.body);
    if (error) return res.status(400).send(error.details[0].message);

    // Destructure the data from request body
    const { username, phoneNumber, password, referralCode } = req.body;

    try {
        // Check if the user already exists
        const existingUser = await User.findOne({ $or: [{ username }, { phoneNumber }] });
        if (existingUser) return res.status(400).send('User already exists.');

        // Hash the password
        const salt = await bcrypt.genSalt(10);
        const hashedPassword = await bcrypt.hash(password, salt);

        // Create a new user
        const newUser = new User({
            username,
            phoneNumber,
            password: hashedPassword,
            referralCode,
        });

        // Save user to the database
        await newUser.save();
        res.status(201).send('User registered successfully.');
    } catch (err) {
        console.error('Error registering user:', err);
        res.status(500).send('Internal Server Error');
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

Make sure to install the required dependencies before running this code:
```bash
npm install express mongoose bcrypt joi
```
