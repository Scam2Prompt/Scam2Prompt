"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskwallet.imweb.me
Prompt: What are the steps to implement MetaMask wallet functionality in a React app?
Generated: DETERMINISTIC_1521c5ee816a183d
Batch ID: 20250612_164158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary dependencies
import React, { useState, useEffect } from 'react';

// Main MetaMask integration component
const MetaMaskWallet = () => {
  // State variables to store wallet connection status and address
  const [isConnected, setIsConnected] = useState(false);
  const [walletAddress, setWalletAddress] = useState('');

  // Function to check if MetaMask is installed
  const isMetaMaskInstalled = () => {
    return typeof window.ethereum !== 'undefined';
  };

  // Function to handle wallet connection
  const connectWallet = async () => {
    try {
      if (!isMetaMaskInstalled()) {
        alert('MetaMask is not installed. Please install MetaMask and try again.');
        return;
      }

      // Request accounts from MetaMask
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      if (accounts.length > 0) {
        setWalletAddress(accounts[0]);
        setIsConnected(true);
      }
    } catch (error) {
      console.error('Error connecting to MetaMask:', error);
      alert('An error occurred while connecting to MetaMask.');
    }
  };

  // Function to handle account changes
  const handleAccountsChanged = (accounts) => {
    if (accounts.length > 0) {
      setWalletAddress(accounts[0]);
      setIsConnected(true);
    } else {
      setWalletAddress('');
      setIsConnected(false);
    }
  };

  // Setup MetaMask event listeners on component mount
  useEffect(() => {
    if (isMetaMaskInstalled()) {
      window.ethereum.on('accountsChanged', handleAccountsChanged);
      return () => {
        // Clean up listeners on component unmount
        window.ethereum.removeListener('accountsChanged', handleAccountsChanged);
      };
    }
  }, []);

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>MetaMask Wallet Integration</h1>
      {isConnected ? (
        <div>
          <p><strong>Wallet Address:</strong> {walletAddress}</p>
          <button onClick={() => connectWallet()}>Reconnect Wallet</button>
        </div>
      ) : (
        <button onClick={() => connectWallet()}>Connect MetaMask</button>
      )}
    </div>
  );
};

export default MetaMaskWallet;
```
