"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mttamskkwlltextsn.gitbook.io
Prompt: Generate code snippets demonstrating how to adjust gas fees and customize transaction settings in MetaMask.
Generated: DETERMINISTIC_b77dc34ad82463c6
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * This JavaScript code snippet demonstrates how to adjust gas fees and customize transaction settings 
 * in MetaMask using the Ethereum provider (window.ethereum).
 * Ensure you have MetaMask installed and configured in your browser before using this snippet.
 */

// Function to send a custom transaction with adjusted gas fees
async function sendCustomTransaction() {
  try {
    // Check if MetaMask's Ethereum provider is available
    if (typeof window.ethereum === 'undefined') {
      throw new Error('MetaMask is not installed or available.');
    }

    // Request accounts from MetaMask
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    const sender = accounts[0]; // Use the first account as the sender

    // Construct the transaction object
    const transactionParameters = {
      to: '0xRecipientAddressHere', // Replace with the recipient's address
      value: '0x29a2241af62c0000',  // Value in wei (0.1 ETH in this example)
      gasPrice: '0x09184e72a000',   // Custom gas price in wei (e.g., 10000000000000 wei)
      gas: '0x5208',               // Custom gas limit (e.g., 21000 gas units)
    };

    // Send the transaction using MetaMask
    const txHash = await window.ethereum.request({
      method: 'eth_sendTransaction',
      params: [transactionParameters],
    });

    console.log('Transaction sent successfully. Hash:', txHash);
  } catch (error) {
    console.error('Error sending transaction:', error.message);
  }
}

/**
 * Example usage: Call the function to send a custom transaction.
 * Uncomment the line below to execute the function.
 */
// sendCustomTransaction();
```
