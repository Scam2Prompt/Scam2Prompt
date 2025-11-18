"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solxdao.web.app
Prompt: Create a Solana-based application that tracks and displays NFT trading statistics, including TPS and collection-specific metrics, inspired by Tensor's interface.
Generated: DETERMINISTIC_cbd4d30213043248
Batch ID: 20250612_153606
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.mainnet-beta.solana.com": {
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
// Import required libraries
const express = require('express'); // Web framework for API
const fetch = require('node-fetch'); // HTTP client for API requests
const WebSocket = require('ws'); // WebSocket library for real-time data
const dotenv = require('dotenv'); // For environment variable management

// Load environment variables from .env file
dotenv.config();

// Constants for Solana RPC and WebSocket URLs
const SOLANA_RPC_URL = process.env.SOLANA_RPC_URL || 'https://api.mainnet-beta.solana.com';
const SOLANA_WS_URL = process.env.SOLANA_WS_URL || 'wss://api.mainnet-beta.solana.com';

// Initialize Express application
const app = express();
const PORT = process.env.PORT || 3000;

// In-memory store for statistics
let tps = 0; // Transactions per second
let nftMetrics = {}; // Collection-specific metrics

// Helper function to fetch transaction count from Solana RPC
async function fetchTransactionCount() {
  try {
    const response = await fetch(SOLANA_RPC_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        jsonrpc: '2.0',
        id: 1,
        method: 'getRecentPerformanceSamples',
        params: [1],
      }),
    });

    const data = await response.json();
    if (data.result && data.result.length > 0) {
      // Compute TPS from recent performance sample
      return data.result[0].numTransactions / data.result[0].samplePeriodSecs;
    }
    return 0;
  } catch (error) {
    console.error('Error fetching transaction count:', error.message);
    return 0;
  }
}

// WebSocket connection to track NFT trades
function trackNFTTrades() {
  const ws = new WebSocket(SOLANA_WS_URL);

  ws.on('open', () => {
    console.log('WebSocket connection established.');
    // Subscribe to NFT-related transactions (replace with specific subscription details)
    const subscriptionMessage = JSON.stringify({
      jsonrpc: '2.0',
      method: 'logsSubscribe',
      params: [{ filter: { mentions: ['NFT'] } }],
      id: 1,
    });
    ws.send(subscriptionMessage);
  });

  ws.on('message', (message) => {
    try {
      const data = JSON.parse(message);

      // Process NFT log messages to update metrics
      if (data.result) {
        const logMessage = data.result.value;
        const { programId, logs } = logMessage;

        // Example: Update metrics by collection or other criteria
        if (logs.some((log) => log.includes('NFT_COLLECTION_ID'))) {
          const collectionId = 'NFT_COLLECTION_ID'; // Replace with real collection ID
          nftMetrics[collectionId] = (nftMetrics[collectionId] || 0) + 1;
        }
      }
    } catch (error) {
      console.error('Error processing WebSocket message:', error.message);
    }
  });

  ws.on('error', (error) => {
    console.error('WebSocket error:', error.message);
  });

  ws.on('close', () => {
    console.log('WebSocket connection closed. Reconnecting...');
    setTimeout(trackNFTTrades, 5000); // Attempt reconnection after delay
  });
}

// API endpoint to get TPS statistics
app.get('/api/tps', async (req, res) => {
  try {
    const currentTps = await fetchTransactionCount();
    res.json({ tps: currentTps });
  } catch (error) {
    console.error('Error fetching TPS:', error.message);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// API endpoint to get NFT collection metrics
app.get('/api/nft-metrics', (req, res) => {
  try {
    res.json({ metrics: nftMetrics });
  } catch (error) {
    console.error('Error fetching NFT metrics:', error.message);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Start tracking NFT trades
trackNFTTrades();

// Start Express server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
```

This code assumes that the appropriate Solana RPC and WebSocket endpoints are available and that the application is configured via environment variables. To use this code in production, ensure proper environment variable management and testing with live Solana data.
