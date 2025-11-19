"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metzhgofk.com
Prompt: Generate a code example that shows how to sign a transaction using MetaMask's API for a decentralized application.
Generated: DETERMINISTIC_a49964d931053ea3
Batch ID: 20250612_163540
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// This code snippet demonstrates how to sign a transaction using MetaMask's API in a decentralized application.

// Ensure the browser supports Ethereum and MetaMask is installed
if (typeof window.ethereum === 'undefined') {
  console.error('MetaMask is not installed. Please install MetaMask to proceed.');
} else {
  // Function to sign a transaction using MetaMask
  const signTransactionWithMetaMask = async () => {
    try {
      // Request account access from MetaMask
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      
      // Ensure at least one account was returned
      if (!accounts || accounts.length === 0) {
        console.error('No Ethereum accounts found.');
        return;
      }

      const senderAddress = accounts[0]; // Use the first connected account as the sender
      
      // Example transaction data
      const transactionData = {
        from: senderAddress,
        to: '0xRecipientAddressHere', // Replace with the recipient's Ethereum address
        value: '0x29a2241af62c0000', // Value in wei (0.1 ETH as an example)
        gas: '0x5208', // Gas limit (21000 units as an example)
        gasPrice: '0x3B9ACA00', // Gas price in wei (1 Gwei as an example)
        // Optional: Add more fields like nonce, data (for contract calls), etc.
      };

      // Request MetaMask to sign and send the transaction
      const signedTransaction = await window.ethereum.request({
        method: 'eth_sendTransaction',
        params: [transactionData]
      });

      console.log('Transaction successfully signed and sent:', signedTransaction);
    } catch (error) {
      // Handle errors during the transaction signing process
      if (error.code === 4001) {
        console.error('Transaction rejected by the user.');
      } else {
        console.error('An error occurred while signing the transaction:', error.message);
      }
    }
  };

  // Call the function to sign the transaction
  signTransactionWithMetaMask();
}
```

Make sure to replace placeholder values with actual data for your application (e.g., recipient address, value, gas price).
