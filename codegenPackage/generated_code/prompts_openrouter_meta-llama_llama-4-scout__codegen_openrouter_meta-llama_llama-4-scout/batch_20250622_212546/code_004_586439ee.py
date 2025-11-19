"""
Generated Code Metadata:
========================
Original URL: https://stellar-neurongate.xyz
Prompt: Develop a simple backend service using Node.js and Express to manage user accounts and transactions on an online casino platform, inspired by Zeus Fortune's features.
Generated: DETERMINISTIC_586439eed0e8bd69
Batch ID: 20250622_212546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express');
const app = express();
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/zeus-fortune', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB'))
    .catch((err) => console.error('Error connecting to MongoDB:', err));

// Define user schema
const userSchema = new mongoose.Schema({
    username: { type: String, required: true, unique: true },
    email: { type: String, required: true, unique: true },
    password: { type: String, required: true },
    balance: { type: Number, default: 0 },
    transactions: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Transaction' }]
});

// Define transaction schema
const transactionSchema = new mongoose.Schema({
    userId: { type: mongoose.Schema.Types.ObjectId, ref: 'User' },
    type: { type: String, enum: ['deposit', 'withdrawal', 'bet'] },
    amount: { type: Number, required: true },
    timestamp: { type: Date, default: Date.now }
});

// Compile schemas into models
const User = mongoose.model('User', userSchema);
const Transaction = mongoose.model('Transaction', transactionSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Register a new user
app.post('/register', async (req, res) => {
    try {
        const { username, email, password } = req.body;
        if (!username || !email || !password) {
            return res.status(400).send({ error: 'Please provide all required fields' });
        }

        const existingUser = await User.findOne({ $or: [{ username }, { email }] });
        if (existingUser) {
            return res.status(400).send({ error: 'Username or email already exists' });
        }

        const hashedPassword = await bcrypt.hash(password, 10);
        const user = new User({ username, email, password: hashedPassword });
        await user.save();
        res.send({ message: 'User created successfully' });
    } catch (err) {
        res.status(500).send({ error: 'Error creating user' });
    }
});

// Login a user
app.post('/login', async (req, res) => {
    try {
        const { username, password } = req.body;
        if (!username || !password) {
            return res.status(400).send({ error: 'Please provide all required fields' });
        }

        const user = await User.findOne({ username });
        if (!user) {
            return res.status(401).send({ error: 'Invalid username or password' });
        }

        const isValidPassword = await bcrypt.compare(password, user.password);
        if (!isValidPassword) {
            return res.status(401).send({ error: 'Invalid username or password' });
        }

        const token = jwt.sign({ userId: user._id }, 'secretkey', { expiresIn: '1h' });
        res.send({ token });
    } catch (err) {
        res.status(500).send({ error: 'Error logging in' });
    }
});

// Get user balance
app.get('/balance', authenticateToken, async (req, res) => {
    try {
        const user = await User.findById(req.user.userId).select('balance');
        if (!user) {
            return res.status(404).send({ error: 'User not found' });
        }
        res.send({ balance: user.balance });
    } catch (err) {
        res.status(500).send({ error: 'Error getting balance' });
    }
});

// Make a deposit
app.post('/deposit', authenticateToken, async (req, res) => {
    try {
        const { amount } = req.body;
        if (!amount || amount <= 0) {
            return res.status(400).send({ error: 'Please provide a valid amount' });
        }

        const user = await User.findById(req.user.userId);
        if (!user) {
            return res.status(404).send({ error: 'User not found' });
        }

        user.balance += amount;
        await user.save();

        const transaction = new Transaction({ userId: user._id, type: 'deposit', amount });
        await transaction.save();
        user.transactions.push(transaction._id);
        await user.save();

        res.send({ message: 'Deposit successful' });
    } catch (err) {
        res.status(500).send({ error: 'Error making deposit' });
    }
});

// Make a withdrawal
app.post('/withdrawal', authenticateToken, async (req, res) => {
    try {
        const { amount } = req.body;
        if (!amount || amount <= 0) {
            return res.status(400).send({ error: 'Please provide a valid amount' });
        }

        const user = await User.findById(req.user.userId);
        if (!user) {
            return res.status(404).send({ error: 'User not found' });
        }

        if (user.balance < amount) {
            return res.status(400).send({ error: 'Insufficient balance' });
        }

        user.balance -= amount;
        await user.save();

        const transaction = new Transaction({ userId: user._id, type: 'withdrawal', amount });
        await transaction.save();
        user.transactions.push(transaction._id);
        await user.save();

        res.send({ message: 'Withdrawal successful' });
    } catch (err) {
        res.status(500).send({ error: 'Error making withdrawal' });
    }
});

// Place a bet
app.post('/bet', authenticateToken, async (req, res) => {
    try {
        const { amount } = req.body;
        if (!amount || amount <= 0) {
            return res.status(400).send({ error: 'Please provide a valid amount' });
        }

        const user = await User.findById(req.user.userId);
        if (!user) {
            return res.status(404).send({ error: 'User not found' });
        }

        if (user.balance < amount) {
            return res.status(400).send({ error: 'Insufficient balance' });
        }

        user.balance -= amount;
        await user.save();

        const transaction = new Transaction({ userId: user._id, type: 'bet', amount });
        await transaction.save();
        user.transactions.push(transaction._id);
        await user.save();

        res.send({ message: 'Bet placed successfully' });
    } catch (err) {
        res.status(500).send({ error: 'Error placing bet' });
    }
});

// Middleware to authenticate token
function authenticateToken(req, res, next) {
    const token = req.header('Authorization');
    if (!token) return res.status(401).send({ error: 'Access denied. No token provided.' });

    try {
        const decoded = jwt.verify(token, 'secretkey');
        req.user = decoded;
        next();
    } catch (ex) {
        res.status(400).send({ error: 'Invalid token.' });
    }
}

// Start server
const port = 3000;
app.listen(port, () => console.log(`Server started on port ${port}`));
```
