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

```jsx
// Import required React and Starknet libraries
import React, { useState } from 'react';
import { useConnectors, useAccount } from '@starknet-react/core';

const WalletConnector = () => {
  // State to track connection errors
  const [errorMessage, setErrorMessage] = useState(null);

  // Access Starknet connectors and account information
  const { connect, connectors } = useConnectors();
  const { address } = useAccount();

  // Handler for connecting a wallet
  const handleConnect = async (connector) => {
    try {
      // Attempt to connect using the provided connector
      await connect(connector);
      // Clear any existing error messages
      setErrorMessage(null);
    } catch (error) {
      // Display error message on connection failure
      setErrorMessage('Failed to connect wallet. Please try again.');
      console.error('Wallet connection error:', error);
    }
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>Starknet Wallet Connector</h1>

      {/* Display the user's Starknet account address if connected */}
      <div>
        {address ? (
          <p>
            <strong>Connected Address:</strong> {address}
          </p>
        ) : (
          <p>
            <strong>No wallet connected.</strong>
          </p>
        )}
      </div>

      {/* Display a list of available connectors */}
      <div>
        <h2>Connect Wallet</h2>
        {connectors.map((connector) => (
          <button
            key={connector.id}
            style={{
              margin: '5px',
              padding: '10px 15px',
              backgroundColor: '#6200ea',
              color: 'white',
              border: 'none',
              borderRadius: '5px',
              cursor: 'pointer',
            }}
            onClick={() => handleConnect(connector)}
          >
            Connect with {connector.name}
          </button>
        ))}
      </div>

      {/* Display error message if connection fails */}
      {errorMessage && (
        <p style={{ color: 'red', marginTop: '10px' }}>
          <strong>Error:</strong> {errorMessage}
        </p>
      )}
    </div>
  );
};

export default WalletConnector;
```
