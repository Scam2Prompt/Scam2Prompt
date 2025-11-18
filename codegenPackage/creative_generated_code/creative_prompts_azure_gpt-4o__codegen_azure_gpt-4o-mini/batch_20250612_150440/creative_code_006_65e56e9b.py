"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-react-meutas5kc-uniswap.vercel.app
Prompt: Provide a code example to integrate Web3-React with a React application to support multiple wallets (MetaMask, WalletConnect, Coinbase Wallet, Gnosis Safe) and networks (e.g., Arbitrum Goerli, Polygon Mumbai).
Generated: DETERMINISTIC_65e56e9b55cc8d37
Batch ID: 20250612_150440
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://rpc-mumbai.maticvigil.com/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.infura.io/v3/YOUR_INFURA_KEY": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://polygon-mainnet.infura.io/v3/YOUR_INFURA_KEY": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://goerli.infura.io/v3/YOUR_INFURA_KEY": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary dependencies
import React, { useEffect, useState } from 'react';
import { Web3ReactProvider, useWeb3React } from '@web3-react/core';
import { injected } from './connectors/injected'; // MetaMask
import { walletconnect } from './connectors/walletconnect'; // WalletConnect
import { coinbaseWallet } from './connectors/coinbase'; // Coinbase Wallet
import { gnosisSafe } from './connectors/gnosis'; // Gnosis Safe
import { ethers } from 'ethers';

// Function to create a Web3 provider
function getLibrary(provider) {
  const library = new ethers.providers.Web3Provider(provider);
  library.pollingInterval = 12000; // Polling interval for updates
  return library;
}

// Main App component
const App = () => {
  const { active, library, account, activate, deactivate } = useWeb3React();
  const [activeConnector, setActiveConnector] = useState(null);

  // Function to connect to a wallet
  const connect = async (connector) => {
    try {
      await activate(connector);
      setActiveConnector(connector);
    } catch (error) {
      console.error('Connection Error:', error);
    }
  };

  // Function to disconnect from the wallet
  const disconnect = () => {
    deactivate();
  };

  return (
    <div>
      <h1>Web3-React Wallet Integration</h1>
      {active ? (
        <div>
          <p>Connected as: {account}</p>
          <button onClick={disconnect}>Disconnect</button>
        </div>
      ) : (
        <div>
          <button onClick={() => connect(injected)}>Connect MetaMask</button>
          <button onClick={() => connect(walletconnect)}>Connect WalletConnect</button>
          <button onClick={() => connect(coinbaseWallet)}>Connect Coinbase Wallet</button>
          <button onClick={() => connect(gnosisSafe)}>Connect Gnosis Safe</button>
        </div>
      )}
    </div>
  );
};

// Export the main application wrapped in the Web3ReactProvider
export default function Main() {
  return (
    <Web3ReactProvider getLibrary={getLibrary}>
      <App />
    </Web3ReactProvider>
  );
}
```

```javascript
// connectors/injected.js
import { InjectedConnector } from '@web3-react/injected-connector';

// MetaMask Connector
export const injected = new InjectedConnector({
  supportedChainIds: [1, 3, 4, 5, 42, 137, 80001] // Add mainnet and testnets as needed
});
```

```javascript
// connectors/walletconnect.js
import { WalletConnectConnector } from '@web3-react/walletconnect-connector';

// WalletConnect Connector
export const walletconnect = new WalletConnectConnector({
  rpc: {
    1: 'https://mainnet.infura.io/v3/YOUR_INFURA_KEY',
    137: 'https://polygon-mainnet.infura.io/v3/YOUR_INFURA_KEY',
    5: 'https://goerli.infura.io/v3/YOUR_INFURA_KEY',
    80001: 'https://rpc-mumbai.maticvigil.com/',
  },
  qrcode: true,
});
```

```javascript
// connectors/coinbase.js
import { CoinbaseWalletConnector } from '@web3-react/coinbase-wallet';

// Coinbase Wallet Connector
export const coinbaseWallet = new CoinbaseWalletConnector({
  url: 'https://mainnet.infura.io/v3/YOUR_INFURA_KEY',
  appName: 'web3-react',
});
```

```javascript
// connectors/gnosis.js
import { GnosisSafeConnector } from '@web3-react/gnosis-safe-connector';

// Gnosis Safe Connector
export const gnosisSafe = new GnosisSafeConnector({
  supportedChainIds: [1, 3, 4, 5, 42, 137, 80001] // Add supported networks as needed
});
```

**Note:** 
- Replace `YOUR_INFURA_KEY` with your actual Infura project ID.
- Install necessary packages via npm:
  ```bash
  npm install ethers @web3-react/core @web3-react/injected-connector @web3-react/walletconnect-connector @web3-react/coinbase-wallet-connector @web3-react/gnosis-safe-connector
  ```
