"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-1s2gz5hbg-dunghd.vercel.app
Prompt: Generate a Next.js page for a blockchain-based application that uses daisyUI for styling and integrates WalletConnect and MetaMask, as outlined in the Dapp Starter documentation.
Generated: DETERMINISTIC_dd0d58882668f5c3
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// pages/index.js

import { useState, useEffect } from "react";
import Web3 from "web3";
import WalletConnectProvider from "@walletconnect/web3-provider";
import { ethers } from "ethers";
import "daisyui/dist/full.css"; // Import DaisyUI styles

export default function Home() {
  // State for managing wallet connection
  const [walletAddress, setWalletAddress] = useState(null);
  const [errorMessage, setErrorMessage] = useState(null);

  // Function to connect with MetaMask
  const connectMetaMask = async () => {
    try {
      // Check if MetaMask is installed
      if (!window.ethereum) {
        throw new Error("MetaMask is not installed. Please install it to use this feature.");
      }

      // Request accounts
      const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });
      setWalletAddress(accounts[0]);
    } catch (error) {
      setErrorMessage(error.message);
    }
  };

  // Function to connect using WalletConnect
  const connectWalletConnect = async () => {
    try {
      // Create WalletConnect provider
      const provider = new WalletConnectProvider({
        infuraId: "your-infura-id", // Replace with your Infura project ID
      });

      // Enable the provider
      await provider.enable();

      // Create Web3 instance
      const web3 = new Web3(provider);

      // Get accounts
      const accounts = await web3.eth.getAccounts();
      setWalletAddress(accounts[0]);

      // Handle provider disconnection
      provider.on("disconnect", () => {
        setWalletAddress(null);
        setErrorMessage(null);
      });
    } catch (error) {
      setErrorMessage(error.message);
    }
  };

  // Function to disconnect the wallet
  const disconnectWallet = () => {
    setWalletAddress(null);
    setErrorMessage(null);
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-base-200">
      <h1 className="text-4xl font-bold mb-4">Blockchain Dapp</h1>
      <div className="card bg-base-100 shadow-xl p-6 w-96">
        <div className="card-body">
          {walletAddress ? (
            <>
              <p className="text-lg font-semibold">Connected Wallet:</p>
              <p className="text-sm text-gray-500">{walletAddress}</p>
              <button className="btn btn-error mt-4" onClick={disconnectWallet}>
                Disconnect
              </button>
            </>
          ) : (
            <>
              <button className="btn btn-primary mb-2" onClick={connectMetaMask}>
                Connect MetaMask
              </button>
              <button className="btn btn-secondary" onClick={connectWalletConnect}>
                Connect WalletConnect
              </button>
            </>
          )}
          {errorMessage && (
            <div className="alert alert-error mt-4">
              <div>
                <span>{errorMessage}</span>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
```

**Notes:**
- Replace `"your-infura-id"` with your actual Infura project ID for WalletConnect.
- Make sure the `daisyui` package is installed (`npm install daisyui`) and configured in your project.
- Error messages are displayed to the user using DaisyUI's `alert-error` styling.
