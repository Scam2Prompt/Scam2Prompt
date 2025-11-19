"""
Generated Code Metadata:
========================
Original URL: https://x1blockdag.pages.dev
Prompt: Write a Node.js script to interact with the BlockDAG blockchain using the Meta Mask method for wallet integration and EVM compatibility.
Generated: DETERMINISTIC_9ce5e41712c11110
Batch ID: 20250622_204712
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
  "https://mainnet.blockdag.network": {
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
const express = require('express');
const Web3 = require('web3');
const { ethers } = require('ethers');
const cors = require('cors');
const bodyParser = require('body-parser');

// Initialize Express app
const app = express();
const port = 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Initialize Web3 provider (MetaMask injected or custom)
let web3;
let provider;
let signer;

// Check if MetaMask is available
if (typeof window !== 'undefined' && window.ethereum) {
    provider = new ethers.providers.Web3Provider(window.ethereum);
    web3 = new Web3(window.ethereum);
} else {
    // Fallback to a local or remote node
    provider = new ethers.providers.JsonRpcProvider('https://mainnet.blockdag.network');
    web3 = new Web3('https://mainnet.blockdag.network');
}

// Connect wallet endpoint
app.post('/connect-wallet', async (req, res) => {
    try {
        if (!window.ethereum) {
            throw new Error('MetaMask not detected');
        }

        // Request account access
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        signer = provider.getSigner();
        
        res.json({
            success: true,
            address: accounts[0],
            message: 'Wallet connected successfully'
        });
    } catch (error) {
        res.status(400).json({
            success: false,
            error: error.message
        });
    }
});

// Get balance endpoint
app.get('/balance/:address', async (req, res) => {
    try {
        const balance = await web3.eth.getBalance(req.params.address);
        res.json({
            success: true,
            balance: web3.utils.fromWei(balance, 'ether')
        });
    } catch (error) {
        res.status(400).json({
            success: false,
            error: error.message
        });
    }
});

// Send transaction endpoint
app.post('/send-transaction', async (req, res) => {
    try {
        const { to, value } = req.body;
        
        if (!to || !value) {
            throw new Error('Missing required parameters');
        }

        if (!signer) {
            throw new Error('Wallet not connected');
        }

        const tx = await signer.sendTransaction({
            to,
            value: ethers.utils.parseEther(value)
        });

        res.json({
            success: true,
            txHash: tx.hash,
            message: 'Transaction sent successfully'
        });
    } catch (error) {
        res.status(400).json({
            success: false,
            error: error.message
        });
    }
});

// Start server
app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});

// Export for testing
module.exports = app;
```
