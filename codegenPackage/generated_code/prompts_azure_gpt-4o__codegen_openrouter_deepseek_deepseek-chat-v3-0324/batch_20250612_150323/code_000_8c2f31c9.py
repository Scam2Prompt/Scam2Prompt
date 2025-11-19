"""
Generated Code Metadata:
========================
Original URL: https://web3modal.com
Prompt: Write a React component that integrates Reown's AppKit to enable web3 wallet login for users, supporting 500+ wallet providers as described on the Web3Modal website.
Generated: DETERMINISTIC_8c2f31c94737f387
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import Web3Modal from 'web3modal';
import WalletConnectProvider from '@walletconnect/web3-provider';
import { ethers } from 'ethers';

// Configuration for Web3Modal
const providerOptions = {
  walletconnect: {
    package: WalletConnectProvider,
    options: {
      infuraId: process.env.REACT_APP_INFURA_ID, // Replace with your Infura ID
    }
  },
  // Other wallet providers can be added here
};

const web3Modal = new Web3Modal({
  cacheProvider: true, // optional
  providerOptions, // required
  theme: 'dark', // optional
});

const Web3Login = () => {
  const [provider, setProvider] = useState(null);
  const [account, setAccount] = useState(null);
  const [error, setError] = useState(null);
  const [isConnecting, setIsConnecting] = useState(false);

  // Connect to wallet
  const connectWallet = async () => {
    try {
      setIsConnecting(true);
      setError(null);
      
      const instance = await web3Modal.connect();
      const web3Provider = new ethers.providers.Web3Provider(instance);
      
      // Subscribe to accounts change
      instance.on('accountsChanged', (accounts) => {
        setAccount(accounts[0] || null);
      });

      // Subscribe to chainId change
      instance.on('chainChanged', (chainId) => {
        window.location.reload();
      });

      // Subscribe to provider disconnection
      instance.on('disconnect', (error) => {
        disconnectWallet();
        setError(error);
      });

      const accounts = await web3Provider.listAccounts();
      setProvider(web3Provider);
      setAccount(accounts[0] || null);
    } catch (err) {
      console.error('Error connecting wallet:', err);
      setError(err.message || 'Failed to connect wallet');
    } finally {
      setIsConnecting(false);
    }
  };

  // Disconnect wallet
  const disconnectWallet = () => {
    if (provider?.provider?.disconnect) {
      provider.provider.disconnect();
    }
    web3Modal.clearCachedProvider();
    setProvider(null);
    setAccount(null);
  };

  // Auto-connect if cached provider exists
  useEffect(() => {
    if (web3Modal.cachedProvider) {
      connectWallet();
    }
  }, []);

  return (
    <div className="web3-login-container">
      {error && (
        <div className="error-message">
          {error}
        </div>
      )}

      {!account ? (
        <button 
          onClick={connectWallet} 
          disabled={isConnecting}
          className="connect-button"
        >
          {isConnecting ? 'Connecting...' : 'Connect Wallet'}
        </button>
      ) : (
        <div className="wallet-info">
          <p>Connected: {`${account.substring(0, 6)}...${account.substring(account.length - 4)}`}</p>
          <button 
            onClick={disconnectWallet}
            className="disconnect-button"
          >
            Disconnect
          </button>
        </div>
      )}
    </div>
  );
};

export default Web3Login;
```
