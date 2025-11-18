"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cesta.finance
Prompt: Provide an example of how to implement a "Connect Wallet" button using React and Web3.js, inspired by the Cesta Finance interface.
Generated: DETERMINISTIC_107253137ccebd75
Batch ID: 20250612_145117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import React, { useState } from 'react';
import Web3 from 'web3';

// Define the ConnectWallet component
const ConnectWallet = () => {
  // State to hold the wallet address
  const [walletAddress, setWalletAddress] = useState(null);

  // Function to handle wallet connection
  const connectWallet = async () => {
    try {
      // Check if Web3 provider (e.g., MetaMask) is available
      if (window.ethereum) {
        // Request access to the user's wallet
        const web3 = new Web3(window.ethereum);
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Set the first account (wallet address) to state
        setWalletAddress(accounts[0]);
        console.log(`Connected wallet: ${accounts[0]}`);
      } else {
        // Handle case where no Web3 provider is available
        alert('No Web3 provider detected. Please install MetaMask or another wallet.');
      }
    } catch (error) {
      // Log error and notify user in case of failure
      console.error('Error connecting wallet:', error);
      alert('Failed to connect wallet. Please try again.');
    }
  };

  return (
    <div>
      {/* Display the Connect Wallet button */}
      <button
        onClick={connectWallet}
        style={{
          padding: '10px 20px',
          fontSize: '16px',
          cursor: 'pointer',
          backgroundColor: '#4CAF50',
          color: 'white',
          border: 'none',
          borderRadius: '5px',
        }}
      >
        {walletAddress ? 'Wallet Connected' : 'Connect Wallet'}
      </button>

      {/* Display the connected wallet address */}
      {walletAddress && <p>Connected Wallet Address: {walletAddress}</p>}
    </div>
  );
};

export default ConnectWallet;
```
