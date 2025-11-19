"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rascal-land-nextjs-mint.vercel.app
Prompt: How can I integrate a wallet connection feature in a Next.js application for NFT projects?
Generated: DETERMINISTIC_2f2f11b347e7b538
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// walletConnection.js
// This file contains functionality for integrating a wallet connection feature in a Next.js application

import { useState, useEffect } from 'react';
import detectEthereumProvider from '@metamask/detect-provider';
import Web3 from 'web3';

// WalletConnection Component
const WalletConnection = () => {
  const [walletAddress, setWalletAddress] = useState(null);
  const [errorMessage, setErrorMessage] = useState('');

  // Check if MetaMask is installed and connect to wallet
  const connectWallet = async () => {
    try {
      const provider = await detectEthereumProvider();

      if (provider) {
        const web3 = new Web3(provider);

        // Request account access
        const accounts = await provider.request({ method: 'eth_requestAccounts' });
        setWalletAddress(accounts[0]); // Set the first account as the connected wallet
      } else {
        throw new Error('MetaMask not found. Please install MetaMask to connect your wallet.');
      }
    } catch (error) {
      setErrorMessage(error.message || 'An error occurred while connecting to the wallet.');
    }
  };

  // Disconnect wallet
  const disconnectWallet = () => {
    setWalletAddress(null);
    setErrorMessage('');
  };

  // Automatically detect account changes
  useEffect(() => {
    const handleAccountsChanged = (accounts) => {
      if (accounts.length > 0) {
        setWalletAddress(accounts[0]);
      } else {
        // No accounts available, handle disconnect
        disconnectWallet();
      }
    };

    // Detect provider and add listener for account changes
    const init = async () => {
      const provider = await detectEthereumProvider();
      if (provider) {
        provider.on('accountsChanged', handleAccountsChanged);
      }
    };

    init();

    // Cleanup listener on component unmount
    return () => {
      const provider = window.ethereum; // Assumption: MetaMask is injected into `window.ethereum`
      if (provider) {
        provider.removeListener('accountsChanged', handleAccountsChanged);
      }
    };
  }, []);

  return (
    <div>
      {/* Display wallet connection status */}
      <h2>Wallet Connection</h2>
      {walletAddress ? (
        <div>
          <p>Connected Wallet: {walletAddress}</p>
          <button onClick={disconnectWallet}>Disconnect Wallet</button>
        </div>
      ) : (
        <div>
          <p>No wallet connected.</p>
          <button onClick={connectWallet}>Connect Wallet</button>
        </div>
      )}

      {/* Display error message if any */}
      {errorMessage && <p style={{ color: 'red' }}>{errorMessage}</p>}
    </div>
  );
};

export default WalletConnection;

// pages/index.js
// Import the WalletConnection component and render it in the Next.js app

import WalletConnection from '../components/walletConnection';

export default function Home() {
  return (
    <div>
      <h1>NFT Project</h1>
      <WalletConnection />
    </div>
  );
}
```
