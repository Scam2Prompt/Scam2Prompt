"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythnet.com
Prompt: Generate code for a decentralized application (dApp) that leverages PythNet's price feed oracles to display live market data.
Generated: DETERMINISTIC_eab90103405278cf
Batch ID: 20250612_155015
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const Web3 = require('web3');
const Pyth = require('@pythnetwork/client'); // Ensure this package is installed
const express = require('express');

// Initialize the Web3 instance
const web3 = new Web3('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID');

// Initialize the Pyth client
const pythClient = new Pyth.PythClient({
    web3Provider: web3.provider,
});

// Initialize the Express application
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to handle JSON requests
app.use(express.json());

// Endpoint to fetch live market data from PythNet
app.get('/market-data/:symbol', async (req, res) => {
    const { symbol } = req.params;

    try {
        // Fetch price data from PythNet for the specified symbol
        const priceData = await pythClient.getPriceData(symbol);

        // Check if price data is available
        if (!priceData) {
            return res.status(404).json({ error: 'Price data not found for the symbol' });
        }

        // Respond with the price data
        res.json({
            symbol,
            price: priceData.price,
            confidenceInterval: priceData.confidenceInterval,
            timestamp: priceData.publishTime,
        });
    } catch (error) {
        console.error('Error fetching market data:', error);
        res.status(500).json({ error: 'An error occurred while fetching market data' });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```

In this code:
- Replace `YOUR_INFURA_PROJECT_ID` with your actual Infura project ID.
- You need to install dependencies using npm:
  ```bash
  npm install web3 @pythnetwork/client express
  ```
- Make sure to handle CORS and other security practices in a production environment as needed.
