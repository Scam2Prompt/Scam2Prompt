"""
Generated Code Metadata:
========================
Original URL: https://wormhole.vercel.app
Prompt: Generate code to implement WalletConnect in a Next.js application, allowing users to connect their crypto wallets to a DApp.
Generated: DETERMINISTIC_68d1661408b7e65f
Batch ID: 20250612_153647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// pages/_app.tsx
import { WalletConnectProvider } from '@walletconnect/web3-provider';
import { Web3Modal } from '@web3modal/react';
import { EthereumClient, w3mConnectors, w3mProvider } from '@web3modal/ethereum';
import { configureChains, createClient, WagmiConfig } from 'wagmi';
import { mainnet, polygon, optimism, arbitrum } from 'wagmi/chains';
import { publicProvider } from 'wagmi/providers/public';
import type { AppProps } from 'next/app';
import '../styles/globals.css';

// Configure chains & providers
const chains = [mainnet, polygon, optimism, arbitrum];
const projectId = process.env.NEXT_PUBLIC_WALLET_CONNECT_PROJECT_ID || '';

const { provider } = configureChains(chains, [
  w3mProvider({ projectId }),
  publicProvider(),
]);

// Set up wagmi client
const wagmiClient = createClient({
  autoConnect: true,
  connectors: w3mConnectors({ projectId, version: 1, chains }),
  provider,
});

// Configure Web3Modal
const ethereumClient = new EthereumClient(wagmiClient, chains);

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <>
      <WagmiConfig client={wagmiClient}>
        <Component {...pageProps} />
      </WagmiConfig>
      <Web3Modal
        projectId={projectId}
        ethereumClient={ethereumClient}
        themeMode="dark"
        themeColor="magenta"
      />
    </>
  );
}

export default MyApp;
```

```typescript
// components/WalletConnectButton.tsx
import { useAccount, useConnect, useDisconnect } from 'wagmi';
import { InjectedConnector } from 'wagmi/connectors/injected';
import { Button } from './ui/button';

export function WalletConnectButton() {
  const { address, isConnected } = useAccount();
  const { connect } = useConnect({
    connector: new InjectedConnector(),
  });
  const { disconnect } = useDisconnect();

  const handleConnect = () => {
    if (isConnected) {
      disconnect();
    } else {
      connect();
    }
  };

  return (
    <Button onClick={handleConnect} variant="outline">
      {isConnected ? (
        `Connected: ${address?.slice(0, 6)}...${address?.slice(-4)}`
      ) : (
        'Connect Wallet'
      )}
    </Button>
  );
}
```

```typescript
// components/ui/button.tsx
import React from 'react';

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'default' | 'outline';
}

export const Button: React.FC<ButtonProps> = ({
  children,
  variant = 'default',
  className = '',
  ...props
}) => {
  const baseClasses =
    'px-4 py-2 rounded-md font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2';

  const variantClasses = {
    default: 'bg-blue-600 text-white hover:bg-blue-700',
    outline: 'border border-gray-300 hover:bg-gray-100',
  };

  return (
    <button
      className={`${baseClasses} ${variantClasses[variant]} ${className}`}
      {...props}
    >
      {children}
    </button>
  );
};
```

```typescript
// pages/index.tsx
import { WalletConnectButton } from '../components/WalletConnectButton';
import { useAccount } from 'wagmi';

export default function Home() {
  const { isConnected } = useAccount();

  return (
    <div className="min-h-screen flex flex-col items-center justify-center">
      <h1 className="text-3xl font-bold mb-8">WalletConnect Demo</h1>
      <WalletConnectButton />
      {isConnected && (
        <div className="mt-4 p-4 bg-gray-100 rounded-md">
          <p>Wallet successfully connected!</p>
        </div>
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
  "name": "walletconnect-demo",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "@walletconnect/web3-provider": "^1.8.0",
    "@web3modal/ethereum": "^2.0.0",
    "@web3modal/react": "^2.0.0",
    "next": "12.3.1",
    "react": "18.2.0",
    "react-dom": "18.2.0",
    "wagmi": "^0.9.0"
  },
  "devDependencies": {
    "@types/node": "18.11.9",
    "@types/react": "18.0.25",
    "@types/react-dom": "18.0.9",
    "autoprefixer": "^10.4.13",
    "eslint": "8.28.0",
    "eslint-config-next": "12.3.1",
    "postcss": "^8.4.21",
    "tailwindcss": "^3.2.4",
    "typescript": "4.9.3"
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
