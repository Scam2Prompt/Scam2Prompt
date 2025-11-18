"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskwallett.creatorlink.net
Prompt: Develop a tutorial in code for integrating MetaMask with a React-based dApp, including functionality for connecting the wallet and displaying the user's account balance.
Generated: DETERMINISTIC_47df05a93b794f4a
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: src/App.js

import React, { useState, useEffect } from "react";
import { ethers } from "ethers";

function App() {
  // State variables
  const [account, setAccount] = useState(null); // Stores connected account
  const [balance, setBalance] = useState(null); // Stores account balance
  const [error, setError] = useState(null); // Stores any error messages

  // Function to check if MetaMask is installed
  const checkMetaMaskAvailability = () => {
    return typeof window.ethereum !== "undefined";
  };

  // Function to connect MetaMask wallet
  const connectWallet = async () => {
    try {
      if (!checkMetaMaskAvailability()) {
        throw new Error("MetaMask is not installed. Please install MetaMask to continue.");
      }

      // Request account access
      const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });
      setAccount(accounts[0]); // Set the first account as the connected account
      setError(null); // Clear any existing error messages
    } catch (err) {
      setError(err.message);
    }
  };

  // Function to fetch and format the user's account balance
  const fetchBalance = async () => {
    try {
      if (!account) {
        throw new Error("No account connected. Please connect your wallet first.");
      }

      const provider = new ethers.providers.Web3Provider(window.ethereum); // Create a provider using MetaMask
      const balance = await provider.getBalance(account); // Fetch balance in Wei
      setBalance(ethers.utils.formatEther(balance)); // Convert balance to Ether and update state
    } catch (err) {
      setError(err.message);
    }
  };

  // Listen for account changes or network changes
  useEffect(() => {
    if (checkMetaMaskAvailability()) {
      // Listen for account changes
      window.ethereum.on("accountsChanged", (accounts) => {
        setAccount(accounts.length > 0 ? accounts[0] : null);
        setBalance(null); // Reset balance when account changes
      });

      // Listen for network changes
      window.ethereum.on("chainChanged", () => {
        setBalance(null); // Reset balance when network changes
      });
    }

    // Cleanup event listeners when component unmounts
    return () => {
      if (checkMetaMaskAvailability()) {
        window.ethereum.removeListener("accountsChanged", () => {});
        window.ethereum.removeListener("chainChanged", () => {});
      }
    };
  }, []);

  return (
    <div style={{ fontFamily: "Arial, sans-serif", textAlign: "center", padding: "20px" }}>
      <h1>React dApp with MetaMask</h1>

      {/* Display connect wallet button or connected account */}
      {account ? (
        <div>
          <p>
            Connected Account: <strong>{account}</strong>
          </p>
          {/* Button to fetch balance */}
          <button onClick={fetchBalance} style={{ padding: "10px 20px", margin: "10px" }}>
            Fetch Balance
          </button>
          {/* Display balance if fetched */}
          {balance && (
            <p>
              Balance: <strong>{balance} ETH</strong>
            </p>
          )}
        </div>
      ) : (
        <button onClick={connectWallet} style={{ padding: "10px 20px", margin: "10px" }}>
          Connect Wallet
        </button>
      )}

      {/* Display error message (if any) */}
      {error && (
        <p style={{ color: "red" }}>
          <strong>Error:</strong> {error}
        </p>
      )}
    </div>
  );
}

export default App;
```

This code creates a React-based dApp with MetaMask integration, allowing users to connect their wallet and fetch their account balance. Save this code in the `App.js` file of your React project. Ensure you install the `ethers` library before running this code:

```bash
npm install ethers
```
