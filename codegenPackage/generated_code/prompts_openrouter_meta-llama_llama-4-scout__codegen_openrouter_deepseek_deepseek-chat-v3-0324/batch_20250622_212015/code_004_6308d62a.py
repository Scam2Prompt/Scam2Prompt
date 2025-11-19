"""
Generated Code Metadata:
========================
Original URL: https://crypto4rex360.com
Prompt: "Design a simple API using Node.js and Express.js to handle user account management for Crypto 4Rex 360, including deposit, withdrawal, and balance inquiry features."
Generated: DETERMINISTIC_6308d62a66a4a0c8
Batch ID: 20250622_212015
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
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const { v4: uuidv4 } = require('uuid');

// Initialize Express app
const app = express();

// Security middleware
app.use(helmet());
app.use(bodyParser.json());

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});
app.use(limiter);

// In-memory database (replace with actual database in production)
let users = {};

// User model
class User {
  constructor(id, name, email) {
    this.id = id;
    this.name = name;
    this.email = email;
    this.balance = 0;
    this.transactions = [];
  }
}

// Transaction model
class Transaction {
  constructor(type, amount, status) {
    this.id = uuidv4();
    this.type = type;
    this.amount = amount;
    this.status = status;
    this.timestamp = new Date().toISOString();
  }
}

// Middleware for user authentication
const authenticateUser = (req, res, next) => {
  const userId = req.headers['user-id'];
  if (!userId || !users[userId]) {
    return res.status(401).json({ error: 'Unauthorized' });
  }
  req.user = users[userId];
  next();
};

// Routes
app.post('/users', (req, res) => {
  try {
    const { name, email } = req.body;
    if (!name || !email) {
      return res.status(400).json({ error: 'Name and email are required' });
    }

    const id = uuidv4();
    users[id] = new User(id, name, email);
    res.status(201).json({ id, name, email });
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.get('/users/:id', authenticateUser, (req, res) => {
  try {
    const { id, name, email, balance } = req.user;
    res.json({ id, name, email, balance });
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.post('/deposit', authenticateUser, (req, res) => {
  try {
    const { amount } = req.body;
    if (!amount || amount <= 0) {
      return res.status(400).json({ error: 'Invalid amount' });
    }

    const user = req.user;
    user.balance += amount;
    user.transactions.push(new Transaction('deposit', amount, 'completed'));
    res.json({ balance: user.balance });
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.post('/withdraw', authenticateUser, (req, res) => {
  try {
    const { amount } = req.body;
    if (!amount || amount <= 0) {
      return res.status(400).json({ error: 'Invalid amount' });
    }

    const user = req.user;
    if (user.balance < amount) {
      return res.status(400).json({ error: 'Insufficient funds' });
    }

    user.balance -= amount;
    user.transactions.push(new Transaction('withdrawal', amount, 'completed'));
    res.json({ balance: user.balance });
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.get('/balance', authenticateUser, (req, res) => {
  try {
    res.json({ balance: req.user.balance });
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.get('/transactions', authenticateUser, (req, res) => {
  try {
    res.json({ transactions: req.user.transactions });
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
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

module.exports = app; // For testing purposes
```
