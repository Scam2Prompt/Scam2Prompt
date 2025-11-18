"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dxldao.org
Prompt: Explain how to implement wallet connection functionality using MetaMask or WalletConnect for a dApp, as seen on dxldao.org.
Generated: DETERMINISTIC_79250372029dfbd0
Batch ID: 20250612_145117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState } from "react";
import Web3 from "web3";
import WalletConnectProvider from "@walletconnect/web3-provider";

// MetaMask and WalletConnect integration for a dApp
const WalletConnection = () => {
  const [account, setAccount] = useState(null); // Stores connected wallet address
  const [connectionError, setConnectionError] = useState(null); // Stores connection errors

  // Function to connect wallet using MetaMask
  async function connectMetaMask() {
    try {
      // Check if MetaMask is available
      if (typeof window.ethereum === "undefined") {
        throw new Error("MetaMask is not installed. Please install it to connect.");
      }

      // Request account access
      const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });

      // Set the connected account
      setAccount(accounts[0]);

      // Initialize Web3 instance
      const web3 = new Web3(window.ethereum);
      console.log("Connected with MetaMask:", accounts[0]);
    } catch (error) {
      // Handle errors and display message
      setConnectionError(error.message);
      console.error("Error connecting MetaMask:", error);
    }
  }

  // Function to connect wallet using WalletConnect
  async function connectWalletConnect() {
    try {
      // Initialize WalletConnect Provider
      const provider = new WalletConnectProvider({
        infuraId: "YOUR_INFURA_PROJECT_ID", // Replace with your Infura project ID
      });

      // Enable provider (triggers QR Code modal for WalletConnect)
      await provider.enable();

      // Initialize Web3 instance with WalletConnect provider
      const web3 = new Web3(provider);

      // Get accounts
      const accounts = await web3.eth.getAccounts();
      setAccount(accounts[0]);

      console.log("Connected with WalletConnect:", accounts[0]);
    } catch (error) {
      // Handle errors and display message
      setConnectionError(error.message);
      console.error("Error connecting WalletConnect:", error);
    }
  }

  return (
    <div>
      {/* Display connected account or error message */}
      {account ? <p>Connected Account: {account}</p> : <p>No Wallet Connected</p>}
      {connectionError && <p className="error">Error: {connectionError}</p>}

      {/* Buttons to initiate wallet connection */}
      <button onClick={connectMetaMask}>Connect MetaMask</button>
      <button onClick={connectWalletConnect}>Connect WalletConnect</button>
    </div>
  );
};

export default WalletConnection;
```

---

### Notes for Implementation:
1. Replace `"YOUR_INFURA_PROJECT_ID"` with your actual Infura project ID when using WalletConnect.
2. Ensure that the `@walletconnect/web3-provider` and `web3` libraries are installed in your project (`npm install @walletconnect/web3-provider web3`).
3. Proper error handling is included to guide users in case of missing wallet extensions or connection issues.
4. This component is production-ready but can be further styled and integrated into larger dApp architectures.
