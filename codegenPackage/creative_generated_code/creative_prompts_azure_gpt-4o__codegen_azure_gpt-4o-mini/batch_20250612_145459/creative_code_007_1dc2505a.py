"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-kelexo-en.web.app
Prompt: Create a React component for a "Connect Wallet" button with functionality similar to Kelexo's implementation.
Generated: DETERMINISTIC_1dc2505ab0c4c0a1
Batch ID: 20250612_145459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState } from 'react';
import PropTypes from 'prop-types';

// A ConnectWalletButton component to facilitate wallet connection
const ConnectWalletButton = ({ onConnect, onDisconnect }) => {
  // State to hold the wallet connection status
  const [connected, setConnected] = useState(false);

  // Function to handle wallet connection
  const handleConnect = async () => {
    try {
      // Assuming a method to connect to a wallet is available
      const walletConnection = await connectToWallet(); // Replace with actual connection logic

      if (walletConnection) {
        setConnected(true); // Update connection status
        onConnect(walletConnection); // Callback for successful connection
      }
    } catch (error) {
      console.error('Wallet connection failed:', error);
      alert('Failed to connect wallet. Please try again.'); // User-friendly error message
    }
  };

  // Function to handle wallet disconnection
  const handleDisconnect = () => {
    try {
      // Logic to disconnect from the wallet
      disconnectFromWallet(); // Replace with actual disconnection logic
      setConnected(false); // Update connection status
      onDisconnect(); // Callback for disconnection
    } catch (error) {
      console.error('Wallet disconnection failed:', error);
      alert('Failed to disconnect wallet. Please try again.'); // User-friendly error message
    }
  };

  return (
    <button
      type="button"
      onClick={connected ? handleDisconnect : handleConnect}
      className={`connect-wallet-button ${connected ? 'connected' : 'disconnected'}`}
    >
      {connected ? 'Disconnect Wallet' : 'Connect Wallet'}
    </button>
  );
};

// PropTypes for type checking
ConnectWalletButton.propTypes = {
  onConnect: PropTypes.func.isRequired, // Callback function for successful connection
  onDisconnect: PropTypes.func.isRequired, // Callback function for disconnection
};

// Example placeholder functions to simulate wallet operations
const connectToWallet = async () => {
  // Replace this with actual wallet connection logic
  return new Promise((resolve) => {
    setTimeout(() => resolve('WalletConnected'), 1000);
  });
};

const disconnectFromWallet = () => {
  // Replace this with actual wallet disconnection logic
  console.log('Wallet disconnected');
};

export default ConnectWalletButton;
```
