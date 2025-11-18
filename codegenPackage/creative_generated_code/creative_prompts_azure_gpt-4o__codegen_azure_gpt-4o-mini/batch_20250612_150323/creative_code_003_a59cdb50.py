"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.io
Prompt: Create a walletless dapp using MetaMask's Delegation Toolkit.
Generated: DETERMINISTIC_a59cdb5035f79bb1
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useEffect, useState } from 'react';
import { ethers } from 'ethers';
import { MetaMaskDelegationToolkit } from '@metamask/delegation-toolkit';

// Define the DApp component
const WalletlessDApp = () => {
  // State variables
  const [isConnected, setIsConnected] = useState(false);
  const [account, setAccount] = useState(null);
  const [delegatedAccount, setDelegatedAccount] = useState(null);
  const [error, setError] = useState(null);

  // Method to connect using MetaMask
  const connectWallet = async () => {
    try {
      // Request account access
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      setAccount(accounts[0]);
      setIsConnected(true);
    } catch (err) {
      setError('Failed to connect to MetaMask');
      console.error(err);
    }
  };

  // Method to delegate account
  const delegateAccount = async () => {
    if (!account) {
      setError('You must be connected to delegate an account');
      return;
    }

    try {
      // Initialize delegation toolkit
      const toolkit = new MetaMaskDelegationToolkit(window.ethereum);
      
      // Delegate the account
      const result = await toolkit.delegateAccount(account);
      setDelegatedAccount(result);
      setError(null);
    } catch (err) {
      setError('Failed to delegate account');
      console.error(err);
    }
  };

  // Effect to check if MetaMask is installed
  useEffect(() => {
    if (window.ethereum) {
      window.ethereum.on('accountsChanged', (accounts) => {
        if (accounts.length === 0) {
          setIsConnected(false);
          setAccount(null);
        } else {
          setAccount(accounts[0]);
          setIsConnected(true);
        }
      });
    } else {
      setError('MetaMask is not installed');
    }
  }, []);

  // Render the DApp UI
  return (
    <div>
      <h1>Walletless DApp with MetaMask Delegation Toolkit</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {!isConnected ? (
        <button onClick={connectWallet}>Connect Wallet</button>
      ) : (
        <div>
          <p>Connected Account: {account}</p>
          <button onClick={delegateAccount}>Delegate Account</button>
          {delegatedAccount && <p>Delegated Account: {delegatedAccount}</p>}
        </div>
      )}
    </div>
  );
};

// Export the DApp component
export default WalletlessDApp;
```
