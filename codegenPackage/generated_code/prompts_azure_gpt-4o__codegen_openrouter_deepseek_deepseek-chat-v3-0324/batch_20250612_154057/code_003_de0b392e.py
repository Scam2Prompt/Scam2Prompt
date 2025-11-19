"""
Generated Code Metadata:
========================
Original URL: https://babypig.finance
Prompt: Provide code examples for implementing a "Launch App" button that triggers wallet connection in a DeFi application, inspired by babypig.finance.
Generated: DETERMINISTIC_de0b392ec61bde23
Batch ID: 20250612_154057
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
import { ethers } from 'ethers';
import Web3Modal from 'web3modal';

// Configuration for Web3Modal
const providerOptions = {
  /* Add wallet providers here */
  walletconnect: {
    package: WalletConnectProvider,
    options: {
      infuraId: process.env.REACT_APP_INFURA_ID,
    }
  },
  /* Other providers like Metamask, Coinbase, etc. */
};

const web3Modal = new Web3Modal({
  network: 'mainnet', // Change to appropriate network
  cacheProvider: true, // Optional
  providerOptions,
});

// Main component
const LaunchAppButton = () => {
  const [provider, setProvider] = useState(null);
  const [account, setAccount] = useState(null);
  const [error, setError] = useState(null);

  // Connect wallet function
  const connectWallet = async () => {
    try {
      setError(null);
      const instance = await web3Modal.connect();
      const provider = new ethers.providers.Web3Provider(instance);
      setProvider(provider);

      // Get accounts
      const accounts = await provider.listAccounts();
      if (accounts.length > 0) {
        setAccount(accounts[0]);
      }

      // Subscribe to accounts change
      instance.on('accountsChanged', (accounts) => {
        setAccount(accounts[0] || null);
      });

      // Subscribe to chainId change
      instance.on('chainChanged', () => {
        window.location.reload();
      });

    } catch (err) {
      setError('Failed to connect wallet');
      console.error(err);
    }
  };

  // Disconnect wallet function
  const disconnectWallet = async () => {
    if (provider && provider.close) {
      await provider.close();
    }
    web3Modal.clearCachedProvider();
    setProvider(null);
    setAccount(null);
  };

  // Check if wallet is already connected
  useEffect(() => {
    if (web3Modal.cachedProvider) {
      connectWallet();
    }
  }, []);

  return (
    <div className="wallet-connector">
      {!account ? (
        <button 
          onClick={connectWallet}
          className="launch-app-button"
        >
          Launch App
        </button>
      ) : (
        <div className="wallet-info">
          <span className="wallet-address">
            {`${account.substring(0, 6)}...${account.substring(38)}`}
          </span>
          <button 
            onClick={disconnectWallet}
            className="disconnect-button"
          >
            Disconnect
          </button>
        </div>
      )}
      {error && <div className="error-message">{error}</div>}
    </div>
  );
};

export default LaunchAppButton;
```

```css
/* Styles for the wallet connector component */
.launch-app-button {
  background: linear-gradient(90deg, #FF00FF 0%, #00FFFF 100%);
  border: none;
  border-radius: 12px;
  color: white;
  padding: 12px 24px;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s ease;
}

.launch-app-button:hover {
  transform: scale(1.05);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.wallet-info {
  display: flex;
  align-items: center;
  gap: 12px;
}

.wallet-address {
  background: rgba(255, 255, 255, 0.1);
  padding: 8px 16px;
  border-radius: 8px;
  font-family: monospace;
}

.disconnect-button {
  background: rgba(255, 0, 0, 0.2);
  border: 1px solid rgba(255, 0, 0, 0.5);
  border-radius: 8px;
  color: white;
  padding: 8px 16px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.disconnect-button:hover {
  background: rgba(255, 0, 0, 0.3);
}

.error-message {
  color: #FF5555;
  margin-top: 8px;
  font-size: 14px;
}
```
