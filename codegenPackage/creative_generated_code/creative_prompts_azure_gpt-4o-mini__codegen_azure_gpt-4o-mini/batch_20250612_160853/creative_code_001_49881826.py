"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yellow-bush-1372.on.fleek.co
Prompt: What are the best practices for connecting a cryptocurrency wallet to a DApp?
Generated: DETERMINISTIC_49881826c5ecf848
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import Web3 from 'web3';
import detectEthereumProvider from '@metamask/detect-provider';

// Initialize Web3 instance
let web3;

// Function to initialize the connection to the wallet
async function initWalletConnection() {
    try {
        // Detect the Ethereum provider (MetaMask)
        const provider = await detectEthereumProvider();

        // Check if provider is found
        if (provider) {
            // Assign provider to web3 instance
            web3 = new Web3(provider);
            console.log("Ethereum provider found!");

            // Request account access if needed
            await provider.request({ method: 'eth_requestAccounts' });
            console.log("Accounts have been granted access.");
        } else {
            console.error("Please install MetaMask!");
        }
    } catch (error) {
        console.error("Failed to connect to wallet:", error);
    }
}

// Function to get the connected account
async function getConnectedAccount() {
    try {
        const accounts = await web3.eth.getAccounts();
        if (accounts.length > 0) {
            return accounts[0]; // Return the first connected account
        } else {
            console.warn("No accounts found. Please connect to your wallet.");
            return null;
        }
    } catch (error) {
        console.error("Failed to get accounts:", error);
        return null;
    }
}

// Function to send a transaction
async function sendTransaction(to, value) {
    try {
        const account = await getConnectedAccount();
        if (account) {
            const transactionParameters = {
                to, // The recipient address
                from: account, // The sender address
                value: web3.utils.toHex(web3.utils.toWei(value, 'ether')), // The amount to send in wei
            };

            // Send the transaction using the Ethereum provider
            const txHash = await web3.eth.sendTransaction(transactionParameters);
            console.log("Transaction successful with hash:", txHash);
        }
    } catch (error) {
        console.error("Transaction failed:", error);
    }
}

// Function to handle wallet disconnection and cleanup
async function disconnectWallet() {
    // This is more relevant for wallets that support disconnection, 
    // MetaMask does not require explicit disconnection.
    console.log("Wallet disconnected. Please refresh the page to reconnect.");
}

// Initialize wallet connection on page load
window.onload = initWalletConnection;
```
