"""
Generated Code Metadata:
========================
Original URL: https://jupiter-nextjs-example.vercel.app
Prompt: What are the steps to set up a dApp using Next.js, TypeScript, and TailwindCSS with the Jupiter scaffold?
Generated: DETERMINISTIC_295bc5ddf43ad3d4
Batch ID: 20250612_155737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// File: pages/_app.tsx
import type { AppProps } from 'next/app';
import { JupiterProvider } from '@jup-ag/react-hook';
import { Connection } from '@solana/web3.js';
import { WalletAdapterNetwork } from '@solana/wallet-adapter-base';
import { WalletModalProvider } from '@solana/wallet-adapter-react-ui';
import { WalletProvider } from '@solana/wallet-adapter-react';
import { PhantomWalletAdapter } from '@solana/wallet-adapter-phantom';
import { SolflareWalletAdapter } from '@solana/wallet-adapter-solflare';
import { clusterApiUrl } from '@solana/web3.js';
import '../styles/globals.css';

function MyApp({ Component, pageProps }: AppProps) {
  const network = WalletAdapterNetwork.Mainnet;
  const endpoint = clusterApiUrl(network);
  const wallets = [
    new PhantomWalletAdapter(),
    new SolflareWalletAdapter({ network }),
  ];

  return (
    <ConnectionProvider endpoint={endpoint}>
      <WalletProvider wallets={wallets} autoConnect>
        <WalletModalProvider>
          <JupiterProvider connection={new Connection(endpoint)} cluster={network}>
            <Component {...pageProps} />
          </JupiterProvider>
        </WalletModalProvider>
      </WalletProvider>
    </ConnectionProvider>
  );
}

export default MyApp;
```

```typescript
// File: pages/index.tsx
import { useJupiter } from '@jup-ag/react-hook';
import { useState } from 'react';

export default function Home() {
  const [inputMint, setInputMint] = useState('So11111111111111111111111111111111111111112');
  const [outputMint, setOutputMint] = useState('EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v');
  const [amount, setAmount] = useState('1');

  const { routeMap, routes, loading, error } = useJupiter({
    amount: Number(amount),
    inputMint,
    outputMint,
  });

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <div className="max-w-md mx-auto bg-white rounded-xl shadow-md overflow-hidden md:max-w-2xl p-6">
        <h1 className="text-2xl font-bold mb-6">Jupiter Swap</h1>
        
        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2">Input Token</label>
          <input
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            value={inputMint}
            onChange={(e) => setInputMint(e.target.value)}
          />
        </div>

        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2">Output Token</label>
          <input
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            value={outputMint}
            onChange={(e) => setOutputMint(e.target.value)}
          />
        </div>

        <div className="mb-6">
          <label className="block text-gray-700 text-sm font-bold mb-2">Amount</label>
          <input
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            type="number"
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
          />
        </div>

        {loading && <p className="text-gray-600">Loading routes...</p>}
        {error && <p className="text-red-500">Error: {error.message}</p>}

        {routes && (
          <div className="mt-4">
            <h2 className="text-lg font-semibold mb-2">Available Routes</h2>
            <ul className="list-disc pl-5">
              {routes.map((route, index) => (
                <li key={index} className="mb-1">
                  {route.marketInfos.map((info, i) => (
                    <span key={i}>
                      {info.amm.label} ({info.inAmount} → {info.outAmount})
                      {i < route.marketInfos.length - 1 && ' → '}
                    </span>
                  ))}
                </li>
              ))}
            </ul>
          </div>
        )}
      </div>
    </div>
  );
}
```

```typescript
// File: next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  webpack: (config) => {
    config.resolve.fallback = { fs: false, net: false, tls: false };
    return config;
  },
};

module.exports = nextConfig;
```

```typescript
// File: package.json
{
  "name": "jupiter-dapp",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "@jup-ag/react-hook": "^0.0.5",
    "@solana/wallet-adapter-base": "^0.9.23",
    "@solana/wallet-adapter-phantom": "^0.9.23",
    "@solana/wallet-adapter-react": "^0.15.35",
    "@solana/wallet-adapter-react-ui": "^0.9.24",
    "@solana/wallet-adapter-solflare": "^0.6.23",
    "@solana/web3.js": "^1.84.0",
    "next": "^13.4.19",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "tailwindcss": "^3.3.3"
  },
  "devDependencies": {
    "@types/node": "^20.5.7",
    "@types/react": "^18.2.21",
    "@types/react-dom": "^18.2.7",
    "autoprefixer": "^10.4.15",
    "eslint": "^8.48.0",
    "eslint-config-next": "^13.4.19",
    "postcss": "^8.4.29",
    "typescript": "^5.2.2"
  }
}
```

```typescript
// File: tailwind.config.js
module.exports = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
```

```typescript
// File: postcss.config.js
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
};
```

```typescript
// File: styles/globals.css
@tailwind base;
@tailwind components;
@tailwind utilities;
```
