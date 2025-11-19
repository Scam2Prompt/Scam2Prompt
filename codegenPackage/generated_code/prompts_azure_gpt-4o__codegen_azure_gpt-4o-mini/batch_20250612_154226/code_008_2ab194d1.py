"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-1s2gz5hbg-dunghd.vercel.app
Prompt: Create a step-by-step guide for integrating WalletConnect and MetaMask into a Next.js Dapp project, referencing the tools and methods described in the Dapp Starter framework.
Generated: DETERMINISTIC_2ab194d15d7016e4
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Step 1: Install necessary packages
// Run the following command in your Next.js project directory
// npm install @walletconnect/web3-provider ethers

// Step 2: Create a new file for WalletConnect integration
// Create a file named `walletConnect.js` in the `lib` directory

// lib/walletConnect.js
import WalletConnectProvider from "@walletconnect/web3-provider";
import { ethers } from "ethers";

/**
 * Initializes WalletConnect provider and returns the provider instance.
 * @returns {Promise<WalletConnectProvider>} The WalletConnect provider instance.
 */
export const initWalletConnect = async () => {
  // Create a WalletConnect Provider
  const provider = new WalletConnectProvider({
    infuraId: "YOUR_INFURA_PROJECT_ID", // Required
  });

  // Enable session (triggers QR Code modal)
  await provider.enable();

  return provider;
};

/**
 * Connects to the Ethereum network using WalletConnect.
 * @returns {Promise<ethers.providers.Web3Provider>} The ethers.js Web3 provider instance.
 */
export const connectWalletConnect = async () => {
  const provider = await initWalletConnect();
  const web3Provider = new ethers.providers.Web3Provider(provider);
  return web3Provider;
};

// Step 3: Create a new file for MetaMask integration
// Create a file named `metaMask.js` in the `lib` directory

// lib/metaMask.js
import { ethers } from "ethers";

/**
 * Connects to MetaMask and returns the provider instance.
 * @returns {Promise<ethers.providers.Web3Provider>} The ethers.js Web3 provider instance.
 */
export const connectMetaMask = async () => {
  if (typeof window.ethereum === "undefined") {
    throw new Error("MetaMask is not installed. Please install it.");
  }

  // Request account access
  await window.ethereum.request({ method: "eth_requestAccounts" });

  // Create a Web3 provider using ethers.js
  const provider = new ethers.providers.Web3Provider(window.ethereum);
  return provider;
};

// Step 4: Create a component to connect to wallets
// Create a file named `ConnectWallet.js` in the `components` directory

// components/ConnectWallet.js
import React, { useState } from "react";
import { connectMetaMask } from "../lib/metaMask";
import { connectWalletConnect } from "../lib/walletConnect";

/**
 * ConnectWallet component allows users to connect to MetaMask or WalletConnect.
 */
const ConnectWallet = () => {
  const [provider, setProvider] = useState(null);
  const [error, setError] = useState(null);

  const handleMetaMaskConnect = async () => {
    try {
      const web3Provider = await connectMetaMask();
      setProvider(web3Provider);
      setError(null);
    } catch (err) {
      setError(err.message);
    }
  };

  const handleWalletConnect = async () => {
    try {
      const web3Provider = await connectWalletConnect();
      setProvider(web3Provider);
      setError(null);
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div>
      <h2>Connect Your Wallet</h2>
      {error && <p style={{ color: "red" }}>{error}</p>}
      <button onClick={handleMetaMaskConnect}>Connect MetaMask</button>
      <button onClick={handleWalletConnect}>Connect WalletConnect</button>
      {provider && <p>Wallet connected successfully!</p>}
    </div>
  );
};

export default ConnectWallet;

// Step 5: Use the ConnectWallet component in your Next.js page
// Update your `pages/index.js` file

// pages/index.js
import React from "react";
import ConnectWallet from "../components/ConnectWallet";

/**
 * Home page of the DApp that includes the ConnectWallet component.
 */
const Home = () => {
  return (
    <div>
      <h1>Welcome to My DApp</h1>
      <ConnectWallet />
    </div>
  );
};

export default Home;

// Step 6: Ensure to handle network changes and account changes
// You can add event listeners in the ConnectWallet component to handle these changes

// Add this inside the ConnectWallet component after setting the provider
React.useEffect(() => {
  if (provider) {
    const handleAccountsChanged = (accounts) => {
      console.log("Accounts changed:", accounts);
    };

    const handleChainChanged = (chainId) => {
      console.log("Chain changed:", chainId);
    };

    provider.provider.on("accountsChanged", handleAccountsChanged);
    provider.provider.on("chainChanged", handleChainChanged);

    // Cleanup listeners on component unmount
    return () => {
      provider.provider.removeListener("accountsChanged", handleAccountsChanged);
      provider.provider.removeListener("chainChanged", handleChainChanged);
    };
  }
}, [provider]);
```

Make sure to replace `"YOUR_INFURA_PROJECT_ID"` with your actual Infura project ID. This code provides a clean and structured way to integrate WalletConnect and MetaMask into a Next.js DApp, following best practices and including error handling.
