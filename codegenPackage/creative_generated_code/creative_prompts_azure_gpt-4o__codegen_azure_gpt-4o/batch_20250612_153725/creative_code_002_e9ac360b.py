"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabby.at
Prompt: Provide an example of using Rabby Wallet to import an existing MetaMask account and manage addresses programmatically.
Generated: DETERMINISTIC_e9ac360bc1cd492a
Batch ID: 20250612_153725
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Example of using Rabby Wallet to import an existing MetaMask account
 * and manage addresses programmatically.
 * 
 * Requirements:
 * - Rabby Wallet extension installed in the browser.
 * - MetaMask account already set up.
 * 
 * Note: Rabby Wallet and MetaMask interact with dApps through the injected `window.ethereum` object.
 */

// Ensure the code runs in a browser environment with Rabby Wallet installed.

// Function to import MetaMask account into Rabby Wallet and manage addresses
async function manageAddresses() {
  try {
    // Ensure Rabby Wallet is installed
    if (!window.ethereum || !window.ethereum.isRabby) {
      throw new Error('Rabby Wallet not detected. Please install Rabby Wallet extension.');
    }

    // Request access to the user's account(s)
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

    if (!accounts || accounts.length === 0) {
      throw new Error('No accounts found. User may have rejected the connection request.');
    }

    console.log('Accounts imported successfully:', accounts);

    // Initialize account management
    const primaryAccount = accounts[0]; // Select the first account as the main one
    console.log('Primary account:', primaryAccount);

    // Example: Fetch the balance of the primary account
    const balanceHex = await window.ethereum.request({
      method: 'eth_getBalance',
      params: [primaryAccount, 'latest'], // Address and block
    });

    // Convert balance from hexadecimal to decimal
    const balance = parseInt(balanceHex, 16) / Math.pow(10, 18); // Convert Wei to Ether
    console.log(`Balance of ${primaryAccount}: ${balance} ETH`);

    // Example: Programmatically sign a message using the imported account
    const message = 'This is a test message for signing.';
    const signedMessage = await window.ethereum.request({
      method: 'personal_sign',
      params: [message, primaryAccount], // Message and account address
    });

    console.log('Signed message:', signedMessage);

    // Example: Programmatically send a transaction
    const transactionParameters = {
      to: '0xRecipientAddressHere', // Replace with the recipient's address
      from: primaryAccount,
      value: '0x29a2241af62c0000', // Value in Wei (e.g., 0.1 ETH -> 0x29a2241af62c0000)
      gas: '0x5208', // Gas limit (e.g., 21000 -> 0x5208)
    };

    const transactionHash = await window.ethereum.request({
      method: 'eth_sendTransaction',
      params: [transactionParameters],
    });

    console.log('Transaction sent successfully. Hash:', transactionHash);

  } catch (error) {
    // Handle errors gracefully
    console.error('An error occurred:', error.message);
  }
}

// Execute the function
manageAddresses();
```
