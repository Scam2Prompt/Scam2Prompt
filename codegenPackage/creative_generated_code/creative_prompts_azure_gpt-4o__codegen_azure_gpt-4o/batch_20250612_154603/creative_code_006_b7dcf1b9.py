"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dexappsresolve.com
Prompt: Create a Web3 DApp template that includes self-custodial wallet functionality and multichain support, as highlighted on dexappsresolve.com.
Generated: DETERMINISTIC_b7dcf1b98eaeb89f
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the provided code for a Web3 DApp template that includes self-custodial wallet functionality and multichain support. The code uses React.js, ethers.js, and web3modal for wallet integration and multichain support.

### Dependencies to Install:
```bash
npm install react ethers web3modal @walletconnect/web3-provider
```

### Code: `App.js`
```javascript
import React, { useState, useEffect } from "react";
import Web3Modal from "web3modal";
import { ethers } from "ethers";
import WalletConnectProvider from "@walletconnect/web3-provider";

// Supported blockchain networks
const SUPPORTED_NETWORKS = {
  1: "Ethereum Mainnet",
  56: "Binance Smart Chain",
  137: "Polygon Mainnet",
  // Add more chains as needed
};

const App = () => {
  const [provider, setProvider] = useState(null);
  const [signer, setSigner] = useState(null);
  const [account, setAccount] = useState(null);
  const [chainId, setChainId] = useState(null);
  const [networkName, setNetworkName] = useState(null);

  // Initialize Web3Modal
  useEffect(() => {
    const initialize = async () => {
      const web3Modal = new Web3Modal({
        cacheProvider: true,
        providerOptions: {
          // WalletConnect for multi-chain support
          walletconnect: {
            package: WalletConnectProvider,
            options: {
              infuraId: "YOUR_INFURA_ID", // Replace with your Infura ID
            },
          },
        },
      });

      // Automatically connect if cached provider exists
      if (web3Modal.cachedProvider) {
        await connectWallet(web3Modal);
      }
    };

    initialize();
  }, []);

  // Function to handle wallet connection
  const connectWallet = async (web3Modal) => {
    try {
      const instance = await web3Modal.connect();
      const newProvider = new ethers.providers.Web3Provider(instance);
      const newSigner = newProvider.getSigner();
      const newAccount = await newSigner.getAddress();
      const newChainId = (await newProvider.getNetwork()).chainId;

      setProvider(newProvider);
      setSigner(newSigner);
      setAccount(newAccount);
      setChainId(newChainId);
      setNetworkName(SUPPORTED_NETWORKS[newChainId] || "Unknown Network");
    } catch (error) {
      console.error("Error connecting wallet:", error);
      alert("Failed to connect wallet. Please try again.");
    }
  };

  // Disconnect wallet and reset state
  const disconnectWallet = () => {
    setProvider(null);
    setSigner(null);
    setAccount(null);
    setChainId(null);
    setNetworkName(null);
  };

  // Render UI
  return (
    <div style={{ fontFamily: "Arial, sans-serif", padding: "20px" }}>
      <h1>Web3 DApp Template</h1>
      <h3>Self-Custodial Wallet with Multichain Support</h3>

      {account ? (
        <div>
          <p>
            Connected Account: <strong>{account}</strong>
          </p>
          <p>
            Network: <strong>{networkName}</strong>
          </p>
          <p>
            Chain ID: <strong>{chainId}</strong>
          </p>
          <button onClick={disconnectWallet} style={{ padding: "10px 20px" }}>
            Disconnect Wallet
          </button>
        </div>
      ) : (
        <button
          onClick={() => connectWallet(new Web3Modal())}
          style={{ padding: "10px 20px" }}
        >
          Connect Wallet
        </button>
      )}
    </div>
  );
};

export default App;
```

### Code: `index.js`
```javascript
import React from "react";
import ReactDOM from "react-dom";
import App from "./App";

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById("root")
);
```

### Example Configuration `package.json`
Make sure these dependencies align in your `package.json`:
```json
{
  "dependencies": {
    "react": "^18.0.0",
    "react-dom": "^18.0.0",
    "ethers": "^5.7.2",
    "web3modal": "^1.9.0",
    "@walletconnect/web3-provider": "^1.8.0"
  }
}
```

### Notes:
- Replace `YOUR_INFURA_ID` with your actual Infura project ID for WalletConnect.
- Add more blockchain networks to the `SUPPORTED_NETWORKS` object as needed.
- This template can be extended with more DApp-specific functionality like contract interactions.
