"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-homepage.vercel.app
Prompt: Write a React component using Starknet-React to connect a wallet for purchasing pixels on the Starknet Homepage.
Generated: DETERMINISTIC_afa3ac9eca130a38
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useEffect, useState } from 'react';
import { useWallet } from 'starknet-react';
import { Button, Alert } from 'reactstrap'; // Assuming you're using Reactstrap for UI components

// A React component for connecting a wallet to purchase pixels on the Starknet Homepage
const PixelPurchase = () => {
  const { account, connect, disconnect } = useWallet();
  const [error, setError] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  // Function to connect to the user's wallet
  const handleConnect = async () => {
    setIsLoading(true);
    try {
      await connect(); // Attempt to connect
    } catch (err) {
      // Handle connection errors
      setError('Failed to connect to the wallet. Please try again.');
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  // Function to disconnect from the user's wallet
  const handleDisconnect = async () => {
    setIsLoading(true);
    try {
      await disconnect(); // Attempt to disconnect
    } catch (err) {
      // Handle disconnection errors
      setError('Failed to disconnect from the wallet. Please try again.');
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  // Effect to reset error message when account changes
  useEffect(() => {
    if (account) {
      setError(null); // Reset error if account is connected
    }
  }, [account]);

  return (
    <div className="pixel-purchase">
      {error && <Alert color="danger">{error}</Alert>} {/* Display error if any */}
      <h1>Purchase Your Pixels</h1>
      {account ? (
        <>
          <p>Connected as: {account}</p>
          <Button color="danger" onClick={handleDisconnect} disabled={isLoading}>
            {isLoading ? 'Disconnecting...' : 'Disconnect Wallet'}
          </Button>
        </>
      ) : (
        <Button color="primary" onClick={handleConnect} disabled={isLoading}>
          {isLoading ? 'Connecting...' : 'Connect Wallet'}
        </Button>
      )}
    </div>
  );
};

export default PixelPurchase;
```
