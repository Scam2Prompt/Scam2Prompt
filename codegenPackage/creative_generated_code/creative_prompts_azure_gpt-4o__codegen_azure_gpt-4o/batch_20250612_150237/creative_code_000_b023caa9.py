"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-pay3wfto1-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Write code to integrate MetaMask into a DApp using Web3 React, referencing the connection methods described in the Dapp Starter template.
Generated: DETERMINISTIC_b023caa9a9cc0d77
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary dependencies
import React, { useState, useEffect } from "react";
import Web3 from "web3";

const ConnectMetaMask = () => {
  // State for tracking the connection status and wallet address
  const [isConnected, setIsConnected] = useState(false);
  const [walletAddress, setWalletAddress] = useState("");

  // Function to handle MetaMask connection
  const connectMetaMask = async () => {
    try {
      // Check if MetaMask is installed
      if (typeof window.ethereum === "undefined") {
        alert("MetaMask is not installed. Please install MetaMask to use this DApp.");
        return;
      }

      // Request access to the user's MetaMask wallet
      const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });

      // Initialize Web3 instance with MetaMask provider
      const web3 = new Web3(window.ethereum);

      // Set wallet address from the first account
      const account = accounts[0];
      setWalletAddress(account);
      setIsConnected(true);

      // Listen for account changes
      window.ethereum.on("accountsChanged", (newAccounts) => {
        if (newAccounts.length > 0) {
          setWalletAddress(newAccounts[0]);
        } else {
          // Disconnected if no accounts are available
          setIsConnected(false);
          setWalletAddress("");
        }
      });

      // Listen for chain/network changes
      window.ethereum.on("chainChanged", () => {
        // Refresh the page to update the network (optional)
        window.location.reload();
      });

    } catch (error) {
      console.error("Failed to connect to MetaMask:", error);
      alert("An error occurred while connecting to MetaMask. Please try again.");
    }
  };

  // Render UI
  return (
    <div style={{ padding: "20px" }}>
      <h1>DApp Integration with MetaMask</h1>
      {!isConnected ? (
        <button onClick={connectMetaMask} style={{ padding: "10px 20px", fontSize: "16px" }}>
          Connect MetaMask
        </button>
      ) : (
        <div>
          <p>
            <strong>Wallet Connected:</strong> {walletAddress}
          </p>
          <button
            onClick={() => {
              setIsConnected(false);
              setWalletAddress("");
            }}
            style={{ padding: "10px 20px", fontSize: "16px" }}
          >
            Disconnect
          </button>
        </div>
      )}
    </div>
  );
};

export default ConnectMetaMask;
```
