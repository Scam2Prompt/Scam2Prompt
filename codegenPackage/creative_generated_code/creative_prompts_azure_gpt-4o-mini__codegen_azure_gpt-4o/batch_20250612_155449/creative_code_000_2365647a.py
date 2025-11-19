"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.earthmeta.xyzapp.net
Prompt: How can I implement a wallet connection feature for the EarthMeta platform using MetaMask or Trust Wallet?
Generated: DETERMINISTIC_2365647ae3207c60
Batch ID: 20250612_155449
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// walletConnection.js
// This script implements a wallet connection feature for the EarthMeta platform using MetaMask or Trust Wallet.
// Requires a web3 provider (e.g., MetaMask or Trust Wallet) installed in the user's browser.

// Import web3.js library (ensure this is installed using npm or a CDN)
import Web3 from 'web3';

// Initialize Web3 instance
let web3;

// Utility function to detect if a web3 provider is available
const isWeb3ProviderAvailable = () => {
  return typeof window.ethereum !== 'undefined';
};

// Function to connect wallet and retrieve account information
export async function connectWallet() {
  try {
    // Check if web3 provider is available
    if (!isWeb3ProviderAvailable()) {
      throw new Error('No web3 provider detected. Please install MetaMask or Trust Wallet.');
    }

    // Initialize the Web3 instance using the provider injected by the wallet
    web3 = new Web3(window.ethereum);

    // Request access to the user's wallet
    await window.ethereum.request({ method: 'eth_requestAccounts' });

    // Get the list of accounts connected to the wallet
    const accounts = await web3.eth.getAccounts();

    if (accounts.length === 0) {
      throw new Error('No accounts found. Please ensure your wallet is properly configured.');
    }

    // Get the connected wallet's address (first account)
    const walletAddress = accounts[0];

    // Retrieve the current network ID
    const networkId = await web3.eth.net.getId();

    // Return connection details
    return {
      walletAddress,
      networkId,
    };
  } catch (err) {
    console.error('Error connecting to wallet:', err.message);

    // Return an error object
    return {
      error: true,
      message: err.message,
    };
  }
}

// Function to disconnect wallet (clears any session data, if implemented)
export function disconnectWallet() {
  // Since web3 connections are session-based, there isn't a direct "disconnect" method.
  // However, you can clear any UI state or locally stored wallet data.
  web3 = null;
  console.log('Wallet disconnected.');
}

// Example usage (to be integrated into the EarthMeta platform's frontend):
// async function initWalletConnection() {
//   const connectionResult = await connectWallet();
//   if (connectionResult.error) {
//     console.error('Wallet connection failed:', connectionResult.message);
//   } else {
//     console.log('Wallet connected:', connectionResult.walletAddress);
//     console.log('Network ID:', connectionResult.networkId);
//   }
// }
```
