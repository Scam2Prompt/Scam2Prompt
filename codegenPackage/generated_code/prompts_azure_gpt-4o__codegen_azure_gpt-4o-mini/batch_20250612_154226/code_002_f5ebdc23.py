"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-1s2gz5hbg-dunghd.vercel.app
Prompt: Implement hot module replacement (HMR) in a Next.js Dapp project that uses Web3 React for blockchain interactions, following the structure of the Dapp Starter framework.
Generated: DETERMINISTIC_f5ebdc23b533e76e
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// next.config.js

const withTM = require('next-transpile-modules')(['web3-react']); // Transpile web3-react for HMR support

module.exports = {
  reactStrictMode: true,
  webpack: (config, { isServer }) => {
    // Enable Hot Module Replacement (HMR) for development
    if (!isServer) {
      config.devServer = {
        hot: true,
        liveReload: true,
      };
    }
    return config;
  },
};
```

```javascript
// pages/_app.js

import { AppProps } from 'next/app';
import { Web3ReactProvider } from '@web3-react/core';
import { ethers } from 'ethers';

// Function to get the library for web3-react
function getLibrary(provider) {
  const library = new ethers.providers.Web3Provider(provider);
  library.pollingInterval = 12000; // Set polling interval for updates
  return library;
}

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <Web3ReactProvider getLibrary={getLibrary}>
      <Component {...pageProps} />
    </Web3ReactProvider>
  );
}

export default MyApp;
```

```javascript
// components/WalletConnect.js

import { useWeb3React } from '@web3-react/core';
import { injected } from '../connectors'; // Import your connector

const WalletConnect = () => {
  const { activate, active, account, library } = useWeb3React();

  // Function to connect to the wallet
  const connectWallet = async () => {
    try {
      await activate(injected);
    } catch (error) {
      console.error('Failed to connect wallet:', error);
    }
  };

  return (
    <div>
      {active ? (
        <p>Connected as: {account}</p>
      ) : (
        <button onClick={connectWallet}>Connect Wallet</button>
      )}
    </div>
  );
};

export default WalletConnect;
```

```javascript
// pages/index.js

import WalletConnect from '../components/WalletConnect';

const Home = () => {
  return (
    <div>
      <h1>Welcome to the DApp</h1>
      <WalletConnect />
    </div>
  );
};

export default Home;
```

```javascript
// connectors/index.js

import { InjectedConnector } from '@web3-react/injected-connector';

// Define the injected connector for MetaMask
export const injected = new InjectedConnector({
  supportedChainIds: [1, 3, 4, 5, 42], // Mainnet and testnets
});
```

```javascript
// styles/globals.css

/* Global styles for the application */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f0f0f0;
}
```

```javascript
// package.json

{
  "name": "nextjs-dapp",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  },
  "dependencies": {
    "next": "latest",
    "react": "latest",
    "react-dom": "latest",
    "web3-react": "^6.1.9",
    "ethers": "^5.4.6",
    "next-transpile-modules": "^10.0.0"
  }
}
```

This code provides a basic structure for a Next.js DApp with Hot Module Replacement (HMR) enabled, using Web3 React for blockchain interactions. Ensure to install the necessary dependencies and configure your environment accordingly.
