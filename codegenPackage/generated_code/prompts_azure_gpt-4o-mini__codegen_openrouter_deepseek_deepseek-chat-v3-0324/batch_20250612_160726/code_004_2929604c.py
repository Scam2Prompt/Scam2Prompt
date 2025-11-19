"""
Generated Code Metadata:
========================
Original URL: https://blubhub.app
Prompt: How do I implement a user interface for wallet connection in a project like Blub the Blob?
Generated: DETERMINISTIC_2929604c7f3ff1d7
Batch ID: 20250612_160726
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// WalletConnectionUI.js
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import './WalletConnectionUI.css';

// Supported wallet providers
const WALLET_PROVIDERS = {
  METAMASK: 'metamask',
  WALLETCONNECT: 'walletconnect',
  COINBASE: 'coinbase'
};

const WalletConnectionUI = ({ onConnect, onDisconnect }) => {
  const [currentAccount, setCurrentAccount] = useState(null);
  const [provider, setProvider] = useState(null);
  const [error, setError] = useState(null);
  const [isConnecting, setIsConnecting] = useState(false);

  // Check if wallet is connected on component mount
  useEffect(() => {
    checkWalletConnection();
    setupEventListeners();
    return () => removeEventListeners();
  }, []);

  const checkWalletConnection = async () => {
    if (window.ethereum) {
      try {
        const accounts = await window.ethereum.request({ method: 'eth_accounts' });
        if (accounts.length > 0) {
          const provider = new ethers.providers.Web3Provider(window.ethereum);
          setProvider(provider);
          setCurrentAccount(accounts[0]);
          if (onConnect) onConnect(provider, accounts[0]);
        }
      } catch (err) {
        console.error('Error checking wallet connection:', err);
        setError('Failed to check wallet connection');
      }
    }
  };

  const setupEventListeners = () => {
    if (window.ethereum) {
      window.ethereum.on('accountsChanged', handleAccountsChanged);
      window.ethereum.on('chainChanged', handleChainChanged);
    }
  };

  const removeEventListeners = () => {
    if (window.ethereum) {
      window.ethereum.removeListener('accountsChanged', handleAccountsChanged);
      window.ethereum.removeListener('chainChanged', handleChainChanged);
    }
  };

  const handleAccountsChanged = (accounts) => {
    if (accounts.length === 0) {
      handleDisconnect();
    } else {
      setCurrentAccount(accounts[0]);
      if (onConnect) onConnect(provider, accounts[0]);
    }
  };

  const handleChainChanged = () => {
    window.location.reload();
  };

  const connectWallet = async (walletType) => {
    setIsConnecting(true);
    setError(null);

    try {
      let provider;
      switch (walletType) {
        case WALLET_PROVIDERS.METAMASK:
          provider = await connectMetaMask();
          break;
        case WALLET_PROVIDERS.WALLETCONNECT:
          provider = await connectWalletConnect();
          break;
        case WALLET_PROVIDERS.COINBASE:
          provider = await connectCoinbase();
          break;
        default:
          throw new Error('Unsupported wallet type');
      }

      const signer = provider.getSigner();
      const address = await signer.getAddress();
      
      setProvider(provider);
      setCurrentAccount(address);
      if (onConnect) onConnect(provider, address);
    } catch (err) {
      console.error('Error connecting wallet:', err);
      setError(err.message || 'Failed to connect wallet');
    } finally {
      setIsConnecting(false);
    }
  };

  const connectMetaMask = async () => {
    if (!window.ethereum) {
      throw new Error('MetaMask is not installed');
    }
    
    await window.ethereum.request({ method: 'eth_requestAccounts' });
    return new ethers.providers.Web3Provider(window.ethereum);
  };

  const connectWalletConnect = async () => {
    // Implementation for WalletConnect would go here
    throw new Error('WalletConnect integration not implemented');
  };

  const connectCoinbase = async () => {
    // Implementation for Coinbase Wallet would go here
    throw new Error('Coinbase Wallet integration not implemented');
  };

  const handleDisconnect = () => {
    setCurrentAccount(null);
    setProvider(null);
    if (onDisconnect) onDisconnect();
  };

  const shortenAddress = (address) => {
    return `${address.substring(0, 6)}...${address.substring(address.length - 4)}`;
  };

  return (
    <div className="wallet-connection-container">
      {currentAccount ? (
        <div className="wallet-connected">
          <span className="wallet-address">{shortenAddress(currentAccount)}</span>
          <button onClick={handleDisconnect} className="disconnect-button">
            Disconnect
          </button>
        </div>
      ) : (
        <div className="wallet-options">
          <button
            onClick={() => connectWallet(WALLET_PROVIDERS.METAMASK)}
            disabled={isConnecting}
            className="connect-button metamask"
          >
            {isConnecting ? 'Connecting...' : 'Connect with MetaMask'}
          </button>
          {/* Additional wallet buttons would go here */}
          {error && <div className="error-message">{error}</div>}
        </div>
      )}
    </div>
  );
};

export default WalletConnectionUI;
```

```css
/* WalletConnectionUI.css */
.wallet-connection-container {
  font-family: 'Arial', sans-serif;
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border-radius: 8px;
  background-color: #f5f5f5;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.wallet-connected {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.wallet-address {
  font-weight: bold;
  color: #333;
}

.connect-button, .disconnect-button {
  padding: 10px 15px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
  transition: background-color 0.2s;
}

.connect-button {
  background-color: #f6851b;
  color: white;
}

.connect-button:hover {
  background-color: #e2761b;
}

.connect-button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

.disconnect-button {
  background-color: #ff4444;
  color: white;
}

.disconnect-button:hover {
  background-color: #cc0000;
}

.error-message {
  margin-top: 10px;
  color: #ff4444;
  font-size: 14px;
}

.metamask {
  background-color: #f6851b;
}

.metamask:hover {
  background-color: #e2761b;
}

/* Add additional wallet provider styles as needed */
```
