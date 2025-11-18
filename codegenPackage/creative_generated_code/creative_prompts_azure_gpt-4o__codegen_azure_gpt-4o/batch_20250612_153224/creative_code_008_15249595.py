"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nuevaciudad.com.co
Prompt: Create a REST API in Node.js to manage user accounts for property owners and tenants, including endpoints for viewing account statements and making payments online, as described in the "Estados de cuenta" and "Pagos PSE" sections of the Nueva Ciudad website.
Generated: DETERMINISTIC_15249595c5b86f1c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid'); // For generating unique IDs

// Initialize the Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware for parsing JSON requests
app.use(bodyParser.json());

// In-memory database (for demonstration purposes)
const users = []; // Array of user accounts (property owners and tenants)
const transactions = []; // Array of payment transactions

// Utility function to find a user by ID
const findUserById = (id) => users.find((user) => user.id === id);

// Utility function to find transactions by user ID
const findTransactionsByUserId = (userId) => transactions.filter((txn) => txn.userId === userId);

// Routes

/**
 * @route   POST /users
 * @desc    Create a new user account
 * @access  Public
 */
app.post('/users', (req, res) => {
    try {
        const { name, role } = req.body; // role can be "property_owner" or "tenant"
        if (!name || !role) {
            return res.status(400).json({ error: 'Name and role are required.' });
        }

        const newUser = {
            id: uuidv4(),
            name,
            role,
            createdAt: new Date(),
        };
        users.push(newUser);
        res.status(201).json(newUser);
    } catch (error) {
        res.status(500).json({ error: 'Internal Server Error.' });
    }
});

/**
 * @route   GET /users/:id/statements
 * @desc    View account statements for a user
 * @access  Public
 */
app.get('/users/:id/statements', (req, res) => {
    try {
        const userId = req.params.id;
        const user = findUserById(userId);

        if (!user) {
            return res.status(404).json({ error: 'User not found.' });
        }

        const userTransactions = findTransactionsByUserId(userId);
        res.status(200).json({
            user,
            statements: userTransactions,
        });
    } catch (error) {
        res.status(500).json({ error: 'Internal Server Error.' });
    }
});

/**
 * @route   POST /users/:id/payments
 * @desc    Make an online payment
 * @access  Public
 */
app.post('/users/:id/payments', (req, res) => {
    try {
        const userId = req.params.id;
        const { amount, description } = req.body;

        if (!amount || isNaN(amount) || amount <= 0) {
            return res.status(400).json({ error: 'Valid payment amount is required.' });
        }

        const user = findUserById(userId);
        if (!user) {
            return res.status(404).json({ error: 'User not found.' });
        }

        const newTransaction = {
            id: uuidv4(),
            userId,
            amount,
            description: description || 'Payment',
            createdAt: new Date(),
        };
        transactions.push(newTransaction);
        res.status(201).json(newTransaction);
    } catch (error) {
        res.status(500).json({ error: 'Internal Server Error.' });
    }
});

/**
 * @route   GET /users
 * @desc    Retrieve all users (for admin or testing purposes)
 * @access  Public
 */
app.get('/users', (req, res) => {
    try {
        res.status(200).json(users);
    } catch (error) {
        res.status(500).json({ error: 'Internal Server Error.' });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

This code provides a REST API for managing user accounts, viewing account statements, and making payments online. You can test it using tools like Postman or cURL, and integrate it with a database for production use.
