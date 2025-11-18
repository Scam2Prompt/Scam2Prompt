"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter.productsway.com
Prompt: Write code to display a user's account balance and chain ID in a DApp using Web3 React and MetaMask, referencing the Dapp Starter framework.
Generated: DETERMINISTIC_8d26c7c906ba6f65
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary dependencies
import React, { useEffect, useState } from "react";
import { ethers } from "ethers";
import { useWeb3React } from "@web3-react/core";
import { injected } from "./connectors"; // Assumes a DApp Starter-like project structure

// Component to display account balance and chain ID
const AccountInfo = () => {
  const { activate, active, account, library, chainId } = useWeb3React(); // Web3React hooks
  const [balance, setBalance] = useState(null);

  // Function to connect wallet (MetaMask)
  const connectWallet = async () => {
    try {
      await activate(injected); // Activate the injected connector (MetaMask)
    } catch (error) {
      console.error("Error connecting wallet:", error);
    }
  };

  // Fetch the user's balance when account or library changes
  useEffect(() => {
    const fetchBalance = async () => {
      if (active && account && library) {
        try {
          const bal = await library.getBalance(account); // Get the balance from the blockchain
          setBalance(ethers.utils.formatEther(bal)); // Convert balance from Wei to Ether
        } catch (error) {
          console.error("Error fetching balance:", error);
        }
      }
    };

    fetchBalance();
  }, [active, account, library]);

  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
      {/* If wallet is not connected, show the connect button */}
      {!active ? (
        <button
          onClick={connectWallet}
          style={{
            padding: "10px 20px",
            backgroundColor: "#4CAF50",
            color: "white",
            border: "none",
            borderRadius: "5px",
            cursor: "pointer",
          }}
        >
          Connect Wallet
        </button>
      ) : (
        // If wallet is connected, show account information
        <div>
          <h3>Account Information</h3>
          <p>
            <strong>Account:</strong> {account}
          </p>
          <p>
            <strong>Balance:</strong> {balance ? `${balance} ETH` : "Loading..."}
          </p>
          <p>
            <strong>Chain ID:</strong> {chainId}
          </p>
        </div>
      )}
    </div>
  );
};

export default AccountInfo;
```

This code assumes you have already set up the Web3 React environment and configured the `injected` connector to support MetaMask. The component connects to MetaMask, retrieves the user's account balance and chain ID, and displays them.
