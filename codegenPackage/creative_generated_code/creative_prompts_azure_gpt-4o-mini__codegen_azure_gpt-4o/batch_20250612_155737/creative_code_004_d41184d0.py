"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eng-metamask-cdn.teachable.com
Prompt: Explain how to handle Metamask events in a React app when a user connects their wallet.
Generated: DETERMINISTIC_d41184d0eb7d9221
Batch ID: 20250612_155737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary dependencies
import React, { useState, useEffect } from 'react';

const MetamaskIntegration = () => {
  // State to store wallet connection status and account information
  const [walletConnected, setWalletConnected] = useState(false);
  const [account, setAccount] = useState(null);

  // Function to check if Metamask is installed
  const isMetamaskInstalled = () => {
    return typeof window.ethereum !== 'undefined';
  };

  // Function to connect wallet
  const connectWallet = async () => {
    try {
      if (!isMetamaskInstalled()) {
        alert('Metamask is not installed. Please install Metamask and try again.');
        return;
      }

      // Request wallet connection
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      setAccount(accounts[0]); // Set the first connected account
      setWalletConnected(true);
    } catch (error) {
      console.error('Error connecting wallet:', error);
      alert('Failed to connect wallet. Please try again.');
    }
  };

  // Function to handle account change event
  const handleAccountsChanged = (accounts) => {
    if (accounts.length === 0) {
      // Wallet is disconnected
      setWalletConnected(false);
      setAccount(null);
    } else {
      // Update the account state
      setAccount(accounts[0]);
      setWalletConnected(true);
    }
  };

  // Function to handle chain change event
  const handleChainChanged = (chainId) => {
    console.log('Chain changed to:', chainId);
    // Reload the app to handle the new chain
    window.location.reload();
  };

  // Effect to listen for Metamask events
  useEffect(() => {
    if (isMetamaskInstalled()) {
      // Listen for account change events
      window.ethereum.on('accountsChanged', handleAccountsChanged);

      // Listen for chain change events
      window.ethereum.on('chainChanged', handleChainChanged);

      // Cleanup event listeners on component unmount
      return () => {
        window.ethereum.removeListener('accountsChanged', handleAccountsChanged);
        window.ethereum.removeListener('chainChanged', handleChainChanged);
      };
    }
  }, []);

  return (
    <div>
      <h1>Metamask Wallet Integration</h1>
      {walletConnected ? (
        <div>
          <p>Wallet Connected</p>
          <p>Account: {account}</p>
        </div>
      ) : (
        <button onClick={connectWallet}>Connect Wallet</button>
      )}
    </div>
  );
};

export default MetamaskIntegration;
```
