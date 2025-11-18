"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitlayerorg.pages.dev
Prompt: Provide an example of how to integrate a wallet connection feature into a DApp using Bitlayer's supported wallets and APIs.
Generated: DETERMINISTIC_b8dd5c7823abc4fb
Batch ID: 20250612_151158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries for wallet connection
import React, { useState, useEffect } from 'react';
import { WalletConnectProvider } from "@walletconnect/react";
import { useWalletConnect } from "@walletconnect/react-native-dapp";

// Define the main DApp component
const WalletConnectionDApp = () => {
  // Initialize state to manage connection status
  const connector = useWalletConnect();
  const [connected, setConnected] = useState(false);

  // Effect to handle connection changes
  useEffect(() => {
    if (connector.connected) {
      setConnected(true);
    } else {
      setConnected(false);
    }

    // Subscribe to connection events
    const handleConnect = () => setConnected(true);
    const handleDisconnect = () => setConnected(false);
    
    connector.on("connect", handleConnect);
    connector.on("disconnect", handleDisconnect);
    
    // Cleanup subscription on unmount
    return () => {
      connector.off("connect", handleConnect);
      connector.off("disconnect", handleDisconnect);
    };
  }, [connector]);

  // Function to connect to wallet
  const connectWallet = async () => {
    try {
      // Check if already connected
      if (!connector.connected) {
        await connector.connect();
      }
    } catch (error) {
      console.error("Error connecting to wallet:", error);
      alert("Failed to connect to wallet. Please try again.");
    }
  };

  // Function to disconnect from wallet
  const disconnectWallet = async () => {
    try {
      await connector.killSession();
    } catch (error) {
      console.error("Error disconnecting from wallet:", error);
      alert("Failed to disconnect from wallet. Please try again.");
    }
  };

  return (
    <div>
      <h1>Wallet Connection DApp</h1>
      {connected ? (
        <div>
          <p>Wallet connected!</p>
          <button onClick={disconnectWallet}>Disconnect Wallet</button>
        </div>
      ) : (
        <button onClick={connectWallet}>Connect Wallet</button>
      )}
    </div>
  );
};

// Wrap the DApp component with WalletConnectProvider
const App = () => {
  return (
    <WalletConnectProvider>
      <WalletConnectionDApp />
    </WalletConnectProvider>
  );
};

export default App;
```
