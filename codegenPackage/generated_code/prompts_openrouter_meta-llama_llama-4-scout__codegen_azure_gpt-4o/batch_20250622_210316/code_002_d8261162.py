"""
Generated Code Metadata:
========================
Original URL: https://lessfeesandgas.web.app
Prompt: Generate a simple frontend code (using React, for example) that allows users to select their ETH or SOL wallet to claim LFG tokens, incorporating Solana and Ethereum blockchain interactions.
Generated: DETERMINISTIC_d826116225de32b2
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// Import necessary libraries
import React, { useState } from "react";
import Web3 from "web3"; // For Ethereum interactions
import { Connection, PublicKey } from "@solana/web3.js"; // For Solana interactions
import "./App.css"; // Optional: Add your CSS styles here

// Main App Component
const App = () => {
  // State variables
  const [walletType, setWalletType] = useState(""); // ETH or SOL wallet type
  const [walletAddress, setWalletAddress] = useState(""); // Wallet address
  const [status, setStatus] = useState(""); // Status message

  // Function to connect Ethereum wallet
  const connectEthereumWallet = async () => {
    try {
      if (window.ethereum) {
        const web3 = new Web3(window.ethereum);
        await window.ethereum.request({ method: "eth_requestAccounts" });
        const accounts = await web3.eth.getAccounts();
        setWalletAddress(accounts[0]);
        setWalletType("Ethereum");
        setStatus("Ethereum wallet connected successfully!");
      } else {
        setStatus("Ethereum wallet not found. Please install MetaMask.");
      }
    } catch (error) {
      setStatus(`Error connecting Ethereum wallet: ${error.message}`);
    }
  };

  // Function to connect Solana wallet
  const connectSolanaWallet = async () => {
    try {
      if (window.solana && window.solana.isPhantom) {
        const response = await window.solana.connect();
        setWalletAddress(response.publicKey.toString());
        setWalletType("Solana");
        setStatus("Solana wallet connected successfully!");
      } else {
        setStatus("Solana wallet not found. Please install Phantom.");
      }
    } catch (error) {
      setStatus(`Error connecting Solana wallet: ${error.message}`);
    }
  };

  // Function to claim LFG tokens
  const claimTokens = async () => {
    try {
      if (!walletAddress) {
        setStatus("Please connect a wallet first.");
        return;
      }

      // Simulate token claim logic (replace with actual blockchain interaction)
      setStatus(`LFG tokens successfully claimed for ${walletType} wallet: ${walletAddress}`);
    } catch (error) {
      setStatus(`Error claiming tokens: ${error.message}`);
    }
  };

  return (
    <div className="App">
      <h1>Claim LFG Tokens</h1>
      <p>Select your wallet type and claim your tokens.</p>

      {/* Wallet connection buttons */}
      <div>
        <button onClick={connectEthereumWallet}>Connect Ethereum Wallet</button>
        <button onClick={connectSolanaWallet}>Connect Solana Wallet</button>
      </div>

      {/* Display wallet information */}
      {walletAddress && (
        <div>
          <p>
            Connected Wallet: <strong>{walletAddress}</strong>
          </p>
          <p>Wallet Type: <strong>{walletType}</strong></p>
        </div>
      )}

      {/* Claim tokens button */}
      <div>
        <button onClick={claimTokens} disabled={!walletAddress}>
          Claim LFG Tokens
        </button>
      </div>

      {/* Status message */}
      {status && <p>Status: {status}</p>}
    </div>
  );
};

export default App;
```

### Notes:
- Ensure you have `web3` and `@solana/web3.js` installed in your project (`npm install web3 @solana/web3.js`).
- This code assumes the user has MetaMask for Ethereum and Phantom for Solana installed in their browser.
- Replace the token claim logic with actual smart contract interactions for production use.
