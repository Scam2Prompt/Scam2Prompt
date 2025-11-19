"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-ju06cb1h2-dunghd.vercel.app
Prompt: Explain how to manage account balances in a DApp with Web3 React and MetaMask integration.
Generated: DETERMINISTIC_797a6db5c631638a
Batch ID: 20250612_163526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required dependencies
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';

// Component: AccountBalanceManager
const AccountBalanceManager = () => {
  // State variables to store account, balance, and connection status
  const [account, setAccount] = useState(null);
  const [balance, setBalance] = useState(null);
  const [isConnected, setIsConnected] = useState(false);

  // Initialize Web3 instance
  let web3;

  // Function to connect to MetaMask
  const connectWallet = async () => {
    try {
      if (window.ethereum) {
        // Request account access
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        web3 = new Web3(window.ethereum);
        setAccount(accounts[0]);
        setIsConnected(true);
      } else {
        alert('MetaMask not detected. Please install MetaMask.');
      }
    } catch (error) {
      console.error('Error connecting to MetaMask:', error);
    }
  };

  // Function to fetch the account balance
  const fetchBalance = async () => {
    try {
      if (account && web3) {
        const balanceInWei = await web3.eth.getBalance(account);
        const balanceInEth = web3.utils.fromWei(balanceInWei, 'ether');
        setBalance(balanceInEth);
      }
    } catch (error) {
      console.error('Error fetching balance:', error);
    }
  };

  // Effect hook to auto-fetch balance when account changes
  useEffect(() => {
    if (account && isConnected) {
      fetchBalance();
    }
  }, [account, isConnected]);

  // Render the component
  return (
    <div>
      <h1>DApp Account Balance Manager</h1>
      {/* Display connected account information */}
      {isConnected ? (
        <div>
          <p>Connected Account: {account}</p>
          <p>Balance: {balance ? `${balance} ETH` : 'Fetching...'}</p>
          <button onClick={fetchBalance}>Refresh Balance</button>
        </div>
      ) : (
        // Button to connect to MetaMask
        <button onClick={connectWallet}>Connect MetaMask</button>
      )}
    </div>
  );
};

export default AccountBalanceManager;
```
