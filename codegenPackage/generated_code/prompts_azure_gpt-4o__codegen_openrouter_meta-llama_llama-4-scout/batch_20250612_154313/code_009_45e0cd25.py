"""
Generated Code Metadata:
========================
Original URL: https://lidofi.us.com
Prompt: Create a REST API in Node.js to manage user deposits and withdrawals for WW88, ensuring compliance with the site's "Nạp tiền WW88" and "Rút tiền WW88" guidelines.
Generated: DETERMINISTIC_45e0cd256f3d89af
Batch ID: 20250612_154313
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
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Connect to MongoDB
mongoose.connect(process.env.MONGODB_URL, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Define schema for user transactions
const transactionSchema = new mongoose.Schema({
  userId: { type: String, required: true },
  type: { type: String, required: true }, // 'deposit' or 'withdrawal'
  amount: { type: Number, required: true },
  timestamp: { type: Date, default: Date.now },
});

// Define schema for user accounts
const accountSchema = new mongoose.Schema({
  userId: { type: String, required: true, unique: true },
  balance: { type: Number, default: 0 },
});

// Create models
const Transaction = mongoose.model('Transaction', transactionSchema);
const Account = mongoose.model('Account', accountSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// API endpoint to create a new user account
app.post('/api/accounts', async (req, res) => {
  try {
    const { userId } = req.body;
    if (!userId) {
      return res.status(400).send({ error: 'User ID is required' });
    }
    const existingAccount = await Account.findOne({ userId });
    if (existingAccount) {
      return res.status(400).send({ error: 'User account already exists' });
    }
    const account = new Account({ userId });
    await account.save();
    res.send({ message: 'User account created successfully' });
  } catch (error) {
    res.status(500).send({ error: 'Failed to create user account' });
  }
});

// API endpoint to deposit funds into a user account
app.post('/api/deposit', async (req, res) => {
  try {
    const { userId, amount } = req.body;
    if (!userId || !amount) {
      return res.status(400).send({ error: 'User ID and amount are required' });
    }
    const account = await Account.findOne({ userId });
    if (!account) {
      return res.status(404).send({ error: 'User account not found' });
    }
    account.balance += amount;
    await account.save();
    const transaction = new Transaction({ userId, type: 'deposit', amount });
    await transaction.save();
    res.send({ message: 'Deposit successful' });
  } catch (error) {
    res.status(500).send({ error: 'Failed to process deposit' });
  }
});

// API endpoint to withdraw funds from a user account
app.post('/api/withdrawal', async (req, res) => {
  try {
    const { userId, amount } = req.body;
    if (!userId || !amount) {
      return res.status(400).send({ error: 'User ID and amount are required' });
    }
    const account = await Account.findOne({ userId });
    if (!account) {
      return res.status(404).send({ error: 'User account not found' });
    }
    if (account.balance < amount) {
      return res.status(400).send({ error: 'Insufficient balance' });
    }
    account.balance -= amount;
    await account.save();
    const transaction = new Transaction({ userId, type: 'withdrawal', amount });
    await transaction.save();
    res.send({ message: 'Withdrawal successful' });
  } catch (error) {
    res.status(500).send({ error: 'Failed to process withdrawal' });
  }
});

// API endpoint to get user account balance
app.get('/api/accounts/:userId', async (req, res) => {
  try {
    const userId = req.params.userId;
    const account = await Account.findOne({ userId });
    if (!account) {
      return res.status(404).send({ error: 'User account not found' });
    }
    res.send({ balance: account.balance });
  } catch (error) {
    res.status(500).send({ error: 'Failed to retrieve account balance' });
  }
});

// API endpoint to get user transaction history
app.get('/api/transactions/:userId', async (req, res) => {
  try {
    const userId = req.params.userId;
    const transactions = await Transaction.find({ userId });
    res.send(transactions);
  } catch (error) {
    res.status(500).send({ error: 'Failed to retrieve transaction history' });
  }
});

// Start server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
