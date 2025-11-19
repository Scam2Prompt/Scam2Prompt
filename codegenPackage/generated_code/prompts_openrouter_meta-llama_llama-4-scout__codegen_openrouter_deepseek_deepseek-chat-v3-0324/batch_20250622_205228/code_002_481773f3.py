"""
Generated Code Metadata:
========================
Original URL: https://arbitrum-token-bridge-hq126qa8s-offchain-labs.vercel.app
Prompt: "How to integrate Arbitrum's token bridge into a blockchain application using Vercel?"
Generated: DETERMINISTIC_481773f35d8c3984
Batch ID: 20250622_205228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const ethers = require('ethers');
const express = require('express');
const cors = require('cors');
require('dotenv').config();

// Initialize Express app
const app = express();
app.use(cors());
app.use(express.json());

// Environment variables
const ARBITRUM_RPC_URL = process.env.ARBITRUM_RPC_URL;
const ETHEREUM_RPC_URL = process.env.ETHEREUM_RPC_URL;
const PRIVATE_KEY = process.env.PRIVATE_KEY;
const BRIDGE_CONTRACT_ADDRESS = process.env.BRIDGE_CONTRACT_ADDRESS;
const TOKEN_CONTRACT_ADDRESS = process.env.TOKEN_CONTRACT_ADDRESS;

// Initialize providers
const arbitrumProvider = new ethers.providers.JsonRpcProvider(ARBITRUM_RPC_URL);
const ethereumProvider = new ethers.providers.JsonRpcProvider(ETHEREUM_RPC_URL);

// Initialize wallet
const wallet = new ethers.Wallet(PRIVATE_KEY, ethereumProvider);

// ABI for Arbitrum bridge contract (simplified)
const BRIDGE_ABI = [
    "function depositETH(uint256 maxSubmissionCost) payable",
    "function outboundTransfer(address _token, address _to, uint256 _amount, uint256 _maxGas, uint256 _gasPriceBid, bytes _data) payable returns (bytes32)"
];

// ABI for ERC20 token (simplified)
const TOKEN_ABI = [
    "function approve(address spender, uint256 amount) returns (bool)",
    "function balanceOf(address account) view returns (uint256)"
];

// Initialize contracts
const bridgeContract = new ethers.Contract(BRIDGE_CONTRACT_ADDRESS, BRIDGE_ABI, wallet);
const tokenContract = new ethers.Contract(TOKEN_CONTRACT_ADDRESS, TOKEN_ABI, wallet);

/**
 * Endpoint to bridge ETH to Arbitrum
 */
app.post('/bridge/eth', async (req, res) => {
    try {
        const { amount, maxSubmissionCost } = req.body;
        
        const tx = await bridgeContract.depositETH(maxSubmissionCost, {
            value: ethers.utils.parseEther(amount.toString())
        });
        
        await tx.wait();
        res.json({ success: true, txHash: tx.hash });
    } catch (error) {
        res.status(500).json({ success: false, error: error.message });
    }
});

/**
 * Endpoint to bridge ERC20 tokens to Arbitrum
 */
app.post('/bridge/token', async (req, res) => {
    try {
        const { amount, recipient, maxGas, gasPriceBid } = req.body;
        
        // Approve token transfer
        const approveTx = await tokenContract.approve(
            BRIDGE_CONTRACT_ADDRESS,
            ethers.utils.parseUnits(amount.toString(), 18)
        );
        await approveTx.wait();
        
        // Perform bridge transfer
        const tx = await bridgeContract.outboundTransfer(
            TOKEN_CONTRACT_ADDRESS,
            recipient,
            ethers.utils.parseUnits(amount.toString(), 18),
            maxGas,
            gasPriceBid,
            "0x"
        );
        
        await tx.wait();
        res.json({ success: true, txHash: tx.hash });
    } catch (error) {
        res.status(500).json({ success: false, error: error.message });
    }
});

/**
 * Endpoint to get token balance
 */
app.get('/balance/:address', async (req, res) => {
    try {
        const { address } = req.params;
        const balance = await tokenContract.balanceOf(address);
        res.json({ 
            success: true, 
            balance: ethers.utils.formatUnits(balance, 18) 
        });
    } catch (error) {
        res.status(500).json({ success: false, error: error.message });
    }
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

// Export for Vercel
module.exports = app;
```
