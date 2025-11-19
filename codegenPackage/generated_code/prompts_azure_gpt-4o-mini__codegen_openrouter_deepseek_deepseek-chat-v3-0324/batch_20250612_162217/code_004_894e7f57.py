"""
Generated Code Metadata:
========================
Original URL: https://v0-uniswap-clone-project.vercel.app
Prompt: How do I set up a user interface for connecting wallets in a Uniswap clone application?
Generated: DETERMINISTIC_894e7f57482049c0
Batch ID: 20250612_162217
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// WalletConnector.tsx
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

// Create Web3Modal instance
const web3Modal = new Web3Modal({
  cacheProvider: true, // optional
  providerOptions, // required
  theme: 'dark', // optional
});

interface WalletState {
  address: string | null;
  provider: ethers.providers.Web3Provider | null;
  connected: boolean;
  chainId: number | null;
}

const WalletConnector: React.FC = () => {
  const [walletState, setWalletState] = useState<WalletState>({
    address: null,
    provider: null,
    connected: false,
    chainId: null,
  });
  const [error, setError] = useState<string | null>(null);

  // Connect wallet handler
  const connectWallet = async () => {
    try {
      setError(null);
      const instance = await web3Modal.connect();
      const provider = new ethers.providers.Web3Provider(instance);
      
      // Subscribe to accounts change
      instance.on('accountsChanged', (accounts: string[]) => {
        setWalletState(prev => ({
          ...prev,
          address: accounts[0] || null,
        }));
      });

      // Subscribe to chainId change
      instance.on('chainChanged', (chainId: string) => {
        setWalletState(prev => ({
          ...prev,
          chainId: parseInt(chainId, 16),
        }));
      });

      // Subscribe to provider disconnection
      instance.on('disconnect', (code: number, reason: string) => {
        disconnectWallet();
      });

      const signer = provider.getSigner();
      const address = await signer.getAddress();
      const network = await provider.getNetwork();

      setWalletState({
        address,
        provider,
        connected: true,
        chainId: network.chainId,
      });
    } catch (err) {
      console.error('Wallet connection error:', err);
      setError('Failed to connect wallet. Please try again.');
    }
  };

  // Disconnect wallet handler
  const disconnectWallet = () => {
    web3Modal.clearCachedProvider();
    setWalletState({
      address: null,
      provider: null,
      connected: false,
      chainId: null,
    });
  };

  // Check if wallet is already connected on component mount
  useEffect(() => {
    if (web3Modal.cachedProvider) {
      connectWallet();
    }
  }, []);

  return (
    <div className="wallet-connector">
      {error && <div className="error-message">{error}</div>}
      
      {!walletState.connected ? (
        <button onClick={connectWallet} className="connect-button">
          Connect Wallet
        </button>
      ) : (
        <div className="wallet-info">
          <span className="wallet-address">
            {`${walletState.address?.substring(0, 6)}...${walletState.address?.substring(38)}`}
          </span>
          <button onClick={disconnectWallet} className="disconnect-button">
            Disconnect
          </button>
        </div>
      )}
    </div>
  );
};

export default WalletConnector;
```

```typescript
// App.tsx
import React from 'react';
import WalletConnector from './WalletConnector';
import './App.css';

const App: React.FC = () => {
  return (
    <div className="app">
      <header className="app-header">
        <h1>Uniswap Clone</h1>
        <WalletConnector />
      </header>
    </div>
  );
};

export default App;
```

```css
/* App.css */
.app {
  text-align: center;
  min-height: 100vh;
  background-color: #282c34;
  color: white;
}

.app-header {
  padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.wallet-connector {
  margin-top: 20px;
}

.connect-button, .disconnect-button {
  background-color: #61dafb;
  border: none;
  color: #282c34;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  font-weight: bold;
  transition: background-color 0.3s;
}

.connect-button:hover, .disconnect-button:hover {
  background-color: #4fa8d3;
}

.wallet-info {
  display: flex;
  align-items: center;
  gap: 15px;
}

.wallet-address {
  background-color: #3a3f4b;
  padding: 8px 12px;
  border-radius: 5px;
  font-family: monospace;
}

.error-message {
  color: #ff6b6b;
  margin-bottom: 10px;
}
```

```json
// package.json (relevant dependencies)
{
  "dependencies": {
    "@walletconnect/web3-provider": "^1.7.8",
    "ethers": "^5.7.2",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "web3modal": "^1.9.10"
  }
}
```
