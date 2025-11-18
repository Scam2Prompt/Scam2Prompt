"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallet-connect-app.productsway.com
Prompt: How can I use RainbowKit with Next.js to implement a "Connect Wallet" button? Provide code examples.
Generated: DETERMINISTIC_62a8bb700d58470d
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Install dependencies before using this code:
// npm install @rainbow-me/rainbowkit wagmi ethers

// pages/_app.js
import '../styles/globals.css';
import '@rainbow-me/rainbowkit/styles.css';
import { getDefaultWallets, RainbowKitProvider } from '@rainbow-me/rainbowkit';
import { configureChains, createClient, WagmiConfig } from 'wagmi';
import { chain, publicProvider } from 'wagmi/providers/public';

// Configure chains for wallet connection
const { chains, provider } = configureChains(
  [chain.mainnet, chain.polygon, chain.optimism, chain.arbitrum], // Add desired chains
  [publicProvider()] // Use the public provider
);

// Configure default wallets
const { connectors } = getDefaultWallets({
  appName: 'My RainbowKit App', // Name of your application
  chains,
});

// Create Wagmi client
const wagmiClient = createClient({
  autoConnect: true, // Automatically connect wallets
  connectors,
  provider,
});

function MyApp({ Component, pageProps }) {
  return (
    <WagmiConfig client={wagmiClient}>
      <RainbowKitProvider chains={chains}>
        <Component {...pageProps} />
      </RainbowKitProvider>
    </WagmiConfig>
  );
}

export default MyApp;

// pages/index.js
import Head from 'next/head';
import { ConnectButton } from '@rainbow-me/rainbowkit';

export default function Home() {
  return (
    <div>
      <Head>
        <title>Connect Wallet Demo</title>
        <meta name="description" content="A simple Connect Wallet button demo using RainbowKit." />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main style={{ textAlign: 'center', marginTop: '2rem' }}>
        <h1>Welcome to RainbowKit Wallet Connection Demo</h1>
        {/* RainbowKit's Connect Wallet Button */}
        <ConnectButton />
      </main>
    </div>
  );
}

// Note: Ensure you have a favicon.ico file in the public directory for the best experience.

// styles/globals.css (Optional)
/* Add any global styles here */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f5f5f5;
}
```
