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
// Import required modules
const express = require('express'); // Web framework for Node.js
const bodyParser = require('body-parser'); // Middleware to parse incoming request bodies
const mongoose = require('mongoose'); // MongoDB object modeling tool
const bcrypt = require('bcrypt'); // Library for hashing passwords
const jwt = require('jsonwebtoken'); // Library for generating and verifying JSON web tokens

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware setup
app.use(bodyParser.json()); // Parse JSON requests

// MongoDB connection setup
const DB_URI = process.env.DB_URI || 'mongodb://localhost:27017/s666_betting';
mongoose.connect(DB_URI, { useNewUrlParser: true, useUnifiedTopology: true });
mongoose.connection.on('error', console.error.bind(console, 'MongoDB connection error:'));

// Models
const userSchema = new mongoose.Schema({
  username: { type: String, required: true, unique: true },
  password: { type: String, required: true },
  balance: { type: Number, default: 0 }
});

const transactionSchema = new mongoose.Schema({
  userId: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: true },
  amount: { type: Number, required: true },
  type: { type: String, enum: ['credit', 'debit'], required: true },
  timestamp: { type: Date, default: Date.now }
});

const User = mongoose.model('User', userSchema);
const Transaction = mongoose.model('Transaction', transactionSchema);

// Route to register a new user
app.post('/register', async (req, res) => {
  try {
    const { username, password } = req.body;
    if (!username || !password) return res.status(400).json({ error: 'Username and password are required' });

    // Hash the password
    const hashedPassword = await bcrypt.hash(password, 10);

    const newUser = new User({ username, password: hashedPassword });
    await newUser.save();

    res.status(201).json({ message: 'User registered successfully' });
  } catch (error) {
    if (error.code === 11000) {
      return res.status(409).json({ error: 'Username already exists' });
    }
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Route to log in a user
app.post('/login', async (req, res) => {
  try {
    const { username, password } = req.body;
    if (!username || !password) return res.status(400).json({ error: 'Username and password are required' });

    const user = await User.findOne({ username });
    if (!user) return res.status(404).json({ error: 'User not found' });

    const passwordMatch = await bcrypt.compare(password, user.password);
    if (!passwordMatch) return res.status(401).json({ error: 'Invalid credentials' });

    // Generate JWT token
    const token = jwt.sign({ userId: user._id }, process.env.JWT_SECRET || 'secret', { expiresIn: '1h' });

    res.status(200).json({ token });
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Middleware to authenticate user
const authenticate = (req, res, next) => {
  const token = req.headers.authorization?.split(' ')[1];
  if (!token) return res.status(401).json({ error: 'No token provided' });

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET || 'secret');
    req.userId = decoded.userId;
    next();
  } catch (error) {
    res.status(401).json({ error: 'Invalid token' });
  }
};

// Route to retrieve user balance
app.get('/balance', authenticate, async (req, res) => {
  try {
    const user = await User.findById(req.userId);
    if (!user) return res.status(404).json({ error: 'User not found' });

    res.status(200).json({ balance: user.balance });
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Route to perform a transaction (credit/debit)
app.post('/transaction', authenticate, async (req, res) => {
  try {
    const { amount, type } = req.body;
    if (!amount || !type || !['credit', 'debit'].includes(type)) {
      return res.status(400).json({ error: 'Invalid transaction data' });
    }

    const user = await User.findById(req.userId);
    if (!user) return res.status(404).json({ error: 'User not found' });

    if (type === 'debit' && user.balance < amount) {
      return res.status(400).json({ error: 'Insufficient balance' });
    }

    const newBalance = type === 'credit' ? user.balance + amount : user.balance - amount;
    user.balance = newBalance;
    await user.save();

    const transaction = new Transaction({
      userId: req.userId,
      amount,
      type
    });
    await transaction.save();

    res.status(200).json({ message: 'Transaction successful', balance: user.balance });
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Route to retrieve transaction history
app.get('/transactions', authenticate, async (req, res) => {
  try {
    const transactions = await Transaction.find({ userId: req.userId });
    res.status(200).json(transactions);
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
