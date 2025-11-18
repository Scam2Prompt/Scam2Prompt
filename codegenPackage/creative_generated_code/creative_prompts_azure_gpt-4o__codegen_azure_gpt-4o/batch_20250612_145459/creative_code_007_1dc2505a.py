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

```jsx
// Import necessary libraries and hooks
import React, { useState } from 'react';
import { ethers } from 'ethers'; // ethers.js to interact with Ethereum blockchain

// Define the ConnectWalletButton component
const ConnectWalletButton = () => {
  // State to store wallet connection status and address
  const [walletAddress, setWalletAddress] = useState(null);
  const [error, setError] = useState(null);

  // Function to handle wallet connection
  const connectWallet = async () => {
    try {
      // Check if the browser has an Ethereum provider (like MetaMask)
      if (!window.ethereum) {
        throw new Error('No Ethereum provider found. Install MetaMask or another wallet.');
      }

      // Request wallet connection
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

      // Set the wallet address (first account in the array)
      setWalletAddress(accounts[0]);
      setError(null); // Clear any previous errors
    } catch (err) {
      // Handle errors and set error message
      console.error('Failed to connect wallet:', err.message);
      setError(err.message);
    }
  };

  // Function to truncate wallet address for better readability
  const truncateAddress = (address) => {
    return `${address.slice(0, 6)}...${address.slice(-4)}`;
  };

  return (
    <div>
      {/* Button to connect wallet */}
      <button
        onClick={connectWallet}
        style={{
          backgroundColor: '#4CAF50',
          color: 'white',
          padding: '10px 20px',
          border: 'none',
          borderRadius: '5px',
          cursor: 'pointer',
          fontSize: '16px',
        }}
      >
        {walletAddress ? `Connected: ${truncateAddress(walletAddress)}` : 'Connect Wallet'}
      </button>

      {/* Display error message if any */}
      {error && (
        <p style={{ color: 'red', marginTop: '10px' }}>
          {`Error: ${error}`}
        </p>
      )}
    </div>
  );
};

export default ConnectWalletButton;
```
