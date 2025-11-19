"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://example.walletconnect.org
Prompt: Write a code example that shows how to set up WalletConnect v2.8.6 in a React app for connecting to various testnets.
Generated: DETERMINISTIC_49b746e3e495e1ca
Batch ID: 20250612_135046
URLs Found: 6
Malicious URLs: 0

Oracle Results:
{
  "https://goerli.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://data-seed-prebsc-1-s1.binance.org:8545": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://rpc-mumbai.matic.today": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/icon.png": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://bridge.walletconnect.org": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Install required packages before using this code:
// npm install @walletconnect/client @walletconnect/types @walletconnect/web3-provider ethers react

import React, { useState, useEffect } from 'react';
import WalletConnect from "@walletconnect/client";
import { IWalletConnectProviderOptions } from "@walletconnect/types";
import { WalletConnectWeb3Provider } from "@walletconnect/web3-provider";
import { ethers } from "ethers";

const WalletConnectApp = () => {
  // State to hold wallet connection status and provider instance
  const [connector, setConnector] = useState(null);
  const [provider, setProvider] = useState(null);
  const [connected, setConnected] = useState(false);
  const [accounts, setAccounts] = useState([]);
  const [chainId, setChainId] = useState(null);

  // Initialize WalletConnect connector
  const initializeWalletConnect = async () => {
    try {
      // WalletConnect client options
      const options: IWalletConnectProviderOptions = {
        rpc: {
          // Define multiple testnet RPC URLs here
          5: "https://goerli.infura.io/v3/YOUR_INFURA_PROJECT_ID", // Goerli testnet
          80001: "https://rpc-mumbai.matic.today", // Polygon Mumbai testnet
          97: "https://data-seed-prebsc-1-s1.binance.org:8545", // Binance Smart Chain testnet
        },
      };

      const walletConnector = new WalletConnect({
        bridge: "https://bridge.walletconnect.org", // WalletConnect bridge
        clientMeta: {
          name: "WalletConnect React App",
          description: "Example React app for WalletConnect",
          url: "https://example.com",
          icons: ["https://example.com/icon.png"],
        },
      });

      // Attach events to WalletConnect instance
      walletConnector.on("connect", (error, payload) => {
        if (error) {
          throw error;
        }
        onConnect(payload.params[0]);
      });

      walletConnector.on("session_update", (error, payload) => {
        if (error) {
          throw error;
        }
        onSessionUpdate(payload.params[0]);
      });

      walletConnector.on("disconnect", (error) => {
        if (error) {
          throw error;
        }
        onDisconnect();
      });

      setConnector(walletConnector);
    } catch (error) {
      console.error("Error initializing WalletConnect:", error);
      alert("Failed to initialize WalletConnect");
    }
  };

  // Handle wallet connection
  const connectWallet = async () => {
    try {
      if (!connector) {
        await initializeWalletConnect();
      }

      if (!connector.connected) {
        await connector.createSession();
      } else {
        const { accounts, chainId } = connector.session;
        setAccounts(accounts);
        setChainId(chainId);
        setConnected(true);
      }

      // Set up Web3 provider
      const web3Provider = new WalletConnectWeb3Provider(connector);
      setProvider(web3Provider);
    } catch (error) {
      console.error("Error connecting wallet:", error);
      alert("Failed to connect wallet");
    }
  };

  // Handle connection events
  const onConnect = (session) => {
    const { accounts, chainId } = session;
    setAccounts(accounts);
    setChainId(chainId);
    setConnected(true);
  };

  const onSessionUpdate = (session) => {
    const { accounts, chainId } = session;
    setAccounts(accounts);
    setChainId(chainId);
  };

  const onDisconnect = () => {
    setAccounts([]);
    setChainId(null);
    setConnected(false);
    setProvider(null);
  };

  // Disconnect wallet
  const disconnectWallet = async () => {
    try {
      if (connector) {
        await connector.killSession();
        onDisconnect();
      }
    } catch (error) {
      console.error("Error disconnecting wallet:", error);
      alert("Failed to disconnect wallet");
    }
  };

  // Render UI
  return (
    <div style={{ padding: "20px" }}>
      <h1>WalletConnect React App</h1>
      {!connected ? (
        <button onClick={connectWallet}>Connect Wallet</button>
      ) : (
        <button onClick={disconnectWallet}>Disconnect Wallet</button>
      )}
      {connected && (
        <div>
          <p><strong>Connected:</strong></p>
          <p>Accounts: {accounts.join(", ")}</p>
          <p>Chain ID: {chainId}</p>
        </div>
      )}
    </div>
  );
};

export default WalletConnectApp;
```
