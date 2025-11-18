"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mttamskkwlltextsn.gitbook.io
Prompt: Write JavaScript code to integrate MetaMask into a web application for interacting with Ethereum-based DApps, ensuring users can connect their wallet and approve transactions directly from the browser.
Generated: DETERMINISTIC_9019fba574302d7d
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * MetaMask Integration for Ethereum-based DApps
 * This code allows users to connect their MetaMask wallet and interact with Ethereum-based DApps.
 * It ensures proper error handling and follows best practices.
 */

// Check if MetaMask is installed
if (typeof window.ethereum === 'undefined') {
  console.error('MetaMask is not installed. Please install MetaMask and refresh the page.');
} else {
  console.log('MetaMask detected! Ready for interaction.');
}

/**
 * Connect to MetaMask wallet
 * Prompts the user to connect their wallet and returns the connected accounts.
 */
async function connectWallet() {
  try {
    // Request account access
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    console.log('Connected account:', accounts[0]);
    return accounts[0]; // Return the first account
  } catch (error) {
    console.error('Error connecting to MetaMask:', error.message);
    throw new Error('Failed to connect MetaMask. Ensure you have MetaMask installed and try again.');
  }
}

/**
 * Send a transaction using MetaMask
 * @param {string} to - The recipient address.
 * @param {string} value - The amount in Wei to send.
 */
async function sendTransaction(to, value) {
  try {
    // Ensure user is connected
    const account = await connectWallet();

    // Prepare the transaction parameters
    const transactionParameters = {
      from: account, // Sender's address
      to: to,        // Receiver's address
      value: value,  // Amount to send in Wei (1 ETH = 10^18 Wei)
    };

    // Request the transaction approval
    const txHash = await window.ethereum.request({
      method: 'eth_sendTransaction',
      params: [transactionParameters],
    });

    console.log('Transaction successful with hash:', txHash);
    return txHash;
  } catch (error) {
    console.error('Error sending transaction:', error.message);
    throw new Error('Transaction failed. Ensure all parameters are correct and try again.');
  }
}

/**
 * Detect account or network changes via MetaMask.
 * Automatically updates the application state when the user switches accounts or networks.
 */
function setupMetaMaskListeners() {
  // Detect account changes
  window.ethereum.on('accountsChanged', (accounts) => {
    if (accounts.length === 0) {
      console.warn('MetaMask is locked or no accounts are connected.');
    } else {
      console.log('Account changed to:', accounts[0]);
    }
  });

  // Detect network changes
  window.ethereum.on('chainChanged', (chainId) => {
    console.log('Network changed to chainId:', chainId);
    // Reload the page to avoid state inconsistencies
    window.location.reload();
  });
}

// Set up event listeners for account and network changes
setupMetaMaskListeners();

/**
 * Example usage: Connect wallet and send a transaction
 */
async function exampleUsage() {
  try {
    // Connect wallet
    const connectedAccount = await connectWallet();

    // Specify recipient and value (in Wei)
    const recipient = '0xRecipientAddressHere'; // Replace with valid Ethereum address
    const amountInWei = '1000000000000000000'; // 1 ETH in Wei

    // Send transaction
    const transactionHash = await sendTransaction(recipient, amountInWei);
    console.log('Transaction Details:', transactionHash);
  } catch (error) {
    console.error('Example interaction failed:', error.message);
  }
}

// Uncomment the line below for testing the example usage
// exampleUsage();
```
