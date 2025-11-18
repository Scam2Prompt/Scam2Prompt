"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-1s2gz5hbg-dunghd.vercel.app
Prompt: Create a step-by-step guide for integrating WalletConnect and MetaMask into a Next.js Dapp project, referencing the tools and methods described in the Dapp Starter framework.
Generated: DETERMINISTIC_2ab194d15d7016e4
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Step 1: Install required dependencies
// In your Next.js project, install WalletConnect and MetaMask libraries.
npm install @walletconnect/client @walletconnect/web3-provider ethers

// Step 2: Create a WalletConnect and MetaMask integration file
// Create a file named walletConnect.js in your project’s utils folder.
import WalletConnectProvider from "@walletconnect/web3-provider";
import { ethers } from "ethers";

// Create a function to initialize WalletConnect
export const initWalletConnect = async () => {
  // Create a WalletConnect Provider
  const provider = new WalletConnectProvider({
    infuraId: "YOUR_INFURA_PROJECT_ID", // Replace with your Infura project ID
  });

  // Enable session (triggers QR Code modal)
  await provider.enable();

  // Create a web3 instance
  const web3Provider = new ethers.providers.Web3Provider(provider);

  return { provider, web3Provider };
};

// Step 3: Create a MetaMask connection function
export const initMetaMask = async () => {
  if (typeof window.ethereum === 'undefined') {
    throw new Error("MetaMask is not installed");
  }

  // Request account access
  await window.ethereum.request({ method: 'eth_requestAccounts' });

  // Create a web3 instance using ethers.js
  const web3Provider = new ethers.providers.Web3Provider(window.ethereum);

  return web3Provider;
};

// Step 4: Create a connection hook
// Create a file named useWallet.js in your hooks folder.
import { useState, useEffect } from 'react';
import { initWalletConnect, initMetaMask } from '../utils/walletConnect';

const useWallet = () => {
  const [provider, setProvider] = useState(null);
  const [web3Provider, setWeb3Provider] = useState(null);
  
  const connectWallet = async (walletType) => {
    try {
      if (walletType === 'walletconnect') {
        const { provider, web3Provider } = await initWalletConnect();
        setProvider(provider);
        setWeb3Provider(web3Provider);
      } else if (walletType === 'metamask') {
        const web3Provider = await initMetaMask();
        setWeb3Provider(web3Provider);
      }
    } catch (error) {
      console.error("Failed to connect to wallet:", error);
    }
  };

  return { provider, web3Provider, connectWallet };
};

// Step 5: Use the hook in your DApp component
// Example usage in a component
import { useWallet } from '../hooks/useWallet';

const WalletConnector = () => {
  const { connectWallet } = useWallet();

  return (
    <div>
      <h1>Connect Your Wallet</h1>
      <button onClick={() => connectWallet('metamask')}>Connect MetaMask</button>
      <button onClick={() => connectWallet('walletconnect')}>Connect WalletConnect</button>
    </div>
  );
};

export default WalletConnector;

// Step 6: Ensure proper cleanup when the component unmounts
// Modify the useWallet hook to include a cleanup function
useEffect(() => {
  return () => {
    if (provider) {
      // Properly disconnect WalletConnect session
      provider.disconnect();
    }
  };
}, [provider]);

// Add this cleanup to avoid memory leaks and ensure the session is closed on unmount.
```

Make sure to replace `"YOUR_INFURA_PROJECT_ID"` with your actual Infura project ID. This code provides a modular approach to integrating WalletConnect and MetaMask into a Next.js DApp, following best practices and including proper error handling and cleanup.
