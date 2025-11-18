"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wormhole.vercel.app
Prompt: Create a responsive user interface for a DApp using daisyUI that allows users to connect their wallets via MetaMask or WalletConnect.
Generated: DETERMINISTIC_46d1c6131fb2bcf3
Batch ID: 20250612_153647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the requested code, written in JavaScript using React.js for the front-end and DaisyUI for styling. It includes wallet connection functionality via MetaMask and WalletConnect.

```javascript
// Package dependencies:
// Ensure you have installed the following packages:
// - react
// - react-dom
// - daisyui
// - ethers
// - @walletconnect/web3-provider

import React, { useState, useEffect } from "react";
import { ethers } from "ethers";
import Web3Modal from "web3modal";
import WalletConnectProvider from "@walletconnect/web3-provider";
import "./App.css"; // Include DaisyUI styles via Tailwind CSS

const App = () => {
  const [walletAddress, setWalletAddress] = useState("");
  const [provider, setProvider] = useState(null);

  // Initialize Web3Modal with providers
  const web3Modal = new Web3Modal({
    cacheProvider: true, // Cache user wallet for faster reconnection
    providerOptions: {
      walletconnect: {
        package: WalletConnectProvider,
        options: {
          infuraId: "YOUR_INFURA_PROJECT_ID", // Replace with your Infura ID
        },
      },
    },
  });

  // Connect wallet function
  const connectWallet = async () => {
    try {
      const instance = await web3Modal.connect();
      const web3Provider = new ethers.providers.Web3Provider(instance);

      const signer = web3Provider.getSigner();
      const address = await signer.getAddress();

      setProvider(web3Provider);
      setWalletAddress(address);
    } catch (error) {
      console.error("Connection error:", error);
      alert("Failed to connect wallet. Please try again.");
    }
  };

  // Disconnect wallet function
  const disconnectWallet = () => {
    setWalletAddress("");
    setProvider(null);
    web3Modal.clearCachedProvider();
  };

  useEffect(() => {
    if (web3Modal.cachedProvider) {
      connectWallet();
    }
  }, []); // Automatically reconnect if provider is cached

  return (
    <div className="min-h-screen bg-base-100 flex flex-col items-center justify-center">
      <div className="card w-96 bg-neutral text-neutral-content shadow-lg">
        <div className="card-body">
          <h2 className="card-title text-center">DApp Wallet Connection</h2>

          {walletAddress ? (
            <>
              <p className="text-sm">
                Connected Wallet:
                <span className="font-bold block break-words">
                  {walletAddress}
                </span>
              </p>
              <button
                onClick={disconnectWallet}
                className="btn btn-error mt-4"
              >
                Disconnect Wallet
              </button>
            </>
          ) : (
            <button onClick={connectWallet} className="btn btn-primary">
              Connect Wallet
            </button>
          )}
        </div>
      </div>
    </div>
  );
};

export default App;
```

### Additional Notes:
1. Replace `"YOUR_INFURA_PROJECT_ID"` with your actual Infura project ID.
2. Ensure Tailwind CSS and DaisyUI are properly set up in your project for styling.
3. Create a file named `App.css` if you want to extend DaisyUI/Tailwind styling or include global styles.
