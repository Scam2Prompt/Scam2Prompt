"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallet-connect-app.productsway.com
Prompt: Provide an example of using RainbowKit to enable wallet connections in a Next.js application.
Generated: DETERMINISTIC_5618ffa2043d574f
Batch ID: 20250612_155322
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://polygonscan.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://polygon-rpc.com/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://etherscan.io": {
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
// pages/_app.js

import React from 'react';
import { AppProps } from 'next/app';
import { RainbowKitProvider } from '@rainbow-me/rainbowkit';
import { Chain, configureChains, createClient, WagmiConfig } from 'wagmi';
import { alchemyProvider } from 'wagmi/providers/alchemy';
import { publicProvider } from 'wagmi/providers/public';

// Define your supported chains (e.g., Ethereum and Polygon)
const chains: Chain[] = [
  {
    id: 1, // Ethereum Mainnet
    name: 'Ethereum',
    network: 'mainnet',
    nativeCurrency: { name: 'Ether', symbol: 'ETH', decimals: 18 },
    rpcUrls: { default: 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID' },
    blockExplorers: {
      default: { name: 'Etherscan', url: 'https://etherscan.io' },
    },
  },
  {
    id: 137, // Polygon Mainnet
    name: 'Polygon',
    network: 'polygon',
    nativeCurrency: { name: 'MATIC', symbol: 'MATIC', decimals: 18 },
    rpcUrls: { default: 'https://polygon-rpc.com/' },
    blockExplorers: {
      default: { name: 'Polygonscan', url: 'https://polygonscan.com' },
    },
  },
];

const { provider } = configureChains(chains, [
  alchemyProvider({ apiKey: 'YOUR_ALCHEMY_API_KEY' }),
  publicProvider(),
]);

// Create a Wagmi client instance
const wagmiClient = createClient({
  autoConnect: true,
  provider,
});

// Main application component
const MyApp = ({ Component, pageProps }: AppProps) => {
  return (
    <WagmiConfig client={wagmiClient}>
      <RainbowKitProvider chains={chains}>
        <Component {...pageProps} />
      </RainbowKitProvider>
    </WagmiConfig>
  );
};

export default MyApp;
```

```javascript
// pages/index.js

import React from 'react';
import { useAccount, useConnect, useDisconnect } from 'wagmi';
import { InjectedConnector } from 'wagmi/connectors/injected';

const HomePage = () => {
  const { connect, connectors } = useConnect();
  const { disconnect } = useDisconnect();
  const { isConnected, address } = useAccount();

  return (
    <div style={{ padding: '20px' }}>
      <h1>Wallet Connection Example</h1>
      {isConnected ? (
        <div>
          <p>Connected as: {address}</p>
          <button onClick={() => disconnect()}>Disconnect</button>
        </div>
      ) : (
        <div>
          <p>Please connect your wallet</p>
          {connectors.map((connector) => (
            <button
              key={connector.id}
              onClick={() => connect(connector)}
              style={{ margin: '5px' }}
            >
              Connect with {connector.name}
            </button>
          ))}
        </div>
      )}
    </div>
  );
};

export default HomePage;
```

```bash
# Install required dependencies
npm install next react react-dom wagmi @rainbow-me/rainbowkit
``` 

```json
// package.json (add this section if not already present)
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  },
  "dependencies": {
    "next": "latest",
    "react": "latest",
    "react-dom": "latest",
    "wagmi": "^1.0.0",
    "@rainbow-me/rainbowkit": "^0.0.0"
  }
}
```

Make sure to replace `YOUR_INFURA_PROJECT_ID` and `YOUR_ALCHEMY_API_KEY` with your actual API keys. This example sets up a basic Next.js application that supports wallet connections using RainbowKit.
