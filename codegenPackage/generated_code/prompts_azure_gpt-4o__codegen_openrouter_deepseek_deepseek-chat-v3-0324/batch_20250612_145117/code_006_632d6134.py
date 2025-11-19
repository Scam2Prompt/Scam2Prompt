"""
Generated Code Metadata:
========================
Original URL: https://draco.finance
Prompt: Provide a step-by-step guide for integrating a wallet connection button into a decentralized finance app, inspired by the user flow on draco.finance.
Generated: DETERMINISTIC_632d6134c8b5f165
Batch ID: 20250612_145117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// WalletConnectionButton.js
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import Web3Modal from 'web3modal';
import WalletConnectProvider from '@walletconnect/web3-provider';

// Supported wallet providers configuration
const providerOptions = {
  walletconnect: {
    package: WalletConnectProvider,
    options: {
      infuraId: process.env.REACT_APP_INFURA_ID, // Replace with your Infura ID
    },
  },
};

const web3Modal = new Web3Modal({
  cacheProvider: true, // optional
  providerOptions, // required
});

const WalletConnectionButton = () => {
  const [account, setAccount] = useState('');
  const [provider, setProvider] = useState(null);
  const [chainId, setChainId] = useState(null);
  const [error, setError] = useState('');

  // Connect wallet handler
  const connectWallet = async () => {
    try {
      setError('');
      const instance = await web3Modal.connect();
      const provider = new ethers.providers.Web3Provider(instance);
      const signer = provider.getSigner();
      const address = await signer.getAddress();
      const network = await provider.getNetwork();

      setProvider(provider);
      setAccount(address);
      setChainId(network.chainId);

      // Subscribe to accounts change
      instance.on('accountsChanged', (accounts) => {
        setAccount(accounts[0] || '');
      });

      // Subscribe to chainId change
      instance.on('chainChanged', (chainId) => {
        setChainId(parseInt(chainId, 16));
      });

    } catch (err) {
      console.error('Wallet connection error:', err);
      setError('Failed to connect wallet. Please try again.');
    }
  };

  // Disconnect wallet handler
  const disconnectWallet = async () => {
    if (provider && provider.close) {
      await provider.close();
    }
    web3Modal.clearCachedProvider();
    setAccount('');
    setProvider(null);
    setChainId(null);
  };

  // Check if wallet is already connected
  useEffect(() => {
    if (web3Modal.cachedProvider) {
      connectWallet();
    }
  }, []);

  return (
    <div className="wallet-connection">
      {account ? (
        <div className="connected-wallet">
          <span className="wallet-address">
            {`${account.substring(0, 6)}...${account.substring(account.length - 4)}`}
          </span>
          <button onClick={disconnectWallet} className="disconnect-button">
            Disconnect
          </button>
        </div>
      ) : (
        <button onClick={connectWallet} className="connect-button">
          Connect Wallet
        </button>
      )}
      {error && <div className="error-message">{error}</div>}
    </div>
  );
};

export default WalletConnectionButton;
```

```css
/* WalletConnectionButton.css */
.wallet-connection {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.connect-button, .disconnect-button {
  padding: 10px 20px;
  border: none;
  border-radius: 8px;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s ease;
}

.connect-button {
  background-color: #4CAF50;
  color: white;
}

.connect-button:hover {
  background-color: #45a049;
}

.disconnect-button {
  background-color: #f44336;
  color: white;
  margin-left: 10px;
}

.disconnect-button:hover {
  background-color: #d32f2f;
}

.connected-wallet {
  display: flex;
  align-items: center;
}

.wallet-address {
  background-color: #f1f1f1;
  padding: 8px 12px;
  border-radius: 8px;
  font-family: monospace;
}

.error-message {
  color: #f44336;
  margin-top: 10px;
  font-size: 14px;
}
```

```javascript
// App.js (Example usage)
import React from 'react';
import './App.css';
import WalletConnectionButton from './WalletConnectionButton';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>DeFi Application</h1>
        <WalletConnectionButton />
      </header>
    </div>
  );
}

export default App;
```

```javascript
// index.js (Main entry point)
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

reportWebVitals();
```
