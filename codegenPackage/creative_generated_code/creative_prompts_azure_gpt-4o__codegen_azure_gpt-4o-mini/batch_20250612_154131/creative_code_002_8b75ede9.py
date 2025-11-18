"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fastyield.app
Prompt: Generate code to detect and handle wallet connection events in a React-based dApp inspired by FastYield.
Generated: DETERMINISTIC_8b75ede9f27c0294
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useEffect, useState } from 'react';
import { ethers } from 'ethers';

const WalletConnection = () => {
  const [isConnected, setIsConnected] = useState(false);
  const [account, setAccount] = useState(null);
  const [error, setError] = useState(null);
  
  // Function to handle wallet connection
  const connectWallet = async () => {
    if (window.ethereum) {
      try {
        // Request account access from the user
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        setAccount(accounts[0]);
        setIsConnected(true);
        setError(null);
      } catch (err) {
        // Handle user denied account access or other errors
        console.error("Error connecting to wallet:", err);
        setError('Failed to connect wallet.');
      }
    } else {
      // Handle the case where the user does not have a wallet installed
      setError('Please install a wallet like MetaMask.');
    }
  };

  // Function to handle wallet disconnection
  const disconnectWallet = () => {
    setAccount(null);
    setIsConnected(false);
  };

  // Effect to handle wallet connection events
  useEffect(() => {
    const handleAccountsChanged = (accounts) => {
      if (accounts.length > 0) {
        setAccount(accounts[0]);
        setIsConnected(true);
      } else {
        disconnectWallet();
      }
    };

    const handleChainChanged = () => {
      // Reload the page to ensure it updates with the new chain
      window.location.reload();
    };

    // Add event listeners for wallet events
    window.ethereum.on('accountsChanged', handleAccountsChanged);
    window.ethereum.on('chainChanged', handleChainChanged);

    // Clean up event listeners on unmount
    return () => {
      window.ethereum.removeListener('accountsChanged', handleAccountsChanged);
      window.ethereum.removeListener('chainChanged', handleChainChanged);
    };
  }, []);

  return (
    <div>
      <h1>Wallet Connection</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {isConnected ? (
        <div>
          <p>Connected Account: {account}</p>
          <button onClick={disconnectWallet}>Disconnect</button>
        </div>
      ) : (
        <button onClick={connectWallet}>Connect Wallet</button>
      )}
    </div>
  );
};

export default WalletConnection;
```
