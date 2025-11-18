"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter.productsway.com
Prompt: Write code to integrate MetaMask into a Next.js DApp using the Web3 React library, as described in the Dapp Starter documentation.
Generated: DETERMINISTIC_e0c4468018b4f941
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// pages/_app.js

import React from 'react';
import { AppProps } from 'next/app';
import { Web3ReactProvider } from '@web3-react/core';
import { ethers } from 'ethers';

// Function to get the library for use with web3-react
function getLibrary(provider) {
  const library = new ethers.providers.Web3Provider(provider);
  library.pollingInterval = 12000; // Metamask auto-refreshes every 12 seconds
  return library;
}

const MyApp = ({ Component, pageProps }: AppProps) => {
  return (
    <Web3ReactProvider getLibrary={getLibrary}>
      <Component {...pageProps} />
    </Web3ReactProvider>
  );
};

export default MyApp;
```

```javascript
// components/ConnectButton.js

import React from 'react';
import { useWeb3React } from '@web3-react/core';
import { injected } from '../connectors'; // Assuming you have a connectors.js where you define your connector

const ConnectButton = () => {
  const { activate, active, account, error } = useWeb3React();

  // Function to handle connecting to MetaMask
  const connect = async () => {
    try {
      await activate(injected);
    } catch (err) {
      console.error('Failed to connect to MetaMask:', err);
    }
  };

  return (
    <div>
      {active ? (
        <div>
          <p>Connected as: {account}</p>
        </div>
      ) : (
        <button onClick={connect}>Connect to MetaMask</button>
      )}
      {error && <p style={{ color: 'red' }}>Error: {error.message}</p>}
    </div>
  );
};

export default ConnectButton;
```

```javascript
// connectors.js

import { InjectedConnector } from '@web3-react/injected-connector';

// Define the injected connector for connecting to MetaMask
export const injected = new InjectedConnector({
  // Specify the supported chain IDs for your DApp
  supportedChainIds: [1, 3, 4, 5, 42], // Mainnet and testnets
});
```

```javascript
// pages/index.js

import React from 'react';
import ConnectButton from '../components/ConnectButton';

const Home = () => {
  return (
    <div>
      <h1>Welcome to the DApp!</h1>
      <ConnectButton />
    </div>
  );
};

export default Home;
```

```bash
# Install required packages
npm install ethers @web3-react/core @web3-react/injected-connector
```

```json
// package.json (add this section if you don't have it)
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  },
  "dependencies": {
    "ethers": "^5.5.0",
    "@web3-react/core": "^6.0.0",
    "@web3-react/injected-connector": "^6.0.0",
    "next": "latest",
    "react": "latest",
    "react-dom": "latest"
  }
}
```
