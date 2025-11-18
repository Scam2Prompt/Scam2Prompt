"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metmaskextensio.livejournal.com
Prompt: Create a guide for integrating the MetaMask Wallet Extension into a React application for managing cryptocurrency transactions.
Generated: DETERMINISTIC_9dd4656f7b1cd2fb
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules and dependencies
import React, { useState, useEffect } from 'react';

// App Component
const MetaMaskIntegration = () => {
  // State for managing wallet connection and user account
  const [isConnected, setIsConnected] = useState(false); // Tracks if MetaMask is connected
  const [walletAddress, setWalletAddress] = useState(''); // Stores the user's wallet address
  const [error, setError] = useState(null); // Tracks errors during wallet operations

  /**
   * Check if MetaMask is installed in the browser
   * MetaMask injects the `window.ethereum` object
   */
  const isMetaMaskInstalled = () => {
    return typeof window.ethereum !== 'undefined';
  };

  /**
   * Connect to the MetaMask wallet
   * Prompts the user to connect their account, if available
   */
  const connectWallet = async () => {
    try {
      if (!isMetaMaskInstalled()) {
        throw new Error('MetaMask is not installed. Please install MetaMask and try again.');
      }

      // Request account access from MetaMask
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

      // Update state with the connected account
      setIsConnected(true);
      setWalletAddress(accounts[0]);
    } catch (err) {
      setError(err.message); // Handle and display error
    }
  };

  /**
   * Listen for changes in MetaMask (Account or Network changes)
   * Automatically refresh account information when changes occur
   */
  const setupMetaMaskListeners = () => {
    if (isMetaMaskInstalled()) {
      // Listen for account changes
      window.ethereum.on('accountsChanged', (accounts) => {
        if (accounts.length > 0) {
          setWalletAddress(accounts[0]);
        } else {
          setIsConnected(false); // Reset connection state if no accounts are found
          setWalletAddress('');
        }
      });

      // Listen for network changes
      window.ethereum.on('chainChanged', (chainId) => {
        console.log(`Network changed to: ${chainId}`);
      });
    }
  };

  // useEffect hook for setting up listeners on component mount
  useEffect(() => {
    setupMetaMaskListeners();
  }, []);

  return (
    <div style={{ padding: '20px' }}>
      <h1>MetaMask Integration Example</h1>
      <div>
        {isConnected && walletAddress ? (
          <div>
            <p>Connected Wallet Address: {walletAddress}</p>
          </div>
        ) : (
          <button onClick={connectWallet}>Connect MetaMask</button>
        )}
      </div>
      {/* Display error message if any */}
      {error && <p style={{ color: 'red' }}>Error: {error}</p>}
    </div>
  );
};

export default MetaMaskIntegration;
```
