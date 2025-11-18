"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-curve.com
Prompt: Generate code to integrate MetaMask’s Wallet Guard for enhanced security alerts in a dapp.
Generated: DETERMINISTIC_a2bae49f726bcec1
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries
import React, { useEffect } from 'react';
import { useWallet } from 'use-wallet';
import WalletGuard from '@metamask/wallet-guard';

// Main Application Component
const App = () => {
  const wallet = useWallet();

  // Function to initialize Wallet Guard
  const initializeWalletGuard = () => {
    try {
      // Check if Wallet Guard is available
      if (WalletGuard) {
        WalletGuard.init();
        console.log("Wallet Guard initialized successfully");
      } else {
        console.error("Wallet Guard is not available");
      }
    } catch (error) {
      console.error("Error initializing Wallet Guard:", error);
    }
  };

  // Effect to set up Wallet Guard on component mount
  useEffect(() => {
    initializeWalletGuard();

    // Optional: Setup a listener for Wallet Guard events
    const handleSecurityAlert = (alert) => {
      alert.show(); // Display the alert to the user
    };

    WalletGuard.on('securityAlert', handleSecurityAlert);

    // Cleanup function to remove event listener
    return () => {
      WalletGuard.off('securityAlert', handleSecurityAlert);
    };
  }, []);

  // Render function
  return (
    <div>
      <h1>My DApp with MetaMask Wallet Guard</h1>
      {wallet.status === 'connected' ? (
        <p>Connected to {wallet.account}</p>
      ) : (
        <button onClick={wallet.connect}>Connect Wallet</button>
      )}
    </div>
  );
};

// Export the App component as the default export
export default App;
```
