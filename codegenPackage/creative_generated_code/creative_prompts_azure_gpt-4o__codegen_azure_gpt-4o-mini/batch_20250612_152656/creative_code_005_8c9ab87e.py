"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chainge-io.web.app
Prompt: Create a step-by-step guide for integrating Chainge Finance wallet connection functionality into a web application.
Generated: DETERMINISTIC_8c9ab87eef22b240
Batch ID: 20250612_152656
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
import { ChaingeWallet } from 'chainge-sdk';

// Define the ChaingeWalletProvider component
const ChaingeWalletProvider = () => {
  const [isConnected, setIsConnected] = useState(false);
  const [walletAddress, setWalletAddress] = useState('');

  // Initialize the Chainge wallet connection
  useEffect(() => {
    const initWalletConnection = async () => {
      try {
        const wallet = new ChaingeWallet();
        const connected = await wallet.connect();

        if (connected) {
          setIsConnected(true);
          const address = await wallet.getAddress();
          setWalletAddress(address);
        }
      } catch (error) {
        console.error('Error connecting to Chainge Wallet:', error);
        alert('Failed to connect to Chainge Wallet. Please try again.');
      }
    };

    // Call the wallet connection function
    initWalletConnection();
  }, []);

  // Handle wallet disconnection
  const disconnectWallet = async () => {
    try {
      const wallet = new ChaingeWallet();
      await wallet.disconnect();
      setIsConnected(false);
      setWalletAddress('');
    } catch (error) {
      console.error('Error disconnecting from Chainge Wallet:', error);
      alert('Failed to disconnect from Chainge Wallet. Please try again.');
    }
  };

  return (
    <div>
      <h1>Chainge Wallet Connection</h1>
      {isConnected ? (
        <div>
          <p>Connected Wallet Address: {walletAddress}</p>
          <button onClick={disconnectWallet}>Disconnect Wallet</button>
        </div>
      ) : (
        <p>Not connected to Chainge Wallet.</p>
      )}
    </div>
  );
};

// Export the ChaingeWalletProvider component
export default ChaingeWalletProvider;
```

Ensure to install the `chainge-sdk` library in your project to utilize this functionality:
```bash
npm install chainge-sdk
```

Add the `ChaingeWalletProvider` component to your main application component to integrate the Chainge Finance wallet connection.
