"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vault-puffer.com
Prompt: Provide an example of how to use the MetaMask API for securely managing user transactions in a decentralized application.
Generated: DETERMINISTIC_5b5b14ff47b9ef29
Batch ID: 20250612_162828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries
// Ensure you have installed web3.js by running: npm install web3
const Web3 = require('web3');

// Create a new instance of Web3 using the MetaMask provider
// MetaMask injects `window.ethereum` into the browser
if (typeof window.ethereum !== 'undefined') {
  const web3 = new Web3(window.ethereum);

  // Prompt the user to connect their MetaMask wallet
  async function connectWallet() {
    try {
      // Request accounts from MetaMask
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      
      console.log('Wallet connected successfully:', accounts[0]);
      return accounts[0]; // Return the first connected account
    } catch (error) {
      console.error('Failed to connect wallet:', error.message);
      throw new Error('MetaMask connection error');
    }
  }

  // Function to send a transaction from the user's wallet
  async function sendTransaction(fromAddress, toAddress, amount) {
    try {
      // Convert the amount to Wei (smallest unit in Ethereum)
      const valueInWei = Web3.utils.toWei(amount.toString(), 'ether');

      // Build the transaction object
      const transactionParameters = {
        to: toAddress, // Address to send the funds to
        from: fromAddress, // MetaMask will automatically use this as the sender
        value: valueInWei, // Amount to send in Wei
      };

      // Send the transaction using MetaMask
      const txHash = await window.ethereum.request({
        method: 'eth_sendTransaction',
        params: [transactionParameters],
      });

      console.log('Transaction successful. Hash:', txHash);
      return txHash; // Return the transaction hash
    } catch (error) {
      console.error('Transaction failed:', error.message);
      throw new Error('Transaction error');
    }
  }

  // Example usage
  async function executeTransaction() {
    try {
      // Connect the wallet
      const userAddress = await connectWallet();

      // Define recipient address and amount
      const recipientAddress = '0xRecipientWalletAddressHere'; // Replace with actual recipient address
      const amountToSend = 0.01; // Amount in Ether

      // Send the transaction
      const transactionHash = await sendTransaction(userAddress, recipientAddress, amountToSend);

      // Log the transaction hash
      console.log('Transaction hash:', transactionHash);
    } catch (error) {
      console.error('Error during transaction execution:', error.message);
    }
  }

  // Call the example function to demonstrate functionality
  executeTransaction();

} else {
  console.error('MetaMask is not installed. Please install MetaMask and refresh the page.');
  alert('MetaMask is required to interact with this application.');
}
```
