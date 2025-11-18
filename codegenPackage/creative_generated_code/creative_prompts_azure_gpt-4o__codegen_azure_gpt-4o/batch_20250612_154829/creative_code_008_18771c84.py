"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-sdk-examples-relink.vercel.app
Prompt: Write code to display wallet connection status in a Next.js app using the MetaMask SDK, as demonstrated in the quickstart example on the webpage.
Generated: DETERMINISTIC_18771c846f42d363
Batch ID: 20250612_154829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// pages/index.js

import { useEffect, useState } from "react";
import detectEthereumProvider from "@metamask/detect-provider";

export default function Home() {
  const [walletConnected, setWalletConnected] = useState(false);
  const [walletAddress, setWalletAddress] = useState("");

  // Function to handle wallet connection
  const connectWallet = async () => {
    try {
      const provider = await detectEthereumProvider();

      if (!provider) {
        console.error("MetaMask is not installed");
        alert("Please install MetaMask to connect your wallet!");
        return;
      }

      // Request account access
      const accounts = await provider.request({ method: "eth_requestAccounts" });
      if (accounts.length > 0) {
        setWalletConnected(true);
        setWalletAddress(accounts[0]);
      }
    } catch (error) {
      console.error("Error connecting to MetaMask:", error);
      alert("Failed to connect to MetaMask. Please try again.");
    }
  };

  // Function to check wallet connection status
  const checkWalletConnection = async () => {
    try {
      const provider = await detectEthereumProvider();

      if (!provider) {
        console.error("MetaMask is not installed");
        return;
      }

      const accounts = await provider.request({ method: "eth_accounts" });
      if (accounts.length > 0) {
        setWalletConnected(true);
        setWalletAddress(accounts[0]);
      } else {
        setWalletConnected(false);
        setWalletAddress("");
      }
    } catch (error) {
      console.error("Error checking wallet connection:", error);
    }
  };

  // Run on component mount to check connection status
  useEffect(() => {
    checkWalletConnection();

    // Listen for account changes
    const handleAccountsChanged = (accounts) => {
      if (accounts.length > 0) {
        setWalletConnected(true);
        setWalletAddress(accounts[0]);
      } else {
        setWalletConnected(false);
        setWalletAddress("");
      }
    };

    detectEthereumProvider().then((provider) => {
      if (provider) {
        provider.on("accountsChanged", handleAccountsChanged);
      }
    });

    // Cleanup event listener on component unmount
    return () => {
      detectEthereumProvider().then((provider) => {
        if (provider) {
          provider.removeListener("accountsChanged", handleAccountsChanged);
        }
      });
    };
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>MetaMask Wallet Connection Status</h1>
      {walletConnected ? (
        <div>
          <p style={{ color: "green" }}>Wallet Connected</p>
          <p>Address: {walletAddress}</p>
        </div>
      ) : (
        <p style={{ color: "red" }}>Wallet Not Connected</p>
      )}
      <button
        onClick={connectWallet}
        style={{
          padding: "10px 20px",
          backgroundColor: "#f6851b",
          color: "#fff",
          border: "none",
          borderRadius: "5px",
          cursor: "pointer",
        }}
      >
        Connect Wallet
      </button>
    </div>
  );
}

// Notes:
// - Make sure to install the MetaMask SDK dependency with:
//   `npm install @metamask/detect-provider`
// - This code follows Next.js best practices and includes error handling.
// - Ensure that MetaMask is installed in the browser for testing.
```
