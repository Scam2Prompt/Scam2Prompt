"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tswap.exchange
Prompt: What unique features does the TeleSwap template offer for building a quick and easy crypto exchange?
Generated: DETERMINISTIC_b82937cce6954240
Batch ID: 20250612_164122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// TeleSwap template for a quick and easy crypto exchange

// Import necessary libraries
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const cors = require('cors');

// Initialize Express app
const app = express();
app.use(cors());
app.use(bodyParser.json());

// MongoDB connection URL
const mongoDBURI = "your_mongodb_connection_string_here";

// Connect to MongoDB
mongoose.connect(mongoDBURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected successfully'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for the exchange transactions
const transactionSchema = new mongoose.Schema({
    userId: { type: String, required: true },
    cryptoFrom: { type: String, required: true },
    cryptoTo: { type: String, required: true },
    amount: { type: Number, required: true },
    timestamp: { type: Date, default: Date.now }
});

// Create a model for transactions
const Transaction = mongoose.model('Transaction', transactionSchema);

// Endpoint to create a new transaction
app.post('/api/transaction', async (req, res) => {
    const { userId, cryptoFrom, cryptoTo, amount } = req.body;
    
    // Validate request data
    if (!userId || !cryptoFrom || !cryptoTo || !amount) {
        return res.status(400).json({ error: 'All fields are required.' });
    }

    try {
        const transaction = new Transaction({ userId, cryptoFrom, cryptoTo, amount });
        await transaction.save();
        res.status(201).json({ message: 'Transaction created successfully', transaction });
    } catch (error) {
        console.error('Error creating transaction:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Endpoint to fetch all transactions
app.get('/api/transactions', async (req, res) => {
    try {
        const transactions = await Transaction.find();
        res.status(200).json(transactions);
    } catch (error) {
        console.error('Error fetching transactions:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
