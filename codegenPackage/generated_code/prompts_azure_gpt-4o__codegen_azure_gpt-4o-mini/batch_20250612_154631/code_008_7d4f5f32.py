"""
Generated Code Metadata:
========================
Original URL: https://flaredrop.in
Prompt: Create a tutorial for building a decentralized application that leverages Flare's enshrined oracles for real-time data access.
Generated: DETERMINISTIC_7d4f5f32df1f92bf
Batch ID: 20250612_154631
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${port}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://flare-node-url": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
const Web3 = require('web3');
const Flare = require('@flarexyz/flare-sdk'); // Hypothetical Flare SDK
const express = require('express');

// Initialize Express app
const app = express();
const port = process.env.PORT || 3000;

// Initialize Web3 and Flare
const web3 = new Web3(new Web3.providers.HttpProvider('https://flare-node-url'));
const flare = new Flare();

// Middleware to parse JSON requests
app.use(express.json());

// Function to fetch data from Flare's enshrined oracles
async function fetchOracleData(oracleId) {
    try {
        const data = await flare.getOracleData(oracleId);
        return data;
    } catch (error) {
        console.error('Error fetching oracle data:', error);
        throw new Error('Failed to fetch oracle data');
    }
}

// API endpoint to get real-time data from an oracle
app.get('/api/oracle/:id', async (req, res) => {
    const oracleId = req.params.id;

    try {
        const data = await fetchOracleData(oracleId);
        res.status(200).json({
            success: true,
            data: data,
        });
    } catch (error) {
        res.status(500).json({
            success: false,
            message: error.message,
        });
    }
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});

// Graceful shutdown
process.on('SIGINT', () => {
    console.log('Shutting down gracefully...');
    process.exit(0);
});
```

### Notes:
- Ensure you have the necessary packages installed: `npm install web3 @flarexyz/flare-sdk express`.
- Replace `'https://flare-node-url'` with the actual Flare node URL.
- The Flare SDK and its methods are hypothetical; adjust according to the actual SDK documentation.
