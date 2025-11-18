"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.services-money91.com
Prompt: Generate code to connect a web application to MetaMask and send an Ethereum transaction using Web3.js.
Generated: DETERMINISTIC_db3ee601d3de587f
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the Web3 library
const Web3 = require('web3');

// Ensure the code runs only in the browser with MetaMask installed
if (typeof window.ethereum !== 'undefined') {
  // Create a Web3 instance connected to MetaMask
  const web3 = new Web3(window.ethereum);

  // Function to connect to MetaMask and send an Ethereum transaction
  const connectAndSendTransaction = async () => {
    try {
      // Request account access from MetaMask
      await window.ethereum.request({ method: 'eth_requestAccounts' });

      // Retrieve the current accounts connected to MetaMask
      const accounts = await web3.eth.getAccounts();
      
      // Check if accounts were retrieved successfully
      if (accounts.length === 0) {
        console.error('No accounts connected.');
        return;
      }

      const sender = accounts[0]; // Use the first account as the sender

      // Specify the recipient address (replace with a valid Ethereum address)
      const recipient = '0xRecipientAddressHere';

      // Specify the amount to send (in Wei)
      const amountToSend = web3.utils.toWei('0.1', 'ether'); // Sends 0.1 Ether

      // Create the transaction object
      const transaction = {
        from: sender,
        to: recipient,
        value: amountToSend,
      };

      // Send the transaction
      const txHash = await web3.eth.sendTransaction(transaction);

      // Log the transaction hash
      console.log('Transaction successful! Hash:', txHash);
    } catch (error) {
      // Handle any errors that occur during the process
      console.error('Error occurred:', error.message);
    }
  };

  // Attach the function to a button click or call it directly
  document.getElementById('sendTransactionButton').addEventListener('click', connectAndSendTransaction);
} else {
  console.error('MetaMask is not installed. Please install MetaMask and try again.');
}
```

### HTML Button Example (to trigger the code above)
```html
<button id="sendTransactionButton">Send Ethereum Transaction</button>
```
