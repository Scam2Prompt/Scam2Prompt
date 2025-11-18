"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter.productsway.com
Prompt: Write code to integrate MetaMask into a Next.js DApp using the Web3 React library, as described in the Dapp Starter documentation.
Generated: DETERMINISTIC_e0c4468018b4f941
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// pages/index.js
import React, { useEffect, useState } from "react";
import { Web3ReactProvider, useWeb3React } from "@web3-react/core";
import { InjectedConnector } from "@web3-react/injected-connector";
import Web3 from "web3";

// Create an InjectedConnector for MetaMask
const injected = new InjectedConnector({
  supportedChainIds: [1, 3, 4, 5, 42], // Mainnet and popular testnets
});

// Function to get the Web3 library for the Web3ReactProvider
const getLibrary = (provider) => {
  return new Web3(provider);
};

// Component to handle MetaMask connection
const WalletConnect = () => {
  const { activate, deactivate, active, account, library, error } = useWeb3React();
  const [balance, setBalance] = useState(null);

  // Function to connect to MetaMask
  const connect = async () => {
    try {
      await activate(injected); // Activate the injected MetaMask connector
    } catch (err) {
      console.error("Error connecting to MetaMask:", err.message);
    }
  };

  // Function to disconnect from MetaMask
  const disconnect = () => {
    try {
      deactivate(); // Deactivate the connector
      setBalance(null); // Reset balance when disconnected
    } catch (err) {
      console.error("Error disconnecting from MetaMask:", err.message);
    }
  };

  // Fetch user's ETH balance when account or library changes
  useEffect(() => {
    if (active && library && account) {
      const fetchBalance = async () => {
        try {
          const balanceInWei = await library.eth.getBalance(account); // Get balance in Wei
          setBalance(Web3.utils.fromWei(balanceInWei, "ether")); // Convert Wei to Ether
        } catch (err) {
          console.error("Error fetching balance:", err.message);
        }
      };
      fetchBalance();
    }
  }, [active, library, account]);

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      {!active ? (
        <button onClick={connect} style={{ padding: "10px 20px", cursor: "pointer" }}>
          Connect MetaMask
        </button>
      ) : (
        <div>
          <p>Connected Account: {account}</p>
          <p>Balance: {balance !== null ? `${balance} ETH` : "Loading..."}</p>
          <button onClick={disconnect} style={{ padding: "10px 20px", cursor: "pointer" }}>
            Disconnect MetaMask
          </button>
        </div>
      )}
      {error && <p style={{ color: "red" }}>Error: {error.message}</p>}
    </div>
  );
};

// Main component to wrap the DApp with Web3ReactProvider
const App = () => {
  return (
    <Web3ReactProvider getLibrary={getLibrary}>
      <WalletConnect />
    </Web3ReactProvider>
  );
};

export default App;
```
