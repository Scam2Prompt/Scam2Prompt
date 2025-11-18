"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://open-sea-web3-app.vercel.app
Prompt: Write code to implement a "Connect Wallet" button in React that interacts with Metamask in a Web3 application.
Generated: DETERMINISTIC_34a9925bf52a91f5
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState } from 'react';

// Importing the ethers library to interact with Ethereum
import { ethers } from 'ethers';

const ConnectWalletButton = () => {
  // State to hold the connected wallet address
  const [walletAddress, setWalletAddress] = useState(null);

  // Function to connect to Metamask
  const connectWallet = async () => {
    if (typeof window.ethereum !== 'undefined') {
      try {
        // Requesting account access from the user
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        
        // Set the first account address to state
        setWalletAddress(accounts[0]);
      } catch (error) {
        // Handling errors, such as user denying account access
        console.error("Error connecting to wallet:", error);
        alert("Could not connect to wallet. Please try again.");
      }
    } else {
      // If Metamask is not installed
      alert("Please install Metamask to connect your wallet.");
    }
  };

  return (
    <div>
      <button onClick={connectWallet} style={styles.button}>
        {walletAddress ? `Connected: ${walletAddress.substring(0, 6)}...${walletAddress.substring(38)}` : 'Connect Wallet'}
      </button>
    </div>
  );
};

// Simple styles for the button
const styles = {
  button: {
    padding: '10px 20px',
    fontSize: '16px',
    borderRadius: '5px',
    cursor: 'pointer',
    backgroundColor: '#1e88e5',
    color: 'white',
    border: 'none',
    outline: 'none',
  },
};

export default ConnectWalletButton;
```
