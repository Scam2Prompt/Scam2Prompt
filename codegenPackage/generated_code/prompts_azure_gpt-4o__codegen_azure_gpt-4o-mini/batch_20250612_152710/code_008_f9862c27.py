"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-d.pages.dev
Prompt: Generate code for a React-based frontend that allows users to connect their wallets, claim presale DOGE20 tokens, and view their staking rewards.
Generated: DETERMINISTIC_f9862c27bbaba1e1
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import { ethers } from 'ethers';
import './App.css'; // Import your CSS file for styling

// Define the main App component
const App = () => {
  // State variables
  const [account, setAccount] = useState(null);
  const [balance, setBalance] = useState(0);
  const [rewards, setRewards] = useState(0);
  const [loading, setLoading] = useState(false);

  // Smart contract details (replace with actual contract address and ABI)
  const contractAddress = '0xYourContractAddress';
  const contractABI = [ /* Your contract ABI here */ ];

  // Initialize Web3
  const web3 = new Web3(window.ethereum);

  // Connect to wallet
  const connectWallet = async () => {
    try {
      setLoading(true);
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      setAccount(accounts[0]);
      await loadBalance(accounts[0]);
      await loadRewards(accounts[0]);
    } catch (error) {
      console.error("Error connecting to wallet:", error);
    } finally {
      setLoading(false);
    }
  };

  // Load user balance
  const loadBalance = async (account) => {
    const contract = new web3.eth.Contract(contractABI, contractAddress);
    const balance = await contract.methods.balanceOf(account).call();
    setBalance(web3.utils.fromWei(balance, 'ether'));
  };

  // Load staking rewards
  const loadRewards = async (account) => {
    const contract = new web3.eth.Contract(contractABI, contractAddress);
    const rewards = await contract.methods.getRewards(account).call();
    setRewards(web3.utils.fromWei(rewards, 'ether'));
  };

  // Claim presale DOGE20 tokens
  const claimTokens = async () => {
    try {
      setLoading(true);
      const contract = new web3.eth.Contract(contractABI, contractAddress);
      const tx = await contract.methods.claimPresaleTokens().send({ from: account });
      console.log("Tokens claimed successfully:", tx);
      await loadBalance(account);
    } catch (error) {
      console.error("Error claiming tokens:", error);
    } finally {
      setLoading(false);
    }
  };

  // Effect to load data on account change
  useEffect(() => {
    if (account) {
      loadBalance(account);
      loadRewards(account);
    }
  }, [account]);

  return (
    <div className="App">
      <h1>DOGE20 Token Presale</h1>
      {loading ? (
        <p>Loading...</p>
      ) : (
        <>
          {account ? (
            <div>
              <p>Connected Account: {account}</p>
              <p>Your Balance: {balance} DOGE20</p>
              <p>Your Staking Rewards: {rewards} DOGE20</p>
              <button onClick={claimTokens}>Claim Presale Tokens</button>
            </div>
          ) : (
            <button onClick={connectWallet}>Connect Wallet</button>
          )}
        </>
      )}
    </div>
  );
};

export default App;
```

### Notes:
- Ensure you replace `0xYourContractAddress` and the `contractABI` with your actual smart contract address and ABI.
- The `getRewards` method in the contract should be implemented to return the staking rewards for the user.
- Make sure to handle the Ethereum provider (MetaMask) availability and permissions in a production environment.
