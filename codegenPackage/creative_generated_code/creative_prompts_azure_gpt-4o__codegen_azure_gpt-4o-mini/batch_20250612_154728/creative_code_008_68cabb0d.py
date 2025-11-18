"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://manualresolve-dev.web.app
Prompt: Develop a Web3 application that leverages WalletConnect to allow users to interact with multiple DeFi projects globally, ensuring ease of use and secure connections.
Generated: DETERMINISTIC_68cabb0d0424a2d8
Batch ID: 20250612_154728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and packages
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';
import { WalletConnectProvider } from "@walletconnect/web3-provider";
import { ethers } from "ethers";

// Define the main App component
const App = () => {
  const [provider, setProvider] = useState(null);
  const [web3, setWeb3] = useState(null);
  const [accounts, setAccounts] = useState([]);
  const [isConnected, setIsConnected] = useState(false);

  // Initialize WalletConnect provider
  const connectWallet = async () => {
    try {
      // Create a WalletConnect Provider
      const walletConnectProvider = new WalletConnectProvider({
        infuraId: "YOUR_INFURA_ID", // Replace with your Infura ID
      });

      // Enable session (triggers QR Code modal)
      await walletConnectProvider.enable();
      
      // Create a Web3 instance
      const web3Instance = new Web3(walletConnectProvider);
      const accounts = await web3Instance.eth.getAccounts();

      // Set state variables
      setProvider(walletConnectProvider);
      setWeb3(web3Instance);
      setAccounts(accounts);
      setIsConnected(true);
    } catch (error) {
      console.error("Error connecting wallet:", error);
      alert("Failed to connect wallet. Please try again.");
    }
  };

  // Disconnect from the wallet
  const disconnectWallet = async () => {
    if (provider) {
      await provider.disconnect();
      setProvider(null);
      setWeb3(null);
      setAccounts([]);
      setIsConnected(false);
    }
  };

  // Handle component unmount
  useEffect(() => {
    return () => {
      if (provider) {
        provider.disconnect();
      }
    };
  }, [provider]);

  return (
    <div style={{ textAlign: 'center', margin: '50px' }}>
      <h1>Web3 DeFi Application</h1>
      {isConnected ? (
        <div>
          <h2>Connected Account: {accounts[0]}</h2>
          <button onClick={disconnectWallet}>Disconnect Wallet</button>
        </div>
      ) : (
        <button onClick={connectWallet}>Connect Wallet</button>
      )}
    </div>
  );
};

// Export the App component as default
export default App;

// Note: Ensure to add the necessary dependencies in your project:
// npm install web3 @walletconnect/web3-provider ethers react
```
