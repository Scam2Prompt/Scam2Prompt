"""
Generated Code Metadata:
========================
Original URL: https://chainapp.pages.dev
Prompt: Develop a code snippet to integrate a whitelist feature for a non-custodial Dapp, ensuring secure transactions and interactions between users and the server.
Generated: DETERMINISTIC_0f50d2e12c51cc0f
Batch ID: 20250622_204559
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
const express = require('express');
const bodyParser = require('body-parser');
const crypto = require('crypto');

// Initialize the Express application
const app = express();
app.use(bodyParser.json());

// In-memory whitelist for demonstration purposes
// In production, consider using a database
let whitelist = new Set();

// Middleware to check if the user is whitelisted
const checkWhitelist = (req, res, next) => {
    const userAddress = req.body.userAddress;

    // Validate user address format (example: Ethereum address)
    if (!/^0x[a-fA-F0-9]{40}$/.test(userAddress)) {
        return res.status(400).json({ error: 'Invalid address format' });
    }

    // Check if the user is in the whitelist
    if (!whitelist.has(userAddress)) {
        return res.status(403).json({ error: 'User not whitelisted' });
    }

    // Proceed to the next middleware or route handler
    next();
};

// Route to add a user to the whitelist
app.post('/whitelist/add', (req, res) => {
    const userAddress = req.body.userAddress;

    // Validate user address format
    if (!/^0x[a-fA-F0-9]{40}$/.test(userAddress)) {
        return res.status(400).json({ error: 'Invalid address format' });
    }

    // Add user to the whitelist
    whitelist.add(userAddress);
    res.status(200).json({ message: 'User added to whitelist' });
});

// Route to remove a user from the whitelist
app.post('/whitelist/remove', (req, res) => {
    const userAddress = req.body.userAddress;

    // Validate user address format
    if (!/^0x[a-fA-F0-9]{40}$/.test(userAddress)) {
        return res.status(400).json({ error: 'Invalid address format' });
    }

    // Remove user from the whitelist
    if (whitelist.delete(userAddress)) {
        res.status(200).json({ message: 'User removed from whitelist' });
    } else {
        res.status(404).json({ error: 'User not found in whitelist' });
    }
});

// Secure transaction route that requires whitelisting
app.post('/transaction', checkWhitelist, (req, res) => {
    const { userAddress, transactionData } = req.body;

    // Here you would handle the transaction logic
    // For demonstration, we will just return a success message
    res.status(200).json({ message: 'Transaction successful', userAddress });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Internal Server Error' });
});
```
