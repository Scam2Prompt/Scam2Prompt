"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://3t2t23t32t3.pages.dev
Prompt: Provide code for integrating wallet connection functionality in a web application for OniPetz NFT campaigns.
Generated: DETERMINISTIC_d46845e0731356b5
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: walletIntegration.js

/**
 * Wallet connection functionality for OniPetz NFT campaigns.
 * This script provides functions for interacting with Ethereum wallets 
 * (like MetaMask) in a web application.
 */

import { ethers } from 'ethers';

// Check if the browser has an Ethereum provider (e.g., MetaMask)
const isEthereumAvailable = () => {
  return typeof window.ethereum !== 'undefined';
};

// Function to request wallet connection
export const connectWallet = async () => {
  try {
    if (!isEthereumAvailable()) {
      throw new Error('No Ethereum provider detected. Please install MetaMask or use a supported wallet.');
    }

    // Request accounts from the user
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    console.log('Connected account:', accounts[0]);
    return accounts[0]; // Return the first connected account
  } catch (error) {
    console.error('Error connecting wallet:', error.message);
    throw error; // Throw the error to be handled by the caller
  }
};

// Function to get the current wallet address (if connected)
export const getWalletAddress = async () => {
  try {
    if (!isEthereumAvailable()) {
      throw new Error('No Ethereum provider detected.');
    }

    const accounts = await window.ethereum.request({ method: 'eth_accounts' });
    if (accounts.length === 0) {
      throw new Error('No wallet connected. Please connect your wallet.');
    }

    console.log('Current wallet address:', accounts[0]);
    return accounts[0];
  } catch (error) {
    console.error('Error retrieving wallet address:', error.message);
    throw error; // Throw the error to be handled by the caller
  }
};

// Function to get wallet balance (ETH)
export const getWalletBalance = async () => {
  try {
    const walletAddress = await getWalletAddress();
    const provider = new ethers.providers.Web3Provider(window.ethereum);

    // Fetch the balance
    const balance = await provider.getBalance(walletAddress);
    const etherBalance = ethers.utils.formatEther(balance); // Convert balance to readable format
    console.log(`Wallet balance for ${walletAddress}: ${etherBalance} ETH`);
    return etherBalance;
  } catch (error) {
    console.error('Error fetching wallet balance:', error.message);
    throw error;
  }
};

// Function to listen for wallet account changes
export const listenForAccountChanges = (onAccountChangeCallback) => {
  if (!isEthereumAvailable()) {
    console.warn('No Ethereum provider detected. Cannot listen for account changes.');
    return;
  }

  // Subscribe to account changes
  window.ethereum.on('accountsChanged', (accounts) => {
    console.log('Accounts changed:', accounts);
    onAccountChangeCallback(accounts);
  });
};

// Function to listen for network changes
export const listenForNetworkChanges = (onNetworkChangeCallback) => {
  if (!isEthereumAvailable()) {
    console.warn('No Ethereum provider detected. Cannot listen for network changes.');
    return;
  }

  // Subscribe to network changes
  window.ethereum.on('chainChanged', (chainId) => {
    console.log('Network changed to chain ID:', chainId);
    onNetworkChangeCallback(chainId);
  });
};

// Example usage:
// Uncomment the lines below to test the functionality in your application

// (async () => {
//   try {
//     const walletAddress = await connectWallet();
//     console.log('Wallet connected:', walletAddress);

//     const balance = await getWalletBalance();
//     console.log('Wallet balance:', balance);

//     listenForAccountChanges((accounts) => {
//       console.log('Connected accounts changed:', accounts);
//     });

//     listenForNetworkChanges((chainId) => {
//       console.log('Network changed:', chainId);
//     });
//   } catch (error) {
//     console.error('Error:', error.message);
//   }
// })();
```

This code is designed for integrating wallet connection functionality in a web application for OniPetz NFT campaigns. It covers wallet connection, retrieving wallet address and balance, and listening for account/network changes. Ensure that you have installed the `ethers` package (`npm install ethers`) to use this code.
