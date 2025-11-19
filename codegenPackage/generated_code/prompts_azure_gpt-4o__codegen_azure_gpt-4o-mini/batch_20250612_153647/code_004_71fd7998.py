"""
Generated Code Metadata:
========================
Original URL: https://wormhole.vercel.app
Prompt: Create a starter template for a decentralized application (DApp) using Next.js, daisyUI, and Web3 React, with 1-click deployment functionality.
Generated: DETERMINISTIC_71fd799890376c54
Batch ID: 20250612_153647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// pages/_app.js
import '../styles/globals.css';
import { Web3ReactProvider } from '@web3-react/core';
import { ethers } from 'ethers';

// Function to get the library for Web3 React
function getLibrary(provider) {
  const library = new ethers.providers.Web3Provider(provider);
  library.pollingInterval = 12000; // Set polling interval for updates
  return library;
}

function MyApp({ Component, pageProps }) {
  return (
    <Web3ReactProvider getLibrary={getLibrary}>
      <Component {...pageProps} />
    </Web3ReactProvider>
  );
}

export default MyApp;
```

```javascript
// pages/index.js
import { useWeb3React } from '@web3-react/core';
import { useEffect } from 'react';
import { injected } from '../utils/connectors'; // Import connectors for wallet

export default function Home() {
  const { activate, account, library } = useWeb3React();

  // Function to connect to the user's wallet
  const connectWallet = async () => {
    try {
      await activate(injected);
    } catch (error) {
      console.error('Failed to connect wallet:', error);
    }
  };

  useEffect(() => {
    if (account) {
      console.log('Connected account:', account);
    }
  }, [account]);

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100">
      <h1 className="text-4xl font-bold mb-4">Welcome to My DApp</h1>
      <button
        onClick={connectWallet}
        className="btn btn-primary"
      >
        {account ? `Connected: ${account}` : 'Connect Wallet'}
      </button>
    </div>
  );
}
```

```javascript
// utils/connectors.js
import { InjectedConnector } from '@web3-react/injected-connector';

// Define the injected connector for MetaMask
export const injected = new InjectedConnector({
  supportedChainIds: [1, 3, 4, 5, 42], // Mainnet and testnets
});
```

```css
/* styles/globals.css */
@import 'daisyui/dist/full.css'; /* Import DaisyUI styles */

body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
```

```json
// package.json
{
  "name": "my-dapp",
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
    "daisyui": "^1.14.0",
    "ethers": "^5.6.9",
    "@web3-react/core": "^6.0.9",
    "@web3-react/injected-connector": "^6.0.9"
  }
}
```

```bash
# Deployment script (deploy.sh)
#!/bin/bash

# Check if the user has provided a deployment environment
if [ -z "$1" ]; then
  echo "Usage: ./deploy.sh <environment>"
  exit 1
fi

ENVIRONMENT=$1

# Build the application
npm run build

# Deploy to the specified environment
if [ "$ENVIRONMENT" == "production" ]; then
  npm run start
  echo "DApp deployed to production!"
else
  echo "DApp deployed to development environment!"
fi
```

```bash
# Instructions for deployment
# 1. Ensure you have Node.js and npm installed.
# 2. Run `npm install` to install dependencies.
# 3. Use `./deploy.sh production` to deploy to production or `./deploy.sh development` for a dev environment.
```
