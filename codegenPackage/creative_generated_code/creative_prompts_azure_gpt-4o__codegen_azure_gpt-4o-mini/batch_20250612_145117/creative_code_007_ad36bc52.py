"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://detto.finance
Prompt: Provide a code snippet for integrating wallet connection functionality in a decentralized finance app using WalletConnect, as Detto Finance might support.
Generated: DETERMINISTIC_ad36bc52cc50bcbf
Batch ID: 20250612_145117
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://bridge.walletconnect.org": {
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
import WalletConnectProvider from "@walletconnect/web3-provider"; // WalletConnect Provider
import { ethers } from "ethers"; // Ethers.js for Ethereum interaction

// Initialize state variables for the WalletConnect provider and signer
let connector;
let signer;

// Function to initialize WalletConnect
async function initWalletConnect() {
    try {
        // Create a new WalletConnect provider
        connector = new WalletConnectProvider({
            bridge: "https://bridge.walletconnect.org", // WalletConnect bridge server
            qrcode: true, // Show QR Code for connection
        });

        // Enable session (triggers QR Code modal)
        await connector.enable();

        // Create an ethers provider and signer
        const provider = new ethers.providers.Web3Provider(connector);
        signer = provider.getSigner();

        // Log connected account address
        const account = await signer.getAddress();
        console.log("Connected account:", account);
    } catch (error) {
        console.error("Failed to connect WalletConnect:", error);
    }
}

// Function to disconnect WalletConnect
async function disconnectWalletConnect() {
    if (connector) {
        await connector.killSession(); // End the WalletConnect session
        console.log("WalletConnect session disconnected.");
    }
}

// Function to send a transaction
async function sendTransaction() {
    if (!signer) {
        console.error("Wallet not connected. Please connect first.");
        return;
    }

    const transaction = {
        to: "0xRecipientAddress", // Replace with recipient address
        value: ethers.utils.parseEther("0.01"), // Transaction value in Ether
        gasLimit: 21000, // Gas limit
    };

    try {
        const txResponse = await signer.sendTransaction(transaction);
        console.log("Transaction sent:", txResponse.hash);
        await txResponse.wait(); // Wait for transaction to be mined
        console.log("Transaction confirmed:", txResponse.hash);
    } catch (error) {
        console.error("Transaction failed:", error);
    }
}

// Example usage
// Uncomment the lines below to test the functions
// initWalletConnect();
// sendTransaction();
// disconnectWalletConnect();
```
