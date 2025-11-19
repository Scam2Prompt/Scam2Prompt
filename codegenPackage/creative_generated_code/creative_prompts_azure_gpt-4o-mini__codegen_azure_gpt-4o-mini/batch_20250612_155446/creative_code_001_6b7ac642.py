"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappssolutionxyz.web.app
Prompt: How can I implement multichain support in my DApp to interact with both Metamask and WalletConnect?
Generated: DETERMINISTIC_6b7ac6424db510dd
Batch ID: 20250612_155446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3';
import { ethers } from 'ethers';
import WalletConnectProvider from "@walletconnect/web3-provider";

// Define supported chains
const SUPPORTED_CHAINS = {
    1: 'Ethereum Mainnet',
    56: 'Binance Smart Chain',
    137: 'Polygon',
    // Add additional chains as necessary
};

// Initialize Web3 instance
let web3;

// Function to detect and connect to user's wallet
async function connectWallet() {
    try {
        // Check if MetaMask is installed
        if (window.ethereum) {
            // Request account access
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            web3 = new Web3(window.ethereum);
            console.log("Connected to MetaMask");
        } else {
            // Initialize WalletConnect provider
            const connector = new WalletConnectProvider({
                infuraId: "YOUR_INFURA_ID" // Required for WalletConnect
            });

            // Enable session (triggers QR Code modal)
            await connector.enable();
            web3 = new Web3(connector);
            console.log("Connected to WalletConnect");
        }
    } catch (error) {
        console.error("Failed to connect to wallet:", error);
    }
}

// Function to switch network
async function switchNetwork(chainId) {
    try {
        if (window.ethereum) {
            await window.ethereum.request({
                method: 'wallet_switchEthereumChain',
                params: [{ chainId: `0x${chainId.toString(16)}` }],
            });
            console.log(`Switched to network: ${SUPPORTED_CHAINS[chainId]}`);
        } else {
            console.warn("No wallet found to switch networks.");
        }
    } catch (error) {
        console.error("Failed to switch network:", error);
        if (error.code === 4902) {
            console.log(`Chain not added. Please add ${SUPPORTED_CHAINS[chainId]} to your wallet.`);
        }
    }
}

// Function to get the current account address
async function getCurrentAccount() {
    try {
        const accounts = await web3.eth.getAccounts();
        return accounts[0];
    } catch (error) {
        console.error("Failed to get accounts:", error);
    }
}

// Main function to initiate wallet connection and set up event listeners
async function main() {
    await connectWallet();
    const account = await getCurrentAccount();
    console.log("Current account:", account);

    // Example: Switch to a specific network (for demonstration)
    // Call this function with the desired chainId
    // await switchNetwork(56); // For Binance Smart Chain
}

// Run the main function
main().catch(error => {
    console.error("An error occurred in the main function:", error);
});
```

Make sure to replace `"YOUR_INFURA_ID"` with your actual Infura project ID before deploying the code.
