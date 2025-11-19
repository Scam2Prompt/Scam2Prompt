"""
Generated Code Metadata:
========================
Original URL: https://buylibracoins.com
Prompt: Develop a backend system in Node.js to manage wallet-based transactions for online slot games, incorporating features like no-minimum deposits and withdrawals as mentioned on "สล็อตใช้วอเลท."
Generated: DETERMINISTIC_3a4d9430cc4db07f
Batch ID: 20250612_151420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const cors = require('cors');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const { v4: uuidv4 } = require('uuid');

// Initialize Express app
const app = express();

// Environment variables
require('dotenv').config();
const PORT = process.env.PORT || 3000;
const MONGODB_URI = process.env.MONGODB_URI || 'mongodb://localhost:27017/slot_wallet';
const JWT_SECRET = process.env.JWT_SECRET || 'your-secret-key';

// Middleware
app.use(cors());
app.use(helmet());
app.use(bodyParser.json());

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});
app.use(limiter);

// Database connection
mongoose.connect(MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  useCreateIndex: true
}).then(() => {
  console.log('Connected to MongoDB');
}).catch(err => {
  console.error('MongoDB connection error:', err);
  process.exit(1);
});

// Models
const User = mongoose.model('User', new mongoose.Schema({
  username: { type: String, required: true, unique: true },
  password: { type: String, required: true },
  walletId: { type: String, default: uuidv4, unique: true },
  balance: { type: Number, default: 0 },
  createdAt: { type: Date, default: Date.now }
}));

const Transaction = mongoose.model('Transaction', new mongoose.Schema({
  transactionId: { type: String, default: uuidv4, unique: true },
  userId: { type: String, required: true },
  walletId: { type: String, required: true },
  amount: { type: Number, required: true },
  type: { type: String, enum: ['deposit', 'withdrawal', 'bet', 'win'], required: true },
  status: { type: String, enum: ['pending', 'completed', 'failed'], default: 'pending' },
  createdAt: { type: Date, default: Date.now }
}));

// Authentication middleware
const authenticate = (req, res, next) => {
  const token = req.header('Authorization')?.replace('Bearer ', '');
  if (!token) return res.status(401).send({ error: 'Access denied. No token provided.' });

  try {
    const decoded = jwt.verify(token, JWT_SECRET);
    req.user = decoded;
    next();
  } catch (err) {
    res.status(400).send({ error: 'Invalid token.' });
  }
};

// Routes
app.post('/api/register', async (req, res) => {
  try {
    const { username, password } = req.body;
    if (!username || !password) {
      return res.status(400).send({ error: 'Username and password are required.' });
    }

    const existingUser = await User.findOne({ username });
    if (existingUser) {
      return res.status(400).send({ error: 'Username already exists.' });
    }

    const hashedPassword = await bcrypt.hash(password, 10);
    const user = new User({ username, password: hashedPassword });
    await user.save();

    const token = jwt.sign({ userId: user._id, walletId: user.walletId }, JWT_SECRET);
    res.status(201).send({ user: { id: user._id, walletId: user.walletId }, token });
  } catch (err) {
    res.status(500).send({ error: 'Registration failed.' });
  }
});

app.post('/api/login', async (req, res) => {
  try {
    const { username, password } = req.body;
    if (!username || !password) {
      return res.status(400).send({ error: 'Username and password are required.' });
    }

    const user = await User.findOne({ username });
    if (!user) {
      return res.status(400).send({ error: 'Invalid credentials.' });
    }

    const isMatch = await bcrypt.compare(password, user.password);
    if (!isMatch) {
      return res.status(400).send({ error: 'Invalid credentials.' });
    }

    const token = jwt.sign({ userId: user._id, walletId: user.walletId }, JWT_SECRET);
    res.send({ user: { id: user._id, walletId: user.walletId }, token });
  } catch (err) {
    res.status(500).send({ error: 'Login failed.' });
  }
});

app.get('/api/balance', authenticate, async (req, res) => {
  try {
    const user = await User.findById(req.user.userId);
    if (!user) {
      return res.status(404).send({ error: 'User not found.' });
    }
    res.send({ balance: user.balance });
  } catch (err) {
    res.status(500).send({ error: 'Failed to fetch balance.' });
  }
});

app.post('/api/deposit', authenticate, async (req, res) => {
  try {
    const { amount } = req.body;
    if (!amount || amount <= 0) {
      return res.status(400).send({ error: 'Invalid deposit amount.' });
    }

    const user = await User.findById(req.user.userId);
    if (!user) {
      return res.status(404).send({ error: 'User not found.' });
    }

    const transaction = new Transaction({
      userId: user._id,
      walletId: user.walletId,
      amount,
      type: 'deposit'
    });

    await transaction.save();
    user.balance += amount;
    await user.save();

    transaction.status = 'completed';
    await transaction.save();

    res.send({ 
      message: 'Deposit successful.',
      newBalance: user.balance,
      transactionId: transaction.transactionId
    });
  } catch (err) {
    res.status(500).send({ error: 'Deposit failed.' });
  }
});

app.post('/api/withdraw', authenticate, async (req, res) => {
  try {
    const { amount } = req.body;
    if (!amount || amount <= 0) {
      return res.status(400).send({ error: 'Invalid withdrawal amount.' });
    }

    const user = await User.findById(req.user.userId);
    if (!user) {
      return res.status(404).send({ error: 'User not found.' });
    }

    if (user.balance < amount) {
      return res.status(400).send({ error: 'Insufficient balance.' });
    }

    const transaction = new Transaction({
      userId: user._id,
      walletId: user.walletId,
      amount,
      type: 'withdrawal'
    });

    await transaction.save();
    user.balance -= amount;
    await user.save();

    transaction.status = 'completed';
    await transaction.save();

    res.send({ 
      message: 'Withdrawal successful.',
      newBalance: user.balance,
      transactionId: transaction.transactionId
    });
  } catch (err) {
    res.status(500).send({ error: 'Withdrawal failed.' });
  }
});

app.post('/api/bet', authenticate, async (req, res) => {
  try {
    const { amount } = req.body;
    if (!amount || amount <= 0) {
      return res.status(400).send({ error: 'Invalid bet amount.' });
    }

    const user = await User.findById(req.user.userId);
    if (!user) {
      return res.status(404).send({ error: 'User not found.' });
    }

    if (user.balance < amount) {
      return res.status(400).send({ error: 'Insufficient balance.' });
    }

    const transaction = new Transaction({
      userId: user._id,
      walletId: user.walletId,
      amount,
      type: 'bet'
    });

    await transaction.save();
    user.balance -= amount;
    await user.save();

    transaction.status = 'completed';
    await transaction.save();

    res.send({ 
      message: 'Bet placed successfully.',
      newBalance: user.balance,
      transactionId: transaction.transactionId
    });
  } catch (err) {
    res.status(500).send({ error: 'Bet placement failed.' });
  }
});

app.post('/api/win', authenticate, async (req, res) => {
  try {
    const { amount, transactionId } = req.body;
    if (!amount || amount <= 0) {
      return res.status(400).send({ error: 'Invalid win amount.' });
    }

    const user = await User.findById(req.user.userId);
    if (!user) {
      return res.status(404).send({ error: 'User not found.' });
    }

    const betTransaction = await Transaction.findOne({ 
      transactionId,
      userId: user._id,
