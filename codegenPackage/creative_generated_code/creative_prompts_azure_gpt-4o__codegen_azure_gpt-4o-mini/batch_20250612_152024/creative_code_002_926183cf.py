"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallet-connect-app.productsway.com
Prompt: Generate a Next.js component that uses RainbowKit to allow users to connect their cryptocurrency wallets.
Generated: DETERMINISTIC_926183cfefcb5cad
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// components/WalletConnect.js

import React from 'react';
import { useAccount, useConnect, useDisconnect } from 'wagmi';
import { ConnectButton } from '@rainbow-me/rainbowkit';

/**
 * WalletConnect component allows users to connect their cryptocurrency wallets
 * using RainbowKit and Wagmi for handling wallet connections.
 */
const WalletConnect = () => {
  const { isConnected } = useAccount();
  const { connect, connectors } = useConnect();
  const { disconnect } = useDisconnect();

  return (
    <div>
      {/* Display the ConnectButton from RainbowKit for wallet connection */}
      <ConnectButton 
        onConnect={(connector) => {
          console.log(`Connected with ${connector.name}`);
        }} 
        onDisconnect={() => {
          console.log('Disconnected');
        }} 
      />
      
      {/* Show disconnect button if connected */}
      {isConnected && (
        <button
          onClick={() => {
            disconnect();
            console.log('Wallet disconnected');
          }}
          style={{ marginTop: '10px', padding: '10px', backgroundColor: '#ff4c4c', color: '#fff', border: 'none', borderRadius: '5px' }}
        >
          Disconnect Wallet
        </button>
      )}
    </div>
  );
};

export default WalletConnect;
```

```javascript
// pages/_app.js

import '../styles/globals.css';
import { WagmiConfig, createClient } from 'wagmi';
import { RainbowKitProvider, darkTheme } from '@rainbow-me/rainbowkit';

// Create a Wagmi client
const client = createClient({
  autoConnect: true,
  providers: (provider) => [
    provider.injected(),
    provider.walletConnect({ qrcode: true }),
    provider.chain("mainnet"), // Specify the networks you want to support
  ],
});

/**
 * Main application component that wraps the app in Wagmi and RainbowKit providers.
 */
function MyApp({ Component, pageProps }) {
  return (
    <WagmiConfig client={client}>
      <RainbowKitProvider theme={darkTheme({ accentColor: '#6f00ff' })}>
        <Component {...pageProps} />
      </RainbowKitProvider>
    </WagmiConfig>
  );
}

export default MyApp;
```

```javascript
// pages/index.js

import React from 'react';
import WalletConnect from '../components/WalletConnect';

/**
 * Home page component that renders the WalletConnect component.
 */
const Home = () => {
  return (
    <div style={{ padding: '20px', textAlign: 'center' }}>
      <h1>Connect Your Wallet</h1>
      <WalletConnect />
    </div>
  );
};

export default Home;
```

```bash
# Install dependencies using npm or yarn
npm install wagmi @rainbow-me/rainbowkit ethers
# or
yarn add wagmi @rainbow-me/rainbowkit ethers
```

Make sure to run the Next.js application using `npm run dev` or `yarn dev`.
