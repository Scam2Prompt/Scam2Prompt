"""
Generated Code Metadata:
========================
Original URL: https://sovads.ru
Prompt: Create a simple web service using Node.js to manage a marketplace for buying and selling Telegram usernames, inspired by SovaDS's offerings.
Generated: DETERMINISTIC_cb2d39351588632a
Batch ID: 20250622_205411
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
const cors = require('cors');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const { v4: uuidv4 } = require('uuid');

// Initialize Express app
const app = express();

// Middleware
app.use(helmet());
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});
app.use(limiter);

// Database connection
mongoose.connect(process.env.MONGODB_URI || 'mongodb://localhost/telegram_marketplace', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  useCreateIndex: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Models
const Username = mongoose.model('Username', new mongoose.Schema({
  id: { type: String, default: uuidv4, unique: true },
  username: { type: String, required: true, unique: true },
  price: { type: Number, required: true },
  sellerId: { type: String, required: true },
  status: { type: String, enum: ['available', 'sold', 'pending'], default: 'available' },
  createdAt: { type: Date, default: Date.now },
  updatedAt: { type: Date, default: Date.now }
}));

const User = mongoose.model('User', new mongoose.Schema({
  id: { type: String, default: uuidv4, unique: true },
  telegramId: { type: String, unique: true },
  balance: { type: Number, default: 0 },
  createdAt: { type: Date, default: Date.now }
}));

const Transaction = mongoose.model('Transaction', new mongoose.Schema({
  id: { type: String, default: uuidv4, unique: true },
  buyerId: { type: String, required: true },
  sellerId: { type: String, required: true },
  usernameId: { type: String, required: true },
  amount: { type: Number, required: true },
  status: { type: String, enum: ['pending', 'completed', 'failed'], default: 'pending' },
  createdAt: { type: Date, default: Date.now }
}));

// Routes
app.get('/api/usernames', async (req, res) => {
  try {
    const usernames = await Username.find({ status: 'available' });
    res.json(usernames);
  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch usernames' });
  }
});

app.post('/api/usernames', async (req, res) => {
  try {
    const { username, price, sellerId } = req.body;
    
    if (!username || !price || !sellerId) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    const newUsername = new Username({ username, price, sellerId });
    await newUsername.save();
    
    res.status(201).json(newUsername);
  } catch (err) {
    if (err.code === 11000) {
      res.status(400).json({ error: 'Username already exists' });
    } else {
      res.status(500).json({ error: 'Failed to create username listing' });
    }
  }
});

app.post('/api/usernames/:id/purchase', async (req, res) => {
  try {
    const { id } = req.params;
    const { buyerId } = req.body;

    if (!buyerId) {
      return res.status(400).json({ error: 'Missing buyer ID' });
    }

    const username = await Username.findOne({ id, status: 'available' });
    if (!username) {
      return res.status(404).json({ error: 'Username not available' });
    }

    const buyer = await User.findOne({ id: buyerId });
    if (!buyer) {
      return res.status(404).json({ error: 'Buyer not found' });
    }

    if (buyer.balance < username.price) {
      return res.status(400).json({ error: 'Insufficient balance' });
    }

    // Start transaction
    const session = await mongoose.startSession();
    session.startTransaction();

    try {
      // Update username status
      username.status = 'sold';
      await username.save({ session });

      // Create transaction record
      const transaction = new Transaction({
        buyerId,
        sellerId: username.sellerId,
        usernameId: username.id,
        amount: username.price,
        status: 'completed'
      });
      await transaction.save({ session });

      // Transfer funds
      const seller = await User.findOne({ id: username.sellerId }).session(session);
      seller.balance += username.price;
      await seller.save({ session });

      buyer.balance -= username.price;
      await buyer.save({ session });

      await session.commitTransaction();
      session.endSession();

      res.json({ message: 'Purchase successful', transaction });
    } catch (err) {
      await session.abortTransaction();
      session.endSession();
      throw err;
    }
  } catch (err) {
    res.status(500).json({ error: 'Failed to process purchase' });
  }
});

app.get('/api/users/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const user = await User.findOne({ id });
    
    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }
    
    res.json(user);
  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch user' });
  }
});

app.post('/api/users/:id/deposit', async (req, res) => {
  try {
    const { id } = req.params;
    const { amount } = req.body;

    if (!amount || amount <= 0) {
      return res.status(400).json({ error: 'Invalid amount' });
    }

    const user = await User.findOne({ id });
    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    user.balance += amount;
    await user.save();

    res.json({ message: 'Deposit successful', newBalance: user.balance });
  } catch (err) {
    res.status(500).json({ error: 'Failed to process deposit' });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

module.exports = app;
```
