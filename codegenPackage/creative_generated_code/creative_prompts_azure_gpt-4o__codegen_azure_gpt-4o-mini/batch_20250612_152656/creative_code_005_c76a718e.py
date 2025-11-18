"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gblastclaim.pages.dev
Prompt: Develop a web interface using React that includes a "Connect Wallet" button for Injected, Phantom, and MetaMask wallets, based on the wallet connection options on the GBlastClaim platform.
Generated: DETERMINISTIC_c76a718e5b9138ab
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// App.js
import React, { useState } from 'react';
import { InjectedConnector } from '@web3-react/injected-connector';
import { useWeb3React } from '@web3-react/core';
import { PhantomConnector } from '@web3-react/phantom-connector';
import { MetaMaskConnector } from '@web3-react/metamask-connector';

// Define connectors for different wallets
const injected = new InjectedConnector({ supportedChainIds: [1, 3, 4, 5, 42] });
const phantom = new PhantomConnector({ supportedChainIds: [1, 3, 4, 5, 42] });
const metaMask = new MetaMaskConnector({ supportedChainIds: [1, 3, 4, 5, 42] });

const App = () => {
  const { activate, account, active, error } = useWeb3React();
  
  // Function to connect to a wallet
  const connectWallet = async (connector) => {
    try {
      await activate(connector);
    } catch (error) {
      console.error("Failed to connect wallet:", error);
    }
  };

  return (
    <div style={styles.container}>
      <h1>Connect Your Wallet</h1>
      {error && <p style={styles.error}>{error.message}</p>}
      {active ? (
        <p style={styles.success}>Connected as: {account}</p>
      ) : (
        <div>
          <button style={styles.button} onClick={() => connectWallet(injected)}>
            Connect Injected Wallet
          </button>
          <button style={styles.button} onClick={() => connectWallet(phantom)}>
            Connect Phantom Wallet
          </button>
          <button style={styles.button} onClick={() => connectWallet(metaMask)}>
            Connect MetaMask
          </button>
        </div>
      )}
    </div>
  );
};

// Basic styling for the app
const styles = {
  container: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    height: '100vh',
    backgroundColor: '#f0f0f0',
  },
  button: {
    margin: '10px',
    padding: '10px 20px',
    fontSize: '16px',
    cursor: 'pointer',
  },
  error: {
    color: 'red',
  },
  success: {
    color: 'green',
  },
};

// Exporting the App component
export default App;

// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import { Web3ReactProvider } from '@web3-react/core';
import getLibrary from './getLibrary';
import App from './App';

// Function to get the library for web3-react
const Main = () => {
  return (
    <Web3ReactProvider getLibrary={getLibrary}>
      <App />
    </Web3ReactProvider>
  );
};

// Render the main application
ReactDOM.render(<Main />, document.getElementById('root'));

// getLibrary.js
import { ethers } from 'ethers';

// Function to create a new ethers provider
const getLibrary = (provider) => {
  const library = new ethers.providers.Web3Provider(provider);
  library.pollingInterval = 12000; // Set polling interval for new blocks
  return library;
};

export default getLibrary;
```
