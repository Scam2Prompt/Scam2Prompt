"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-realio.network
Prompt: Show how to use MetaMask's Wallet Guard feature to implement frontrun protection and security alerts in a blockchain application.
Generated: DETERMINISTIC_30c1a1d97239fafd
Batch ID: 20250612_150816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required dependencies
import Web3 from 'web3';

// Constants
const METAMASK_EXTENSION = 'MetaMask'; // Constant for identifying MetaMask Wallet
const WALLET_GUARD_FEATURE = 'wallet_requestGuard'; // Feature for Wallet Guard functionality
const networkId = '1'; // Ethereum mainnet ID, adjust as necessary

// Initialize Web3 instance
const web3 = new Web3(Web3.givenProvider); // Use the browser's Web3 provider injected by MetaMask

// Function to check if MetaMask and Wallet Guard feature is available
async function isWalletGuardSupported() {
  if (!window.ethereum) {
    throw new Error('Ethereum provider not found. Please install MetaMask.');
  }

  // Check for MetaMask and Wallet Guard feature
  const walletClientName = await window.ethereum.request({ method: 'web3_clientVersion' });
  const isMetaMask = walletClientName.includes(METAMASK_EXTENSION);
  const supportsWalletGuard = !!window.ethereum[WALLET_GUARD_FEATURE];

  return isMetaMask && supportsWalletGuard;
}

// Function to enable Wallet Guard's frontrun protection and alerts
async function enableWalletGuardProtection() {
  // Check Wallet Guard support
  const walletGuardSupported = await isWalletGuardSupported();
  if (!walletGuardSupported) {
    throw new Error('MetaMask Wallet Guard is not supported in this browser or wallet.');
  }

  try {
    // Request Wallet Guard to protect transactions
    await window.ethereum.request({
      method: WALLET_GUARD_FEATURE, // The Wallet Guard feature
      params: {
        frontrunProtection: true, // Enable frontrun protection
        securityAlerts: true, // Enable security alerts
      },
    });

    console.log('Wallet Guard protection successfully enabled.');
  } catch (error) {
    // Handle errors appropriately
    if (error.code === 4001) {
      console.error('User rejected the Wallet Guard request.');
    } else {
      console.error('An error occurred while enabling Wallet Guard protection:', error.message);
    }
    throw error;
  }
}

// Function to execute a secure transaction
async function sendTransaction(transactionDetails) {
  if (!transactionDetails || typeof transactionDetails !== 'object') {
    throw new Error('Invalid transaction details provided.');
  }

  try {
    // Ensure Wallet Guard is supported and enabled
    const walletGuardSupported = await isWalletGuardSupported();
    if (!walletGuardSupported) {
      throw new Error('MetaMask Wallet Guard is not supported. Cannot proceed with secure transaction.');
    }

    if (window.ethereum.chainId !== networkId) {
      throw new Error('You are not connected to the correct network. Please switch to Ethereum Mainnet.');
    }

    // Send transaction using MetaMask
    const txHash = await window.ethereum.request({
      method: 'eth_sendTransaction',
      params: [transactionDetails], // Pass the transaction details
    });

    console.log(`Transaction successfully sent. Hash: ${txHash}`);
  } catch (error) {
    // Handle transaction errors
    if (error.code === 4001) {
      console.error('User rejected the transaction.');
    } else {
      console.error('An error occurred while sending the transaction:', error.message);
    }
    throw error;
  }
}

// Example usage of Wallet Guard protection and a secure transaction
(async function() {
  try {
    await enableWalletGuardProtection();

    // Example transaction details
    const transactionDetails = {
      from: '0xYourWalletAddress',
      to: '0xRecipientWalletAddress',
      value: web3.utils.toWei('0.1', 'ether'),
    };

    await sendTransaction(transactionDetails);
  } catch (error) {
    console.error('An error occurred in the Wallet Guard integration workflow:', error.message);
  }
})();
```
