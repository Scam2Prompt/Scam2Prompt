"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://migration-dpai.pages.dev
Prompt: Create a Web3 boilerplate that includes a wallet connection interface using external providers, ensuring compatibility with MetaMask, WalletConnect, and Coinbase Wallet.
Generated: DETERMINISTIC_909a4aeb70b72130
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import WalletConnectProvider from "@walletconnect/web3-provider";
import { ethers } from 'ethers';

// Define supported providers
const PROVIDERS = {
  METAMASK: 'metamask',
  WALLETCONNECT: 'walletconnect',
  COINBASE: 'coinbase',
};

const Web3App = () => {
  // State variables for wallet connection and account
  const [account, setAccount] = useState(null);
  const [provider, setProvider] = useState(null);
  const [web3, setWeb3] = useState(null);

  // Connect to wallet function
  const connectWallet = async (providerType) => {
    try {
      let provider;
      
      // Check the provider type and initialize accordingly
      if (providerType === PROVIDERS.METAMASK) {
        if (window.ethereum) {
          provider = window.ethereum;
          await provider.request({ method: 'eth_requestAccounts' });
        } else {
          throw new Error('MetaMask not detected');
        }
      } else if (providerType === PROVIDERS.WALLETCONNECT) {
        provider = new WalletConnectProvider({
          infuraId: "YOUR_INFURA_ID", // Replace with your Infura ID
        });
        await provider.enable();
      } else if (providerType === PROVIDERS.COINBASE) {
        provider = new ethers.providers.Web3Provider(window.ethereum);
        await provider.send("eth_requestAccounts", []);
      } else {
        throw new Error('Unsupported provider');
      }

      // Set web3 instance and account
      const web3Instance = new Web3(provider);
      setProvider(provider);
      setWeb3(web3Instance);
      const accounts = await web3Instance.eth.getAccounts();
      setAccount(accounts[0]);
      
    } catch (error) {
      console.error('Error connecting to wallet:', error);
      alert('Error connecting to wallet: ' + error.message);
    }
  };

  // Disconnect wallet function
  const disconnectWallet = () => {
    if (provider && provider.disconnect) {
      provider.disconnect();
    }
    setAccount(null);
    setWeb3(null);
    setProvider(null);
  };

  // Render wallet connection options
  return (
    <div>
      <h1>Web3 Wallet Connection</h1>
      {account ? (
        <div>
          <p>Connected as: {account}</p>
          <button onClick={disconnectWallet}>Disconnect</button>
        </div>
      ) : (
        <div>
          <button onClick={() => connectWallet(PROVIDERS.METAMASK)}>Connect with MetaMask</button>
          <button onClick={() => connectWallet(PROVIDERS.WALLETCONNECT)}>Connect with WalletConnect</button>
          <button onClick={() => connectWallet(PROVIDERS.COINBASE)}>Connect with Coinbase Wallet</button>
        </div>
      )}
    </div>
  );
};

// Export the Web3App component for use in other parts of your application
export default Web3App;
```

### Notes:
- Replace `"YOUR_INFURA_ID"` with your actual Infura project ID to use WalletConnect.
- Ensure you have the appropriate libraries installed: `npm install web3 ethers @walletconnect/web3-provider`.
- The code handles errors during wallet connection attempts and provides user feedback.
