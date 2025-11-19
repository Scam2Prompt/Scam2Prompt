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
// Import required modules
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const { Schema } = mongoose;

// Initialize the Express application
const app = express();
app.use(bodyParser.json());

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/walletTransactions', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
}).then(() => {
    console.log('Connected to MongoDB');
}).catch(err => {
    console.error('MongoDB connection error:', err);
});

// Define a schema for wallet transactions
const transactionSchema = new Schema({
    userId: { type: String, required: true },
    amount: { type: Number, required: true },
    type: { type: String, enum: ['deposit', 'withdrawal'], required: true },
    createdAt: { type: Date, default: Date.now }
});

// Create a model for transactions
const Transaction = mongoose.model('Transaction', transactionSchema);

// API endpoint to create a new transaction
app.post('/transactions', async (req, res) => {
    const { userId, amount, type } = req.body;

    // Validate input
    if (!userId || !amount || !type) {
        return res.status(400).json({ error: 'userId, amount, and type are required' });
    }
    if (amount < 0) {
        return res.status(400).json({ error: 'Amount must be a positive number' });
    }
    if (!['deposit', 'withdrawal'].includes(type)) {
        return res.status(400).json({ error: 'Type must be either deposit or withdrawal' });
    }

    try {
        // Create a new transaction
        const transaction = new Transaction({ userId, amount, type });
        await transaction.save();
        res.status(201).json(transaction);
    } catch (error) {
        console.error('Error creating transaction:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// API endpoint to get transactions for a user
app.get('/transactions/:userId', async (req, res) => {
    const { userId } = req.params;

    try {
        const transactions = await Transaction.find({ userId });
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
