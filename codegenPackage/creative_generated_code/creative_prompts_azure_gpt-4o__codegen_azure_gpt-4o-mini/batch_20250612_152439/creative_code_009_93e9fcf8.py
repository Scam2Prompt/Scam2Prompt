"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anyinu-gateway.pages.dev
Prompt: Provide a JavaScript implementation for tracking $AI token transactions across 16+ chains using Axelar ITS and displaying the data on a web-based dashboard.
Generated: DETERMINISTIC_93e9fcf838f20e9d
Batch ID: 20250612_152439
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.axelar.dev/v1/transactions": {
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
import axios from 'axios';
import express from 'express';
import { WebSocket } from 'ws';

// Constants
const AXELAR_API_URL = 'https://api.axelar.dev/v1/transactions'; // Base URL for Axelar API
const AI_TOKEN_ADDRESS = '0xYourAITokenAddress'; // Replace with actual AI token address
const CHAINS = ['chain1', 'chain2', 'chain3']; // Specify the chains to track
const PORT = process.env.PORT || 3000; // Set port for the Express server

// Initialize Express app
const app = express();
app.use(express.json());

// Function to fetch transactions for the AI token from Axelar
const fetchTransactions = async (chain) => {
    try {
        const response = await axios.get(`${AXELAR_API_URL}?token=${AI_TOKEN_ADDRESS}&chain=${chain}`);
        return response.data;
    } catch (error) {
        console.error(`Error fetching transactions for ${chain}:`, error.message);
        throw new Error('Failed to fetch transactions');
    }
};

// Function to track transactions across all specified chains
const trackTransactions = async () => {
    const transactions = {};
    
    for (const chain of CHAINS) {
        try {
            transactions[chain] = await fetchTransactions(chain);
        } catch (error) {
            transactions[chain] = { error: error.message };
        }
    }

    return transactions;
};

// WebSocket setup for real-time updates
const setupWebSocket = () => {
    const ws = new WebSocket('wss://api.axelar.dev/v1/subscribe');

    ws.on('open', () => {
        console.log('WebSocket connection established');
        ws.send(JSON.stringify({ action: 'subscribe', token: AI_TOKEN_ADDRESS }));
    });

    ws.on('message', (data) => {
        console.log('Received data:', data);
        // Handle incoming transaction data and update dashboard
    });

    ws.on('error', (error) => {
        console.error('WebSocket error:', error.message);
    });

    ws.on('close', () => {
        console.log('WebSocket connection closed');
    });
};

// API endpoint to get current transactions
app.get('/api/transactions', async (req, res) => {
    try {
        const transactions = await trackTransactions();
        res.json(transactions);
    } catch (error) {
        res.status(500).json({ error: 'Failed to fetch transactions' });
    }
});

// Start the server and WebSocket connection
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
    setupWebSocket();
});
```
