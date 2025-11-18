"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metmaskextensio.livejournal.com
Prompt: Create a guide for integrating the MetaMask Wallet Extension into a React application for managing cryptocurrency transactions.
Generated: DETERMINISTIC_9dd4656f7b1cd2fb
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary packages
import React, { useEffect, useState } from 'react';

// Define a functional component for MetaMask integration
const MetaMaskIntegration = () => {
  // State to hold the user's account and balance
  const [account, setAccount] = useState('');
  const [balance, setBalance] = useState('0');
  const [error, setError] = useState('');

  // Function to connect to MetaMask
  const connectMetaMask = async () => {
    if (typeof window.ethereum === 'undefined') {
      setError('Please install MetaMask!');
      return;
    }

    try {
      // Request account access
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      setAccount(accounts[0]); // Set the user's account

      // Fetch and set the user's balance
      await getBalance(accounts[0]);
    } catch (error) {
      setError(error.message);
    }
  };

  // Function to fetch the user's Ethereum balance
  const getBalance = async (account) => {
    try {
      // Fetch balance from the Ethereum network
      const balance = await window.ethereum.request({
        method: 'eth_getBalance',
        params: [account, 'latest'],
      });

      // Convert balance from Wei to Ether and set it
      setBalance(window.ethereum.utils.fromWei(balance, 'ether'));
    } catch (error) {
      setError(error.message);
    }
  };

  // Effect to detect account changes
  useEffect(() => {
    const handleAccountsChanged = (accounts) => {
      if (accounts.length > 0) {
        setAccount(accounts[0]);
        getBalance(accounts[0]);
      } else {
        setAccount('');
        setBalance('0');
      }
    };

    // Subscribe to accounts change
    window.ethereum.on('accountsChanged', handleAccountsChanged);

    // Cleanup subscription on unmount
    return () => {
      window.ethereum.removeListener('accountsChanged', handleAccountsChanged);
    };
  }, []);

  return (
    <div>
      <h1>MetaMask Integration</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <button onClick={connectMetaMask}>Connect to MetaMask</button>
      {account && (
        <div>
          <p>Account: {account}</p>
          <p>Balance: {balance} ETH</p>
        </div>
      )}
    </div>
  );
};

export default MetaMaskIntegration;
```

### To Use This Component:
1. Install `react` if not already done:
   ```bash
   npm install react
   ```

2. Include `<MetaMaskIntegration />` in your main application component or wherever appropriate.

3. Ensure that you have the MetaMask extension installed in your browser to test this integration.
