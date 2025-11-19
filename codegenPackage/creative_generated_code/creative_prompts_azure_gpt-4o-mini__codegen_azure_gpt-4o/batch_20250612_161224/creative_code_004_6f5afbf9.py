"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaske.com.cn
Prompt: Describe the process of using MetaMask as a browser extension to interact with decentralized applications (DApps).
Generated: DETERMINISTIC_6f5afbf98a5b52dd
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * This code demonstrates how to use MetaMask as a browser extension
 * to interact with decentralized applications (DApps).
 * It includes connecting to MetaMask, requesting an account address,
 * and sending a transaction.
 */

// Check if MetaMask is installed
if (typeof window.ethereum === 'undefined') {
  console.error('MetaMask is not installed. Please install MetaMask to use this DApp.');
} else {
  console.log('MetaMask is detected!');
}

/**
 * Connect to MetaMask and request user's account.
 */
async function connectToMetaMask() {
  try {
    // Request account access
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

    // Use the first account returned by MetaMask
    const userAccount = accounts[0];
    console.log('Connected account:', userAccount);

    return userAccount;
  } catch (error) {
    console.error('Failed to connect to MetaMask:', error);
    throw error; // Rethrow the error for further handling if needed
  }
}

/**
 * Send a transaction using MetaMask.
 * @param {string} to - The recipient address.
 * @param {string} value - The amount of ether to send (in wei format).
 */
async function sendTransaction(to, value) {
  try {
    // Ensure MetaMask is available
    if (typeof window.ethereum === 'undefined') {
      throw new Error('MetaMask is not available.');
    }

    // Get the user's connected account
    const userAccount = await connectToMetaMask();

    // Prepare transaction parameters
    const transactionParameters = {
      from: userAccount, // Sender address
      to: to,           // Recipient address
      value: value,     // Amount to send (in wei)
    };

    // Send the transaction
    const txHash = await window.ethereum.request({
      method: 'eth_sendTransaction',
      params: [transactionParameters],
    });

    console.log('Transaction sent successfully! Transaction hash:', txHash);
    return txHash;
  } catch (error) {
    console.error('Failed to send transaction:', error);
    throw error; // Rethrow the error for further handling if needed
  }
}

/**
 * Listen for account changes in MetaMask.
 */
window.ethereum.on('accountsChanged', (accounts) => {
  console.log('Accounts changed:', accounts);

  if (accounts.length > 0) {
    console.log('Active account:', accounts[0]);
  } else {
    console.warn('No accounts are connected.');
  }
});

/**
 * Listen for network changes in MetaMask.
 */
window.ethereum.on('chainChanged', (chainId) => {
  console.log('Network changed. Current chain ID:', chainId);
  // Reload the page to ensure DApp behaves correctly on the new network
  window.location.reload();
});

/**
 * Example usage
 */
(async function exampleUsage() {
  try {
    const userAccount = await connectToMetaMask();
    console.log('User connected:', userAccount);

    // Example transaction: Send 0.01 ETH (in wei) to a recipient address
    const recipientAddress = '0xRecipientAddressHere'; // Replace with actual recipient address
    const amountInWei = '10000000000000000'; // 0.01 ETH in wei
    const txHash = await sendTransaction(recipientAddress, amountInWei);
    console.log('Transaction hash:', txHash);
  } catch (error) {
    console.error('Error in example usage:', error);
  }
})();
```
