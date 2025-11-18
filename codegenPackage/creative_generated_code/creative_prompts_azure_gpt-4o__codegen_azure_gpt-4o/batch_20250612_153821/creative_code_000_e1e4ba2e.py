"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miden.cloud
Prompt: Write code to integrate the Leo Wallet WebClient SDK into a decentralized finance (DeFi) application, as described in the Miden ecosystem documentation.
Generated: DETERMINISTIC_e1e4ba2e36899e91
Batch ID: 20250612_153821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules and SDK
import { LeoWalletWebClient } from 'leo-wallet-webclient-sdk';

// Initialize Leo Wallet WebClient instance
const leoWallet = new LeoWalletWebClient({
  environment: 'mainnet', // Specify environment: 'mainnet' or 'testnet'
  appId: 'your-app-id',   // Replace with your application ID
});

// Function to connect to the Leo Wallet
async function connectWallet() {
  try {
    // Request user to connect their wallet
    const connection = await leoWallet.connect();
    console.log('Wallet connected successfully:', connection);
    return connection;
  } catch (error) {
    console.error('Error connecting to wallet:', error);
    throw new Error('Wallet connection failed. Please try again.');
  }
}

// Function to fetch the user's wallet addresses
async function getWalletAddresses() {
  try {
    const addresses = await leoWallet.getAddresses();
    console.log('Wallet addresses:', addresses);
    return addresses;
  } catch (error) {
    console.error('Error fetching wallet addresses:', error);
    throw new Error('Unable to retrieve wallet addresses.');
  }
}

// Function to initiate a transaction on the Miden ecosystem
async function initiateTransaction(toAddress, amount, token) {
  try {
    // Check if wallet is connected
    const walletStatus = await leoWallet.getStatus();
    if (!walletStatus.connected) {
      throw new Error('Wallet is not connected. Please connect your wallet first.');
    }

    // Create and sign the transaction
    const transaction = await leoWallet.createTransaction({
      to: toAddress,  // Recipient's wallet address
      value: amount,  // Amount to transfer
      assetId: token, // Token or asset identifier
    });

    // Send the transaction
    const txHash = await leoWallet.sendTransaction(transaction);
    console.log('Transaction sent successfully. Hash:', txHash);
    return txHash;
  } catch (error) {
    console.error('Error initiating transaction:', error);
    throw new Error('Transaction failed.');
  }
}

// Function to disconnect the wallet
async function disconnectWallet() {
  try {
    const result = await leoWallet.disconnect();
    console.log('Wallet disconnected successfully:', result);
    return result;
  } catch (error) {
    console.error('Error disconnecting the wallet:', error);
    throw new Error('Failed to disconnect wallet.');
  }
}

// Example usage
(async () => {
  try {
    // Connect the wallet
    const connection = await connectWallet();

    // Fetch wallet addresses
    const addresses = await getWalletAddresses();

    // Initiate a transaction
    const txHash = await initiateTransaction(
      'recipient-wallet-address', // Replace with recipient's address
      10,                         // Amount to transfer
      'token-id'                  // Replace with the token or asset ID
    );

    console.log('Transaction hash:', txHash);

    // Disconnect the wallet
    await disconnectWallet();
  } catch (error) {
    console.error('Error:', error.message);
  }
})();
```

This code integrates the Leo Wallet WebClient SDK into a DeFi application, following all requested best practices. Be sure to replace placeholders like `'your-app-id'`, `'recipient-wallet-address'`, and `'token-id'` with your specific application values.
