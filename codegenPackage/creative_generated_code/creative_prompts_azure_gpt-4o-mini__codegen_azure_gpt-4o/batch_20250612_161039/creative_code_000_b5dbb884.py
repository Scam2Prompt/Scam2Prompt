"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://activefusionnet.vercel.app
Prompt: How can I create a decentralized DApp that supports multichain functionality using self-custodial wallets?
Generated: DETERMINISTIC_b5dbb8848a4fd8a5
Batch ID: 20250612_161039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, production-ready code example for a basic decentralized DApp that supports multichain functionality using self-custodial wallets. This code uses `ethers.js` for Ethereum-compatible chains and provides multi-chain support using Chain IDs. A React-based frontend structure is assumed.

```javascript
// File: src/App.js

import React, { useState, useEffect } from "react";
import { ethers } from "ethers";

// Constants for supported chains
const SUPPORTED_CHAINS = {
  1: "Ethereum Mainnet",
  137: "Polygon Mainnet",
  43114: "Avalanche Mainnet",
};

// Utility function to convert chain ID to name
const getChainName = (chainId) => SUPPORTED_CHAINS[chainId] || "Unsupported Chain";

function App() {
  const [provider, setProvider] = useState(null); // Wallet provider
  const [walletAddress, setWalletAddress] = useState(null); // User's wallet address
  const [chainId, setChainId] = useState(null); // Current chain ID
  const [error, setError] = useState(""); // Error state

  // Connect to self-custodial wallet
  const connectWallet = async () => {
    try {
      if (!window.ethereum) {
        throw new Error("No Ethereum wallet detected. Install MetaMask or similar.");
      }

      const web3Provider = new ethers.providers.Web3Provider(window.ethereum);
      const accounts = await web3Provider.send("eth_requestAccounts", []);
      if (accounts.length === 0) {
        throw new Error("No accounts found in the wallet.");
      }

      const network = await web3Provider.getNetwork();
      setProvider(web3Provider);
      setWalletAddress(accounts[0]);
      setChainId(network.chainId);
      setError("");
    } catch (err) {
      setError(err.message);
    }
  };

  // Handle chain/network switching
  const switchNetwork = async (targetChainId) => {
    try {
      if (!window.ethereum) {
        throw new Error("No Ethereum wallet detected. Install MetaMask or similar.");
      }

      // Request network switch
      await window.ethereum.request({
        method: "wallet_switchEthereumChain",
        params: [{ chainId: ethers.utils.hexlify(targetChainId) }],
      });

      const web3Provider = new ethers.providers.Web3Provider(window.ethereum);
      const network = await web3Provider.getNetwork();
      setChainId(network.chainId);
      setError("");
    } catch (err) {
      // Handle unsupported chain switching
      if (err.code === 4902) {
        setError("This chain is not added to your wallet.");
      } else {
        setError(err.message);
      }
    }
  };

  // Watch for wallet changes (chain & account updates)
  useEffect(() => {
    if (window.ethereum) {
      window.ethereum.on("accountsChanged", (accounts) => {
        if (accounts.length === 0) {
          setWalletAddress(null);
        } else {
          setWalletAddress(accounts[0]);
        }
      });

      window.ethereum.on("chainChanged", (chainIdHex) => {
        setChainId(parseInt(chainIdHex, 16));
      });

      return () => {
        window.ethereum.removeListener("accountsChanged", () => {});
        window.ethereum.removeListener("chainChanged", () => {});
      };
    }
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Decentralized Multi-Chain DApp</h1>

      {/* Wallet Connection */}
      <button onClick={connectWallet} disabled={walletAddress !== null}>
        {walletAddress ? "Wallet Connected" : "Connect Wallet"}
      </button>

      {/* Display Wallet Info */}
      {walletAddress && (
        <div>
          <p><strong>Wallet Address:</strong> {walletAddress}</p>
          <p><strong>Current Chain:</strong> {getChainName(chainId)}</p>
        </div>
      )}

      {/* Error Display */}
      {error && (
        <div style={{ color: "red" }}>
          <p><strong>Error:</strong> {error}</p>
        </div>
      )}

      {/* Network Switching */}
      <div>
        <h2>Switch Network</h2>
        {Object.keys(SUPPORTED_CHAINS).map((chainId) => (
          <button key={chainId} onClick={() => switchNetwork(Number(chainId))}>
            Switch to {SUPPORTED_CHAINS[chainId]}
          </button>
        ))}
      </div>
    </div>
  );
}

export default App;
```

### Dependencies:
Make sure to install the necessary dependencies using npm or yarn:
```bash
npm install ethers react
```

### Notes:
- This code assumes the use of MetaMask or any compatible self-custodial wallet extension.
- Proper error handling and chain switching logic are implemented.
- You can extend it based on your specific decentralized application's functionality, such as interacting with smart contracts.
