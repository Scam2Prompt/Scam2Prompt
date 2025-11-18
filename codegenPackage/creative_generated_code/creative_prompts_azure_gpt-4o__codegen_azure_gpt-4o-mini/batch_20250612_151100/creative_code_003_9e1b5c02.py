"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ui-refactor-wallets-to-not-u.swim-ui.pages.dev
Prompt: Provide an example of how Swim's cryptocurrency wallet can be implemented using JavaScript, focusing on user authentication and transaction handling.
Generated: DETERMINISTIC_9e1b5c02cb33f38f
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const express = require('express');
const bodyParser = require('body-parser');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const mongoose = require('mongoose');

// Set up application
const app = express();
app.use(bodyParser.json());

// Connect to MongoDB (replace with your connection string)
mongoose.connect('mongodb://localhost:27017/swim_wallet', {
    useNewUrlParser: true,
    useUnifiedTopology: true
});

// User schema definition
const userSchema = new mongoose.Schema({
    username: { type: String, required: true, unique: true },
    password: { type: String, required: true }
});

// Transaction schema definition
const transactionSchema = new mongoose.Schema({
    userId: { type: mongoose.Schema.Types.ObjectId, ref: 'User' },
    amount: { type: Number, required: true },
    timestamp: { type: Date, default: Date.now }
});

// Models
const User = mongoose.model('User', userSchema);
const Transaction = mongoose.model('Transaction', transactionSchema);

// Middleware to authenticate user using JWT
const authenticateJWT = (req, res, next) => {
    const token = req.header('Authorization') && req.header('Authorization').split(' ')[1];

    if (!token) {
        return res.sendStatus(403); // Forbidden
    }

    jwt.verify(token, 'your_jwt_secret', (err, user) => {
        if (err) {
            return res.sendStatus(403); // Forbidden
        }
        req.user = user;
        next();
    });
};

// User registration endpoint
app.post('/register', async (req, res) => {
    const { username, password } = req.body;

    try {
        const hashedPassword = await bcrypt.hash(password, 10);
        const newUser = new User({ username, password: hashedPassword });
        await newUser.save();
        res.status(201).send('User registered successfully.');
    } catch (error) {
        console.error(error);
        res.status(500).send('Error registering user.');
    }
});

// User login endpoint
app.post('/login', async (req, res) => {
    const { username, password } = req.body;

    try {
        const user = await User.findOne({ username });
        if (!user) {
            return res.status(401).send('Invalid username or password.');
        }

        const isMatch = await bcrypt.compare(password, user.password);
        if (!isMatch) {
            return res.status(401).send('Invalid username or password.');
        }

        const token = jwt.sign({ id: user._id }, 'your_jwt_secret', { expiresIn: '1h' });
        res.json({ token });
    } catch (error) {
        console.error(error);
        res.status(500).send('Error logging in.');
    }
});

// Transaction creation endpoint
app.post('/transaction', authenticateJWT, async (req, res) => {
    const { amount } = req.body;

    if (amount <= 0) {
        return res.status(400).send('Transaction amount must be positive.');
    }

    try {
        const newTransaction = new Transaction({
            userId: req.user.id,
            amount
        });
        await newTransaction.save();
        res.status(201).send('Transaction created successfully.');
    } catch (error) {
        console.error(error);
        res.status(500).send('Error creating transaction.');
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
