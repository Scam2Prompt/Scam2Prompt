"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btcqee.com
Prompt: Generate code to integrate Bitcoin payment processing into a pledge system using JavaScript.
Generated: DETERMINISTIC_36402f465f134663
Batch ID: 20250612_152600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// PledgePayment.js

// Import necessary libraries
const express = require('express'); // For handling HTTP requests
const bodyParser = require('body-parser'); // To parse incoming request bodies
const bitcoin = require('bitcoin'); // Bitcoin client library
const app = express();

// Middleware setup
app.use(bodyParser.json()); // Parse JSON bodies

// Configuration for Bitcoin client
const bitcoinClient = new bitcoin.Client({
    host: 'localhost',
    port: 8332,
    user: 'yourusername', // Your Bitcoin RPC username
    pass: 'yourpassword', // Your Bitcoin RPC password
});

// API endpoint for processing pledges
app.post('/pledge', async (req, res) => {
    const { amount, address } = req.body;

    // Validate request body
    if (!amount || !address) {
        return res.status(400).json({ error: 'Amount and address are required' });
    }

    // Check if amount is a positive number
    if (amount <= 0) {
        return res.status(400).json({ error: 'Amount must be a positive number' });
    }

    try {
        // Create a payment transaction
        const transaction = await bitcoinClient.sendToAddress(address, amount);
        res.status(200).json({ success: true, transactionId: transaction });
    } catch (error) {
        // Handle errors from the Bitcoin client
        console.error('Error processing Bitcoin payment:', error);
        res.status(500).json({ error: 'Failed to process payment' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Pledge payment system listening on port ${PORT}`);
});

// Export the app for testing or further integration
module.exports = app;
```

### Instructions for Running the Code
1. Ensure you have Node.js installed.
2. Run `npm install express body-parser bitcoin` to install the required dependencies.
3. Replace the Bitcoin RPC `user` and `pass` values with your actual credentials.
4. Start a Bitcoin node that allows RPC connections.
5. Save the code in a file named `PledgePayment.js` and run it using `node PledgePayment.js`.
6. Send a POST request to `/pledge` with a JSON body containing `amount` and `address`.
