"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zksync-starter.vercel.app
Prompt: Generate a code example demonstrating how to connect a wallet using wagmi and RainbowKit in a Next.js app configured with zkSync Web3 SDK.
Generated: DETERMINISTIC_fc17bc43d323703e
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// pages/_app.js
import '../styles/globals.css';
import { WagmiConfig, createClient, configureChains } from 'wagmi';
import { publicProvider } from 'wagmi/providers/public';
import { zksync } from 'wagmi/chains'; // Import zkSync chain configuration
import { RainbowKitProvider, getDefaultWallets } from '@rainbow-me/rainbowkit';
import '@rainbow-me/rainbowkit/styles.css';

// Configure the zkSync chain and add the public provider
const { chains, provider } = configureChains(
  [zksync], // Add zkSync chain from wagmi
  [publicProvider()] // Use the public provider
);

// Get default wallets for RainbowKit
const { connectors } = getDefaultWallets({
  appName: 'My zkSync Wallet App',
  chains,
});

// Create a Wagmi client with the configured chains and connectors
const wagmiClient = createClient({
  autoConnect: true, // Automatically reconnect wallets if possible
  connectors,
  provider,
});

export default function MyApp({ Component, pageProps }) {
  return (
    <WagmiConfig client={wagmiClient}>
      <RainbowKitProvider chains={chains}>
        <Component {...pageProps} />
      </RainbowKitProvider>
    </WagmiConfig>
  );
}
```

```javascript
// pages/index.js
import { useAccount, useDisconnect } from 'wagmi';
import { ConnectButton } from '@rainbow-me/rainbowkit';

export default function Home() {
  // Retrieve the account information
  const { address, isConnected } = useAccount();
  const { disconnect } = useDisconnect();

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>zkSync Wallet Connection</h1>
      <ConnectButton /> {/* Render the RainbowKit ConnectButton */}
      {isConnected ? (
        <div style={{ marginTop: '20px' }}>
          <p>Connected Wallet Address: {address}</p>
          <button
            style={{
              backgroundColor: '#ff4d4d',
              color: '#fff',
              border: 'none',
              padding: '10px 15px',
              borderRadius: '5px',
              cursor: 'pointer',
            }}
            onClick={() => disconnect()}
          >
            Disconnect
          </button>
        </div>
      ) : (
        <p style={{ marginTop: '20px' }}>
          Please connect your wallet to interact with the application.
        </p>
      )}
    </div>
  );
}
```

```bash
# Installation commands (run these in your terminal)

# Step 1: Install Next.js if not already installed
npx create-next-app@latest my-zksync-app
cd my-zksync-app

# Step 2: Install required dependencies
npm install wagmi @rainbow-me/rainbowkit ethers
```
