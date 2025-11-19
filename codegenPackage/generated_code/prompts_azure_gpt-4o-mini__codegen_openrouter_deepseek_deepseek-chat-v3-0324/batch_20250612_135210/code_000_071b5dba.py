"""
Generated Code Metadata:
========================
Original URL: https://zksync-starter.vercel.app
Prompt: Generate a Next.js application using the zkSync Web3 SDK and integrate it with RainbowKit for wallet connection.
Generated: DETERMINISTIC_071b5dba93386874
Batch ID: 20250612_135210
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// pages/_app.tsx
import { RainbowKitProvider, getDefaultWallets } from '@rainbow-me/rainbowkit';
import { configureChains, createClient, WagmiConfig } from 'wagmi';
import { zkSync, zkSyncTestnet } from 'wagmi/chains';
import { publicProvider } from 'wagmi/providers/public';
import type { AppProps } from 'next/app';
import '@rainbow-me/rainbowkit/styles.css';
import '../styles/globals.css';

const { chains, provider } = configureChains(
  [zkSync, zkSyncTestnet],
  [publicProvider()]
);

const { connectors } = getDefaultWallets({
  appName: 'zkSync RainbowKit App',
  chains,
});

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

```typescript
// pages/index.tsx
import { useAccount, useConnect, useDisconnect } from 'wagmi';
import { InjectedConnector } from 'wagmi/connectors/injected';
import { Button, Heading, Text } from '@chakra-ui/react';

export default function Home() {
  const { address, isConnected } = useAccount();
  const { connect } = useConnect({
    connector: new InjectedConnector(),
  });
  const { disconnect } = useDisconnect();

  return (
    <div style={{ padding: '2rem' }}>
      <Heading as="h1" size="xl" mb="4">
        zkSync + RainbowKit Demo
      </Heading>

      {isConnected ? (
        <div>
          <Text mb="4">Connected to: {address}</Text>
          <Button colorScheme="red" onClick={() => disconnect()}>
            Disconnect
          </Button>
        </div>
      ) : (
        <Button colorScheme="blue" onClick={() => connect()}>
          Connect Wallet
        </Button>
      )}
    </div>
  );
}
```

```typescript
// next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  webpack: (config) => {
    config.resolve.fallback = { fs: false, net: false, tls: false };
    return config;
  },
};

module.exports = nextConfig;
```

```json
// package.json
{
  "name": "zksync-rainbowkit-app",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "@chakra-ui/react": "^2.8.0",
    "@rainbow-me/rainbowkit": "^0.12.5",
    "@wagmi/chains": "^0.1.19",
    "@wagmi/core": "^0.6.7",
    "next": "13.4.7",
    "react": "18.2.0",
    "react-dom": "18.2.0",
    "wagmi": "^0.6.7"
  },
  "devDependencies": {
    "@types/node": "20.4.1",
    "@types/react": "18.2.14",
    "@types/react-dom": "18.2.6",
    "autoprefixer": "^10.4.14",
    "eslint": "8.45.0",
    "eslint-config-next": "13.4.7",
    "postcss": "^8.4.27",
    "tailwindcss": "^3.3.3",
    "typescript": "5.1.6"
  }
}
```

```css
/* styles/globals.css */
@tailwind base;
@tailwind components;
@tailwind utilities;

body {
  margin: 0;
  padding: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
    Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
```
