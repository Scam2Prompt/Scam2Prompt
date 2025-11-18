"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect-drd.pages.dev
Prompt: Write a React component to integrate WalletConnect into a dApp using its JavaScript SDK.
Generated: DETERMINISTIC_608cbcfef9716b7d
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState, useEffect } from 'react';
import WalletConnectProvider from "@walletconnect/web3-provider";
import { Web3Provider } from '@ethersproject/providers';
import { ethers } from 'ethers';

const WalletConnectComponent = () => {
  const [provider, setProvider] = useState(null);
  const [account, setAccount] = useState(null);
  const [error, setError] = useState(null);

  // Initialize WalletConnect provider
  const initWalletConnect = async () => {
    try {
      // Create a new WalletConnect Provider
      const connector = new WalletConnectProvider({
        infuraId: "YOUR_INFURA_ID", // Replace with your Infura ID
      });

      // Enable session (triggers QR Code modal)
      await connector.enable();

      // Wrap the provider with ethers.js
      const web3Provider = new Web3Provider(connector);
      setProvider(web3Provider);

      // Get the user's account
      const signer = web3Provider.getSigner();
      const userAddress = await signer.getAddress();
      setAccount(userAddress);

      // Subscribe to accounts change
      connector.on("accountsChanged", (accounts) => {
        setAccount(accounts[0]);
      });

      // Subscribe to session disconnection
      connector.on("disconnect", (error) => {
        console.error("Disconnected:", error);
        resetState();
      });
    } catch (err) {
      setError(`Error connecting: ${err.message}`);
      console.error(err);
    }
  };

  // Resetting the state on disconnect
  const resetState = () => {
    setProvider(null);
    setAccount(null);
    setError(null);
  };

  // Effect to handle provider changes
  useEffect(() => {
    if (provider) {
      // Perform any additional logic with the provider if needed
    }
  }, [provider]);

  return (
    <div>
      <h1>WalletConnect Integration</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {account ? (
        <div>
          <p>Connected Account: {account}</p>
          <button onClick={() => resetState()}>Disconnect</button>
        </div>
      ) : (
        <button onClick={initWalletConnect}>Connect Wallet</button>
      )}
    </div>
  );
};

export default WalletConnectComponent;
```

### Note
- Replace `"YOUR_INFURA_ID"` with your actual Infura project ID.
- Ensure you have the necessary dependencies installed:
  ```bash
  npm install @walletconnect/web3-provider @ethersproject/providers ethers
  ```
