"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dao1.pro
Prompt: Develop a user interface for connecting multiple wallets (e.g., OKX, MetaMask, Trust Wallet) to a dApp, inspired by the DAO1 platform.
Generated: DETERMINISTIC_8e28a2f239b58118
Batch ID: 20250612_154752
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
import { ethers } from 'ethers';
import WalletConnectProvider from "@walletconnect/web3-provider";

// Define the WalletConnector component
const WalletConnector = () => {
  // State management for connected wallet and error handling
  const [wallet, setWallet] = useState(null);
  const [provider, setProvider] = useState(null);
  const [error, setError] = useState("");

  // Function to connect MetaMask wallet
  const connectMetaMask = async () => {
    try {
      if (!window.ethereum) {
        throw new Error("MetaMask is not installed.");
      }

      const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });
      const web3 = new Web3(window.ethereum);

      setWallet(accounts[0]);
      setProvider(web3);
    } catch (err) {
      setError(err.message);
    }
  };

  // Function to connect WalletConnect-compatible wallets (e.g., Trust Wallet, OKX Wallet)
  const connectWalletConnect = async () => {
    try {
      const walletConnectProvider = new WalletConnectProvider({
        infuraId: "YOUR_INFURA_ID", // Replace with your Infura project ID
      });

      await walletConnectProvider.enable();

      const web3 = new Web3(walletConnectProvider);

      const accounts = await web3.eth.getAccounts();

      setWallet(accounts[0]);
      setProvider(web3);
    } catch (err) {
      setError(err.message);
    }
  };

  // Disconnect wallet
  const disconnectWallet = () => {
    setWallet(null);
    setProvider(null);
    setError("");
  };

  // Effect hook to detect account changes
  useEffect(() => {
    if (window.ethereum) {
      window.ethereum.on("accountsChanged", (accounts) => {
        if (accounts.length > 0) {
          setWallet(accounts[0]);
        } else {
          disconnectWallet();
        }
      });

      window.ethereum.on("disconnect", () => disconnectWallet());
    }
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Wallet Connector</h1>

      {/* Display the connected wallet */}
      {wallet && (
        <div>
          <p>
            <strong>Connected Wallet:</strong> {wallet}
          </p>
          <button onClick={disconnectWallet} style={{ marginTop: "10px" }}>
            Disconnect Wallet
          </button>
        </div>
      )}

      {/* Display any error messages */}
      {error && <p style={{ color: "red" }}>{error}</p>}

      {/* Buttons for connecting wallets */}
      {!wallet && (
        <div>
          <button
            onClick={connectMetaMask}
            style={{
              marginRight: "10px",
              backgroundColor: "#F6851B",
              color: "#fff",
              padding: "10px 20px",
              border: "none",
              borderRadius: "5px",
              cursor: "pointer",
            }}
          >
            Connect MetaMask
          </button>
          <button
            onClick={connectWalletConnect}
            style={{
              backgroundColor: "#3B99FC",
              color: "#fff",
              padding: "10px 20px",
              border: "none",
              borderRadius: "5px",
              cursor: "pointer",
            }}
          >
            Connect WalletConnect
          </button>
        </div>
      )}
    </div>
  );
};

// Export the WalletConnector component as default
export default WalletConnector;
```
