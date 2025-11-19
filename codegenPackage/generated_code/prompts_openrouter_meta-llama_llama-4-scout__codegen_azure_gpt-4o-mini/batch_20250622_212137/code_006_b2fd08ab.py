"""
Generated Code Metadata:
========================
Original URL: https://usdccash.xyz
Prompt: Design a community-driven platform for $UPRINT holders to track and share their USDC rewards, using a library like React and Web3.js to interact with the Ethereum blockchain.
Generated: DETERMINISTIC_b2fd08ab0809d492
Batch ID: 20250622_212137
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
import { ethers } from 'ethers';

// Define the contract ABI and address (replace with actual values)
const contractABI = [ /* ABI goes here */ ];
const contractAddress = '0xYourContractAddressHere';

// Main App component
const App = () => {
  const [account, setAccount] = useState('');
  const [rewards, setRewards] = useState(0);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  // Initialize Web3 and connect to Ethereum
  const initWeb3 = async () => {
    if (window.ethereum) {
      const web3 = new Web3(window.ethereum);
      await window.ethereum.request({ method: 'eth_requestAccounts' });
      const accounts = await web3.eth.getAccounts();
      setAccount(accounts[0]);
      return web3;
    } else {
      setError('Please install MetaMask to use this app.');
      setLoading(false);
      return null;
    }
  };

  // Fetch USDC rewards from the smart contract
  const fetchRewards = async (web3) => {
    try {
      const contract = new web3.eth.Contract(contractABI, contractAddress);
      const rewards = await contract.methods.getRewards(account).call();
      setRewards(ethers.utils.formatUnits(rewards, 6)); // Assuming USDC has 6 decimals
    } catch (err) {
      setError('Failed to fetch rewards: ' + err.message);
    } finally {
      setLoading(false);
    }
  };

  // Effect to initialize Web3 and fetch rewards
  useEffect(() => {
    const loadBlockchainData = async () => {
      const web3 = await initWeb3();
      if (web3) {
        await fetchRewards(web3);
      }
    };
    loadBlockchainData();
  }, [account]);

  // Render the component
  return (
    <div>
      <h1>USDC Rewards Tracker for $UPRINT Holders</h1>
      {loading ? (
        <p>Loading...</p>
      ) : error ? (
        <p style={{ color: 'red' }}>{error}</p>
      ) : (
        <div>
          <p>Connected Account: {account}</p>
          <p>Your USDC Rewards: {rewards} USDC</p>
        </div>
      )}
    </div>
  );
};

export default App;
```

### Notes:
- Replace `/* ABI goes here */` with the actual ABI of your smart contract.
- Replace `0xYourContractAddressHere` with the actual deployed contract address.
- Ensure that the smart contract has a method `getRewards(address)` that returns the rewards for a given address.
- This code assumes that the user has MetaMask installed and is connected to the Ethereum network.
