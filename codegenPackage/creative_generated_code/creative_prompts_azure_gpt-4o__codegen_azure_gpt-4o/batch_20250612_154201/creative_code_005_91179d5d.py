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
import Web3 from 'web3';

// Define a functional component
const WalletConnectionStatus = () => {
  // State variables to track wallet connection and block number
  const [isWalletConnected, setIsWalletConnected] = useState(false);
  const [blockNumber, setBlockNumber] = useState(null);
  const [errorMessage, setErrorMessage] = useState('');

  // Function to check wallet connection and fetch the block number
  const checkWalletConnection = async () => {
    try {
      // Check if Web3 is injected (e.g. by a browser wallet like MetaMask)
      if (window.ethereum) {
        const web3 = new Web3(window.ethereum);

        // Request access to the user's wallet
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Set wallet connection status
        setIsWalletConnected(true);

        // Fetch the latest block number
        const blockNum = await web3.eth.getBlockNumber();
        setBlockNumber(blockNum);
      } else {
        // Handle case when Web3 provider is not available
        setErrorMessage('No Web3 provider detected. Please install MetaMask or another Ethereum-compatible wallet.');
        setIsWalletConnected(false);
      }
    } catch (error) {
      // Handle errors gracefully
      console.error('Error connecting to wallet:', error);
      setErrorMessage('Failed to connect to wallet. Please try again.');
      setIsWalletConnected(false);
    }
  };

  // UseEffect hook to check wallet connection status on component mount
  useEffect(() => {
    checkWalletConnection();
  }, []);

  // JSX to render the UI
  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>Wallet Connection Status</h1>
      {/* Display connection status */}
      <p>
        Wallet Connected: <strong>{isWalletConnected ? 'Yes' : 'No'}</strong>
      </p>
      {/* Display block number if available */}
      {isWalletConnected && blockNumber !== null && (
        <p>
          Current Block Number: <strong>{blockNumber}</strong>
        </p>
      )}
      {/* Display error message if any */}
      {errorMessage && <p style={{ color: 'red' }}>{errorMessage}</p>}
    </div>
  );
};

// Export the component
export default WalletConnectionStatus;
```
