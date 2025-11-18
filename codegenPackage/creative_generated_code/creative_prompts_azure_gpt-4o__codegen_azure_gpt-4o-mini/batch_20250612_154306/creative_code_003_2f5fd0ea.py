"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://develop2022.d3fflw0d8k607c.amplifyapp.com
Prompt: Provide an example of using PiBridge to create a decentralized application (dApp) within the Pi ecosystem.
Generated: DETERMINISTIC_2f5fd0eafa978249
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const PiBridge = require('pibridge'); // Assuming a library for PiBridge exists
const express = require('express');
const bodyParser = require('body-parser');

// Initialize the Express application
const app = express();
app.use(bodyParser.json());

// Define your PiBridge configuration
const pibridgeConfig = {
    accessToken: 'YOUR_ACCESS_TOKEN', // Replace with your Pi Network access token
    network: 'testnet' // Change to 'mainnet' for production
};

// Initialize PiBridge with the configuration
const piBridge = new PiBridge(pibridgeConfig);

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack); // Log the error stack for debugging
    res.status(500).send({ error: 'Something went wrong!' }); // Send a generic error response
});

// Endpoint to submit a transaction
app.post('/submitTransaction', async (req, res) => {
    const { recipientAddress, amount } = req.body;

    // Validate input
    if (!recipientAddress || !amount) {
        return res.status(400).send({ error: 'Recipient address and amount are required.' });
    }

    try {
        // Create a new transaction
        const transaction = await piBridge.createTransaction({
            to: recipientAddress,
            value: amount,
            currency: 'Pi' // Specify the currency
        });

        // Send the transaction to the Pi network
        const result = await piBridge.sendTransaction(transaction);

        // Respond with the transaction result
        res.status(200).send({ success: true, transactionId: result.transactionId });
    } catch (error) {
        // Handle errors during transaction creation or sending
        console.error('Transaction error:', error);
        res.status(500).send({ error: 'Failed to submit transaction.' });
    }
});

// Endpoint to check transaction status
app.get('/transactionStatus/:transactionId', async (req, res) => {
    const { transactionId } = req.params;

    try {
        // Retrieve transaction status
        const status = await piBridge.getTransactionStatus(transactionId);
        res.status(200).send({ transactionId, status });
    } catch (error) {
        console.error('Error fetching transaction status:', error);
        res.status(500).send({ error: 'Could not retrieve transaction status.' });
    }
});

// Start the Express server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

**Note**: This code assumes the existence of a `pibridge` library and its methods. Please ensure to replace placeholders, such as the access token, with actual values and verify that the library methods align with the actual implementation.
