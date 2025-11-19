"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fudthepug.pages.dev
Prompt: Develop a simple API endpoint in Node.js that allows users to buy Simon’s Cat Token ($CAT) and logs the transaction details.
Generated: DETERMINISTIC_c5f4d17c85982b22
Batch ID: 20250612_163902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Required dependencies
const express = require('express'); // Web framework
const bodyParser = require('body-parser'); // Middleware for parsing request body
const fs = require('fs'); // File system module for logging
const path = require('path'); // Module for handling file and directory paths

// Create an instance of Express app
const app = express();

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// Set the port for the server
const PORT = process.env.PORT || 3000;

// Transaction logging function
const logTransaction = (transactionDetails) => {
    const logFilePath = path.join(__dirname, 'transactions.log');
    const logEntry = `${new Date().toISOString()} - ${JSON.stringify(transactionDetails)}\n`;
    
    // Append the transaction to the log file
    fs.appendFile(logFilePath, logEntry, (err) => {
        if (err) {
            console.error('Error logging transaction:', err);
        }
    });
};

// API endpoint to buy Simon's Cat Token ($CAT)
app.post('/buy-token', (req, res) => {
    const { userId, amount } = req.body;

    // Validate input
    if (!userId || !amount || typeof amount !== 'number' || amount <= 0) {
        return res.status(400).json({ error: 'Invalid input. Please provide a valid userId and a positive amount.' });
    }

    // Simulate transaction processing (In production, you would integrate with a payment gateway)
    const transactionDetails = {
        userId,
        amount,
        status: 'success',
        timestamp: new Date().toISOString(),
    };

    // Log the transaction
    logTransaction(transactionDetails);

    // Respond with transaction details
    res.status(201).json({
        message: 'Transaction successful',
        transaction: transactionDetails,
    });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
