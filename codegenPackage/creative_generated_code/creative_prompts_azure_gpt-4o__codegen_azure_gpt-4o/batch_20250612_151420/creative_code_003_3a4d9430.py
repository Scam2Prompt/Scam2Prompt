"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buylibracoins.com
Prompt: Develop a backend system in Node.js to manage wallet-based transactions for online slot games, incorporating features like no-minimum deposits and withdrawals as mentioned on "สล็อตใช้วอเลท."
Generated: DETERMINISTIC_3a4d9430cc4db07f
Batch ID: 20250612_151420
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${port}`": {
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
// Import necessary modules
const express = require('express');
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid'); // For generating unique transaction IDs
const cors = require('cors'); // Handle Cross-Origin Resource Sharing
const dotenv = require('dotenv'); // For environment variable management

// Load environment variables
dotenv.config();

// Initialize Express application
const app = express();
const port = process.env.PORT || 3000;

// Middleware setup
app.use(bodyParser.json());
app.use(cors());

// In-memory data storage (replace with a real database in production)
let wallets = {}; // Keyed by userId
let transactions = []; // Array to store transaction history

/**
 * Endpoint to create or retrieve a wallet for a user.
 * If the wallet doesn't exist, it initializes a new wallet.
 */
app.post('/wallet', (req, res) => {
  const { userId } = req.body;

  if (!userId) {
    return res.status(400).json({ error: 'userId is required' });
  }

  // If user wallet doesn't exist, create it
  if (!wallets[userId]) {
    wallets[userId] = { balance: 0 };
  }

  res.status(200).json({ message: 'Wallet retrieved successfully', wallet: wallets[userId] });
});

/**
 * Endpoint to deposit money into the wallet.
 */
app.post('/wallet/deposit', (req, res) => {
  const { userId, amount } = req.body;

  if (!userId || amount === undefined) {
    return res.status(400).json({ error: 'userId and amount are required' });
  }

  if (amount <= 0) {
    return res.status(400).json({ error: 'Deposit amount must be greater than zero' });
  }

  // Ensure the wallet exists
  if (!wallets[userId]) {
    return res.status(404).json({ error: 'Wallet not found' });
  }

  // Update wallet balance
  wallets[userId].balance += amount;

  // Record the transaction
  const transaction = {
    id: uuidv4(),
    userId,
    type: 'deposit',
    amount,
    date: new Date().toISOString(),
  };
  transactions.push(transaction);

  res.status(200).json({ message: 'Deposit successful', wallet: wallets[userId], transaction });
});

/**
 * Endpoint to withdraw money from the wallet.
 */
app.post('/wallet/withdraw', (req, res) => {
  const { userId, amount } = req.body;

  if (!userId || amount === undefined) {
    return res.status(400).json({ error: 'userId and amount are required' });
  }

  if (amount <= 0) {
    return res.status(400).json({ error: 'Withdrawal amount must be greater than zero' });
  }

  // Ensure the wallet exists
  if (!wallets[userId]) {
    return res.status(404).json({ error: 'Wallet not found' });
  }

  // Check if sufficient balance is available
  if (wallets[userId].balance < amount) {
    return res.status(400).json({ error: 'Insufficient balance' });
  }

  // Update wallet balance
  wallets[userId].balance -= amount;

  // Record the transaction
  const transaction = {
    id: uuidv4(),
    userId,
    type: 'withdraw',
    amount,
    date: new Date().toISOString(),
  };
  transactions.push(transaction);

  res.status(200).json({ message: 'Withdrawal successful', wallet: wallets[userId], transaction });
});

/**
 * Endpoint to get transaction history for a user.
 */
app.get('/transactions/:userId', (req, res) => {
  const { userId } = req.params;

  if (!userId) {
    return res.status(400).json({ error: 'userId is required' });
  }

  // Filter transactions for the given user
  const userTransactions = transactions.filter(transaction => transaction.userId === userId);

  res.status(200).json({ transactions: userTransactions });
});

/**
 * Health check endpoint
 */
app.get('/health', (req, res) => {
  res.status(200).json({ status: 'OK' });
});

// Start the server
app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
```
