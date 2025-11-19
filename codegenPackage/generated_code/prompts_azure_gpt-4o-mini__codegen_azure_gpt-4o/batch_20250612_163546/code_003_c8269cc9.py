"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-1s2gz5hbg-dunghd.vercel.app
Prompt: Can you provide an example of using daisyUI with Web3 React for a DApp, referencing the Dapp Starter site?
Generated: DETERMINISTIC_c8269cc92cbf7c45
Batch ID: 20250612_163546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries and components
import React, { useState, useEffect } from "react";
import { ethers } from "ethers"; // For interacting with Ethereum blockchain
import { useWeb3React } from "@web3-react/core"; // Web3 React for wallet connection
import { InjectedConnector } from "@web3-react/injected-connector"; // Wallet connector
import "daisyui/dist/full.css"; // Import daisyUI styles

// Initialize the injected connector for MetaMask
const injected = new InjectedConnector({
  supportedChainIds: [1, 3, 4, 5, 42], // Mainnet and testnets
});

// Main DApp component
const DApp = () => {
  const { activate, active, account, library, deactivate } = useWeb3React(); // Web3 React hooks
  const [balance, setBalance] = useState(null); // State for storing wallet balance
  const [error, setError] = useState(null); // State for error handling

  // Function to connect wallet
  const connectWallet = async () => {
    try {
      await activate(injected); // Activate the injected connector
      setError(null); // Clear any previous errors
    } catch (err) {
      setError("Failed to connect wallet. Please try again."); // Handle connection errors
    }
  };

  // Function to disconnect wallet
  const disconnectWallet = () => {
    deactivate(); // Deactivate the wallet connection
    setBalance(null); // Clear balance state
    setError(null); // Clear error state
  };

  // Fetch wallet balance when account changes
  useEffect(() => {
    const fetchBalance = async () => {
      if (active && account && library) {
        try {
          const balance = await library.getBalance(account); // Get wallet balance
          setBalance(ethers.utils.formatEther(balance)); // Format balance to Ether
        } catch (err) {
          setError("Failed to fetch balance."); // Handle balance fetch errors
        }
      }
    };
    fetchBalance();
  }, [active, account, library]);

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold text-center mb-4">DApp Starter</h1>
      <div className="card bg-base-100 shadow-xl p-4">
        {/* Wallet connection status */}
        {active ? (
          <div>
            <p className="text-lg">
              Connected Account: <span className="font-mono">{account}</span>
            </p>
            <p className="text-lg">
              Balance: <span className="font-mono">{balance} ETH</span>
            </p>
            <button
              className="btn btn-error mt-4"
              onClick={disconnectWallet}
            >
              Disconnect Wallet
            </button>
          </div>
        ) : (
          <div>
            <p className="text-lg">Wallet not connected.</p>
            <button
              className="btn btn-primary mt-4"
              onClick={connectWallet}
            >
              Connect Wallet
            </button>
          </div>
        )}

        {/* Error message display */}
        {error && (
          <div className="alert alert-error mt-4">
            <span>{error}</span>
          </div>
        )}
      </div>
    </div>
  );
};

export default DApp;
```

### Notes:
- This code assumes you have installed the required dependencies (`react`, `@web3-react/core`, `ethers`, `daisyui`) in your project.
- To run this code, ensure you have a React environment set up and properly configured with Web3 React and daisyUI.
