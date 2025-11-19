"""
Generated Code Metadata:
========================
Original URL: https://travelobay.com
Prompt: Create a simple API using Node.js and Express to manage user accounts and transactions for an online casino like R7 Casino.
Generated: DETERMINISTIC_4aa6241986641168
Batch ID: 20250622_205412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Required dependencies
const express = require('express');
const bodyParser = require('body-parser');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const mongoose = require('mongoose');
const cors = require('cors');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');

// Initialize Express app
const app = express();

// Environment variables
require('dotenv').config();
const PORT = process.env.PORT || 3000;
const JWT_SECRET = process.env.JWT_SECRET || 'your-secret-key';
const MONGO_URI = process.env.MONGO_URI || 'mongodb://localhost:27017/casino';

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
mongoose.connect(MONGO_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  useCreateIndex: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Mongoose models
const UserSchema = new mongoose.Schema({
  username: { type: String, required: true, unique: true },
  email: { type: String, required: true, unique: true },
  password: { type: String, required: true },
  balance: { type: Number, default: 0 },
  createdAt: { type: Date, default: Date.now }
});

const TransactionSchema = new mongoose.Schema({
  userId: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: true },
  amount: { type: Number, required: true },
  type: { type: String, enum: ['deposit', 'withdrawal', 'bet', 'win'], required: true },
  description: { type: String },
  createdAt: { type: Date, default: Date.now }
});

const User = mongoose.model('User', UserSchema);
const Transaction = mongoose.model('Transaction', TransactionSchema);

// Authentication middleware
const authenticateToken = (req, res, next) => {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];
  
  if (!token) return res.sendStatus(401);

  jwt.verify(token, JWT_SECRET, (err, user) => {
    if (err) return res.sendStatus(403);
    req.user = user;
    next();
  });
};

// Routes

// User registration
app.post('/api/register', async (req, res) => {
  try {
    const { username, email, password } = req.body;
    
    if (!username || !email || !password) {
      return res.status(400).json({ message: 'All fields are required' });
    }

    const existingUser = await User.findOne({ $or: [{ username }, { email }] });
    if (existingUser) {
      return res.status(400).json({ message: 'Username or email already exists' });
    }

    const hashedPassword = await bcrypt.hash(password, 10);
    const user = new User({
      username,
      email,
      password: hashedPassword
    });

    await user.save();
    
    const token = jwt.sign({ userId: user._id, username: user.username }, JWT_SECRET, { expiresIn: '1h' });
    
    res.status(201).json({ token, userId: user._id, username: user.username });
  } catch (error) {
    console.error('Registration error:', error);
    res.status(500).json({ message: 'Internal server error' });
  }
});

// User login
app.post('/api/login', async (req, res) => {
  try {
    const { username, password } = req.body;
    
    if (!username || !password) {
      return res.status(400).json({ message: 'Username and password are required' });
    }

    const user = await User.findOne({ username });
    if (!user) {
      return res.status(401).json({ message: 'Invalid credentials' });
    }

    const passwordMatch = await bcrypt.compare(password, user.password);
    if (!passwordMatch) {
      return res.status(401).json({ message: 'Invalid credentials' });
    }

    const token = jwt.sign({ userId: user._id, username: user.username }, JWT_SECRET, { expiresIn: '1h' });
    
    res.json({ token, userId: user._id, username: user.username, balance: user.balance });
  } catch (error) {
    console.error('Login error:', error);
    res.status(500).json({ message: 'Internal server error' });
  }
});

// Get user balance
app.get('/api/balance', authenticateToken, async (req, res) => {
  try {
    const user = await User.findById(req.user.userId);
    if (!user) {
      return res.status(404).json({ message: 'User not found' });
    }
    res.json({ balance: user.balance });
  } catch (error) {
    console.error('Balance error:', error);
    res.status(500).json({ message: 'Internal server error' });
  }
});

// Deposit funds
app.post('/api/deposit', authenticateToken, async (req, res) => {
  try {
    const { amount } = req.body;
    
    if (!amount || amount <= 0) {
      return res.status(400).json({ message: 'Invalid amount' });
    }

    const user = await User.findById(req.user.userId);
    if (!user) {
      return res.status(404).json({ message: 'User not found' });
    }

    user.balance += amount;
    await user.save();

    const transaction = new Transaction({
      userId: user._id,
      amount,
      type: 'deposit',
      description: `Deposit of $${amount}`
    });
    await transaction.save();

    res.json({ balance: user.balance });
  } catch (error) {
    console.error('Deposit error:', error);
    res.status(500).json({ message: 'Internal server error' });
  }
});

// Withdraw funds
app.post('/api/withdraw', authenticateToken, async (req, res) => {
  try {
    const { amount } = req.body;
    
    if (!amount || amount <= 0) {
      return res.status(400).json({ message: 'Invalid amount' });
    }

    const user = await User.findById(req.user.userId);
    if (!user) {
      return res.status(404).json({ message: 'User not found' });
    }

    if (user.balance < amount) {
      return res.status(400).json({ message: 'Insufficient funds' });
    }

    user.balance -= amount;
    await user.save();

    const transaction = new Transaction({
      userId: user._id,
      amount,
      type: 'withdrawal',
      description: `Withdrawal of $${amount}`
    });
    await transaction.save();

    res.json({ balance: user.balance });
  } catch (error) {
    console.error('Withdrawal error:', error);
    res.status(500).json({ message: 'Internal server error' });
  }
});

// Place a bet
app.post('/api/bet', authenticateToken, async (req, res) => {
  try {
    const { amount } = req.body;
    
    if (!amount || amount <= 0) {
      return res.status(400).json({ message: 'Invalid bet amount' });
    }

    const user = await User.findById(req.user.userId);
    if (!user) {
      return res.status(404).json({ message: 'User not found' });
    }

    if (user.balance < amount) {
      return res.status(400).json({ message: 'Insufficient funds' });
    }

    user.balance -= amount;
    await user.save();

    const transaction = new Transaction({
      userId: user._id,
      amount,
      type: 'bet',
      description: `Bet of $${amount}`
    });
    await transaction.save();

    res.json({ balance: user.balance });
  } catch (error) {
    console.error('Bet error:', error);
    res.status(500).json({ message: 'Internal server error' });
  }
});

// Win payout
app.post('/api/win', authenticateToken, async (req, res) => {
  try {
    const { amount } = req.body;
    
    if (!amount || amount <= 0) {
      return res.status(400).json({ message: 'Invalid win amount' });
    }

    const user = await User.findById(req.user.userId);
    if (!user) {
      return res.status(404).json({ message: 'User not found' });
    }

    user.balance += amount;
    await user.save();

    const transaction = new Transaction({
      userId: user._id,
      amount,
      type: 'win',
      description: `Win of $${amount}`
    });
    await transaction.save();
