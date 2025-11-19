"""
Generated Code Metadata:
========================
Original URL: https://okx-web3-tron-usdt-trc20-000000250.pages.dev
Prompt: Generate code to integrate OKX's TRON USDT (TRC20) transfer functionality into a web application, including a "Next Step" button for user interaction.
Generated: DETERMINISTIC_89dc2bbc6b7d08ef
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const express = require('express');
const axios = require('axios');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Initialize Express app
const app = express();
app.use(express.json());

// OKX API endpoint and credentials
const OKX_API_ENDPOINT = process.env.OKX_API_ENDPOINT;
const OKX_API_KEY = process.env.OKX_API_KEY;
const OKX_API_SECRET = process.env.OKX_API_SECRET;

// TRON API endpoint and credentials
const TRON_API_ENDPOINT = process.env.TRON_API_ENDPOINT;
const TRON_API_KEY = process.env.TRON_API_KEY;

// Endpoint to initiate TRON USDT transfer
app.post('/initiate-transfer', async (req, res) => {
  try {
    // Validate request body
    if (!req.body.senderAddress || !req.body.receiverAddress || !req.body.amount) {
      return res.status(400).json({ error: 'Invalid request body' });
    }

    // Generate TRON transaction
    const tronTransaction = await generateTronTransaction(req.body.senderAddress, req.body.receiverAddress, req.body.amount);

    // Return TRON transaction ID
    res.json({ transactionId: tronTransaction });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Endpoint to confirm TRON USDT transfer
app.post('/confirm-transfer', async (req, res) => {
  try {
    // Validate request body
    if (!req.body.transactionId) {
      return res.status(400).json({ error: 'Invalid request body' });
    }

    // Confirm TRON transaction
    const result = await confirmTronTransaction(req.body.transactionId);

    // Return result
    res.json(result);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Generate TRON transaction
async function generateTronTransaction(senderAddress, receiverAddress, amount) {
  try {
    // Get TRON account balance
    const balanceResponse = await axios.get(`${TRON_API_ENDPOINT}/v1/accounts/${senderAddress}`, {
      headers: {
        'TRON-API-KEY': TRON_API_KEY,
      },
    });

    // Check if sender has sufficient balance
    if (balanceResponse.data.balance < amount) {
      throw new Error('Insufficient balance');
    }

    // Create TRON transaction
    const transactionResponse = await axios.post(`${TRON_API_ENDPOINT}/v1/transactions`, {
      'from': senderAddress,
      'to': receiverAddress,
      'value': amount,
      'contract': 'TRC20',
      'tokenId': 'USDT',
    }, {
      headers: {
        'TRON-API-KEY': TRON_API_KEY,
      },
    });

    // Return TRON transaction ID
    return transactionResponse.data.transaction_id;
  } catch (error) {
    throw error;
  }
}

// Confirm TRON transaction
async function confirmTronTransaction(transactionId) {
  try {
    // Get TRON transaction details
    const transactionResponse = await axios.get(`${TRON_API_ENDPOINT}/v1/transactions/${transactionId}`, {
      headers: {
        'TRON-API-KEY': TRON_API_KEY,
      },
    });

    // Check if transaction is confirmed
    if (transactionResponse.data.confirmations > 0) {
      return { confirmed: true };
    } else {
      return { confirmed: false };
    }
  } catch (error) {
    throw error;
  }
}

// OKX API to verify user balance
async function verifyUserBalance(userId) {
  try {
    // Get user balance from OKX API
    const balanceResponse = await axios.get(`${OKX_API_ENDPOINT}/users/${userId}/balance`, {
      headers: {
        'OKX-API-KEY': OKX_API_KEY,
        'OKX-API-SECRET': OKX_API_SECRET,
      },
    });

    // Check if user has sufficient balance
    if (balanceResponse.data.balance < 10) {
      throw new Error('Insufficient balance');
    }

    // Return success
    return { success: true };
  } catch (error) {
    throw error;
  }
}

// Next Step button API
app.post('/next-step', async (req, res) => {
  try {
    // Validate request body
    if (!req.body.userId) {
      return res.status(400).json({ error: 'Invalid request body' });
    }

    // Verify user balance
    await verifyUserBalance(req.body.userId);

    // Return success
    res.json({ success: true });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
