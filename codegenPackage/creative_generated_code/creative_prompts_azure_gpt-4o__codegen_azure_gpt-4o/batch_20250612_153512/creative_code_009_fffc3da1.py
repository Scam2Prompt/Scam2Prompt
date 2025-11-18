"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://puddy.pages.dev
Prompt: Create a secure wallet connection flow for Ethereum and Solana wallets using React and web3.js, inspired by the Pudgy Penguins $PENGU claim page.
Generated: DETERMINISTIC_fffc3da1105f66be
Batch ID: 20250612_153512
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary libraries
import React, { useState, useEffect } from "react";
import Web3 from "web3";
import { Connection, PublicKey } from "@solana/web3.js";

// Wallet connection component
const WalletConnect = () => {
  // State variables
  const [ethereumWallet, setEthereumWallet] = useState(null); // Ethereum wallet address
  const [solanaWallet, setSolanaWallet] = useState(null); // Solana wallet address
  const [error, setError] = useState(null); // Error message

  // Connect Ethereum wallet
  const connectEthereumWallet = async () => {
    try {
      // Check if MetaMask is installed
      if (window.ethereum) {
        const web3 = new Web3(window.ethereum); // Create Web3 instance
        await window.ethereum.request({ method: "eth_requestAccounts" }); // Request wallet access
        const accounts = await web3.eth.getAccounts(); // Fetch wallet address
        setEthereumWallet(accounts[0]); // Set wallet address in state
      } else {
        throw new Error("MetaMask not detected. Please install MetaMask to connect.");
      }
    } catch (e) {
      setError(e.message); // Set error message
    }
  };

  // Connect Solana wallet
  const connectSolanaWallet = async () => {
    try {
      // Check if Solana wallet is installed
      if (window.solana && window.solana.isPhantom) {
        const response = await window.solana.connect(); // Connect to Phantom wallet
        setSolanaWallet(response.publicKey.toString()); // Set wallet address in state
      } else {
        throw new Error("Phantom wallet not detected. Please install Phantom to connect.");
      }
    } catch (e) {
      setError(e.message); // Set error message
    }
  };

  // Error handling
  useEffect(() => {
    if (error) {
      console.error("Wallet connection error:", error); // Log error
    }
  }, [error]);

  return (
    <div style={{ padding: "20px", maxWidth: "400px", margin: "auto" }}>
      <h2>Wallet Connection</h2>
      {/* Ethereum Wallet Section */}
      <div>
        <h3>Ethereum</h3>
        <button onClick={connectEthereumWallet}>
          {ethereumWallet ? "Connected" : "Connect Ethereum Wallet"}
        </button>
        {ethereumWallet && <p>Wallet: {ethereumWallet}</p>}
      </div>

      {/* Solana Wallet Section */}
      <div style={{ marginTop: "20px" }}>
        <h3>Solana</h3>
        <button onClick={connectSolanaWallet}>
          {solanaWallet ? "Connected" : "Connect Solana Wallet"}
        </button>
        {solanaWallet && <p>Wallet: {solanaWallet}</p>}
      </div>

      {/* Error Message Display */}
      {error && <p style={{ color: "red" }}>Error: {error}</p>}
    </div>
  );
};

export default WalletConnect;
```
