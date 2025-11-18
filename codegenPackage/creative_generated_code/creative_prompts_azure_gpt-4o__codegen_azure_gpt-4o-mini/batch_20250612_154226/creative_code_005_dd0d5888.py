"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-1s2gz5hbg-dunghd.vercel.app
Prompt: Generate a Next.js page for a blockchain-based application that uses daisyUI for styling and integrates WalletConnect and MetaMask, as outlined in the Dapp Starter documentation.
Generated: DETERMINISTIC_dd0d58882668f5c3
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// pages/index.js

import { useEffect, useState } from 'react';
import Head from 'next/head';
import { useAccount, useConnect, useDisconnect } from 'wagmi';
import { InjectedConnector } from 'wagmi/connectors/injected';
import WalletConnectProvider from "@walletconnect/web3-provider";
import Web3Modal from "web3modal";

// Main functional component for the DApp
export default function Home() {
  const [provider, setProvider] = useState(null);
  const { isConnected } = useAccount();
  const { connect, connectors } = useConnect();
  const { disconnect } = useDisconnect();

  // Initialize Web3 modal for connection options
  const web3Modal = new Web3Modal({
    cacheProvider: true,
    providerOptions: {
      walletconnect: {
        package: WalletConnectProvider,
        options: {
          infuraId: process.env.NEXT_PUBLIC_INFURA_ID, // Replace with your Infura ID
        },
      },
    },
  });

  // Connect to wallet
  const handleConnect = async (connector) => {
    try {
      const provider = await connect(connector);
      setProvider(provider);
    } catch (err) {
      console.error("Connection error:", err);
      alert("Failed to connect to wallet. Please try again.");
    }
  };

  // Disconnect from wallet
  const handleDisconnect = () => {
    disconnect();
    setProvider(null);
  };

  // Effect to manage wallet connection on component mount
  useEffect(() => {
    const init = async () => {
      // Check for cached provider and connect if found
      const cachedProvider = await web3Modal.connect();
      if (cachedProvider) {
        setProvider(cachedProvider);
      }
    };
    init();
  }, []);

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-base-200">
      <Head>
        <title>Blockchain DApp</title>
        <meta name="description" content="A blockchain-based application using Next.js and daisyUI" />
      </Head>

      <main className="bg-base-100 p-8 rounded-lg shadow-lg">
        <h1 className="text-3xl font-bold mb-4">Welcome to the Blockchain DApp</h1>
        {isConnected ? (
          <div>
            <p className="mb-4">You are connected!</p>
            <button className="btn btn-primary" onClick={handleDisconnect}>
              Disconnect
            </button>
          </div>
        ) : (
          <div>
            <p className="mb-4">Connect your wallet to get started.</p>
            {connectors.map((connector) => (
              <button
                key={connector.id}
                className="btn btn-secondary mb-2"
                onClick={() => handleConnect(connector)}
              >
                Connect with {connector.name}
              </button>
            ))}
          </div>
        )}
      </main>
    </div>
  );
}
```

```javascript
// styles/globals.css

@import 'daisyui/dist/full.css'; // Import daisyUI styles

/* Apply custom global styles */
body {
  font-family: 'Arial', sans-serif;
}
``` 

```bash
# Ensure you have the required dependencies in your package.json
npm install next react react-dom wagmi web3modal @walletconnect/web3-provider daisyui
``` 

Note: Replace `NEXT_PUBLIC_INFURA_ID` with your actual Infura project ID in your environment variables.
