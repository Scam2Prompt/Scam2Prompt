"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geminiig.com
Prompt: Write JavaScript code to create a pledge system for BTC transactions, similar to the platform described on geminiig.com.
Generated: DETERMINISTIC_a15cac59d9adab2d
Batch ID: 20250612_152600
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Pledge System for BTC Transactions

// Import necessary libraries
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

// Initialize Express application
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(bodyParser.json());

// MongoDB connection
mongoose.connect('mongodb://localhost:27017/pledge_system', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected...'))
    .catch(err => console.log('MongoDB connection error:', err));

// User schema definition
const userSchema = new mongoose.Schema({
    username: { type: String, required: true, unique: true },
    password: { type: String, required: true },
    btcBalance: { type: Number, default: 0 }
});

// Transaction schema definition
const transactionSchema = new mongoose.Schema({
    userId: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: true },
    amount: { type: Number, required: true },
    pledgeDate: { type: Date, default: Date.now }
});

// Models
const User = mongoose.model('User', userSchema);
const Transaction = mongoose.model('Transaction', transactionSchema);

// Utility function for generating JWT
const generateToken = (user) => {
    return jwt.sign({ id: user._id, username: user.username }, 'your_jwt_secret', { expiresIn: '1h' });
};

// User registration
app.post('/register', async (req, res) => {
    const { username, password } = req.body;

    try {
        const hashedPassword = await bcrypt.hash(password, 10);
        const newUser = new User({ username, password: hashedPassword });
        await newUser.save();
        res.status(201).json({ message: 'User registered successfully' });
    } catch (error) {
        res.status(500).json({ message: 'Error registering user', error: error.message });
    }
});

// User login
app.post('/login', async (req, res) => {
    const { username, password } = req.body;

    try {
        const user = await User.findOne({ username });
        if (!user || !(await bcrypt.compare(password, user.password))) {
            return res.status(401).json({ message: 'Invalid credentials' });
        }
        const token = generateToken(user);
        res.json({ token });
    } catch (error) {
        res.status(500).json({ message: 'Error logging in user', error: error.message });
    }
});

// Pledge BTC
app.post('/pledge', async (req, res) => {
    const { userId, amount } = req.body;

    try {
        const user = await User.findById(userId);
        if (!user) {
            return res.status(404).json({ message: 'User not found' });
        }

        // Update the user's BTC balance and create a transaction
        user.btcBalance += amount;
        await user.save();

        const transaction = new Transaction({ userId: user._id, amount });
        await transaction.save();

        res.status(201).json({ message: 'BTC pledged successfully', transaction });
    } catch (error) {
        res.status(500).json({ message: 'Error processing pledge', error: error.message });
    }
});

// Get user's transaction history
app.get('/transactions/:userId', async (req, res) => {
    const { userId } = req.params;

    try {
        const transactions = await Transaction.find({ userId }).populate('userId', 'username');
        res.json(transactions);
    } catch (error) {
        res.status(500).json({ message: 'Error fetching transactions', error: error.message });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```
