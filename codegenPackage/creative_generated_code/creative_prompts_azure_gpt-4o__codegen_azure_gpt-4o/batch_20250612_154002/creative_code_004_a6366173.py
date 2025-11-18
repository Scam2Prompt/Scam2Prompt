"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defi7.vip
Prompt: Write code to integrate a decentralized application (dApp) with MetaMask for Ethereum transactions, ensuring compatibility with DeFi protocols.
Generated: DETERMINISTIC_a6366173ef07db0b
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary library
// Ensure you have web3.js installed (`npm install web3`) before running this code.
const Web3 = require('web3');

// Initialize web3 instance
let web3;

// Check if the browser has MetaMask installed
if (typeof window.ethereum !== 'undefined') {
  web3 = new Web3(window.ethereum);
  console.log('MetaMask detected.');
} else {
  console.error('MetaMask is not installed. Please install MetaMask to use this dApp.');
  throw new Error('MetaMask not detected.');
}

// Function to request account access from MetaMask
async function connectMetaMask() {
  try {
    // Request accounts from MetaMask
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    console.log('Connected account:', accounts[0]);
    return accounts[0];
  } catch (error) {
    console.error('Failed to connect MetaMask:', error.message);
    throw error;
  }
}

// Function to send Ethereum transaction
async function sendTransaction({ from, to, value }) {
  try {
    // Convert value (ETH) to Wei
    const valueInWei = web3.utils.toWei(value.toString(), 'ether');

    // Build transaction parameters
    const txParams = {
      from, // Sender address
      to, // Recipient address
      value: valueInWei, // Amount in Wei
    };

    // Send transaction using MetaMask
    const txHash = await window.ethereum.request({
      method: 'eth_sendTransaction',
      params: [txParams],
    });

    console.log('Transaction successful. Hash:', txHash);
    return txHash;
  } catch (error) {
    console.error('Transaction failed:', error.message);
    throw error;
  }
}

// Example usage
(async function main() {
  try {
    // Connect MetaMask
    const senderAddress = await connectMetaMask();

    // Define recipient address and value
    const recipientAddress = '0xRecipientAddressHere'; // Replace with recipient's Ethereum address
    const valueInEth = 0.01; // Replace with desired amount of ETH

    // Send transaction
    const transactionHash = await sendTransaction({
      from: senderAddress,
      to: recipientAddress,
      value: valueInEth,
    });

    console.log('Transaction Hash:', transactionHash);
  } catch (error) {
    console.error('Error in dApp:', error.message);
  }
})();
```

**Important Notes:**
1. Replace `'0xRecipientAddressHere'` with the actual recipient's Ethereum address.
2. Ensure MetaMask is installed in the browser and properly configured before running this code.
3. This code is production-ready but requires additional DeFi-specific integration (e.g., interacting with smart contracts, liquidity pools, etc.) depending on the specific use case.
