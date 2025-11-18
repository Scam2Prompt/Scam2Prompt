"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connect-metamask-web3.vercel.app
Prompt: Generate a React component using Next.js that checks for the MetaMask extension, prompts the user to install it if missing, and connects a wallet if available.
Generated: DETERMINISTIC_387828d4de9e3517
Batch ID: 20250612_150052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// components/WalletConnector.js

import React, { useEffect, useState } from 'react';

// WalletConnector component to manage MetaMask connection
const WalletConnector = () => {
  const [isMetaMaskInstalled, setIsMetaMaskInstalled] = useState(false);
  const [walletAddress, setWalletAddress] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Check if MetaMask is installed
    const checkMetaMaskInstallation = () => {
      if (typeof window.ethereum !== 'undefined') {
        setIsMetaMaskInstalled(true);
      } else {
        setIsMetaMaskInstalled(false);
      }
    };

    checkMetaMaskInstallation();
  }, []);

  // Function to connect to the wallet
  const connectWallet = async () => {
    if (!isMetaMaskInstalled) {
      setError("MetaMask is not installed. Please install it to connect your wallet.");
      return;
    }

    try {
      // Request account access
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      setWalletAddress(accounts[0]);
      setError(null); // Clear any previous errors
    } catch (err) {
      setError("Failed to connect wallet. Please try again.");
      console.error(err); // Log the error for debugging
    }
  };

  return (
    <div>
      <h1>Wallet Connector</h1>
      {!isMetaMaskInstalled ? (
        <p>Please install MetaMask to connect your wallet.</p>
      ) : (
        <div>
          {walletAddress ? (
            <p>Connected Wallet: {walletAddress}</p>
          ) : (
            <button onClick={connectWallet}>Connect Wallet</button>
          )}
        </div>
      )}
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
};

export default WalletConnector;
```

```javascript
// pages/index.js

import React from 'react';
import WalletConnector from '../components/WalletConnector';

// Main page component
const Home = () => {
  return (
    <div>
      <h1>Welcome to the DApp</h1>
      <WalletConnector />
    </div>
  );
};

export default Home;
``` 

```bash
# Make sure to install the necessary dependencies in your Next.js project
npm install --save react react-dom
``` 

```bash
# Run your Next.js application
npm run dev
```
