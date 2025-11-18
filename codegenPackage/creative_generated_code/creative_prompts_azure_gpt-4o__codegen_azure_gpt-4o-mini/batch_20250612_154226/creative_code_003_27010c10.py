"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-1s2gz5hbg-dunghd.vercel.app
Prompt: Build a Dapp using the Dapp Starter template that supports 1-click deployment and includes features for connecting to MetaMask and WalletConnect.
Generated: DETERMINISTIC_27010c101ed497d2
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useEffect, useState } from 'react';
import { ethers } from 'ethers';
import WalletConnectProvider from "@walletconnect/web3-provider";
import './App.css';

// Define the App component
function App() {
  // State variables for managing account and provider
  const [account, setAccount] = useState(null);
  const [provider, setProvider] = useState(null);

  // Connect to MetaMask
  const connectMetaMask = async () => {
    try {
      // Request account access if needed
      if (window.ethereum) {
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        setAccount(accounts[0]);
        const ethersProvider = new ethers.providers.Web3Provider(window.ethereum);
        setProvider(ethersProvider);
      } else {
        alert('MetaMask is not installed. Please install it to use this Dapp.');
      }
    } catch (error) {
      console.error('Error connecting to MetaMask:', error);
    }
  };

  // Connect to WalletConnect
  const connectWalletConnect = async () => {
    const provider = new WalletConnectProvider({
      infuraId: "YOUR_INFURA_PROJECT_ID", // Replace with your Infura project ID
    });

    // Enable session (triggers QR Code modal)
    await provider.enable();

    const ethersProvider = new ethers.providers.Web3Provider(provider);
    const accounts = await ethersProvider.listAccounts();
    setAccount(accounts[0]);
    setProvider(ethersProvider);
  };

  // Effect for handling account changes
  useEffect(() => {
    if (provider) {
      provider.on('accountsChanged', (accounts) => {
        setAccount(accounts[0]);
      });

      provider.on('chainChanged', (chainId) => {
        window.location.reload();
      });

      provider.on('disconnect', (error) => {
        console.error('Wallet disconnected:', error);
        setAccount(null);
      });
    }
  }, [provider]);

  return (
    <div className="App">
      <h1>My DApp</h1>
      {account ? (
        <div>
          <p>Connected account: {account}</p>
        </div>
      ) : (
        <div>
          <button onClick={connectMetaMask}>Connect with MetaMask</button>
          <button onClick={connectWalletConnect}>Connect with WalletConnect</button>
        </div>
      )}
    </div>
  );
}

export default App;
```

Make sure to replace `"YOUR_INFURA_PROJECT_ID"` with your actual Infura project ID for WalletConnect to work properly.
