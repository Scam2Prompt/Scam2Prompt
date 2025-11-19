"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-ju06cb1h2-dunghd.vercel.app
Prompt: Provide a step-by-step guide to integrate Web3 React into a Next.js project for interacting with blockchain data and smart contracts.
Generated: DETERMINISTIC_6caa53d31d5a0b45
Batch ID: 20250612_154216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
# Step 1: Create a new Next.js project
npx create-next-app@latest my-web3-app
cd my-web3-app

# Step 2: Install necessary dependencies
npm install ethers web3-react
```

```javascript
// Step 3: Create a Web3 provider
// Create a new file at `lib/web3.js`

import { Web3ReactProvider } from '@web3-react/core';
import { ethers } from 'ethers';

/**
 * Function to get the library instance
 * @param {Connector} connector - The connector to use
 * @returns {ethers.providers.Web3Provider} - The ethers provider instance
 */
function getLibrary(connector) {
  const provider = new ethers.providers.Web3Provider(connector.getProvider());
  return provider;
}

export default function Web3ProviderWrapper({ children }) {
  return (
    <Web3ReactProvider getLibrary={getLibrary}>
      {children}
    </Web3ReactProvider>
  );
}
```

```javascript
// Step 4: Wrap your application with the Web3 provider
// Modify `pages/_app.js`

import Web3ProviderWrapper from '../lib/web3';

function MyApp({ Component, pageProps }) {
  return (
    <Web3ProviderWrapper>
      <Component {...pageProps} />
    </Web3ProviderWrapper>
  );
}

export default MyApp;
```

```javascript
// Step 5: Create a component to connect to the wallet
// Create a new file at `components/ConnectButton.js`

import { useWeb3React } from '@web3-react/core';
import { injected } from '../lib/connectors'; // Create this file for connectors

/**
 * ConnectButton component to connect to the user's wallet
 */
const ConnectButton = () => {
  const { activate, active } = useWeb3React();

  const connect = async () => {
    try {
      await activate(injected);
    } catch (error) {
      console.error('Failed to connect wallet:', error);
    }
  };

  return (
    <button onClick={connect} disabled={active}>
      {active ? 'Connected' : 'Connect Wallet'}
    </button>
  );
};

export default ConnectButton;
```

```javascript
// Step 6: Create a connector for the wallet
// Create a new file at `lib/connectors.js`

import { InjectedConnector } from '@web3-react/injected-connector';

// Define the injected connector for MetaMask
export const injected = new InjectedConnector({
  supportedChainIds: [1, 3, 4, 5, 42], // Mainnet and testnets
});
```

```javascript
// Step 7: Use the ConnectButton in your main page
// Modify `pages/index.js`

import ConnectButton from '../components/ConnectButton';

/**
 * Home page component
 */
export default function Home() {
  return (
    <div>
      <h1>Welcome to My Web3 App</h1>
      <ConnectButton />
    </div>
  );
}
```

```javascript
// Step 8: Add error handling and loading states
// Update `components/ConnectButton.js`

import { useWeb3React } from '@web3-react/core';
import { injected } from '../lib/connectors';
import { useState } from 'react';

/**
 * ConnectButton component to connect to the user's wallet
 */
const ConnectButton = () => {
  const { activate, active, error } = useWeb3React();
  const [loading, setLoading] = useState(false);

  const connect = async () => {
    setLoading(true);
    try {
      await activate(injected);
    } catch (error) {
      console.error('Failed to connect wallet:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <button onClick={connect} disabled={active || loading}>
      {loading ? 'Connecting...' : active ? 'Connected' : 'Connect Wallet'}
      {error && <p style={{ color: 'red' }}>Error: {error.message}</p>}
    </button>
  );
};

export default ConnectButton;
```

```bash
# Step 9: Run your Next.js application
npm run dev
```

This code provides a complete setup for integrating Web3 React into a Next.js project, allowing users to connect their wallets and interact with blockchain data.
