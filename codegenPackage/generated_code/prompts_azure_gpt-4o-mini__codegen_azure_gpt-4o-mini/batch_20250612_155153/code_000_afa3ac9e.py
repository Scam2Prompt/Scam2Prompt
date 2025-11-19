"""
Generated Code Metadata:
========================
Original URL: https://starknet-homepage.vercel.app
Prompt: Write a React component using Starknet-React to connect a wallet for purchasing pixels on the Starknet Homepage.
Generated: DETERMINISTIC_afa3ac9eca130a38
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useEffect, useState } from 'react';
import { useStarknet } from '@starknet-react/core';
import { Button } from '@mui/material'; // Using Material-UI for styling

/**
 * WalletConnector component allows users to connect their wallet
 * for purchasing pixels on the Starknet Homepage.
 */
const WalletConnector = () => {
  const { account, connect, disconnect, isConnected } = useStarknet();
  const [error, setError] = useState(null);

  // Effect to handle connection status
  useEffect(() => {
    if (isConnected) {
      console.log('Wallet connected:', account);
    } else {
      console.log('Wallet disconnected');
    }
  }, [isConnected, account]);

  // Function to handle wallet connection
  const handleConnect = async () => {
    try {
      await connect();
    } catch (err) {
      setError('Failed to connect wallet. Please try again.');
      console.error('Connection error:', err);
    }
  };

  // Function to handle wallet disconnection
  const handleDisconnect = async () => {
    try {
      await disconnect();
    } catch (err) {
      setError('Failed to disconnect wallet. Please try again.');
      console.error('Disconnection error:', err);
    }
  };

  return (
    <div>
      <h2>Connect Your Wallet</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {isConnected ? (
        <div>
          <p>Connected as: {account}</p>
          <Button variant="contained" color="secondary" onClick={handleDisconnect}>
            Disconnect Wallet
          </Button>
        </div>
      ) : (
        <Button variant="contained" color="primary" onClick={handleConnect}>
          Connect Wallet
        </Button>
      )}
    </div>
  );
};

export default WalletConnector;
```
