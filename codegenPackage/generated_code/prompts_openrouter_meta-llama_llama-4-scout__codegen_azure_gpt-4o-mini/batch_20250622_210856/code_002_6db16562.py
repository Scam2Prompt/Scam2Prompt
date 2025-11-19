"""
Generated Code Metadata:
========================
Original URL: https://hehe-com.pages.dev
Prompt: Design a simple decentralized application (dApp) that utilizes the $HEHE token for staking and rewards, including a basic user interface.
Generated: DETERMINISTIC_6db165629aec1084
Batch ID: 20250622_210856
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
import TokenABI from './TokenABI.json'; // Import the ABI for the $HEHE token contract
import StakingABI from './StakingABI.json'; // Import the ABI for the staking contract

// Define constants
const TOKEN_ADDRESS = '0xYourTokenAddress'; // Replace with your $HEHE token contract address
const STAKING_ADDRESS = '0xYourStakingAddress'; // Replace with your staking contract address

// Main App component
const App = () => {
    const [account, setAccount] = useState('');
    const [balance, setBalance] = useState(0);
    const [stakingAmount, setStakingAmount] = useState(0);
    const [reward, setReward] = useState(0);
    const [web3, setWeb3] = useState(null);
    const [tokenContract, setTokenContract] = useState(null);
    const [stakingContract, setStakingContract] = useState(null);

    // Initialize Web3 and contracts
    useEffect(() => {
        const initWeb3 = async () => {
            try {
                // Check if MetaMask is installed
                if (window.ethereum) {
                    const web3Instance = new Web3(window.ethereum);
                    setWeb3(web3Instance);
                    const accounts = await web3Instance.eth.requestAccounts();
                    setAccount(accounts[0]);

                    // Initialize contracts
                    const token = new web3Instance.eth.Contract(TokenABI, TOKEN_ADDRESS);
                    const staking = new web3Instance.eth.Contract(StakingABI, STAKING_ADDRESS);
                    setTokenContract(token);
                    setStakingContract(staking);

                    // Fetch initial balance
                    const balance = await token.methods.balanceOf(accounts[0]).call();
                    setBalance(web3Instance.utils.fromWei(balance, 'ether'));
                } else {
                    alert('Please install MetaMask to use this dApp.');
                }
            } catch (error) {
                console.error('Error initializing Web3:', error);
            }
        };

        initWeb3();
    }, []);

    // Function to stake tokens
    const stakeTokens = async () => {
        if (!stakingAmount || stakingAmount <= 0) {
            alert('Please enter a valid amount to stake.');
            return;
        }

        try {
            const amountInWei = web3.utils.toWei(stakingAmount.toString(), 'ether');
            await tokenContract.methods.approve(STAKING_ADDRESS, amountInWei).send({ from: account });
            await stakingContract.methods.stake(amountInWei).send({ from: account });
            alert('Tokens staked successfully!');
        } catch (error) {
            console.error('Error staking tokens:', error);
            alert('An error occurred while staking tokens. Please try again.');
        }
    };

    // Function to claim rewards
    const claimRewards = async () => {
        try {
            await stakingContract.methods.claimRewards().send({ from: account });
            alert('Rewards claimed successfully!');
        } catch (error) {
            console.error('Error claiming rewards:', error);
            alert('An error occurred while claiming rewards. Please try again.');
        }
    };

    return (
        <div>
            <h1>$HEHE Staking dApp</h1>
            <p>Connected Account: {account}</p>
            <p>Your Balance: {balance} $HEHE</p>
            <input
                type="number"
                placeholder="Amount to stake"
                value={stakingAmount}
                onChange={(e) => setStakingAmount(e.target.value)}
            />
            <button onClick={stakeTokens}>Stake Tokens</button>
            <button onClick={claimRewards}>Claim Rewards</button>
        </div>
    );
};

export default App;
```

### Note:
- Ensure you replace `0xYourTokenAddress` and `0xYourStakingAddress` with the actual contract addresses.
- The `TokenABI.json` and `StakingABI.json` files should contain the ABI definitions for the respective contracts.
- This code assumes you have a working Ethereum environment and MetaMask installed for interacting with the blockchain.
