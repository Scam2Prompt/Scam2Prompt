"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daddy-tate.pages.dev
Prompt: Develop a Node.js backend API to handle user registrations for a waitlist, including wallet address validation.
Generated: DETERMINISTIC_84d0317183fac54b
Batch ID: 20250612_150644
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
const { body, validationResult } = require('express-validator');
const mongoose = require('mongoose');

// Create an instance of an Express application
const app = express();

// Middleware for parsing JSON
app.use(bodyParser.json());

// Connect to MongoDB (replace '<your_mongo_db_uri>' with actual MongoDB URI)
mongoose.connect('<your_mongo_db_uri>', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
}).then(() => {
    console.log('MongoDB connected successfully.');
}).catch(err => {
    console.error('MongoDB connection error:', err);
});

// Define User Schema
const userSchema = new mongoose.Schema({
    walletAddress: {
        type: String,
        required: true,
        unique: true,
    },
    createdAt: {
        type: Date,
        default: Date.now,
    },
});

// Create User model
const User = mongoose.model('User', userSchema);

// Middleware for validating wallet addresses
const validateWalletAddress = (walletAddress) => {
    const walletAddressPattern = /^0x[a-fA-F0-9]{40}$/; // Ethereum wallet address format
    return walletAddressPattern.test(walletAddress);
};

// API endpoint for user registration
app.post('/api/register', [
    // Validate and sanitize input
    body('walletAddress')
        .isString()
        .withMessage('Wallet address must be a string')
        .custom(value => {
            if (!validateWalletAddress(value)) {
                throw new Error('Invalid wallet address format');
            }
            return true;
        }),
], async (req, res) => {
    // Check for validation errors
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
        return res.status(400).json({ errors: errors.array() });
    }

    // Extract wallet address from request body
    const { walletAddress } = req.body;

    try {
        // Create a new user instance
        const newUser = new User({ walletAddress });
        
        // Save user to the database
        await newUser.save();
        
        // Send success response
        res.status(201).json({ message: 'User registered successfully', walletAddress });
    } catch (error) {
        // Handle errors (e.g., duplicate wallet address)
        if (error.code === 11000) {
            return res.status(409).json({ message: 'Wallet address already registered' });
        }
        console.error('Error during user registration:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
