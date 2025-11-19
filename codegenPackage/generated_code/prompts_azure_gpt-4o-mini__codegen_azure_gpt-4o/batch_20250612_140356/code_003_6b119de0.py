"""
Generated Code Metadata:
========================
Original URL: https://berachain-frontend.vercel.app
Prompt: Explain how to handle wallet disconnection in the Berachain frontend when using MetaMask.
Generated: DETERMINISTIC_6b119de074cf3727
Batch ID: 20250612_140356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';

// WalletDisconnectionHandler Component
const WalletDisconnectionHandler = () => {
  // State to track wallet connection status
  const [isWalletConnected, setIsWalletConnected] = useState(false);
  const [walletAddress, setWalletAddress] = useState(null);

  // Function to handle wallet connection
  const connectWallet = async () => {
    try {
      if (window.ethereum) {
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        setWalletAddress(accounts[0]);
        setIsWalletConnected(true);
      } else {
        console.error('MetaMask is not installed.');
        alert('Please install MetaMask to connect your wallet.');
      }
    } catch (error) {
      console.error('Error connecting wallet:', error);
      alert('Failed to connect wallet. Please try again.');
    }
  };

  // Function to handle wallet disconnection
  const disconnectWallet = () => {
    setWalletAddress(null);
    setIsWalletConnected(false);
    console.log('Wallet disconnected successfully.');
  };

  // Effect to handle wallet disconnection when MetaMask account changes
  useEffect(() => {
    if (window.ethereum) {
      const handleAccountsChanged = (accounts) => {
        if (accounts.length === 0) {
          // No accounts available, wallet disconnected
          disconnectWallet();
        } else {
          // Wallet connected with a new account
          setWalletAddress(accounts[0]);
          setIsWalletConnected(true);
        }
      };

      // Listen for account changes
      window.ethereum.on('accountsChanged', handleAccountsChanged);

      // Cleanup listener on component unmount
      return () => {
        window.ethereum.removeListener('accountsChanged', handleAccountsChanged);
      };
    }
  }, []);

  return (
    <div>
      <h1>Berachain Wallet Connection</h1>
      {isWalletConnected ? (
        <div>
          <p>Wallet Address: {walletAddress}</p>
          <button onClick={disconnectWallet}>Disconnect Wallet</button>
        </div>
      ) : (
        <button onClick={connectWallet}>Connect Wallet</button>
      )}
    </div>
  );
};

export default WalletDisconnectionHandler;
```
