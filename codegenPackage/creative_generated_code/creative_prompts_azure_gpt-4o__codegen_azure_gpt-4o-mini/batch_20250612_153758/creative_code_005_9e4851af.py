"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbiscan-arbiscan.github.io
Prompt: Develop a Node.js application that queries the Arbiscan API for detailed token information, including contract addresses, token holders, and transfer history.
Generated: DETERMINISTIC_9e4851afa7b42920
Batch ID: 20250612_153758
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.arbiscan.io/api": {
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
// Import required modules
const express = require('express');
const axios = require('axios');
const app = express();

// Configuration
const ARBISCAN_API_KEY = 'YOUR_ARBISCAN_API_KEY'; // Replace with your Arbiscan API key
const ARBISCAN_API_URL = 'https://api.arbiscan.io/api';

// Middleware to parse JSON requests
app.use(express.json());

// Helper function to query the Arbiscan API
const queryArbiscanAPI = async (module, action, params = {}) => {
    try {
        const response = await axios.get(ARBISCAN_API_URL, {
            params: {
                module,
                action,
                ...params,
                apikey: ARBISCAN_API_KEY,
            },
        });
        
        // Check for API response success
        if (response.data.status !== '1') {
            throw new Error(response.data.message);
        }
        
        return response.data.result;
    } catch (error) {
        console.error('Error querying Arbiscan API:', error.message);
        throw new Error('Failed to fetch data from Arbiscan API.');
    }
};

// Route to get token information by contract address
app.get('/token/:contractAddress', async (req, res) => {
    const { contractAddress } = req.params;

    try {
        const tokenInfo = await queryArbiscanAPI('token', 'getTokenInfo', { contractaddress: contractAddress });
        const tokenHolders = await queryArbiscanAPI('token', 'getTokenHolders', { contractaddress: contractAddress });
        const transferHistory = await queryArbiscanAPI('account', 'tokentx', { contractaddress: contractAddress });

        // Respond with the aggregated data
        res.json({
            tokenInfo,
            tokenHolders,
            transferHistory,
        });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```
