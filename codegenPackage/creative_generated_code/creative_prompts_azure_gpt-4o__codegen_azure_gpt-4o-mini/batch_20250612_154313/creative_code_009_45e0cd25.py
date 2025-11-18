"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lidofi.us.com
Prompt: Create a REST API in Node.js to manage user deposits and withdrawals for WW88, ensuring compliance with the site's "Nạp tiền WW88" and "Rút tiền WW88" guidelines.
Generated: DETERMINISTIC_45e0cd256f3d89af
Batch ID: 20250612_154313
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
const mongoose = require('mongoose');
const dotenv = require('dotenv');

// Load environment variables from .env file
dotenv.config();

// Initialize Express app
const app = express();
app.use(bodyParser.json()); // Parse JSON request bodies

// Connect to MongoDB
mongoose.connect(process.env.MONGODB_URI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define User schema
const userSchema = new mongoose.Schema({
    username: { type: String, required: true, unique: true },
    balance: { type: Number, default: 0 }
});

// Create User model
const User = mongoose.model('User', userSchema);

// Middleware for error handling
const errorHandler = (err, req, res, next) => {
    console.error(err);
    res.status(500).json({ error: 'Internal server error' });
};

// Create a new user
app.post('/api/users', async (req, res) => {
    const { username } = req.body;

    try {
        const newUser = new User({ username });
        await newUser.save();
        res.status(201).json(newUser);
    } catch (error) {
        res.status(400).json({ error: 'User creation failed', details: error.message });
    }
});

// Deposit money into user account
app.post('/api/users/:username/deposit', async (req, res) => {
    const { username } = req.params;
    const { amount } = req.body;

    try {
        if (amount <= 0) throw new Error('Deposit amount must be greater than zero');

        const user = await User.findOne({ username });
        if (!user) return res.status(404).json({ error: 'User not found' });

        user.balance += amount;
        await user.save();
        res.status(200).json({ message: 'Deposit successful', balance: user.balance });
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

// Withdraw money from user account
app.post('/api/users/:username/withdraw', async (req, res) => {
    const { username } = req.params;
    const { amount } = req.body;

    try {
        if (amount <= 0) throw new Error('Withdrawal amount must be greater than zero');

        const user = await User.findOne({ username });
        if (!user) return res.status(404).json({ error: 'User not found' });

        if (user.balance < amount) throw new Error('Insufficient funds');

        user.balance -= amount;
        await user.save();
        res.status(200).json({ message: 'Withdrawal successful', balance: user.balance });
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

// Get user balance
app.get('/api/users/:username/balance', async (req, res) => {
    const { username } = req.params;

    try {
        const user = await User.findOne({ username });
        if (!user) return res.status(404).json({ error: 'User not found' });

        res.status(200).json({ username: user.username, balance: user.balance });
    } catch (error) {
        res.status(500).json({ error: 'Failed to retrieve balance' });
    }
});

// Apply error handling middleware
app.use(errorHandler);

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
```

**.env Example:**
```
MONGODB_URI=mongodb://<your_mongo_db_connection_string>
PORT=3000
```
