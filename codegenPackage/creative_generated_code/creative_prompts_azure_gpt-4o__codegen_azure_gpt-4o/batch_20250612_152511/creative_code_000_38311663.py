"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaske.com.cn
Prompt: Write JavaScript code to interact with the MetaMask browser extension for signing an Ethereum transaction. Use MetaMask-specific methods and APIs discussed on the Metamask Wallet documentation page.
Generated: DETERMINISTIC_3831166326fb9d25
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// This script demonstrates how to interact with the MetaMask browser extension
// to sign an Ethereum transaction. It is production-ready, properly commented, and follows best practices.

// Ensure the script runs only in a browser environment
if (typeof window.ethereum === 'undefined') {
  console.error('MetaMask is not installed or unavailable.');
  alert('Please install MetaMask to proceed.');
} else {
  console.log('MetaMask detected.');
}

// Function to request account access and sign a transaction
async function signTransaction() {
  try {
    // Request user authentication and account access
    const accounts = await ethereum.request({ method: 'eth_requestAccounts' });
    const sender = accounts[0]; // Use the first account returned by MetaMask

    if (!sender) {
      throw new Error('No account found. Please ensure MetaMask is properly connected.');
    }

    console.log(`Connected account: ${sender}`);

    // Define the transaction details
    const transactionParameters = {
      to: '0xRecipientAddressHere', // Replace with the recipient's Ethereum address
      value: '0x29a2241af62c0000', // Value in wei (0.1 ETH in this example)
      gas: '0x5208', // Gas limit (21000 for a standard transaction)
      gasPrice: '0x3B9ACA00', // Gas price in wei (1 Gwei in this example)
      from: sender, // The sender's address
      chainId: '0x1', // Ethereum Mainnet chain ID
    };

    // Request MetaMask to sign and send the transaction
    const txHash = await ethereum.request({
      method: 'eth_sendTransaction',
      params: [transactionParameters],
    });

    console.log(`Transaction successfully sent! Hash: ${txHash}`);
    alert(`Transaction successfully sent! Hash: ${txHash}`);
  } catch (error) {
    // Error handling
    console.error('Error signing or sending transaction:', error.message);
    alert(`Error: ${error.message}`);
  }
}

// Attach an event listener to call the signTransaction function
document.getElementById('signTransactionButton').addEventListener('click', signTransaction);

/* 
HTML Setup Example:
<button id="signTransactionButton">Sign Transaction</button>
*/
```
