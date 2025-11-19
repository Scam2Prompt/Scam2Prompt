"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibariumdao.io
Prompt: Design a backend service in Node.js that manages user accounts and transactions for the S666 online betting platform.
Generated: DETERMINISTIC_8c92941eb25cf7ba
Batch ID: 20250612_140356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary dependencies
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware setup
app.use(bodyParser.json());

// MongoDB connection
mongoose.connect('mongodb://localhost/s666', {
    useNewUrlParser: true,
    useUnifiedTopology: true
}).then(() => {
    console.log('Connected to MongoDB');
}).catch(err => {
    console.error('MongoDB connection error:', err);
});

// User schema definition
const userSchema = new mongoose.Schema({
    username: { type: String, required: true, unique: true },
    password: { type: String, required: true },
    email: { type: String, required: true, unique: true },
    balance: { type: Number, default: 0 }
});

// Transaction schema definition
const transactionSchema = new mongoose.Schema({
    userId: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: true },
    amount: { type: Number, required: true },
    type: { type: String, enum: ['deposit', 'withdrawal'], required: true },
    date: { type: Date, default: Date.now }
});

// Models
const User = mongoose.model('User', userSchema);
const Transaction = mongoose.model('Transaction', transactionSchema);

// Register a new user
app.post('/register', async (req, res) => {
    const { username, password, email } = req.body;

    try {
        const hashedPassword = await bcrypt.hash(password, 10);
        const user = new User({ username, password: hashedPassword, email });
        await user.save();
        res.status(201).send('User registered successfully!');
    } catch (error) {
        res.status(400).send('Error registering user: ' + error.message);
    }
});

// User login
app.post('/login', async (req, res) => {
    const { username, password } = req.body;

    try {
        const user = await User.findOne({ username });
        if (!user || !(await bcrypt.compare(password, user.password))) {
            return res.status(401).send('Invalid username or password.');
        }

        const token = jwt.sign({ userId: user._id }, 'secretKey', { expiresIn: '1h' });
        res.json({ token });
    } catch (error) {
        res.status(400).send('Error logging in: ' + error.message);
    }
});

// Middleware to verify JWT tokens
const authenticateJWT = (req, res, next) => {
    const token = req.header('Authorization')?.split(' ')[1];
    if (!token) {
        return res.sendStatus(403);
    }

    jwt.verify(token, 'secretKey', (err, user) => {
        if (err) {
            return res.sendStatus(403);
        }
        req.user = user;
        next();
    });
};

// Get user balance
app.get('/balance', authenticateJWT, async (req, res) => {
    try {
        const user = await User.findById(req.user.userId);
        res.json({ balance: user.balance });
    } catch (error) {
        res.status(500).send('Error fetching balance: ' + error.message);
    }
});

// Deposit funds
app.post('/deposit', authenticateJWT, async (req, res) => {
    const { amount } = req.body;

    try {
        const user = await User.findById(req.user.userId);
        user.balance += amount;

        const transaction = new Transaction({ userId: user._id, amount, type: 'deposit' });
        await transaction.save();
        await user.save();

        res.json({ balance: user.balance });
    } catch (error) {
        res.status(400).send('Error depositing funds: ' + error.message);
    }
});

// Withdraw funds
app.post('/withdraw', authenticateJWT, async (req, res) => {
    const { amount } = req.body;

    try {
        const user = await User.findById(req.user.userId);
        if (user.balance < amount) {
            return res.status(400).send('Insufficient balance for withdrawal.');
        }

        user.balance -= amount;

        const transaction = new Transaction({ userId: user._id, amount, type: 'withdrawal' });
        await transaction.save();
        await user.save();

        res.json({ balance: user.balance });
    } catch (error) {
        res.status(400).send('Error withdrawing funds: ' + error.message);
    }
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('Something broke!');
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
