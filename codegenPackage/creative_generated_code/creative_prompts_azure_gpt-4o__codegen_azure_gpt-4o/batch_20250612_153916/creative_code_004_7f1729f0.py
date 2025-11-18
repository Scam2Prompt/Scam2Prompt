"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unichain-rooster.nfts2.me
Prompt: Generate code in React to integrate the "Connect Wallet" functionality for the Unichain-Rooster NFT platform, ensuring compatibility with Ethereum wallets.
Generated: DETERMINISTIC_7f1729f0c50df8a2
Batch ID: 20250612_153916
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

const ConnectWallet = () => {
  // State variables to manage wallet connection and account info
  const [account, setAccount] = useState(null);
  const [error, setError] = useState("");

  // Function to connect the wallet
  const connectWallet = async () => {
    try {
      // Check if the browser has Ethereum provider (e.g., MetaMask)
      if (window.ethereum) {
        const web3 = new Web3(window.ethereum);

        // Request user to connect their wallet
        const accounts = await window.ethereum.request({
          method: "eth_requestAccounts",
        });

        // Set the first account as the connected account
        setAccount(accounts[0]);
        setError(""); // Clear previous errors
      } else {
        setError("Please install MetaMask or another Ethereum wallet provider.");
      }
    } catch (err) {
      setError("Failed to connect wallet. Please try again.");
      console.error(err);
    }
  };

  // Handle account changes (e.g., user switches accounts in MetaMask)
  useEffect(() => {
    if (window.ethereum) {
      window.ethereum.on("accountsChanged", (accounts) => {
        if (accounts.length > 0) {
          setAccount(accounts[0]);
        } else {
          setAccount(null);
          setError("Wallet disconnected.");
        }
      });

      // Optional: Handle chain changes (e.g., user switches networks)
      window.ethereum.on("chainChanged", () => {
        window.location.reload();
      });
    }
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Unichain-Rooster NFT Platform</h1>
      {!account ? (
        <button
          onClick={connectWallet}
          style={{
            padding: "10px 20px",
            fontSize: "16px",
            cursor: "pointer",
            backgroundColor: "#007bff",
            color: "#fff",
            border: "none",
            borderRadius: "5px",
          }}
        >
          Connect Wallet
        </button>
      ) : (
        <div>
          <p style={{ fontSize: "18px" }}>
            Connected Account: <strong>{account}</strong>
          </p>
        </div>
      )}
      {error && <p style={{ color: "red" }}>{error}</p>}
    </div>
  );
};

export default ConnectWallet;
```
