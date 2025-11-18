"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rascal-land-nextjs-mint.vercel.app
Prompt: Write code to implement a "Connect Wallet" button in a Next.js app that supports Solana blockchain integration.
Generated: DETERMINISTIC_dd78b89de2f09ee9
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// File: components/ConnectWalletButton.js

import React, { useState } from 'react';
import { Connection, PublicKey } from '@solana/web3.js';
import { useWallet, WalletProvider } from '@solana/wallet-adapter-react';
import {
  WalletModalProvider,
  WalletMultiButton,
} from '@solana/wallet-adapter-react-ui';
import { PhantomWalletAdapter } from '@solana/wallet-adapter-wallets';
import '@solana/wallet-adapter-react-ui/styles.css'; // Required for wallet UI

// ConnectWalletButton Component
const ConnectWalletButton = () => {
  const [walletAddress, setWalletAddress] = useState(null);
  const wallet = useWallet();

  // Function to handle wallet connection
  const handleConnect = async () => {
    try {
      if (!wallet.connected) {
        throw new Error('Wallet not connected');
      }

      const publicKey = wallet.publicKey;
      if (publicKey) {
        setWalletAddress(publicKey.toString()); // Save wallet address
      } else {
        throw new Error('Unable to retrieve wallet public key');
      }
    } catch (error) {
      console.error('Error connecting wallet:', error.message);
      alert('Failed to connect wallet. Please try again.');
    }
  };

  return (
    <div>
      {/* Solana Wallet Connect Button */}
      <WalletMultiButton />
      {/* Display connected wallet address */}
      {walletAddress && (
        <p>
          Connected Wallet: <b>{walletAddress}</b>
        </p>
      )}
      {/* Connect Wallet Button */}
      <button onClick={handleConnect} disabled={!wallet.connected}>
        Connect Wallet
      </button>
    </div>
  );
};

// Wrapping the component with WalletProvider
const WalletIntegration = () => {
  // Configure wallet adapters
  const wallets = [new PhantomWalletAdapter()];

  return (
    <WalletProvider wallets={wallets} autoConnect>
      <WalletModalProvider>
        <ConnectWalletButton />
      </WalletModalProvider>
    </WalletProvider>
  );
};

export default WalletIntegration;
```

```jsx
// File: pages/_app.js

import React from 'react';
import dynamic from 'next/dynamic';

// Load WalletIntegration dynamically to prevent SSR issues
const WalletIntegration = dynamic(() => import('../components/ConnectWalletButton'), { ssr: false });

function MyApp({ Component, pageProps }) {
  return (
    <div>
      {/* Wallet Integration Component */}
      <WalletIntegration />
      {/* Main Application */}
      <Component {...pageProps} />
    </div>
  );
}

export default MyApp;
```

```json
// File: package.json
{
  "dependencies": {
    "@solana/web3.js": "^1.76.0",
    "@solana/wallet-adapter-react": "^0.20.0",
    "@solana/wallet-adapter-react-ui": "^0.8.0",
    "@solana/wallet-adapter-wallets": "^0.20.0",
    "next": "^12.3.1",
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  }
}
```
