"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://across-to.com
Prompt: Provide code examples for integrating Across Protocol’s wallet connection feature into a web application for cross-chain asset transfers.
Generated: DETERMINISTIC_0772f6ef78d3c97f
Batch ID: 20250612_150135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries for wallet integration and Across Protocol
import React, { useState, useEffect } from 'react'; 
import Web3 from 'web3'; // Web3.js for connecting to Ethereum-compatible wallets
import { AcrossSDK } from '@across-protocol/sdk'; // Across Protocol SDK

// Main wallet connection component
const WalletConnection = () => {
  // State for storing wallet address and Web3 instance
  const [walletAddress, setWalletAddress] = useState(null);
  const [web3Instance, setWeb3Instance] = useState(null);

  // State for error handling
  const [error, setError] = useState(null);

  // Function to connect wallet
  const connectWallet = async () => {
    try {
      // Check if MetaMask or compatible wallet exists
      if (window.ethereum) {
        const web3 = new Web3(window.ethereum); // Initialize Web3 instance
        setWeb3Instance(web3);

        // Request wallet connection
        const accounts = await window.ethereum.request({
          method: 'eth_requestAccounts',
        });

        // Set the connected wallet address
        setWalletAddress(accounts[0]);
        console.log('Wallet connected:', accounts[0]);
      } else {
        throw new Error(
          'MetaMask or compatible wallet not detected. Please install it to proceed.'
        );
      }
    } catch (err) {
      setError(err.message);
      console.error('Wallet connection error:', err);
    }
  };

  // Function to disconnect wallet (optional)
  const disconnectWallet = () => {
    setWalletAddress(null);
    setWeb3Instance(null);
    console.log('Wallet disconnected.');
  };

  // Effect hook to log wallet address changes
  useEffect(() => {
    if (walletAddress) {
      console.log('Wallet address updated:', walletAddress);
    }
  }, [walletAddress]);

  // Function to initiate cross-chain transfer using Across Protocol
  const initiateCrossChainTransfer = async (asset, amount, destinationChainId) => {
    try {
      if (!web3Instance || !walletAddress) {
        throw new Error('Wallet not connected.');
      }

      // Initialize Across Protocol SDK
      const sdk = new AcrossSDK({
        web3: web3Instance,
        account: walletAddress,
      });

      // Construct transfer parameters
      const transferParams = {
        asset, // Token address or symbol (e.g., 'ETH')
        amount, // Amount to transfer (in Wei for Ethereum-based chains)
        destinationChainId, // Target chain ID for transfer
      };

      // Initiate transfer
      const tx = await sdk.transfer(transferParams);

      // Wait for the transaction to be mined
      await tx.wait();
      console.log('Cross-chain transfer successful:', tx);
    } catch (err) {
      setError(err.message);
      console.error('Cross-chain transfer error:', err);
    }
  };

  return (
    <div>
      {/* UI for wallet connection */}
      {walletAddress ? (
        <div>
          <p>Connected Wallet: {walletAddress}</p>
          <button onClick={disconnectWallet}>Disconnect Wallet</button>
        </div>
      ) : (
        <button onClick={connectWallet}>Connect Wallet</button>
      )}

      {/* Button to initiate cross-chain transfer (for demonstration) */}
      <button
        onClick={() =>
          initiateCrossChainTransfer('ETH', '1000000000000000000', 137) // Transfer 1 ETH to Polygon (chainId: 137)
        }
        disabled={!walletAddress}
      >
        Initiate Cross-Chain Transfer
      </button>

      {/* Display errors */}
      {error && <p style={{ color: 'red' }}>Error: {error}</p>}
    </div>
  );
};

// Export the WalletConnection component
export default WalletConnection;
```

- **Notes**:
  - Replace `'ETH'`, `'1000000000000000000'`, and `137` with appropriate values based on your application's requirements. Adjust token decimals accordingly.
  - Make sure the Across Protocol's SDK is properly installed in your project (`npm install @across-protocol/sdk`).
  - Ensure your application handles gas fees appropriately for cross-chain transfers.
  - Customize the UI as necessary to align with your application's design.
