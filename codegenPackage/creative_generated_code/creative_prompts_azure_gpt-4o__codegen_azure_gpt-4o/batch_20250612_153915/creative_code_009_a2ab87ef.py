"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tgdrop.cc
Prompt: Create a backend service in Node.js to handle reward distribution for a TON-based platform, including wallet connection and transaction validation.
Generated: DETERMINISTIC_a2ab87ef10bea567
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const express = require('express'); // Web framework for Node.js
const bodyParser = require('body-parser'); // Middleware to parse incoming requests
const { TonClient } = require('@tonclient/core'); // TON client library
const { libNode } = require('@tonclient/lib-node'); // TON library for Node.js
const dotenv = require('dotenv'); // Environment variable management
const winston = require('winston'); // Logger for error and debugging

// Load environment variables from .env file
dotenv.config();

// Initialize TON client
TonClient.useBinaryLibrary(libNode);
const tonClient = new TonClient({ network: { server_address: process.env.TON_NETWORK_ADDRESS } });

// Create Express application
const app = express();

// Apply middleware
app.use(bodyParser.json()); // Parse JSON request bodies

// Initialize logger
const logger = winston.createLogger({
    level: 'info',
    format: winston.format.json(),
    transports: [
        new winston.transports.Console(),
        new winston.transports.File({ filename: 'app.log' })
    ],
});

// Endpoint to distribute rewards
app.post('/distribute-rewards', async (req, res) => {
    try {
        // Extract request data
        const { walletAddress, amount } = req.body;

        // Basic input validation
        if (!walletAddress || !amount || isNaN(amount)) {
            logger.warn('Invalid input data');
            return res.status(400).json({ error: 'Invalid input data' });
        }

        // Prepare TON transaction payload
        const transactionParams = {
            dest: walletAddress,
            value: amount.toString(),
            bounce: false,
        };

        // Send transaction
        const response = await tonClient.processing.send_message({
            message: transactionParams,
            send_events: false,
        });

        // Validate transaction
        if (!response || !response.transaction) {
            logger.error('Transaction failed');
            return res.status(500).json({ error: 'Transaction failed' });
        }

        logger.info('Transaction successful', { walletAddress, amount });
        return res.status(200).json({ message: 'Rewards distributed successfully', transaction: response.transaction });
    } catch (error) {
        // Handle and log errors
        logger.error('Error during reward distribution', { error: error.message });
        return res.status(500).json({ error: 'Internal server error' });
    }
});

// Handle invalid routes
app.use((req, res) => {
    res.status(404).json({ error: 'Route not found' });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    logger.info(`Server running on port ${PORT}`);
});
```

**Note:** Ensure you create a `.env` file in the root of your project to specify `TON_NETWORK_ADDRESS` and `PORT` values.
