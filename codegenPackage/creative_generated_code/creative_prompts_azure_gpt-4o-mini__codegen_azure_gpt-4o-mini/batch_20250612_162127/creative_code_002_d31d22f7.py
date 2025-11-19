"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onchain.ren
Prompt: Can you provide a code snippet that demonstrates how to enable JavaScript in a web application using Onchain-ETH 2.0?
Generated: DETERMINISTIC_d31d22f71de08c5f
Batch ID: 20250612_162127
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries for Onchain-ETH 2.0 integration
import { ethers } from "ethers";

// Initialize provider and signer for Ethereum network
let provider;
let signer;

async function initializeEthereum() {
    // Check if the browser has Ethereum provider (like MetaMask)
    if (window.ethereum) {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Create a provider using the Ethereum provider
        provider = new ethers.providers.Web3Provider(window.ethereum);

        // Get the signer to interact with the blockchain
        signer = provider.getSigner();
        console.log("Ethereum successfully initialized.");
    } else {
        console.error("Ethereum provider not found. Please install MetaMask or another wallet.");
        alert("Please install MetaMask or another Ethereum wallet to use this application.");
    }
}

// Call the initialization function on page load
window.onload = async () => {
    try {
        await initializeEthereum();
    } catch (error) {
        console.error("Error initializing Ethereum:", error);
        alert("An error occurred while initializing Ethereum. Please check the console for more details.");
    }
};

// Function to check the current network
async function checkNetwork() {
    if (provider) {
        const network = await provider.getNetwork();
        console.log("Current network:", network);
        return network;
    } else {
        console.error("Provider not initialized.");
    }
}

// Example function to send a transaction (ensure to handle exceptions)
async function sendTransaction(toAddress, amount) {
    if (!signer) {
        console.error("Signer not available. Ensure Ethereum is initialized.");
        return;
    }

    const transaction = {
        to: toAddress,
        value: ethers.utils.parseEther(amount), // Convert to Wei
    };

    try {
        const txResponse = await signer.sendTransaction(transaction);
        console.log("Transaction sent:", txResponse);
        const txReceipt = await txResponse.wait(); // Wait for the transaction to be mined
        console.log("Transaction mined:", txReceipt);
    } catch (error) {
        console.error("Transaction failed:", error);
        alert("Transaction failed. Please check the console for details.");
    }
}

// Example usage: sendTransaction("0xReceiverAddressHere", "0.01");
```
