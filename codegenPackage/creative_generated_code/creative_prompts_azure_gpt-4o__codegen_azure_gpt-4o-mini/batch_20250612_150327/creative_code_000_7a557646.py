"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect-demo.sunmoney.net
Prompt: Write a React component that integrates WalletConnect to establish a connection between a dApp and a cryptocurrency wallet, similar to the demo at walletconnect-demo.sunmoney.net.
Generated: DETERMINISTIC_7a557646c3ab8995
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useEffect, useState } from 'react';
import WalletConnectProvider from "@walletconnect/web3-provider"; // Import WalletConnect provider
import { ethers } from "ethers"; // Import ethers.js for interacting with Ethereum
import './App.css'; // Importing CSS for styling

const App = () => {
  // State variables to manage wallet connection and account information
  const [connector, setConnector] = useState(null);
  const [account, setAccount] = useState(null);
  const [provider, setProvider] = useState(null);

  // Function to create a WalletConnect provider
  const createWalletConnectProvider = () => {
    const walletConnector = new WalletConnectProvider({
      infuraId: "YOUR_INFURA_PROJECT_ID" // Replace with your Infura Project ID
    });
    return walletConnector;
  };

  // Function to connect to the wallet
  const connectWallet = async () => {
    try {
      const walletConnector = createWalletConnectProvider();
      await walletConnector.enable(); // Enable session (triggers QR Code modal)
      const ethersProvider = new ethers.providers.Web3Provider(walletConnector); // Create ethers provider
      const accounts = await ethersProvider.listAccounts(); // Get connected accounts
      setAccount(accounts[0]); // Set the first account
      setProvider(ethersProvider); // Set the ethers provider
      setConnector(walletConnector); // Set the connector
    } catch (error) {
      console.error("Failed to connect to wallet:", error);
    }
  };

  // Function to disconnect the wallet
  const disconnectWallet = async () => {
    if (connector) {
      await connector.killSession(); // Disconnect the session
      setAccount(null); // Reset account state
      setProvider(null); // Reset provider state
      setConnector(null); // Reset connector state
    }
  };

  // Effect to handle session expiration
  useEffect(() => {
    if (connector) {
      connector.on("disconnect", (error) => {
        if (error) {
          console.error("WalletConnect disconnect error:", error);
        }
        disconnectWallet();
      });
    }
  }, [connector]);

  return (
    <div className="App">
      <h1>Connect Your Wallet</h1>
      {account ? (
        <div>
          <p>Connected Account: {account}</p>
          <button onClick={disconnectWallet}>Disconnect</button>
        </div>
      ) : (
        <button onClick={connectWallet}>Connect Wallet</button>
      )}
    </div>
  );
};

export default App;
```

**Note:** Remember to replace `"YOUR_INFURA_PROJECT_ID"` with your actual Infura Project ID to enable the connection to Ethereum networks. Make sure to install the necessary dependencies using:
```bash
npm install @walletconnect/web3-provider ethers
```
