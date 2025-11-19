"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mttamskkwlltextsn.gitbook.io
Prompt: How can I use MetaMask to manage my Ethereum-based assets and interact with DApps securely?
Generated: DETERMINISTIC_bb087d1f3221f462
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
 * This script demonstrates how to interact with MetaMask for managing Ethereum-based assets
 * and interacting with decentralized applications (DApps) securely.
 * 
 * Requirements:
 * - MetaMask extension installed in the browser.
 * - A DApp serving this script in a web environment.
 */

// Check if MetaMask is installed
if (typeof window.ethereum === 'undefined') {
  console.error('MetaMask is not installed. Please install MetaMask to proceed.');
} else {
  console.log('MetaMask detected.');
}

// Function to request access to MetaMask account
async function connectToMetaMask() {
  try {
    // Request accounts through MetaMask
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

    // Display the connected account
    console.log('Connected account:', accounts[0]);
    return accounts[0];
  } catch (error) {
    console.error('Failed to connect to MetaMask:', error);
    throw error;
  }
}

// Function to retrieve the current Ethereum network
async function getCurrentNetwork() {
  try {
    // Query the network ID
    const networkId = await window.ethereum.request({ method: 'net_version' });

    console.log('Current network ID:', networkId);
    return networkId;
  } catch (error) {
    console.error('Failed to retrieve network information:', error);
    throw error;
  }
}

// Function to send a transaction using MetaMask
async function sendTransaction(sender, recipient, amount) {
  try {
    // Create a transaction object
    const transactionParams = {
      from: sender,
      to: recipient,
      value: amount, // Value must be in hexadecimal Wei
    };

    // Request MetaMask to send the transaction
    const txHash = await window.ethereum.request({
      method: 'eth_sendTransaction',
      params: [transactionParams],
    });

    console.log('Transaction sent successfully. Transaction Hash:', txHash);
    return txHash;
  } catch (error) {
    console.error('Failed to send transaction:', error);
    throw error;
  }
}

// Event listener for account changes
window.ethereum.on('accountsChanged', (accounts) => {
  console.log('Accounts changed:', accounts);
  if (accounts.length === 0) {
    console.warn('MetaMask is locked or the user is not connected.');
  } else {
    console.log('Connected account changed to:', accounts[0]);
  }
});

// Event listener for network changes
window.ethereum.on('chainChanged', (chainId) => {
  console.log('Network changed. New Chain ID:', chainId);
  // Reload the page to prevent issues with stale data
  window.location.reload();
});

// Example usage:
(async () => {
  // Connect to MetaMask
  const account = await connectToMetaMask();

  // Get current network
  const networkId = await getCurrentNetwork();

  // Example transaction (use with caution, this sends real ETH)
  // const recipient = '0xRecipientAddressHere'; // Replace with valid recipient address
  // const amountInWeiHex = '0xAmountHere'; // Replace with valid amount in hexadecimal Wei
  // await sendTransaction(account, recipient, amountInWeiHex);

  // Note: Uncomment the above lines and provide valid values to send a transaction.
})();
```
