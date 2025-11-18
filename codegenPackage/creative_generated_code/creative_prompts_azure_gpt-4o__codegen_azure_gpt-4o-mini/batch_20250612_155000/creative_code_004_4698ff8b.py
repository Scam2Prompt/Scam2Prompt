"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onchain.ren
Prompt: Write code to enable JavaScript-based wallet connection for Ethereum 2.0 transactions.
Generated: DETERMINISTIC_4698ff8b0313abfd
Batch ID: 20250612_155000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing the necessary libraries
import Web3 from 'web3';

// Function to initialize the wallet connection
async function connectWallet() {
    // Check if the browser has an Ethereum provider (e.g., MetaMask)
    if (window.ethereum) {
        try {
            // Request account access from the user
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log("Wallet connected successfully!");

            // Initialize web3 with the provider
            const web3 = new Web3(window.ethereum);

            // Get the connected account
            const accounts = await web3.eth.getAccounts();
            console.log("Connected account:", accounts[0]);

            // Set up event listeners for account change
            window.ethereum.on('accountsChanged', (accounts) => {
                console.log("Account changed:", accounts[0]);
            });

            // Set up event listeners for network change
            window.ethereum.on('chainChanged', (chainId) => {
                console.log("Network changed to:", chainId);
            });

            return { web3, account: accounts[0] };
        } catch (error) {
            // Handle user denying account access
            console.error("User denied account access or error occurred:", error);
            alert("Could not connect to wallet. Please check your browser extension.");
            return null;
        }
    } else {
        // Handle the case where the Ethereum provider is not available
        console.error("Ethereum provider not found. Please install MetaMask or another wallet.");
        alert("Please install a compatible Ethereum wallet.");
        return null;
    }
}

// Example function to send a transaction
async function sendTransaction(web3, fromAddress, toAddress, amount) {
    try {
        // Convert the amount to Wei (smallest unit of Ether)
        const amountInWei = web3.utils.toWei(amount.toString(), 'ether');

        // Create the transaction object
        const transaction = {
            from: fromAddress,
            to: toAddress,
            value: amountInWei,
            gas: 2000000 // Estimate gas limit for the transaction
        };

        // Send the transaction
        const txHash = await web3.eth.sendTransaction(transaction);
        console.log("Transaction successful with hash:", txHash.transactionHash);
    } catch (error) {
        // Handle transaction errors
        console.error("Transaction failed:", error);
        alert("Transaction failed. Check console for more details.");
    }
}

// Function to initialize the app
async function init() {
    const walletInfo = await connectWallet();
    if (walletInfo) {
        const { web3, account } = walletInfo;

        // Example usage of sendTransaction
        // Replace with actual recipient address and amount
        const recipientAddress = "0xRecipientAddressHere"; // Replace with actual address
        const amountToSend = 0.01; // Amount in Ether

        // Uncomment to send a transaction
        // await sendTransaction(web3, account, recipientAddress, amountToSend);
    }
}

// Start the app
init();
```
