"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-1s2gz5hbg-dunghd.vercel.app
Prompt: Create a step-by-step guide for integrating WalletConnect and MetaMask into a Next.js Dapp project, referencing the tools and methods described in the Dapp Starter framework.
Generated: DETERMINISTIC_2ab194d15d7016e4
Batch ID: 20250612_154226
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://bridge.walletconnect.org": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
// Step-by-Step Guide for Integrating WalletConnect and MetaMask into a Next.js Dapp project

// 1. Install required dependencies
// Run the following commands in your terminal:
// npm install ethers web3 react-walletconnect-modal @web3-react/core @web3-react/metamask @web3-react/walletconnect

// 2. Create a `web3.js` file to manage wallet connections

// /lib/web3.js
import { Web3ReactProvider } from '@web3-react/core';
import { MetaMask } from '@web3-react/metamask';
import { WalletConnect } from '@web3-react/walletconnect';
import { ethers } from 'ethers';

// Function to initialize a provider
function getLibrary(provider) {
  return new ethers.providers.Web3Provider(provider);
}

// Create connectors for MetaMask and WalletConnect
export const metaMask = new MetaMask();
export const walletConnect = new WalletConnect({
  rpc: { 1: 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID' }, // Replace YOUR_INFURA_PROJECT_ID
  bridge: 'https://bridge.walletconnect.org',
  qrcode: true,
});

// Web3ReactProvider component wrapper
export function Web3ProviderWrapper({ children }) {
  return <Web3ReactProvider getLibrary={getLibrary}>{children}</Web3ReactProvider>;
}

// 3. Set up the `App.js` to provide Web3 context and handle wallet connections

// /pages/_app.js
import '../styles/globals.css';
import { Web3ProviderWrapper } from '../lib/web3';

function MyApp({ Component, pageProps }) {
  return (
    <Web3ProviderWrapper>
      <Component {...pageProps} />
    </Web3ProviderWrapper>
  );
}

export default MyApp;

// 4. Create a connection component to connect wallets

// /components/WalletConnection.js
import React, { useState } from 'react';
import { useWeb3React } from '@web3-react/core';
import { metaMask, walletConnect } from '../lib/web3';

const WalletConnection = () => {
  const { activate, deactivate, active, account, chainId } = useWeb3React();
  const [error, setError] = useState(null);

  const connectMetaMask = async () => {
    try {
      setError(null);
      await activate(metaMask);
    } catch (err) {
      console.error('MetaMask Connection Error:', err);
      setError(err.message || 'Failed to connect MetaMask');
    }
  };

  const connectWalletConnect = async () => {
    try {
      setError(null);
      await activate(walletConnect);
    } catch (err) {
      console.error('WalletConnect Connection Error:', err);
      setError(err.message || 'Failed to connect WalletConnect');
    }
  };

  const disconnectWallet = async () => {
    try {
      setError(null);
      deactivate();
    } catch (err) {
      console.error('Disconnection Error:', err);
      setError(err.message || 'Failed to disconnect wallet');
    }
  };

  return (
    <div>
      <h1>Connect Your Wallet</h1>
      {active ? (
        <div>
          <p>Connected Account: {account}</p>
          <p>Chain ID: {chainId}</p>
          <button onClick={disconnectWallet}>Disconnect Wallet</button>
        </div>
      ) : (
        <div>
          <button onClick={connectMetaMask}>Connect MetaMask</button>
          <button onClick={connectWalletConnect}>Connect WalletConnect</button>
        </div>
      )}
      {error && <p style={{ color: 'red' }}>Error: {error}</p>}
    </div>
  );
};

export default WalletConnection;

// 5. Add the WalletConnection component to your main page

// /pages/index.js
import WalletConnection from '../components/WalletConnection';

const Home = () => {
  return (
    <div>
      <h1>Welcome to My Dapp</h1>
      <WalletConnection />
    </div>
  );
};

export default Home;

// 6. Ensure environment variables like Infura project ID are properly managed
// Create a `.env.local` file in your project root and add:
// NEXT_PUBLIC_INFURA_PROJECT_ID=YOUR_INFURA_PROJECT_ID

// 7. Test the application
// Run the development server using `npm run dev` and open your Dapp in a browser.
```
