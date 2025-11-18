"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-homepage-kappa.vercel.app
Prompt: Write a React component using Starknet-React to connect a wallet and display the user's Starknet account address.
Generated: DETERMINISTIC_9c0b9868611181e3
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useEffect, useState } from 'react';
import { useStarknet } from '@starknet-react/core';
import { StarknetProvider, useStarknetContract } from '@starknet-react/core';

// Component to connect a Starknet wallet and display the user's account address
const WalletConnector = () => {
  // State to store the user's account address
  const [accountAddress, setAccountAddress] = useState(null);
  
  // Get the current connection status and account from Starknet context
  const { account, connect, disconnect } = useStarknet();

  // Effect to update the account address when it changes
  useEffect(() => {
    if (account) {
      setAccountAddress(account);
    } else {
      setAccountAddress(null);
    }
  }, [account]);

  // Function to handle wallet connection
  const handleConnect = async () => {
    try {
      await connect();
    } catch (error) {
      console.error('Error connecting to wallet:', error);
      alert('Failed to connect to wallet. Please try again.');
    }
  };

  // Function to handle wallet disconnection
  const handleDisconnect = async () => {
    try {
      await disconnect();
      setAccountAddress(null);
    } catch (error) {
      console.error('Error disconnecting wallet:', error);
      alert('Failed to disconnect from wallet. Please try again.');
    }
  };

  return (
    <div>
      <h2>Starknet Wallet Connector</h2>
      {accountAddress ? (
        <div>
          <p>Your Starknet Account Address:</p>
          <p>{accountAddress}</p>
          <button onClick={handleDisconnect}>Disconnect Wallet</button>
        </div>
      ) : (
        <button onClick={handleConnect}>Connect Wallet</button>
      )}
    </div>
  );
};

// Main application component
const App = () => {
  return (
    <StarknetProvider>
      <WalletConnector />
    </StarknetProvider>
  );
};

export default App;
```
