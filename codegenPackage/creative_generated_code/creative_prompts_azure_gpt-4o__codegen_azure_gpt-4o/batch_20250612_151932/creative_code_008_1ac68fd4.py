"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-dapp.vercel.app
Prompt: Write code to integrate StarkNet wallet authentication into a decentralized application built with Next.js.
Generated: DETERMINISTIC_1ac68fd4388f94dc
Batch ID: 20250612_151932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: pages/_app.js
// Root file for the Next.js app. Initialize StarkNet provider and wallet context.

import { StarknetProvider } from "@starknet-react/core";
import '../styles/globals.css';

function MyApp({ Component, pageProps }) {
  return (
    <StarknetProvider>
      <Component {...pageProps} />
    </StarknetProvider>
  );
}

export default MyApp;

// File: components/WalletConnectButton.js
// Component to handle StarkNet wallet connection/authentication.

import React, { useState } from 'react';
import { useConnectors } from '@starknet-react/core';

const WalletConnectButton = () => {
  const { connect, connectors } = useConnectors(); // Access StarkNet connectors for wallet connection
  const [isConnected, setIsConnected] = useState(false);

  const handleConnect = async (connector) => {
    try {
      await connect(connector);
      setIsConnected(true); // Update state on successful connection
    } catch (error) {
      console.error("Wallet connection failed", error);
    }
  };

  return (
    <div>
      <h2>StarkNet Wallet Authentication</h2>
      {!isConnected && connectors.map((connector) => (
        <button
          key={connector.id}
          onClick={() => handleConnect(connector)}
          style={{
            margin: '5px',
            padding: '10px 20px',
            cursor: 'pointer',
          }}
        >
          Connect {connector.id}
        </button>
      ))}
      {isConnected && <p>Wallet connected successfully!</p>}
    </div>
  );
};

export default WalletConnectButton;

// File: pages/index.js
// Home page, includes the wallet connect button.

import WalletConnectButton from "../components/WalletConnectButton";

export default function Home() {
  return (
    <div style={{ padding: '20px' }}>
      <h1>Welcome to the Decentralized App</h1>
      <WalletConnectButton />
    </div>
  );
}

// File: package.json dependencies
// Install the required dependencies:
// Run: `npm install @starknet-react/core react next`
```
