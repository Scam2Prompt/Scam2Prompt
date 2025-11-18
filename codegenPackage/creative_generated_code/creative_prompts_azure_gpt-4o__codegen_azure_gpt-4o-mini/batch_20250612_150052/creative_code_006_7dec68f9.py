"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connect-metamask-web3.vercel.app
Prompt: Suggest best practices for handling blockchain wallet connections securely in a Next.js application using MetaMask.
Generated: DETERMINISTIC_7dec68f9f7b7b3d2
Batch ID: 20250612_150052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and hooks from React and Next.js
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';

// Define a functional component for handling wallet connections
const WalletConnect = () => {
  // State variables to manage wallet connection and user account
  const [web3, setWeb3] = useState(null);
  const [account, setAccount] = useState(null);
  const [error, setError] = useState(null);

  // Effect hook to detect MetaMask installation and set up Web3
  useEffect(() => {
    // Function to initialize Web3 and check for MetaMask
    const initWeb3 = async () => {
      if (window.ethereum) {
        try {
          // Create a new instance of Web3 with the provider
          const web3Instance = new Web3(window.ethereum);
          setWeb3(web3Instance);

          // Request account access if needed
          await window.ethereum.request({ method: 'eth_requestAccounts' });

          // Fetch the user's accounts
          const accounts = await web3Instance.eth.getAccounts();
          setAccount(accounts[0]);
        } catch (err) {
          // Handle errors during wallet connection
          console.error('Error connecting to MetaMask:', err);
          setError('Failed to connect to MetaMask. Please ensure it is installed and unlock your wallet.');
        }
      } else {
        // Handle the case where MetaMask is not installed
        setError('MetaMask is not installed. Please install it to use this feature.');
      }
    };

    // Call the initialization function
    initWeb3();
  }, []);

  // Function to handle wallet disconnection
  const disconnectWallet = () => {
    setAccount(null);
    setWeb3(null);
  };

  return (
    <div>
      <h1>Connect to MetaMask</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {account ? (
        <div>
          <p>Connected as: {account}</p>
          <button onClick={disconnectWallet}>Disconnect</button>
        </div>
      ) : (
        <button onClick={() => initWeb3()}>Connect Wallet</button>
      )}
    </div>
  );
};

export default WalletConnect;
```
