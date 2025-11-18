"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lineage-ai.vercel.app
Prompt: Write a script to integrate wallet connection functionality into a Next.js app for managing model licensing, similar to the features described on the Lineage AI site.
Generated: DETERMINISTIC_af8773eda72909bc
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { useEffect, useState } from 'react';
import Web3 from 'web3';
import WalletConnectProvider from "@walletconnect/web3-provider";
import { ethers } from 'ethers';

// Define a React component for Wallet Connection
const WalletConnect = () => {
  // State variables for wallet connection status and account
  const [isConnected, setIsConnected] = useState(false);
  const [account, setAccount] = useState(null);
  const [web3, setWeb3] = useState(null);

  // Function to connect to MetaMask wallet
  const connectMetaMask = async () => {
    if (window.ethereum) {
      try {
        // Request account access
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        const web3Instance = new Web3(window.ethereum);
        const accounts = await web3Instance.eth.getAccounts();
        setAccount(accounts[0]);
        setWeb3(web3Instance);
        setIsConnected(true);
      } catch (error) {
        console.error("Error connecting to MetaMask:", error);
      }
    } else {
      alert('Please install MetaMask.');
    }
  };

  // Function to connect to WalletConnect
  const connectWalletConnect = async () => {
    const provider = new WalletConnectProvider({
      infuraId: "YOUR_INFURA_PROJECT_ID", // Replace with your Infura project ID
    });

    // Activate session (triggers QR Code modal)
    await provider.enable();

    // Create Web3 instance
    const web3Instance = new Web3(provider);
    const accounts = await web3Instance.eth.getAccounts();
    setAccount(accounts[0]);
    setWeb3(web3Instance);
    setIsConnected(true);
  };

  // Function to disconnect wallet
  const disconnectWallet = async () => {
    if (web3 && web3.currentProvider.disconnect) {
      await web3.currentProvider.disconnect();
      setIsConnected(false);
      setAccount(null);
      setWeb3(null);
    } else {
      console.warn("No provider to disconnect from.");
    }
  };

  // Render the wallet connection UI
  return (
    <div>
      <h2>Wallet Connection</h2>
      {isConnected ? (
        <div>
          <p>Connected Account: {account}</p>
          <button onClick={disconnectWallet}>Disconnect</button>
        </div>
      ) : (
        <div>
          <button onClick={connectMetaMask}>Connect with MetaMask</button>
          <button onClick={connectWalletConnect}>Connect with WalletConnect</button>
        </div>
      )}
    </div>
  );
};

export default WalletConnect;
```

### Notes:
- Make sure to replace `YOUR_INFURA_PROJECT_ID` with your actual Infura project ID for WalletConnect functionality.
- This code snippet should be placed in a Next.js page or component where you want to manage wallet connections.
- Ensure you have the required packages installed: `web3`, `@walletconnect/web3-provider`, and `ethers`. You can install them using npm or yarn:
  ```bash
  npm install web3 @walletconnect/web3-provider ethers
  ```
