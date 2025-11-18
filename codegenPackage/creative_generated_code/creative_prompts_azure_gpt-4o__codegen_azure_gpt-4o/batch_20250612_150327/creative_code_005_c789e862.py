"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-sdk-demo.pages.dev
Prompt: Create a React app that uses the MetaMask SDK to retrieve and display the user's wallet balance in Ether.
Generated: DETERMINISTIC_c789e862d855689d
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// File: src/App.js

import React, { useState, useEffect } from "react";
import { ethers } from "ethers"; // Import ethers.js for interacting with Ethereum blockchain

const App = () => {
  const [walletConnected, setWalletConnected] = useState(false); // State to track wallet connection
  const [walletAddress, setWalletAddress] = useState(""); // State to store user's wallet address
  const [balance, setBalance] = useState(""); // State to store Ether balance
  const [error, setError] = useState(""); // State to store error messages

  // Function to connect to MetaMask wallet
  const connectWallet = async () => {
    try {
      if (!window.ethereum) {
        throw new Error("MetaMask not detected. Please install MetaMask.");
      }
      const provider = new ethers.providers.Web3Provider(window.ethereum); // Create Web3 provider
      const accounts = await provider.send("eth_requestAccounts", []); // Request wallet connection
      setWalletAddress(accounts[0]); // Set wallet address
      setWalletConnected(true); // Mark wallet as connected
      fetchBalance(provider, accounts[0]); // Fetch Ether balance
    } catch (err) {
      setError(err.message); // Handle and display errors
      setWalletConnected(false); // Mark wallet as not connected
    }
  };

  // Function to fetch Ether balance
  const fetchBalance = async (provider, address) => {
    try {
      const balance = await provider.getBalance(address); // Get balance in Wei
      setBalance(ethers.utils.formatEther(balance)); // Format to Ether and update state
    } catch (err) {
      setError("Failed to fetch balance. Please try again."); // Handle errors
    }
  };

  useEffect(() => {
    // Check if MetaMask is already connected
    const checkWalletConnection = async () => {
      if (window.ethereum) {
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const accounts = await provider.listAccounts(); // Get currently connected accounts
        if (accounts.length > 0) {
          setWalletAddress(accounts[0]); // Set wallet address
          setWalletConnected(true); // Mark wallet as connected
          fetchBalance(provider, accounts[0]); // Fetch Ether balance
        }
      }
    };
    checkWalletConnection();
  }, []);

  return (
    <div style={{ fontFamily: "Arial, sans-serif", padding: "20px" }}>
      <h1>MetaMask Wallet Balance Viewer</h1>
      {!walletConnected ? (
        <div>
          <button onClick={connectWallet} style={{ padding: "10px 20px", cursor: "pointer" }}>
            Connect Wallet
          </button>
          {error && <p style={{ color: "red" }}>{error}</p>}
        </div>
      ) : (
        <div>
          <p>
            <strong>Wallet Address:</strong> {walletAddress}
          </p>
          <p>
            <strong>Balance:</strong> {balance} ETH
          </p>
        </div>
      )}
    </div>
  );
};

export default App;
```

```json
// File: package.json

{
  "name": "metamask-wallet-balance",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "ethers": "^5.7.1"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  }
}
```

```jsx
// File: src/index.js

import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";

// Render the App component to the root element
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
  );
```

```html
<!-- File: public/index.html -->

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>MetaMask Wallet Balance Viewer</title>
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>
```
