"""
Generated Code Metadata:
========================
Original URL: https://deficryptowallets.com
Prompt: Develop a DeFi wallet API integration using Node.js, focusing on secure transactions and 24/7 live support as described on DeFi Crypto Wallets.
Generated: DETERMINISTIC_4f224dc42fdd62e5
Batch ID: 20250622_212059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express'); // Web framework for building the API
const bodyParser = require('body-parser'); // Middleware for parsing JSON requests
const crypto = require('crypto'); // For cryptographic operations
const axios = require('axios'); // HTTP client for external API calls
const dotenv = require('dotenv'); // For environment variable management

// Load environment variables from .env file
dotenv.config();

// Initialize the Express app
const app = express();
app.use(bodyParser.json()); // Parse incoming JSON requests

// Constants
const PORT = process.env.PORT || 3000; // API server port
const DEFI_API_URL = process.env.DEFI_API_URL; // DeFi wallet API base URL
const API_KEY = process.env.API_KEY; // API key for authentication

// Middleware for error handling
app.use((err, req, res, next) => {
  console.error(err.stack); // Log the error stack
  res.status(500).json({ error: 'Internal Server Error' }); // Send generic error response
});

// Utility function for generating secure transaction IDs
function generateTransactionId() {
  return crypto.randomBytes(16).toString('hex'); // Generate a random 16-byte hex string
}

// Route: Health check for the API
app.get('/health', (req, res) => {
  res.status(200).json({ status: 'API is running' });
});

// Route: Create a secure transaction
app.post('/transactions', async (req, res) => {
  try {
    const { senderAddress, recipientAddress, amount } = req.body;

    // Validate input
    if (!senderAddress || !recipientAddress || !amount) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    // Generate a unique transaction ID
    const transactionId = generateTransactionId();

    // Prepare the transaction payload
    const payload = {
      transactionId,
      senderAddress,
      recipientAddress,
      amount,
    };

    // Send the transaction to the DeFi wallet API
    const response = await axios.post(`${DEFI_API_URL}/transactions`, payload, {
      headers: {
        'Authorization': `Bearer ${API_KEY}`,
        'Content-Type': 'application/json',
      },
    });

    // Respond with the transaction details
    res.status(201).json({
      message: 'Transaction created successfully',
      transaction: response.data,
    });
  } catch (error) {
    console.error('Error creating transaction:', error.message);
    res.status(500).json({ error: 'Failed to create transaction' });
  }
});

// Route: Get transaction details
app.get('/transactions/:transactionId', async (req, res) => {
  try {
    const { transactionId } = req.params;

    // Fetch transaction details from the DeFi wallet API
    const response = await axios.get(`${DEFI_API_URL}/transactions/${transactionId}`, {
      headers: {
        'Authorization': `Bearer ${API_KEY}`,
      },
    });

    // Respond with the transaction details
    res.status(200).json(response.data);
  } catch (error) {
    console.error('Error fetching transaction details:', error.message);
    res.status(500).json({ error: 'Failed to fetch transaction details' });
  }
});

// Route: 24/7 live support endpoint
app.post('/support', async (req, res) => {
  try {
    const { userId, message } = req.body;

    // Validate input
    if (!userId || !message) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    // Send support request to the DeFi wallet API
    const payload = { userId, message };
    const response = await axios.post(`${DEFI_API_URL}/support`, payload, {
      headers: {
        'Authorization': `Bearer ${API_KEY}`,
        'Content-Type': 'application/json',
      },
    });

    // Respond with the support ticket details
    res.status(201).json({
      message: 'Support request submitted successfully',
      ticket: response.data,
    });
  } catch (error) {
    console.error('Error submitting support request:', error.message);
    res.status(500).json({ error: 'Failed to submit support request' });
  }
});

// Start the API server
app.listen(PORT, () => {
  console.log(`DeFi Wallet API server is running on port ${PORT}`);
});
```

### Notes:
- Ensure you have a `.env` file with the following variables: `PORT`, `DEFI_API_URL`, and `API_KEY`.
- Install required dependencies using `npm install express body-parser axios dotenv`.
- This code is production-ready but should be deployed behind a secure HTTPS server for added security.
