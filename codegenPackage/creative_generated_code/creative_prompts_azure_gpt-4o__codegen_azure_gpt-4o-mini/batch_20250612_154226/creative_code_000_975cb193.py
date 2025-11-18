"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-1s2gz5hbg-dunghd.vercel.app
Prompt: Write a Next.js-based Dapp starter template that integrates MetaMask and WalletConnect for wallet authentication, referencing the tools mentioned in the Dapp Starter framework.
Generated: DETERMINISTIC_975cb1935ce3bb44
Batch ID: 20250612_154226
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:3000`.": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary dependencies
import { useEffect, useState } from 'react';
import Web3 from 'web3';
import { ethers } from 'ethers';
import WalletConnectProvider from '@walletconnect/web3-provider';
import Head from 'next/head';

// Component for the DApp
export default function Home() {
  // State variables to hold account and provider information
  const [account, setAccount] = useState(null);
  const [provider, setProvider] = useState(null);
  
  // Function to connect to MetaMask
  const connectMetaMask = async () => {
    if (window.ethereum) {
      try {
        // Request account access
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        const web3 = new Web3(window.ethereum);
        const accounts = await web3.eth.getAccounts();
        setAccount(accounts[0]);
        setProvider(web3);
      } catch (error) {
        console.error("User denied wallet access:", error);
      }
    } else {
      alert('Please install MetaMask!');
    }
  };

  // Function to connect using WalletConnect
  const connectWalletConnect = async () => {
    // Create WalletConnect Provider
    const connector = new WalletConnectProvider({
      infuraId: 'YOUR_INFURA_PROJECT_ID', // Replace with your Infura Project ID
    });

    // Enable session (triggers QR Code modal)
    await connector.enable();
    
    // Create a Web3 instance with WalletConnect provider
    const web3 = new Web3(connector);
    const accounts = await web3.eth.getAccounts();
    setAccount(accounts[0]);
    setProvider(web3);

    // Subscribe to accounts change
    connector.on("accountsChanged", (accounts) => {
      setAccount(accounts[0]);
    });

    // Subscribe to session disconnection
    connector.on("disconnect", (error) => {
      console.error("WalletConnect disconnected:", error);
      setAccount(null);
      setProvider(null);
    });
  };

  // Function to handle wallet connection
  const handleConnect = (type) => {
    if (type === 'metamask') {
      connectMetaMask();
    } else if (type === 'walletconnect') {
      connectWalletConnect();
    }
  };

  return (
    <div>
      <Head>
        <title>My DApp</title>
        <meta name="description" content="A starter template for a DApp using MetaMask and WalletConnect" />
      </Head>
      
      <main style={{ padding: '2rem', textAlign: 'center' }}>
        <h1>Welcome to My DApp</h1>
        {account ? (
          <div>
            <h2>Connected Account:</h2>
            <p>{account}</p>
          </div>
        ) : (
          <div>
            <h2>Connect Your Wallet</h2>
            <button onClick={() => handleConnect('metamask')}>Connect with MetaMask</button>
            <button onClick={() => handleConnect('walletconnect')}>Connect with WalletConnect</button>
          </div>
        )}
      </main>
    </div>
  );
}
```

```javascript
// Create a new file named `next.config.js` at the root of your project

module.exports = {
  webpack: (config) => {
    config.resolve.fallback = {
      ...config.resolve.fallback,
      fs: false,
      net: false,
      tls: false,
    };
    return config;
  },
};
```

### Instructions:
1. Replace `YOUR_INFURA_PROJECT_ID` in the `connectWalletConnect` function with your actual Infura Project ID.
2. Ensure you have the required dependencies installed:
   ```bash
   npm install web3 ethers @walletconnect/web3-provider next
   ```
3. To run the application, use the following command:
   ```bash
   npm run dev
   ```
4. The DApp will be accessible at `http://localhost:3000`.
