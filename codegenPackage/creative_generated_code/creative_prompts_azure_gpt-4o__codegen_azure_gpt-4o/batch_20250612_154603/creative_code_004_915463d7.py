"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://accessnodeapp.com
Prompt: Write code to implement multichain transaction support in a Web3 DApp, ensuring compatibility with self-custodial wallets, as discussed on AccessNodeApp.com.
Generated: DETERMINISTIC_915463d751985f5e
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// This code implements multichain transaction support in a Web3 DApp.
// It ensures compatibility with self-custodial wallets using the ethers.js library.
// Make sure you install ethers.js and dotenv before running the code.
// npm install ethers dotenv

require('dotenv').config();
const { ethers } = require("ethers");

// Constants for supported chains
const SUPPORTED_CHAINS = {
    ethereum: {
        rpcUrl: process.env.ETH_RPC_URL, // Ethereum RPC URL
        chainId: 1, // Ethereum Mainnet chain ID
    },
    polygon: {
        rpcUrl: process.env.POLYGON_RPC_URL, // Polygon RPC URL
        chainId: 137, // Polygon Mainnet chain ID
    },
    bsc: {
        rpcUrl: process.env.BSC_RPC_URL, // Binance Smart Chain RPC URL
        chainId: 56, // Binance Smart Chain Mainnet chain ID
    },
};

// Function to connect to a specific blockchain network
async function connectToChain(chainName) {
    if (!SUPPORTED_CHAINS[chainName]) {
        throw new Error(`Unsupported chain: ${chainName}`);
    }

    const rpcUrl = SUPPORTED_CHAINS[chainName].rpcUrl;
    const provider = new ethers.providers.JsonRpcProvider(rpcUrl);
    const signer = provider.getSigner(); // Access user's self-custodial wallet via provider

    return { provider, signer };
}

// Function to send a transaction on a specified chain
async function sendTransaction(chainName, to, value, data = "") {
    try {
        const { provider, signer } = await connectToChain(chainName);

        const walletAddress = (await signer.getAddress()).toLowerCase(); // Ensure connected wallet
        console.log(`Connected wallet address: ${walletAddress}`);

        // Estimate gas limit
        const gasLimit = await provider.estimateGas({
            to,
            value: ethers.utils.parseEther(value.toString()),
            data,
        });

        // Create transaction
        const tx = {
            to, // Recipient address
            value: ethers.utils.parseEther(value.toString()), // Value in ETH or relevant token
            data, // Optional transaction data
            gasLimit, // Estimated gas limit
        };

        // Send transaction
        const txResponse = await signer.sendTransaction(tx);
        console.log(`Transaction sent on ${chainName}: ${txResponse.hash}`);

        // Wait for transaction confirmation
        const txReceipt = await txResponse.wait();
        console.log(`Transaction confirmed: ${txReceipt.transactionHash}`);

        return txReceipt;
    } catch (error) {
        console.error(`Error sending transaction on ${chainName}:`, error.message);
        throw error;
    }
}

// Function to check wallet compatibility
async function checkWalletCompatibility(chainName) {
    try {
        const { provider, signer } = await connectToChain(chainName);
        const walletAddress = await signer.getAddress();
        console.log(`Wallet connected to ${chainName}: ${walletAddress}`);
        return true; // Wallet is compatible
    } catch (error) {
        console.error(`Wallet compatibility error on ${chainName}: ${error.message}`);
        return false; // Wallet is not compatible
    }
}

// Export functions for use in a DApp
module.exports = {
    connectToChain,
    sendTransaction,
    checkWalletCompatibility,
};
```

### Notes
1. Replace `process.env.ETH_RPC_URL`, `process.env.POLYGON_RPC_URL`, and `process.env.BSC_RPC_URL` in `.env` with your blockchain RPC URLs.
2. Ensure your self-custodial wallet (e.g., MetaMask) is connected and has funds for transactions.
3. This code is designed to be modular and production-ready, following best practices for scalability and maintainability.
