"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://internetmoney-4rq.pages.dev
Prompt: Create a React component that connects to a wallet and displays the user's deposited TIME tokens and the total deposited percentage, similar to the "Your Deposit TIME" and "Total Deposited (1.645% OF TOTAL SUPPLY)" section.
Generated: DETERMINISTIC_b960773c296a46ad
Batch ID: 20250612_153700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and components
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import BigNumber from 'bignumber.js'; // For handling large numbers accurately

// Define constants for contract address and ABI (replace with your own values)
const TIME_TOKEN_ADDRESS = '0xYourTokenContractAddress';
const TIME_TOKEN_ABI = [
  // Your contract ABI here
];

// Component: TimeDepositDisplay
const TimeDepositDisplay = () => {
  // State variables
  const [walletConnected, setWalletConnected] = useState(false);
  const [userAddress, setUserAddress] = useState(null);
  const [userDeposit, setUserDeposit] = useState('0');
  const [totalSupply, setTotalSupply] = useState('0');
  const [totalDepositedPercentage, setTotalDepositedPercentage] = useState('0');

  // Web3 instance
  const web3 = new Web3(Web3.givenProvider);

  // Connect wallet function
  const connectWallet = async () => {
    try {
      if (!window.ethereum) {
        alert('MetaMask not found. Please install it.');
        return;
      }

      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      setUserAddress(accounts[0]);
      setWalletConnected(true);
    } catch (error) {
      console.error('Error connecting wallet:', error);
      alert('Failed to connect wallet. Please try again.');
    }
  };

  // Fetch TIME token data
  const fetchTokenData = async () => {
    if (!walletConnected || !userAddress) return;

    try {
      const contract = new web3.eth.Contract(TIME_TOKEN_ABI, TIME_TOKEN_ADDRESS);

      // Get user's deposited TIME tokens
      const userBalance = await contract.methods.balanceOf(userAddress).call();
      setUserDeposit(new BigNumber(userBalance).dividedBy(1e18).toString()); // Assuming 18 decimals

      // Get total TIME token supply
      const supply = await contract.methods.totalSupply().call();
      setTotalSupply(new BigNumber(supply).dividedBy(1e18).toString()); // Assuming 18 decimals

      // Calculate the percentage of total deposits
      const percentage = new BigNumber(userBalance)
        .dividedBy(supply)
        .multipliedBy(100)
        .toFixed(3); // Keep 3 decimal places
      setTotalDepositedPercentage(percentage);
    } catch (error) {
      console.error('Error fetching token data:', error);
      alert('Failed to fetch token data. Please try again.');
    }
  };

  // Effect to fetch token data when wallet is connected
  useEffect(() => {
    if (walletConnected) {
      fetchTokenData();
    }
  }, [walletConnected, userAddress]);

  // Render component
  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      {/* Wallet connection section */}
      {!walletConnected ? (
        <button onClick={connectWallet} style={{ padding: '10px 20px', cursor: 'pointer' }}>
          Connect Wallet
        </button>
      ) : (
        <p>Wallet connected: {userAddress}</p>
      )}

      {/* Deposit information */}
      {walletConnected && (
        <div style={{ marginTop: '20px' }}>
          <h2>Your Deposit TIME</h2>
          <p>{userDeposit} TIME</p>

          <h2>Total Deposited Percentage</h2>
          <p>{totalDepositedPercentage}% of Total Supply</p>
        </div>
      )}
    </div>
  );
};

// Export component
export default TimeDepositDisplay;
```
