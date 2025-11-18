"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blocksdag-networks.pages.dev
Prompt: Develop a web application that allows users to connect their wallets, purchase BDAG coins, and track their referral earnings, following the workflow outlined on the BlockDAG website.
Generated: DETERMINISTIC_bc0b4bd9f55599f3
Batch ID: 20250612_150946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing required libraries
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import './App.css';

// Constants for contract configuration
const CONTRACT_ADDRESS = 'YOUR_CONTRACT_ADDRESS';
const ABI = [ /* Your Contract ABI */ ];

// App Component
const App = () => {
  const [account, setAccount] = useState('');
  const [balance, setBalance] = useState(0);
  const [referralEarnings, setReferralEarnings] = useState(0);
  const [web3, setWeb3] = useState(null);
  const [contract, setContract] = useState(null);

  // Initialize Web3 and Contract
  useEffect(() => {
    const initWeb3 = async () => {
      try {
        // Check for Ethereum provider
        if (window.ethereum) {
          const web3Instance = new Web3(window.ethereum);
          await window.ethereum.request({ method: 'eth_requestAccounts' });
          const accounts = await web3Instance.eth.getAccounts();
          const userAccount = accounts[0];

          // Set account and web3 instance
          setAccount(userAccount);
          setWeb3(web3Instance);
          const contractInstance = new web3Instance.eth.Contract(ABI, CONTRACT_ADDRESS);
          setContract(contractInstance);

          // Fetch initial balance and referral earnings
          fetchBalance(userAccount);
          fetchReferralEarnings(userAccount);
        } else {
          alert('Please install MetaMask to use this app.');
        }
      } catch (error) {
        console.error('Error initializing web3:', error);
      }
    };
    initWeb3();
  }, []);

  // Fetch user's BDAG coin balance
  const fetchBalance = async (account) => {
    try {
      const balance = await contract.methods.balanceOf(account).call();
      setBalance(web3.utils.fromWei(balance, 'ether')); // Assuming 18 decimals
    } catch (error) {
      console.error('Error fetching balance:', error);
    }
  };

  // Fetch user's referral earnings
  const fetchReferralEarnings = async (account) => {
    try {
      const earnings = await contract.methods.getReferralEarnings(account).call();
      setReferralEarnings(web3.utils.fromWei(earnings, 'ether'));
    } catch (error) {
      console.error('Error fetching referral earnings:', error);
    }
  };

  // Purchase BDAG Coins
  const purchaseBDAG = async (amount) => {
    try {
      const value = web3.utils.toWei(amount.toString(), 'ether');
      await contract.methods.purchase().send({
        from: account,
        value: value,
      });
      fetchBalance(account); // Refresh balance after purchase
    } catch (error) {
      console.error('Error purchasing BDAG:', error);
    }
  };

  return (
    <Router>
      <div className="App">
        <h1>BDAG Coin Purchase & Referral Tracker</h1>
        <p>Account: {account}</p>
        <p>BDAG Balance: {balance} BDAG</p>
        <p>Referral Earnings: {referralEarnings} ETH</p>
        <input type="number" placeholder="Amount to Purchase" id="amount" />
        <button onClick={() => purchaseBDAG(document.getElementById('amount').value)}>
          Purchase BDAG
        </button>
      </div>
    </Router>
  );
};

export default App;
```

Make sure to replace `YOUR_CONTRACT_ADDRESS` and `/* Your Contract ABI */` with the actual contract address and ABI for the BDAG coin contract before running the application.
