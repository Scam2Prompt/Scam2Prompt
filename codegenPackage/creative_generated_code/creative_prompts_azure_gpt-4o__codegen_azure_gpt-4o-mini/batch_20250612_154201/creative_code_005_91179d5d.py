"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://berachain-frontend.vercel.app
Prompt: Develop a frontend feature that verifies wallet connection status with Berachain and fetches the block number using `eth_blockNumber`.
Generated: DETERMINISTIC_91179d5d551efa8a
Batch ID: 20250612_154201
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

// Define the WalletConnection component
const WalletConnection = () => {
  // State variables to manage wallet connection status and block number
  const [isConnected, setIsConnected] = useState(false);
  const [blockNumber, setBlockNumber] = useState(null);
  const [error, setError] = useState(null);

  // Function to check wallet connection status
  const checkWalletConnection = async () => {
    if (window.ethereum) {
      try {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        setIsConnected(true);
      } catch (err) {
        // Handle user rejecting the request or other errors
        console.error('User denied account access or error occurred:', err);
        setIsConnected(false);
      }
    } else {
      setError('Metamask or another wallet provider is not detected.');
    }
  };

  // Function to fetch the current block number
  const fetchBlockNumber = async () => {
    if (isConnected && window.ethereum) {
      try {
        // Get the block number from the Ethereum provider
        const blockNum = await window.ethereum.request({ method: 'eth_blockNumber' });
        // Convert block number from hex to decimal
        setBlockNumber(parseInt(blockNum, 16));
      } catch (err) {
        // Handle errors during fetching block number
        console.error('Error fetching block number:', err);
        setError('Failed to fetch block number.');
      }
    }
  };

  // useEffect to check wallet connection on component mount
  useEffect(() => {
    checkWalletConnection();
  }, []);

  // useEffect to fetch block number whenever wallet connection status changes
  useEffect(() => {
    if (isConnected) {
      fetchBlockNumber();
    }
  }, [isConnected]);

  return (
    <div>
      <h1>Wallet Connection Status</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <p>Connection Status: {isConnected ? 'Connected' : 'Not Connected'}</p>
      {isConnected && (
        <p>Current Block Number: {blockNumber !== null ? blockNumber : 'Fetching...'}</p>
      )}
    </div>
  );
};

// Export the WalletConnection component for use in other parts of the application
export default WalletConnection;
```
