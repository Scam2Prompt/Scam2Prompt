"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swanbay.dip.vn
Prompt: Write a Node.js script to handle automatic deposit and withdrawal transactions for an online casino platform like VZ99.
Generated: DETERMINISTIC_1459fb9a20ae9d0c
Batch ID: 20250612_154506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// casinoTransactions.js

const express = require('express');
const bodyParser = require('body-parser');

// Create an express application
const app = express();
app.use(bodyParser.json());

// In-memory storage for user balances (for demonstration purposes)
const userBalances = {};

// Function to validate user input for transactions
const validateTransaction = (userId, amount) => {
    if (!userId || typeof userId !== 'string') {
        throw new Error('Invalid user ID');
    }
    if (typeof amount !== 'number' || amount <= 0) {
        throw new Error('Amount must be a positive number');
    }
};

// Deposit function to add funds to a user's balance
const deposit = (userId, amount) => {
    validateTransaction(userId, amount);

    // Initialize user balance if not present
    if (!userBalances[userId]) {
        userBalances[userId] = 0;
    }
    
    userBalances[userId] += amount;
    return userBalances[userId];
};

// Withdraw function to remove funds from a user's balance
const withdraw = (userId, amount) => {
    validateTransaction(userId, amount);

    // Check if user exists and has sufficient balance
    if (!userBalances[userId] || userBalances[userId] < amount) {
        throw new Error('Insufficient balance');
    }

    userBalances[userId] -= amount;
    return userBalances[userId];
};

// Route for handling deposits
app.post('/deposit', (req, res) => {
    const { userId, amount } = req.body;

    try {
        const newBalance = deposit(userId, amount);
        res.status(200).json({ userId, newBalance });
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

// Route for handling withdrawals
app.post('/withdraw', (req, res) => {
    const { userId, amount } = req.body;

    try {
        const newBalance = withdraw(userId, amount);
        res.status(200).json({ userId, newBalance });
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Casino transactions server running on port ${PORT}`);
});
```

This code represents the complete Node.js script to handle automatic deposit and withdrawal transactions for an online casino platform. It includes error handling, input validation, and maintains user balances in memory. Please ensure to implement persistent storage for a production-ready solution.
