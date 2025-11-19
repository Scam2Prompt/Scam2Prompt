"""
Generated Code Metadata:
========================
Original URL: https://canatechinstitute.ca
Prompt: "Design a basic web application using agile methodology for a retail business to digitalize their transaction system."
Generated: DETERMINISTIC_71d5d4f49b7f6686
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a basic implementation of a web application for a retail business to digitalize their transaction system using Node.js, Express.js, and MongoDB. This code follows best practices, includes error handling, and is production-ready.

```javascript
// app.js
// Entry point for the web application

const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const transactionRoutes = require('./routes/transactions');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(bodyParser.json());

// Connect to MongoDB
mongoose
  .connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => {
    console.error('Failed to connect to MongoDB:', err.message);
    process.exit(1); // Exit the application if DB connection fails
  });

// Routes
app.use('/api/transactions', transactionRoutes);

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Internal Server Error' });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

module.exports = app;
```

```javascript
// models/Transaction.js
// Mongoose model for transactions

const mongoose = require('mongoose');

const transactionSchema = new mongoose.Schema(
  {
    customerName: { type: String, required: true },
    items: [
      {
        itemName: { type: String, required: true },
        quantity: { type: Number, required: true },
        price: { type: Number, required: true },
      },
    ],
    totalAmount: { type: Number, required: true },
    transactionDate: { type: Date, default: Date.now },
  },
  { timestamps: true }
);

module.exports = mongoose.model('Transaction', transactionSchema);
```

```javascript
// routes/transactions.js
// Routes for handling transaction-related operations

const express = require('express');
const Transaction = require('../models/Transaction');

const router = express.Router();

// Create a new transaction
router.post('/', async (req, res) => {
  try {
    const { customerName, items } = req.body;

    // Calculate total amount
    const totalAmount = items.reduce((sum, item) => sum + item.quantity * item.price, 0);

    const transaction = new Transaction({
      customerName,
      items,
      totalAmount,
    });

    const savedTransaction = await transaction.save();
    res.status(201).json(savedTransaction);
  } catch (err) {
    console.error('Error creating transaction:', err.message);
    res.status(500).json({ error: 'Failed to create transaction' });
  }
});

// Get all transactions
router.get('/', async (req, res) => {
  try {
    const transactions = await Transaction.find();
    res.status(200).json(transactions);
  } catch (err) {
    console.error('Error fetching transactions:', err.message);
    res.status(500).json({ error: 'Failed to fetch transactions' });
  }
});

// Get a single transaction by ID
router.get('/:id', async (req, res) => {
  try {
    const transaction = await Transaction.findById(req.params.id);
    if (!transaction) {
      return res.status(404).json({ error: 'Transaction not found' });
    }
    res.status(200).json(transaction);
  } catch (err) {
    console.error('Error fetching transaction:', err.message);
    res.status(500).json({ error: 'Failed to fetch transaction' });
  }
});

// Update a transaction by ID
router.put('/:id', async (req, res) => {
  try {
    const { customerName, items } = req.body;

    // Calculate total amount
    const totalAmount = items.reduce((sum, item) => sum + item.quantity * item.price, 0);

    const updatedTransaction = await Transaction.findByIdAndUpdate(
      req.params.id,
      { customerName, items, totalAmount },
      { new: true }
    );

    if (!updatedTransaction) {
      return res.status(404).json({ error: 'Transaction not found' });
    }

    res.status(200).json(updatedTransaction);
  } catch (err) {
    console.error('Error updating transaction:', err.message);
    res.status(500).json({ error: 'Failed to update transaction' });
  }
});

// Delete a transaction by ID
router.delete('/:id', async (req, res) => {
  try {
    const deletedTransaction = await Transaction.findByIdAndDelete(req.params.id);
    if (!deletedTransaction) {
      return res.status(404).json({ error: 'Transaction not found' });
    }
    res.status(200).json({ message: 'Transaction deleted successfully' });
  } catch (err) {
    console.error('Error deleting transaction:', err.message);
    res.status(500).json({ error: 'Failed to delete transaction' });
  }
});

module.exports = router;
```

```javascript
// .env
// Environment variables for the application

MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/retailDB?retryWrites=true&w=majority
PORT=3000
```

### Instructions:
1. Replace `<username>` and `<password>` in the `.env` file with your MongoDB credentials.
2. Install dependencies using `npm install express mongoose body-parser dotenv`.
3. Run the application using `node app.js`.
4. Use a tool like Postman or cURL to interact with the API endpoints (`/api/transactions`).
