"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nidhidao.finance
Prompt: Write code to integrate a "Connect Wallet" button into a React-based dApp, inspired by the interface on NidhiDAO.
Generated: DETERMINISTIC_3c263f20cfacf7c3
Batch ID: 20250612_145117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and components
import React, { useState } from 'react';
import { ethers } from 'ethers';

// WalletButton Component
const WalletButton = () => {
  const [walletAddress, setWalletAddress] = useState(null); // State to store the connected wallet address
  const [errorMessage, setErrorMessage] = useState(null);  // State to store any error messages

  // Function to handle wallet connection
  const connectWallet = async () => {
    try {
      // Check if Ethereum provider (MetaMask) is available in the window object
      if (window.ethereum) {
        const provider = new ethers.BrowserProvider(window.ethereum);
        const accounts = await provider.send("eth_requestAccounts", []); // Request account access
        setWalletAddress(accounts[0]); // Set the connected wallet address
        setErrorMessage(null); // Reset any error messages
      } else {
        throw new Error('MetaMask is not installed. Please install it to use this dApp.');
      }
    } catch (error) {
      setErrorMessage(error.message); // Display error messages if connection fails
    }
  };

  // Render the Connect Wallet button and wallet information
  return (
    <div style={{ textAlign: 'center', marginTop: '20px' }}>
      {/* Display Connect Wallet button if no wallet is connected */}
      {!walletAddress ? (
        <button
          onClick={connectWallet}
          style={{
            padding: '10px 20px',
            fontSize: '16px',
            backgroundColor: '#4CAF50',
            color: 'white',
            border: 'none',
            borderRadius: '5px',
            cursor: 'pointer',
          }}
        >
          Connect Wallet
        </button>
      ) : (
        // Display connected wallet address if a wallet is connected
        <div>
          <p style={{ fontSize: '16px', fontWeight: 'bold' }}>
            Connected Wallet Address:
          </p>
          <p style={{ fontSize: '14px', color: '#666' }}>{walletAddress}</p>
        </div>
      )}

      {/* Display error message if there is an issue */}
      {errorMessage && (
        <p style={{ color: 'red', marginTop: '10px' }}>{errorMessage}</p>
      )}
    </div>
  );
};

// Export WalletButton component as default
export default WalletButton;
```
