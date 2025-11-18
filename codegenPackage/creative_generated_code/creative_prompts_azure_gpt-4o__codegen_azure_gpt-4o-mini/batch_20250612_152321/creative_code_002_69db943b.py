"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3modal-laboratory-qix0wwvm2-walletconnect1.vercel.app
Prompt: Provide code to implement email and social login functionality using the Ethers library, referencing the Web3Modal documentation.
Generated: DETERMINISTIC_69db943bfafe548f
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { ethers } from "ethers"; // Ethers library for interacting with Ethereum
import Web3Modal from 'web3modal'; // Web3Modal for wallet connection
import WalletConnectProvider from "@walletconnect/web3-provider"; // WalletConnect provider
import Fortmatic from "fortmatic"; // Fortmatic provider for email login

// Define the provider options for Web3Modal
const providerOptions = {
    walletconnect: {
        package: WalletConnectProvider, // Required
        options: {
            infuraId: "YOUR_INFURA_ID" // Required: Your Infura project ID
        }
    },
    fortmatic: {
        package: Fortmatic, // Required
        options: {
            key: "YOUR_FORTMATIC_KEY" // Required: Your Fortmatic API key
        }
    }
};

// Create a new instance of Web3Modal
const web3Modal = new Web3Modal({
    network: "mainnet", // Optional: Specify the network (mainnet/testnet)
    cacheProvider: true, // Optional: Cache provider for faster re-connections
    providerOptions // Required: Provider options defined above
});

// Function to connect to wallet or email login
async function connect() {
    try {
        // Open the modal to select wallet or email provider
        const provider = await web3Modal.connect();
        
        // Create an ethers provider instance
        const ethersProvider = new ethers.providers.Web3Provider(provider);

        // Get the signer for transaction signing
        const signer = ethersProvider.getSigner();
        
        // Log the address of the connected wallet
        const address = await signer.getAddress();
        console.log("Connected wallet address:", address);
        
        // You can now use the signer to send transactions, sign messages, etc.
        // Example: const tx = await signer.sendTransaction({...});

    } catch (error) {
        console.error("Failed to connect to wallet or email provider:", error);
    }
}

// Function to disconnect from the wallet
async function disconnect() {
    try {
        await web3Modal.clearCachedProvider(); // Clear the cached provider
        console.log("Disconnected from wallet");
    } catch (error) {
        console.error("Failed to disconnect:", error);
    }
}

// Event listener for connection button
document.getElementById('connectButton').addEventListener('click', connect);
document.getElementById('disconnectButton').addEventListener('click', disconnect);

// Ensure to handle errors gracefully in your UI, e.g., display error messages to the user.
```

**Note:** Replace `YOUR_INFURA_ID` and `YOUR_FORTMATIC_KEY` with your actual Infura project ID and Fortmatic API key. Make sure to include appropriate HTML elements with IDs `connectButton` and `disconnectButton` in your HTML file to trigger the connection and disconnection functions.
