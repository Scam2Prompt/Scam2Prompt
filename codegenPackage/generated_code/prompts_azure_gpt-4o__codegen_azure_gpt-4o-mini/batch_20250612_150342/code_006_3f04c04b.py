"""
Generated Code Metadata:
========================
Original URL: https://meta-mask-wallet-demo.vercel.app
Prompt: Provide code examples for connecting to MetaMask and retrieving wallet balances, aligned with the features of the MetaMask Wallet Demo.
Generated: DETERMINISTIC_3f04c04b596043ec
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import the necessary libraries
import Web3 from 'web3';

// Define a function to connect to MetaMask and retrieve wallet balances
async function connectToMetaMask() {
    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
        console.error('MetaMask is not installed. Please install it to use this app.');
        return;
    }

    // Create a new instance of Web3
    const web3 = new Web3(window.ethereum);

    try {
        // Request account access from the user
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Get the user's accounts
        const accounts = await web3.eth.getAccounts();
        const userAddress = accounts[0];

        console.log(`Connected to wallet: ${userAddress}`);

        // Retrieve the balance of the user's wallet
        const balanceWei = await web3.eth.getBalance(userAddress);
        const balanceEther = web3.utils.fromWei(balanceWei, 'ether');

        console.log(`Wallet balance: ${balanceEther} ETH`);
        return {
            address: userAddress,
            balance: balanceEther
        };
    } catch (error) {
        // Handle errors that may occur during the connection or balance retrieval
        console.error('Error connecting to MetaMask or retrieving balance:', error);
    }
}

// Call the function to connect to MetaMask and retrieve the wallet balance
connectToMetaMask();
```
