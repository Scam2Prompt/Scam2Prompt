"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-ju06cb1h2-dunghd.vercel.app
Prompt: Explain how to manage account balances in a DApp with Web3 React and MetaMask integration.
Generated: DETERMINISTIC_797a6db5c631638a
Batch ID: 20250612_163526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';

// Define the DApp component
const AccountBalanceManager = () => {
  // State variables to hold account information and balance
  const [account, setAccount] = useState('');
  const [balance, setBalance] = useState('0');
  const [loading, setLoading] = useState(true);

  // Initialize Web3 instance
  const web3 = new Web3(window.ethereum);

  // Function to load account and balance
  const loadAccountData = async () => {
    try {
      // Request account access if needed
      await window.ethereum.request({ method: 'eth_requestAccounts' });
      
      // Get the user's account address
      const accounts = await web3.eth.getAccounts();
      setAccount(accounts[0]);

      // Get the account balance in Wei
      const weiBalance = await web3.eth.getBalance(accounts[0]);
      // Convert Wei to Ether
      const etherBalance = web3.utils.fromWei(weiBalance, 'ether');
      setBalance(etherBalance);
    } catch (error) {
      console.error("Error loading account data:", error);
      alert("Failed to load account data. Please check console for details.");
    } finally {
      setLoading(false);
    }
  };

  // Effect to load account data on component mount
  useEffect(() => {
    loadAccountData();
  }, []);

  // Render the component
  return (
    <div>
      <h1>Account Balance Manager</h1>
      {loading ? (
        <p>Loading...</p>
      ) : (
        <div>
          <p><strong>Account:</strong> {account}</p>
          <p><strong>Balance:</strong> {balance} ETH</p>
        </div>
      )}
    </div>
  );
};

// Export the component for use in other parts of the application
export default AccountBalanceManager;
```
