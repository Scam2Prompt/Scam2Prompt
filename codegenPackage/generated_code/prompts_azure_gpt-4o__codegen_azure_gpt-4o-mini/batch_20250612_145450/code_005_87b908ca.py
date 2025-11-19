"""
Generated Code Metadata:
========================
Original URL: https://ethgas.web.app
Prompt: Write JavaScript code using Web3.js to connect a user's Ethereum wallet and retrieve transaction gas fees, similar to the ETH Gas Refund DApp.
Generated: DETERMINISTIC_87b908cae00de866
Batch ID: 20250612_145450
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import the Web3 library
import Web3 from 'web3';

// Define the main function to connect to the user's Ethereum wallet
async function connectWallet() {
    // Check if the browser has Ethereum provider (MetaMask)
    if (window.ethereum) {
        // Create a new instance of Web3 using the provider
        const web3 = new Web3(window.ethereum);
        
        try {
            // Request account access from the user
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log('Wallet connected successfully.');

            // Retrieve the user's Ethereum address
            const accounts = await web3.eth.getAccounts();
            const userAddress = accounts[0];
            console.log(`Connected account: ${userAddress}`);

            // Fetch the current gas price
            const gasPrice = await web3.eth.getGasPrice();
            console.log(`Current gas price: ${web3.utils.fromWei(gasPrice, 'gwei')} Gwei`);

            // Return the user's address and gas price
            return { userAddress, gasPrice };
        } catch (error) {
            // Handle errors during wallet connection
            console.error('Error connecting to wallet:', error);
            throw new Error('Wallet connection failed. Please try again.');
        }
    } else {
        // Handle the case where the user does not have an Ethereum provider
        console.error('Ethereum provider not found. Please install MetaMask or another wallet.');
        throw new Error('Ethereum provider not found. Please install MetaMask or another wallet.');
    }
}

// Call the connectWallet function on page load
window.onload = async () => {
    try {
        const walletInfo = await connectWallet();
        console.log('Wallet Info:', walletInfo);
    } catch (error) {
        // Handle any errors that occur during the wallet connection process
        alert(error.message);
    }
};
```
