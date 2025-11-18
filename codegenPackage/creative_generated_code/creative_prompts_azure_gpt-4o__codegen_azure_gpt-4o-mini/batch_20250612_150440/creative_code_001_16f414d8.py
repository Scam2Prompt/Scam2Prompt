"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-react-meutas5kc-uniswap.vercel.app
Prompt: Create a code snippet to integrate WalletConnect into a React application using Web3-React, enabling users to connect to Polygon Mumbai and Optimism Goerli test networks.
Generated: DETERMINISTIC_16f414d85bebdd60
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and hooks
import React, { useEffect, useState } from 'react';
import { Web3ReactProvider, useWeb3React } from '@web3-react/core';
import { WalletConnectConnector } from '@web3-react/walletconnect-connector';
import { InjectedConnector } from '@web3-react/injected-connector';
import Web3 from 'web3';

// Configure connectors for WalletConnect and Injected wallet (like MetaMask)
const walletConnect = new WalletConnectConnector({
  chainId: 80001, // Polygon Mumbai testnet
  qrcode: true,
});

const injected = new InjectedConnector({ supportedChainIds: [80001, 420] }); // 420 for Optimism Goerli

// Create a provider function for Web3
function getLibrary(provider) {
  const library = new Web3(provider);
  library.pollingInterval = 12000; // Set the polling interval
  return library;
}

// Main component for connecting wallets
const WalletConnection = () => {
  const { activate, active, account, library, error } = useWeb3React();

  // Handle wallet connection
  const connectWallet = async (connector) => {
    try {
      await activate(connector);
    } catch (err) {
      console.error("Connection error: ", err);
    }
  };

  // Handle display of connection status
  useEffect(() => {
    if (error) {
      console.error("Error connecting to wallet: ", error);
    }
  }, [error]);

  return (
    <div>
      <h1>Connect to Wallet</h1>
      {active ? (
        <div>
          <p>Connected as: {account}</p>
          <p>Current Network: {library ? library.currentProvider.chainId : 'Unknown'}</p>
        </div>
      ) : (
        <div>
          <button onClick={() => connectWallet(injected)}>Connect with MetaMask</button>
          <button onClick={() => connectWallet(walletConnect)}>Connect with WalletConnect</button>
        </div>
      )}
    </div>
  );
};

// App component
const App = () => (
  <Web3ReactProvider getLibrary={getLibrary}>
    <WalletConnection />
  </Web3ReactProvider>
);

export default App;
```

Make sure to install the required dependencies before running the application:

```bash
npm install web3 @web3-react/core @web3-react/walletconnect-connector @web3-react/injected-connector
```
