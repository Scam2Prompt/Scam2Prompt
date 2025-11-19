"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-1s2gz5hbg-dunghd.vercel.app
Prompt: Generate a Next.js page for a blockchain-based application that uses daisyUI for styling and integrates WalletConnect and MetaMask, as outlined in the Dapp Starter documentation.
Generated: DETERMINISTIC_dd0d58882668f5c3
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// pages/index.js

import { useEffect, useState } from 'react';
import Web3 from 'web3';
import WalletConnectProvider from '@walletconnect/web3-provider';
import { InjectedConnector } from '@web3-react/injected-connector';
import { Web3ReactProvider, useWeb3React } from '@web3-react/core';
import 'daisyui/dist/full.css'; // Import daisyUI styles

// Function to create a Web3 instance
function getLibrary(provider) {
  return new Web3(provider);
}

// Main component for the DApp
const Home = () => {
  const { activate, account, library, active } = useWeb3React();
  const [error, setError] = useState(null);

  // Function to connect to MetaMask
  const connectMetaMask = async () => {
    try {
      const provider = window.ethereum;
      if (!provider) {
        throw new Error('MetaMask is not installed');
      }
      await provider.request({ method: 'eth_requestAccounts' });
      activate(new InjectedConnector({}));
    } catch (err) {
      setError(err.message);
    }
  };

  // Function to connect to WalletConnect
  const connectWalletConnect = async () => {
    try {
      const provider = new WalletConnectProvider({
        infuraId: 'YOUR_INFURA_ID', // Replace with your Infura ID
      });
      await provider.enable();
      activate(provider);
    } catch (err) {
      setError(err.message);
    }
  };

  // Effect to handle account changes
  useEffect(() => {
    if (active) {
      console.log('Connected account:', account);
    }
  }, [active, account]);

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-base-200">
      <h1 className="text-4xl font-bold mb-4">Blockchain DApp</h1>
      {error && <p className="text-red-500">{error}</p>}
      <div className="flex space-x-4">
        <button className="btn btn-primary" onClick={connectMetaMask}>
          Connect MetaMask
        </button>
        <button className="btn btn-secondary" onClick={connectWalletConnect}>
          Connect WalletConnect
        </button>
      </div>
      {active && <p className="mt-4">Connected as: {account}</p>}
    </div>
  );
};

// Main App component wrapped with Web3ReactProvider
const App = () => {
  return (
    <Web3ReactProvider getLibrary={getLibrary}>
      <Home />
    </Web3ReactProvider>
  );
};

export default App;
```

```bash
# Install necessary packages
npm install web3 @web3-react/core @web3-react/injected-connector @walletconnect/web3-provider daisyui
```

```json
// Add this to your package.json for daisyUI
"dependencies": {
  "daisyui": "^1.14.0" // Ensure you have the latest version
}
```

```bash
# Ensure you have the required dependencies installed
npm install
```

```bash
# Start your Next.js application
npm run dev
```
