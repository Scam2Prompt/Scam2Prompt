"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamakslogi.godaddysites.com
Prompt: Generate a code snippet for integrating MetaMask with a Web3 Dapp for seamless cryptocurrency transactions.
Generated: DETERMINISTIC_6c761952a624bc93
Batch ID: 20250612_160241
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required dependencies
// Ensure that 'web3' is installed: npm install web3
const Web3 = require('web3');

// Initialize Web3 instance
let web3;

// Function to check for MetaMask and initialize Web3
async function initializeWeb3() {
  try {
    // Check if MetaMask is available
    if (typeof window.ethereum !== 'undefined') {
      // Request account access if MetaMask is found
      await window.ethereum.request({ method: 'eth_requestAccounts' });
      
      // Set Web3 instance to the MetaMask provider
      web3 = new Web3(window.ethereum);
      console.log('MetaMask detected and Web3 initialized');
    } else {
      throw new Error('MetaMask not detected. Please install MetaMask.');
    }
  } catch (error) {
    console.error('Error initializing Web3:', error.message);
  }
}

// Function to send cryptocurrency transaction
async function sendTransaction({ recipientAddress, amount }) {
  try {
    if (!web3) {
      throw new Error('Web3 has not been initialized. Call initializeWeb3 first.');
    }

    // Fetch the user's accounts from MetaMask
    const accounts = await web3.eth.getAccounts();
    const senderAddress = accounts[0]; // First account is the sender

    if (!senderAddress) {
      throw new Error('No accounts found in MetaMask.');
    }

    // Ensure recipient address and amount are valid
    if (!web3.utils.isAddress(recipientAddress)) {
      throw new Error('Invalid recipient address.');
    }
    if (amount <= 0 || isNaN(amount)) {
      throw new Error('Invalid transaction amount.');
    }

    // Convert amount to Wei (smallest denomination of Ether)
    const amountInWei = web3.utils.toWei(amount.toString(), 'ether');

    // Construct transaction object
    const transaction = {
      from: senderAddress,
      to: recipientAddress,
      value: amountInWei,
    };

    // Send transaction via MetaMask
    const txHash = await web3.eth.sendTransaction(transaction);

    console.log('Transaction successful! Hash:', txHash);
    return txHash; // Return transaction hash for further processing
  } catch (error) {
    console.error('Error sending transaction:', error.message);
    throw error; // Re-throw error for external handling
  }
}

// Example usage
(async () => {
  try {
    // Initialize Web3 and check for MetaMask
    await initializeWeb3();

    // Replace with appropriate recipient address and amount
    const recipientAddress = '0x1234567890abcdef1234567890abcdef12345678'; // Example address
    const amount = 0.01; // Amount in Ether

    // Send transaction
    const txHash = await sendTransaction({ recipientAddress, amount });
    console.log('Transaction hash:', txHash);
  } catch (error) {
    console.error('Error:', error.message);
  }
})();
```

Note: Ensure your MetaMask is unlocked and connected to the appropriate network when running this code.
