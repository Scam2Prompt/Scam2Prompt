"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chainge-finance.pages.dev
Prompt: Provide a step-by-step guide to integrate Chainge Finance's wallet connection feature into a React-based web application.
Generated: DETERMINISTIC_2a4b05d77db5dcc3
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Step 1: Install necessary dependencies
// Run the following command in your terminal:
// npm install @web3-react/core @web3-react/injected-connector ethers react-toastify

// Step 2: Set up the wallet connection feature in your React app

// src/connectors/injectedConnector.js
import { InjectedConnector } from '@web3-react/injected-connector';

// Define the supported chain IDs for Chainge Finance
export const injectedConnector = new InjectedConnector({
  supportedChainIds: [1, 137, 56], // Mainnet, Polygon, Binance Smart Chain (update as per Chainge Finance documentation)
});

// src/hooks/useWallet.js
import { useWeb3React } from '@web3-react/core';
import { injectedConnector } from '../connectors/injectedConnector';
import { useState } from 'react';
import { toast } from 'react-toastify';

/**
 * Custom hook for wallet connection logic
 */
export const useWallet = () => {
  const { activate, deactivate, active, account, error } = useWeb3React();
  const [loading, setLoading] = useState(false);

  /**
   * Connect to wallet using the InjectedConnector
   */
  const connectWallet = async () => {
    setLoading(true);
    try {
      await activate(injectedConnector);
      toast.success('Wallet connected successfully!');
    } catch (err) {
      console.error('Error connecting wallet:', err);
      toast.error('Failed to connect wallet. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  /**
   * Disconnect from the wallet
   */
  const disconnectWallet = () => {
    try {
      deactivate();
      toast.info('Wallet disconnected.');
    } catch (err) {
      console.error('Error disconnecting wallet:', err);
      toast.error('Failed to disconnect wallet.');
    }
  };

  return { connectWallet, disconnectWallet, active, account, loading, error };
};

// src/App.js
import React from 'react';
import { Web3ReactProvider } from '@web3-react/core';
import { ethers } from 'ethers';
import WalletConnection from './components/WalletConnection';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

/**
 * Provider function for ethers.js library
 */
function getLibrary(provider) {
  return new ethers.providers.Web3Provider(provider);
}

/**
 * Main App component
 */
function App() {
  return (
    <Web3ReactProvider getLibrary={getLibrary}>
      <ToastContainer />
      <div style={{ padding: '20px' }}>
        <h1>Chainge Finance Wallet Integration</h1>
        <WalletConnection />
      </div>
    </Web3ReactProvider>
  );
}

export default App;

// src/components/WalletConnection.js
import React from 'react';
import { useWallet } from '../hooks/useWallet';

/**
 * WalletConnection component for connecting/disconnecting user wallet
 */
const WalletConnection = () => {
  const { connectWallet, disconnectWallet, active, account, loading } = useWallet();

  return (
    <div>
      {active ? (
        <div>
          <p>Connected account: {account}</p>
          <button onClick={disconnectWallet} disabled={loading}>
            Disconnect Wallet
          </button>
        </div>
      ) : (
        <button onClick={connectWallet} disabled={loading}>
          Connect Wallet
        </button>
      )}
    </div>
  );
};

export default WalletConnection;

// Step 3: Test the application
// Run the following command to start your development server:
// npm start
```
