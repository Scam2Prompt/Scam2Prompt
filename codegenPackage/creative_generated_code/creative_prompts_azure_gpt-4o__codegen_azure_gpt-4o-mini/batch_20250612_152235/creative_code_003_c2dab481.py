"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://siduspad.xyz
Prompt: Provide an example of how to integrate a wallet connection feature into a decentralized application (dApp) for staking pools, similar to the SidusPad platform.
Generated: DETERMINISTIC_c2dab4818ec143ff
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary dependencies
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';
import WalletConnectProvider from '@walletconnect/web3-provider';
import { InjectedConnector } from '@web3-react/injected-connector';
import { useWeb3React } from '@web3-react/core';

// Constants
const INFURA_ID = 'YOUR_INFURA_PROJECT_ID'; // Replace with your Infura project ID

// Create a wallet connection component
const WalletConnect = () => {
  const { activate, active, account, library } = useWeb3React();
  const [error, setError] = useState(null);

  // Function to handle wallet connection
  const connectWallet = async () => {
    try {
      // Create a WalletConnect Provider
      const provider = new WalletConnectProvider({
        infuraId: INFURA_ID, // Required
      });

      // Enable session (triggers QR Code modal)
      await provider.enable();

      // Create a Web3 instance
      const web3 = new Web3(provider);

      // Activate the connection
      await activate(web3);

      // Listen for account and chain changes
      provider.on("accountsChanged", (accounts) => {
        console.log("Accounts changed:", accounts);
      });

      provider.on("chainChanged", (chainId) => {
        console.log("Chain changed:", chainId);
      });

      provider.on("disconnect", (error) => {
        console.log("Disconnected:", error);
        setError(error);
      });

    } catch (err) {
      console.error("Failed to connect wallet:", err);
      setError(err.message);
    }
  };

  // Effect to check for active connection on component load
  useEffect(() => {
    const checkConnection = async () => {
      if (window.ethereum) {
        try {
          await activate(new InjectedConnector());
        } catch (err) {
          console.error("Error activating injected connector:", err);
        }
      }
    };
    
    checkConnection();
  }, [activate]);

  return (
    <div>
      <h2>Connect Your Wallet</h2>
      {active ? (
        <div>
          <p>Connected account: {account}</p>
          <button onClick={() => library.eth.getBalance(account)}>Check Balance</button>
        </div>
      ) : (
        <button onClick={connectWallet}>Connect Wallet</button>
      )}
      {error && <p style={{ color: 'red' }}>Error: {error}</p>}
    </div>
  );
};

export default WalletConnect;
```
