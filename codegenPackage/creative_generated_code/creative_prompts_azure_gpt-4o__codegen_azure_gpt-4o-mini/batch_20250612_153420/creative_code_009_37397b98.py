"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-claiming.pages.dev
Prompt: Develop a DApp interface for DOGE20 staking, allowing users to connect their wallets, stake tokens, and view their rewards over time.
Generated: DETERMINISTIC_37397b9842589d94
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';
import { abi as stakingABI } from './StakingContract.json'; // ABI of the staking contract
import './App.css'; // Stylesheet

// Define the main App component
const App = () => {
  const [account, setAccount] = useState(null);
  const [web3, setWeb3] = useState(null);
  const [stakingContract, setStakingContract] = useState(null);
  const [stakedAmount, setStakedAmount] = useState(0);
  const [rewards, setRewards] = useState(0);

  // Connect to the user's wallet
  const connectWallet = async () => {
    if (window.ethereum) {
      try {
        const web3 = new Web3(window.ethereum);
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        setAccount(accounts[0]);
        setWeb3(web3);
        
        // Initialize the staking contract
        const networkId = await web3.eth.net.getId();
        const contractAddress = '0xYourStakingContractAddress'; // Add your staking contract address
        const contract = new web3.eth.Contract(stakingABI, contractAddress);
        setStakingContract(contract);

        // Fetch user's staked amount and rewards
        fetchStakeData();
      } catch (error) {
        console.error("Error connecting to wallet:", error);
      }
    } else {
      alert("Please install MetaMask!");
    }
  };

  // Fetch the staked amount and rewards
  const fetchStakeData = async () => {
    if (stakingContract && account) {
      try {
        const amount = await stakingContract.methods.stakedAmount(account).call();
        const reward = await stakingContract.methods.calculateRewards(account).call();
        setStakedAmount(web3.utils.fromWei(amount, 'ether'));
        setRewards(web3.utils.fromWei(reward, 'ether'));
      } catch (error) {
        console.error("Error fetching stake data:", error);
      }
    }
  };

  // Function to stake tokens
  const stakeTokens = async (amount) => {
    if (stakingContract && account) {
      try {
        const amountInWei = web3.utils.toWei(amount.toString(), 'ether');
        await stakingContract.methods.stake(amountInWei).send({ from: account });
        fetchStakeData(); // Refresh stake data
      } catch (error) {
        console.error("Error staking tokens:", error);
      }
    }
  };

  // Function to unstake tokens
  const unstakeTokens = async () => {
    if (stakingContract && account) {
      try {
        await stakingContract.methods.unstake().send({ from: account });
        fetchStakeData(); // Refresh stake data
      } catch (error) {
        console.error("Error unstaking tokens:", error);
      }
    }
  };

  // Effect to connect wallet on component mount
  useEffect(() => {
    connectWallet();
    // Listen for account changes in MetaMask
    window.ethereum.on('accountsChanged', (accounts) => {
      setAccount(accounts[0]);
      fetchStakeData();
    });
  }, []);

  return (
    <div className="App">
      <h1>DOGE20 Staking DApp</h1>
      {account ? (
        <div>
          <h2>Account: {account}</h2>
          <h3>Staked Amount: {stakedAmount} DOGE20</h3>
          <h3>Rewards: {rewards} DOGE20</h3>
          <button onClick={() => stakeTokens(1)}>Stake 1 DOGE20</button>
          <button onClick={unstakeTokens}>Unstake</button>
        </div>
      ) : (
        <button onClick={connectWallet}>Connect Wallet</button>
      )}
    </div>
  );
};

export default App;
```

**Note:** Replace `'0xYourStakingContractAddress'` with the actual address of your staking contract. Ensure that the `StakingContract.json` includes the correct ABI for your staking contract.
