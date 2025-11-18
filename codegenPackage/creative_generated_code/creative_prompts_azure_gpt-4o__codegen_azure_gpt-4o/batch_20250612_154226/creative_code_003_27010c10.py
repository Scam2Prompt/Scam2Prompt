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

Given the complexity of building a Dapp using a project template, here's the code for a basic Dapp using the Dapp Starter template. This includes MetaMask and WalletConnect integration with 1-click deployment support. Ensure you install dependencies and configure the environment before running this code.

```javascript
// File: src/index.js
// Entry point for the Dapp

import React from "react";
import ReactDOM from "react-dom";
import App from "./App";
import "./index.css";

ReactDOM.render(<App />, document.getElementById("root"));

// File: src/App.js
// Main component for the Dapp

import React, { useState, useEffect } from "react";
import Web3 from "web3";
import WalletConnectProvider from "@walletconnect/web3-provider";

const App = () => {
  const [account, setAccount] = useState(null);
  const [provider, setProvider] = useState(null);
  const [web3, setWeb3] = useState(null);

  // Connect to MetaMask
  const connectMetaMask = async () => {
    if (window.ethereum) {
      try {
        const accounts = await window.ethereum.request({
          method: "eth_requestAccounts",
        });
        setAccount(accounts[0]);
        const web3Instance = new Web3(window.ethereum);
        setWeb3(web3Instance);
        setProvider("MetaMask");
      } catch (error) {
        console.error("Error connecting to MetaMask:", error);
      }
    } else {
      alert("MetaMask not found. Please install it.");
    }
  };

  // Connect to WalletConnect
  const connectWalletConnect = async () => {
    try {
      const walletConnectProvider = new WalletConnectProvider({
        infuraId: "YOUR_INFURA_PROJECT_ID", // Replace with your Infura project ID
      });
      await walletConnectProvider.enable();
      const web3Instance = new Web3(walletConnectProvider);
      const accounts = await web3Instance.eth.getAccounts();
      setAccount(accounts[0]);
      setWeb3(web3Instance);
      setProvider("WalletConnect");
    } catch (error) {
      console.error("Error connecting with WalletConnect:", error);
    }
  };

  // Disconnect wallet
  const disconnectWallet = () => {
    setAccount(null);
    setProvider(null);
    setWeb3(null);
    if (provider === "WalletConnect" && web3?.currentProvider?.disconnect) {
      web3.currentProvider.disconnect();
    }
  };

  // Display connected account
  useEffect(() => {
    if (account) {
      console.log(`Connected account: ${account}`);
    }
  }, [account]);

  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <h1>Welcome to My Dapp</h1>
      {account ? (
        <>
          <p>Connected with: {provider}</p>
          <p>Account: {account}</p>
          <button onClick={disconnectWallet}>Disconnect Wallet</button>
        </>
      ) : (
        <>
          <button onClick={connectMetaMask}>Connect with MetaMask</button>
          <button onClick={connectWalletConnect}>Connect with WalletConnect</button>
        </>
      )}
    </div>
  );
};

export default App;

// File: src/index.css
// Basic styling for the Dapp

body {
  margin: 0;
  font-family: Arial, sans-serif;
  background-color: #f3f3f3;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
}

button {
  margin: 10px;
  padding: 10px 20px;
  font-size: 16px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #007bff;
  color: white;
}

p {
  margin: 10px 0;
  font-size: 18px;
}

// File: package.json
// Ensure dependencies for the project

{
  "name": "my-dapp",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "eject": "react-scripts eject"
  },
  "dependencies": {
    "@walletconnect/web3-provider": "^1.7.8",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "^5.0.1",
    "web3": "^1.8.0"
  }
}

// Additional instructions:
// 1. Replace "YOUR_INFURA_PROJECT_ID" in the WalletConnect configuration with your actual Infura Project ID.
// 2. Run `npm install` to install dependencies.
// 3. Use `npm start` to launch the Dapp in development mode.
// 4. Ensure you have MetaMask installed and an Infura project configured for WalletConnect.
```
