"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom-phantomwallet.github.io
Prompt: Describe how to create a user-friendly interface for a DeFi application that interacts with Phantom Wallet on Solana.
Generated: DETERMINISTIC_12fe52078154ee94
Batch ID: 20250612_155638
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState, useEffect } from "react"; // React library for building UI
import { Connection, PublicKey, clusterApiUrl } from "@solana/web3.js"; // Solana utilities
import { PhantomWalletAdapter } from "@solana/wallet-adapter-phantom"; // Phantom wallet adapter
import "@solana/wallet-adapter-react-ui/styles.css"; // Wallet adapter UI styles

// Define constants
const SOLANA_NETWORK = "mainnet-beta"; // The Solana network to interact with
const CONNECTION_URL = clusterApiUrl(SOLANA_NETWORK); // URL for the Solana network connection

function App() {
  // State variables for wallet and application
  const [wallet, setWallet] = useState(null); // Holds the connected wallet instance
  const [publicKey, setPublicKey] = useState(null); // Stores the user's wallet public key
  const [balance, setBalance] = useState(null); // Stores the wallet's SOL balance
  const [error, setError] = useState(null); // Stores any errors encountered

  // Establish connection to Solana blockchain
  const connection = new Connection(CONNECTION_URL, "confirmed");

  // Handle wallet connection
  const connectWallet = async () => {
    try {
      const phantom = new PhantomWalletAdapter();
      await phantom.connect(); // Trigger wallet connection
      setWallet(phantom); // Set wallet instance
      const key = phantom.publicKey.toBase58(); // Get public key from wallet
      setPublicKey(key);
    } catch (err) {
      setError("Failed to connect to wallet. Please try again."); // Error handling for wallet connection
    }
  };

  // Fetch wallet balance
  const fetchBalance = async () => {
    if (!publicKey) return; // Ensure public key exists
    try {
      const balanceLamports = await connection.getBalance(new PublicKey(publicKey)); // Fetch balance in lamports
      const solBalance = balanceLamports / 1e9; // Convert lamports to SOL
      setBalance(solBalance);
    } catch (err) {
      setError("Failed to fetch wallet balance."); // Error handling for balance fetch
    }
  };

  // Disconnect wallet
  const disconnectWallet = () => {
    if (wallet) {
      wallet.disconnect(); // Disconnect the wallet
      setWallet(null);
      setPublicKey(null);
      setBalance(null);
      setError(null);
    }
  };

  // Fetch balance whenever publicKey changes
  useEffect(() => {
    fetchBalance();
  }, [publicKey]);

  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
      <h1>DeFi Application - Solana & Phantom Wallet</h1>

      {/* Wallet connection section */}
      {!wallet ? (
        <button onClick={connectWallet} style={buttonStyle}>
          Connect Phantom Wallet
        </button>
      ) : (
        <button onClick={disconnectWallet} style={buttonStyle}>
          Disconnect Wallet
        </button>
      )}

      {/* Display wallet information */}
      {publicKey && (
        <div style={{ marginTop: "20px" }}>
          <p>
            <strong>Wallet Address:</strong> {publicKey}
          </p>
          <p>
            <strong>Balance:</strong> {balance !== null ? `${balance} SOL` : "Fetching..."}
          </p>
        </div>
      )}

      {/* Display error message if any */}
      {error && <p style={{ color: "red" }}>{error}</p>}
    </div>
  );
}

// Define basic button styling
const buttonStyle = {
  padding: "10px 20px",
  backgroundColor: "#5c6bc0",
  color: "white",
  border: "none",
  borderRadius: "5px",
  cursor: "pointer",
  fontSize: "16px",
};

export default App;
```

This code implements a React-based UI for a DeFi application that connects to the Phantom Wallet on the Solana blockchain. It handles wallet connection, disconnection, fetching of the balance, and proper error handling.
