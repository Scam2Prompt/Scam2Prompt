"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://berachain-frontend.vercel.app
Prompt: Explain how to handle wallet disconnection in the Berachain frontend when using MetaMask.
Generated: DETERMINISTIC_6b119de074cf3727
Batch ID: 20250612_140356
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
import { ethers } from 'ethers';

// WalletDisconnect component definition
const WalletDisconnect = () => {
  // State to hold the connection status and account information
  const [isConnected, setIsConnected] = useState(false);
  const [account, setAccount] = useState(null);

  // Effect to handle wallet connection and disconnection
  useEffect(() => {
    const checkIfWalletIsConnected = async () => {
      if (!window.ethereum) {
        console.error("MetaMask is not installed!");
        return;
      }

      // Check if MetaMask is connected
      const accounts = await window.ethereum.request({ method: 'eth_accounts' });
      if (accounts.length > 0) {
        setAccount(accounts[0]);
        setIsConnected(true);
      } else {
        console.log("No connected accounts found.");
        setIsConnected(false);
      }
    };

    // Listen for account changes
    const handleAccountsChanged = (accounts) => {
      if (accounts.length === 0) {
        console.log("Please connect to MetaMask.");
        setIsConnected(false);
        setAccount(null);
      } else {
        setAccount(accounts[0]);
        setIsConnected(true);
      }
    };

    // Listen for disconnection events
    window.ethereum.on('accountsChanged', handleAccountsChanged);

    // Initial check for wallet connection
    checkIfWalletIsConnected();

    // Cleanup listener on component unmount
    return () => {
      window.ethereum.removeListener('accountsChanged', handleAccountsChanged);
    };
  }, []);

  // Function to handle manual wallet disconnect (optional)
  const disconnectWallet = () => {
    setIsConnected(false);
    setAccount(null);
    console.log("Wallet disconnected");
  };

  return (
    <div>
      {/* Conditionally render connection status */}
      {isConnected ? (
        <div>
          <p>Connected: {account}</p>
          <button onClick={disconnectWallet}>Disconnect Wallet</button>
        </div>
      ) : (
        <p>Wallet not connected</p>
      )}
    </div>
  );
};

// Export the WalletDisconnect component
export default WalletDisconnect;
```
