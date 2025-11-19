"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallet-connect-app.productsway.com
Prompt: Write a code snippet that demonstrates how to integrate RainbowKit for wallet connections in a Next.js app.
Generated: DETERMINISTIC_31f29b9e0c3df27b
Batch ID: 20250612_155322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// pages/_app.js

import '@/styles/globals.css';
import '@rainbow-me/rainbowkit/styles.css';
import { RainbowKitProvider, darkTheme } from '@rainbow-me/rainbowkit';
import { configureChains, createClient, WagmiConfig } from 'wagmi';
import { alchemyProvider } from 'wagmi/providers/alchemy';
import { publicProvider } from 'wagmi/providers/public';
import { chain } from 'wagmi';

const { chains, provider } = configureChains(
  [chain.mainnet, chain.polygon, chain.optimism, chain.arbitrum], // Supported chains
  [
    alchemyProvider({ apiKey: process.env.NEXT_PUBLIC_ALCHEMY_API_KEY }), // Alchemy provider
    publicProvider(), // Fallback public provider
  ]
);

// Initialize the wallet client
const wagmiClient = createClient({
  autoConnect: true, // Automatically connect wallets if previously connected
  connectors: RainbowKitProvider.getDefaultConnectors({ chains }), // Default wallet connectors
  provider,
});

export default function App({ Component, pageProps }) {
  return (
    <WagmiConfig client={wagmiClient}>
      <RainbowKitProvider chains={chains} theme={darkTheme()}>
        {/* Wrapping the app with WagmiConfig and RainbowKitProvider */}
        <Component {...pageProps} />
      </RainbowKitProvider>
    </WagmiConfig>
  );
}

// Notes:
// 1. Replace `process.env.NEXT_PUBLIC_ALCHEMY_API_KEY` with your actual Alchemy API key.
// 2. Ensure that your project includes the required dependencies:
//    - @rainbow-me/rainbowkit
//    - wagmi
// 3. Install the dependencies with: `npm install @rainbow-me/rainbowkit wagmi`
```
