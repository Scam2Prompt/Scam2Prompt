"""
Generated Code Metadata:
========================
Original URL: https://metamask-sdk-examples-relink.vercel.app
Prompt: Create a Next.js app that connects a wallet using MetaMask SDK and includes functionality for interacting with smart contracts, referencing the guides on the webpage.
Generated: DETERMINISTIC_93a971fb4a5bdf4e
Batch ID: 20250612_154829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```tsx
// pages/_app.tsx
import type { AppProps } from 'next/app';
import { MetaMaskProvider } from '@metamask/sdk-react';
import { Inter } from 'next/font/google';
import '../styles/globals.css';

const inter = Inter({ subsets: ['latin'] });

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <MetaMaskProvider
      debug={false}
      sdkOptions={{
        dappMetadata: {
          name: 'Next.js DApp',
          url: typeof window !== 'undefined' ? window.location.href : '',
        },
      }}
    >
      <main className={inter.className}>
        <Component {...pageProps} />
      </main>
    </MetaMaskProvider>
  );
}

export default MyApp;
```

```tsx
// pages/index.tsx
import { useState, useEffect } from 'react';
import { useSDK } from '@metamask/sdk-react';
import { ethers } from 'ethers';
import { Contract } from 'ethers';
import { abi } from '../contracts/MyContract.json';

export default function Home() {
  const { sdk, connected, connecting, provider, chainId, account } = useSDK();
  const [contract, setContract] = useState<Contract | null>(null);
  const [contractValue, setContractValue] = useState<string>('');
  const [error, setError] = useState<string>('');

  // Replace with your contract address
  const contractAddress = '0x123...';

  useEffect(() => {
    if (provider && account) {
      const ethersProvider = new ethers.BrowserProvider(provider);
      const signer = ethersProvider.getSigner();
      const contractInstance = new Contract(contractAddress, abi, signer);
      setContract(contractInstance);
    }
  }, [provider, account]);

  const connectWallet = async () => {
    try {
      await sdk?.connect();
    } catch (err) {
      console.error('Failed to connect:', err);
      setError('Failed to connect wallet');
    }
  };

  const disconnectWallet = async () => {
    try {
      await sdk?.disconnect();
    } catch (err) {
      console.error('Failed to disconnect:', err);
      setError('Failed to disconnect wallet');
    }
  };

  const readContract = async () => {
    if (!contract) {
      setError('Contract not initialized');
      return;
    }

    try {
      const value = await contract.someReadFunction();
      setContractValue(value.toString());
    } catch (err) {
      console.error('Failed to read contract:', err);
      setError('Failed to read contract');
    }
  };

  const writeContract = async () => {
    if (!contract) {
      setError('Contract not initialized');
      return;
    }

    try {
      const tx = await contract.someWriteFunction();
      await tx.wait();
      setError('Transaction successful');
    } catch (err) {
      console.error('Failed to write contract:', err);
      setError('Failed to write contract');
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Next.js DApp with MetaMask</h1>
      
      {error && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
          {error}
        </div>
      )}

      {!connected ? (
        <button
          onClick={connectWallet}
          disabled={connecting}
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        >
          {connecting ? 'Connecting...' : 'Connect Wallet'}
        </button>
      ) : (
        <div className="mb-4">
          <p className="mb-2">Connected Account: {account}</p>
          <p className="mb-2">Chain ID: {chainId}</p>
          <button
            onClick={disconnectWallet}
            className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded mr-2"
          >
            Disconnect
          </button>
        </div>
      )}

      {connected && (
        <div className="mt-4">
          <h2 className="text-xl font-semibold mb-2">Contract Interaction</h2>
          <button
            onClick={readContract}
            className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded mr-2"
          >
            Read Contract
          </button>
          <button
            onClick={writeContract}
            className="bg-purple-500 hover:bg-purple-700 text-white font-bold py-2 px-4 rounded"
          >
            Write Contract
          </button>
          {contractValue && (
            <div className="mt-4 p-4 bg-gray-100 rounded">
              <p>Contract Value: {contractValue}</p>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
```

```json
// package.json
{
  "name": "nextjs-metamask-dapp",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "@metamask/sdk-react": "^0.4.0",
    "ethers": "^6.7.1",
    "next": "^14.0.3",
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "@types/node": "^20.8.9",
    "@types/react": "^18.2.41",
    "@types/react-dom": "^18.2.18",
    "autoprefixer": "^10.4.16",
    "eslint": "^8.55.0",
    "eslint-config-next": "14.0.3",
    "postcss": "^8.4.31",
    "tailwindcss": "^3.3.5",
    "typescript": "^5.3.2"
  }
}
```

```json
// contracts/MyContract.json
{
  "abi": [
    {
      "inputs": [],
      "name": "someReadFunction",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "someWriteFunction",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    }
  ]
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
  min-height: 100vh;
}
```

```ts
// next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
};

module.exports = nextConfig;
```
