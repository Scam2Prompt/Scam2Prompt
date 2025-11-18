"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallet-connect16.web.app
Prompt: Provide an example of integrating WalletConnect with a React-based wallet form, ensuring proper handling of user authentication and connection.
Generated: DETERMINISTIC_b2e7716267ede5b6
Batch ID: 20250612_154646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useEffect, useState } from 'react';
import WalletConnectProvider from "@walletconnect/web3-provider";
import { ethers } from 'ethers';

// Component for WalletConnect integration
const WalletConnectForm = () => {
  // State variables to manage wallet connection and account
  const [provider, setProvider] = useState(null);
  const [account, setAccount] = useState(null);
  const [isConnected, setIsConnected] = useState(false);

  // Function to create a WalletConnect provider
  const createProvider = async () => {
    try {
      // Create a new WalletConnect provider
      const connector = new WalletConnectProvider({
        infuraId: "YOUR_INFURA_PROJECT_ID", // Replace with your Infura Project ID
      });

      // Enable session (triggers QR Code modal)
      await connector.enable();
      setProvider(connector);
      
      // Create ethers provider from the WalletConnect provider
      const ethersProvider = new ethers.providers.Web3Provider(connector);
      const signer = ethersProvider.getSigner();
      const userAccount = await signer.getAddress();

      // Update state with account and connection status
      setAccount(userAccount);
      setIsConnected(true);
    } catch (error) {
      console.error("Error connecting to WalletConnect:", error);
      alert("Failed to connect to wallet. Please try again.");
    }
  };

  // Handle disconnecting the wallet
  const disconnectWallet = async () => {
    if (provider) {
      await provider.disconnect();
      setAccount(null);
      setIsConnected(false);
      setProvider(null);
    }
  };

  // Effect to handle provider events
  useEffect(() => {
    if (provider) {
      // Subscribe to session updates
      provider.on("accountsChanged", (accounts) => {
        setAccount(accounts[0]);
      });

      provider.on("chainChanged", (chainId) => {
        console.log("Chain changed to:", chainId);
      });

      provider.on("disconnect", (error) => {
        console.log("Disconnected:", error);
        disconnectWallet();
      });
    }

    // Clean up event listeners on unmount
    return () => {
      if (provider) {
        provider.off("accountsChanged");
        provider.off("chainChanged");
        provider.off("disconnect");
      }
    };
  }, [provider]);

  return (
    <div>
      <h1>WalletConnect Integration</h1>
      {!isConnected ? (
        <button onClick={createProvider}>Connect Wallet</button>
      ) : (
        <div>
          <p>Connected Account: {account}</p>
          <button onClick={disconnectWallet}>Disconnect Wallet</button>
        </div>
      )}
    </div>
  );
};

export default WalletConnectForm;
```

### Notes:
- Replace `YOUR_INFURA_PROJECT_ID` with your actual Infura Project ID to connect properly.
- Ensure you have the necessary dependencies installed: `npm install @walletconnect/web3-provider ethers`.
