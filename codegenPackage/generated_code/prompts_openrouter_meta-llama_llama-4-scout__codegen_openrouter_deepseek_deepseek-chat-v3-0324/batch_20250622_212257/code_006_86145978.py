"""
Generated Code Metadata:
========================
Original URL: https://msk-rk.ru
Prompt: Design a decentralized application (dApp) that leverages Hop Protocol for cross-chain token swaps, focusing on user experience and security.
Generated: DETERMINISTIC_86145978f55b9961
Batch ID: 20250622_212257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries and modules
const { ethers } = require('ethers');
const { Hop } = require('@hop-protocol/sdk');
const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware setup
app.use(cors());
app.use(bodyParser.json());

// Environment variables check
if (!process.env.PRIVATE_KEY || !process.env.INFURA_API_KEY) {
    console.error('Missing required environment variables');
    process.exit(1);
}

// Initialize Hop Protocol SDK
let hop;
try {
    hop = new Hop('mainnet');
} catch (error) {
    console.error('Failed to initialize Hop SDK:', error);
    process.exit(1);
}

// Provider setup
const provider = new ethers.providers.InfuraProvider('mainnet', process.env.INFURA_API_KEY);
const wallet = new ethers.Wallet(process.env.PRIVATE_KEY, provider);

// Token swap endpoint
app.post('/swap', async (req, res) => {
    try {
        const { fromChain, toChain, token, amount, recipient } = req.body;

        // Input validation
        if (!fromChain || !toChain || !token || !amount || !recipient) {
            return res.status(400).json({ error: 'Missing required parameters' });
        }

        if (!ethers.utils.isAddress(recipient)) {
            return res.status(400).json({ error: 'Invalid recipient address' });
        }

        // Get bridge instance
        const bridge = hop.bridge(token);

        // Check if token is supported
        if (!bridge) {
            return res.status(400).json({ error: 'Token not supported' });
        }

        // Get estimated swap time and cost
        const estimatedTime = await bridge.getEstimatedTime(fromChain, toChain);
        const fee = await bridge.getFee(fromChain, toChain);

        // Send transaction
        const tx = await bridge.send(amount, fromChain, toChain, {
            recipient,
            wallet
        });

        // Wait for transaction confirmation
        const receipt = await tx.wait();

        // Return success response
        res.json({
            success: true,
            txHash: receipt.transactionHash,
            estimatedTime,
            fee
        });

    } catch (error) {
        console.error('Swap error:', error);
        res.status(500).json({ 
            error: 'Failed to process swap',
            details: error.message 
        });
    }
});

// Get supported tokens endpoint
app.get('/tokens', async (req, res) => {
    try {
        const tokens = hop.getSupportedTokens();
        res.json({ tokens });
    } catch (error) {
        console.error('Tokens error:', error);
        res.status(500).json({ error: 'Failed to fetch supported tokens' });
    }
});

// Get supported chains endpoint
app.get('/chains', async (req, res) => {
    try {
        const chains = hop.getSupportedChains();
        res.json({ chains });
    } catch (error) {
        console.error('Chains error:', error);
        res.status(500).json({ error: 'Failed to fetch supported chains' });
    }
});

// Health check endpoint
app.get('/health', (req, res) => {
    res.json({ status: 'healthy' });
});

// Start server
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error('Unhandled error:', err);
    res.status(500).json({ error: 'Internal server error' });
});

process.on('unhandledRejection', (reason, promise) => {
    console.error('Unhandled Rejection at:', promise, 'reason:', reason);
});

process.on('uncaughtException', (error) => {
    console.error('Uncaught Exception:', error);
    process.exit(1);
});
```
