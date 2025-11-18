"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallet-connect-app.productsway.com
Prompt: Write code to create a "Connect Wallet" feature using RainbowKit and Next.js, as outlined on the Wallet Connect App page.
Generated: DETERMINISTIC_24b946cbf4dc9af4
Batch ID: 20250612_152024
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
import { RainbowKitProvider, getDefaultWallets } from '@rainbow-me/rainbowkit';
import { chain, configureChains, createClient, WagmiConfig } from 'wagmi';
import { publicProvider } from 'wagmi/providers/public';

// Configure supported chains and providers
const { chains, provider } = configureChains(
  [chain.mainnet, chain.polygon, chain.optimism, chain.arbitrum],
  [publicProvider()]
);

// Get default wallets for the RainbowKit provider
const { connectors } = getDefaultWallets({
  appName: 'My RainbowKit App',
  chains,
});

// Create a Wagmi client
const wagmiClient = createClient({
  autoConnect: true,
  connectors,
  provider,
});

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <WagmiConfig client={wagmiClient}>
      <RainbowKitProvider chains={chains}>
        <Component {...pageProps} />
      </RainbowKitProvider>
    </WagmiConfig>
  );
}

export default MyApp;
```

```javascript
// pages/index.js
import { ConnectButton } from '@rainbow-me/rainbowkit';

const Home = () => {
  return (
    <div style={{ padding: '50px', textAlign: 'center' }}>
      <h1>Connect Your Wallet</h1>
      <ConnectButton />
    </div>
  );
};

export default Home;
```

```javascript
// next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  images: {
    domains: ['example.com'], // Add your image domains here
  },
};

module.exports = nextConfig;
```

```bash
# Install necessary packages
npm install next react react-dom @rainbow-me/rainbowkit wagmi ethers
```

```json
// package.json
{
  "name": "my-rainbowkit-app",
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
    "@rainbow-me/rainbowkit": "^0.5.0", // Ensure this is the latest version
    "wagmi": "^0.5.0", // Ensure this is the latest version
    "ethers": "^5.0.0" // Ensure this is the latest version
  }
}
```

```css
/* styles/globals.css */
body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

code {
  font-family: source-code-pro, Menlo, Monaco, Consolas, 'Courier New', monospace;
}
```

Make sure to replace any necessary values, such as image domains, according to your project's requirements. Test the connection functionality thoroughly to ensure it meets your production needs.
