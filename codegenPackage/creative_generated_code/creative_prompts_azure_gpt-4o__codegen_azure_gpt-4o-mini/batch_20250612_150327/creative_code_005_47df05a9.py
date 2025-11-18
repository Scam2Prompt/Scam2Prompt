"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskwallett.creatorlink.net
Prompt: Develop a tutorial in code for integrating MetaMask with a React-based dApp, including functionality for connecting the wallet and displaying the user's account balance.
Generated: DETERMINISTIC_47df05a93b794f4a
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';

// Define the main App component
const App = () => {
  // State variables to store account and balance
  const [account, setAccount] = useState('');
  const [balance, setBalance] = useState('');

  // Initialize Web3
  const web3 = new Web3(window.ethereum);

  // Function to connect to MetaMask wallet
  const connectWallet = async () => {
    try {
      // Request account access from MetaMask
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      setAccount(accounts[0]);
      fetchBalance(accounts[0]);
    } catch (error) {
      console.error('Error connecting to wallet:', error);
    }
  };

  // Function to fetch the ETH balance of the connected account
  const fetchBalance = async (account) => {
    try {
      const balanceInWei = await web3.eth.getBalance(account);
      // Convert balance from Wei to Ether
      const balanceInEther = web3.utils.fromWei(balanceInWei, 'ether');
      setBalance(balanceInEther);
    } catch (error) {
      console.error('Error fetching balance:', error);
    }
  };

  // Effect to detect changes in the account or network
  useEffect(() => {
    const handleAccountsChanged = (accounts) => {
      if (accounts.length > 0) {
        setAccount(accounts[0]);
        fetchBalance(accounts[0]);
      } else {
        setAccount('');
        setBalance('');
      }
    };

    window.ethereum.on('accountsChanged', handleAccountsChanged);

    // Cleanup the listener on component unmount
    return () => {
      window.ethereum.removeListener('accountsChanged', handleAccountsChanged);
    };
  }, []);

  return (
    <div style={{ padding: '20px' }}>
      <h1>MetaMask Integration Tutorial</h1>
      <button onClick={connectWallet} style={{ padding: '10px', marginBottom: '20px' }}>
        Connect Wallet
      </button>
      {account && (
        <div>
          <h2>Connected Account: {account}</h2>
          <h3>Balance: {balance} ETH</h3>
        </div>
      )}
    </div>
  );
};

// Export the App component
export default App;
```
