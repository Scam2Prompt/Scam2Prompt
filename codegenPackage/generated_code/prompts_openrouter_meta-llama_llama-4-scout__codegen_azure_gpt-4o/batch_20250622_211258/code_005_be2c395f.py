"""
Generated Code Metadata:
========================
Original URL: https://m.zh-imtokenwallet.com
Prompt: Create a RESTful API using Node.js to interact with imToken's blockchain services, enabling users to send and receive digital assets across multiple chains.
Generated: DETERMINISTIC_be2c395f9aa5af76
Batch ID: 20250622_211258
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
const bodyParser = require('body-parser');
const axios = require('axios'); // For making HTTP requests to imToken's blockchain services
require('dotenv').config(); // For environment variables

// Initialize the Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware for parsing JSON requests
app.use(bodyParser.json());

// Base URL for imToken's blockchain services (replace with actual URL)
const IMTOKEN_API_BASE_URL = process.env.IMTOKEN_API_BASE_URL;

// Helper function to handle API requests to imToken
async function callImTokenAPI(endpoint, method, data = {}) {
  try {
    const response = await axios({
      url: `${IMTOKEN_API_BASE_URL}${endpoint}`,
      method: method,
      headers: {
        'Authorization': `Bearer ${process.env.IMTOKEN_API_KEY}`, // Use API key from environment variables
        'Content-Type': 'application/json',
      },
      data: data,
    });
    return response.data;
  } catch (error) {
    console.error('Error calling imToken API:', error.message);
    throw new Error('Failed to interact with blockchain services.');
  }
}

// Route: Send digital assets
app.post('/send', async (req, res) => {
  try {
    const { fromAddress, toAddress, amount, chain } = req.body;

    // Validate request body
    if (!fromAddress || !toAddress || !amount || !chain) {
      return res.status(400).json({ error: 'Missing required fields: fromAddress, toAddress, amount, chain' });
    }

    // Call imToken API to send assets
    const result = await callImTokenAPI('/send', 'POST', {
      fromAddress,
      toAddress,
      amount,
      chain,
    });

    // Respond with the result
    res.status(200).json({ message: 'Transaction successful', data: result });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Route: Receive digital assets (fetch balance)
app.get('/balance/:address/:chain', async (req, res) => {
  try {
    const { address, chain } = req.params;

    // Validate request parameters
    if (!address || !chain) {
      return res.status(400).json({ error: 'Missing required parameters: address, chain' });
    }

    // Call imToken API to fetch balance
    const result = await callImTokenAPI(`/balance/${address}/${chain}`, 'GET');

    // Respond with the result
    res.status(200).json({ message: 'Balance fetched successfully', data: result });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Route: Health check
app.get('/health', (req, res) => {
  res.status(200).json({ message: 'API is running' });
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error('Unhandled error:', err.message);
  res.status(500).json({ error: 'Internal server error' });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

### Notes:
- Replace `IMTOKEN_API_BASE_URL` and `IMTOKEN_API_KEY` with actual values from imToken's API documentation.
- Ensure you have a `.env` file with the required environment variables (`IMTOKEN_API_BASE_URL`, `IMTOKEN_API_KEY`, etc.).
- Install dependencies (`express`, `body-parser`, `axios`, `dotenv`) using `npm install express body-parser axios dotenv`.
