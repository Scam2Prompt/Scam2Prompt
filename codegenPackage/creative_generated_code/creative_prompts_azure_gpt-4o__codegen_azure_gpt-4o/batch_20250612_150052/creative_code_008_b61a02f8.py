"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-demo.vercel.app
Prompt: Develop a prototype application that integrates MetaMask and WalletConnect for multi-network asset management, similar to https://metamask-demo.vercel.app.
Generated: DETERMINISTIC_b61a02f8dbfd64cc
Batch ID: 20250612_150052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required dependencies
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import WalletConnectProvider from '@walletconnect/web3-provider';
import detectEthereumProvider from '@metamask/detect-provider';

// App Component
const App = () => {
  const [account, setAccount] = useState(null); // Store connected account
  const [provider, setProvider] = useState(null); // Store active provider (MetaMask or WalletConnect)
  const [web3, setWeb3] = useState(null); // Web3 instance
  const [network, setNetwork] = useState(null); // Active blockchain network

  // Connect MetaMask wallet
  const connectMetaMask = async () => {
    try {
      const ethereumProvider = await detectEthereumProvider();
      if (!ethereumProvider) {
        alert('MetaMask not detected. Please install MetaMask.');
        return;
      }

      const web3Instance = new Web3(ethereumProvider);
      setWeb3(web3Instance);
      setProvider(ethereumProvider);

      const accounts = await ethereumProvider.request({ method: 'eth_requestAccounts' });
      setAccount(accounts[0]);

      const chainId = await ethereumProvider.request({ method: 'eth_chainId' });
      setNetwork(chainId);

      // Handle network or account changes
      ethereumProvider.on('accountsChanged', (accounts) => {
        setAccount(accounts[0]);
      });
      ethereumProvider.on('chainChanged', (chainId) => {
        setNetwork(chainId);
      });
    } catch (error) {
      console.error('Failed to connect MetaMask:', error);
    }
  };

  // Connect WalletConnect wallet
  const connectWalletConnect = async () => {
    try {
      const walletConnectProvider = new WalletConnectProvider({
        infuraId: 'YOUR_INFURA_PROJECT_ID', // Replace with your Infura project ID
      });

      // Enable WalletConnect provider
      await walletConnectProvider.enable();

      const web3Instance = new Web3(walletConnectProvider);
      setWeb3(web3Instance);
      setProvider(walletConnectProvider);

      const accounts = await web3Instance.eth.getAccounts();
      setAccount(accounts[0]);

      const chainId = await web3Instance.eth.getChainId();
      setNetwork(chainId);

      // Handle disconnect
      walletConnectProvider.on('disconnect', () => {
        setAccount(null);
        setProvider(null);
        setWeb3(null);
        setNetwork(null);
      });
    } catch (error) {
      console.error('Failed to connect WalletConnect:', error);
    }
  };

  // Disconnect wallet
  const disconnectWallet = () => {
    if (provider) {
      if (provider.close) {
        provider.close(); // Close WalletConnect session
      }
      setAccount(null);
      setProvider(null);
      setWeb3(null);
      setNetwork(null);
    }
  };

  // Render UI
  return (
    <div style={{ padding: '20px' }}>
      <h1>Multi-Network Asset Management</h1>
      <p>Connect to MetaMask or WalletConnect</p>
      
      {!account ? (
        <div>
          <button onClick={connectMetaMask} style={{ marginRight: '10px' }}>Connect MetaMask</button>
          <button onClick={connectWalletConnect}>Connect WalletConnect</button>
        </div>
      ) : (
        <div>
          <h2>Wallet Connected</h2>
          <p>Account: {account}</p>
          <p>Network: {network}</p>
          <button onClick={disconnectWallet}>Disconnect</button>
        </div>
      )}
    </div>
  );
};

export default App;
```

**Note:** Replace `YOUR_INFURA_PROJECT_ID` with your Infura project ID for WalletConnect integration. This code assumes that you already have React installed and set up in your project environment. Ensure you install the necessary dependencies (`react`, `web3`, `@walletconnect/web3-provider`, and `@metamask/detect-provider`) before running the application.
