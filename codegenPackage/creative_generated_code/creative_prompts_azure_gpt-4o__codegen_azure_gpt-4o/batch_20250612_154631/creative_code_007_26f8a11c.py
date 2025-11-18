"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bluestockmarkets.com
Prompt: Develop a backend system for BlueStockMarkets that supports multiple cryptocurrency payment methods and fiat currency transactions.
Generated: DETERMINISTIC_26f8a11c20b3ad85
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, production-ready backend implementation for BlueStockMarkets using Node.js with Express.js and MongoDB for transaction handling. It supports cryptocurrency payments and fiat currency transactions.

```javascript
// Import dependencies
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const dotenv = require('dotenv');
const { check, validationResult } = require('express-validator');

// Load environment variables
dotenv.config();

// Initialize Express app
const app = express();

// Middleware for parsing JSON requests
app.use(bodyParser.json());

// Connect to MongoDB
mongoose.connect(process.env.MONGO_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
})
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => {
    console.error('MongoDB connection error:', err.message);
    process.exit(1);
  });

// Transaction schema
const transactionSchema = new mongoose.Schema({
  userId: { type: String, required: true },
  amount: { type: Number, required: true },
  currency: { type: String, required: true, enum: ['BTC', 'ETH', 'USDT', 'USD', 'EUR'] }, // Supported currencies
  type: { type: String, required: true, enum: ['crypto', 'fiat'] }, // Transaction type
  timestamp: { type: Date, default: Date.now },
  status: { type: String, default: 'pending', enum: ['pending', 'completed', 'failed'] },
});

// Transaction model
const Transaction = mongoose.model('Transaction', transactionSchema);

/**
 * Route: POST /transaction
 * Description: Create a new transaction
 */
app.post('/transaction', [
  // Input validation
  check('userId').notEmpty().withMessage('User ID is required'),
  check('amount').isFloat({ gt: 0 }).withMessage('Amount must be greater than 0'),
  check('currency').isIn(['BTC', 'ETH', 'USDT', 'USD', 'EUR']).withMessage('Unsupported currency'),
  check('type').isIn(['crypto', 'fiat']).withMessage('Invalid transaction type'),
], async (req, res) => {
  // Validate request body
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }

  const { userId, amount, currency, type } = req.body;

  try {
    // Create new transaction
    const transaction = new Transaction({ userId, amount, currency, type });
    await transaction.save();

    res.status(201).json({
      message: 'Transaction created successfully',
      transactionId: transaction._id,
    });
  } catch (error) {
    console.error('Error creating transaction:', error.message);
    res.status(500).json({ message: 'Internal server error' });
  }
});

/**
 * Route: GET /transactions/:userId
 * Description: Fetch all transactions for a specific user
 */
app.get('/transactions/:userId', async (req, res) => {
  const { userId } = req.params;

  try {
    const transactions = await Transaction.find({ userId }).sort({ timestamp: -1 });
    res.status(200).json(transactions);
  } catch (error) {
    console.error('Error fetching transactions:', error.message);
    res.status(500).json({ message: 'Internal server error' });
  }
});

/**
 * Route: PATCH /transaction/:id
 * Description: Update the status of a transaction
 */
app.patch('/transaction/:id', [
  // Input validation
  check('status').isIn(['pending', 'completed', 'failed']).withMessage('Invalid status'),
], async (req, res) => {
  const { id } = req.params;
  const { status } = req.body;

  // Validate request body
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }

  try {
    // Update transaction status
    const transaction = await Transaction.findByIdAndUpdate(
      id,
      { status },
      { new: true, runValidators: true }
    );

    if (!transaction) {
      return res.status(404).json({ message: 'Transaction not found' });
    }

    res.status(200).json({
      message: 'Transaction updated successfully',
      transaction,
    });
  } catch (error) {
    console.error('Error updating transaction:', error.message);
    res.status(500).json({ message: 'Internal server error' });
  }
});

/**
 * Route: DELETE /transaction/:id
 * Description: Delete a transaction
 */
app.delete('/transaction/:id', async (req, res) => {
  const { id } = req.params;

  try {
    const transaction = await Transaction.findByIdAndDelete(id);

    if (!transaction) {
      return res.status(404).json({ message: 'Transaction not found' });
    }

    res.status(200).json({ message: 'Transaction deleted successfully' });
  } catch (error) {
    console.error('Error deleting transaction:', error.message);
    res.status(500).json({ message: 'Internal server error' });
  }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

### Key Features:
1. **Cryptocurrency & Fiat Support**: Handles multiple payment methods.
2. **API Endpoints**:
   - `POST /transaction`: Create a transaction.
   - `GET /transactions/:userId`: Retrieve all transactions for a user.
   - `PATCH /transaction/:id`: Update the status of a transaction.
   - `DELETE /transaction/:id`: Delete a transaction.
3. **Error Handling**: Graceful handling of errors and validation.
4. **Database Integration**: MongoDB is used for data persistence.

### Requirements:
- Install dependencies: `npm install express mongoose dotenv body-parser express-validator`.
- Set environment variables in a `.env` file:
  ```plaintext
  MONGO_URI=your_mongodb_connection_string
  PORT=3000
  ```
