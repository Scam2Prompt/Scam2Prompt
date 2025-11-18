"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claims-wienerdogai.pages.dev
Prompt: Develop a decentralized application (dApp) interface for a token presale, including wallet connection, token purchase, staking functionality, and reward tracking, inspired by WienerAI's presale widget.
Generated: DETERMINISTIC_f9a3ebfd885ef4f7
Batch ID: 20250612_150715
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
import './App.css'; // Importing CSS for styling

// Contract ABI and Address (replace with actual values)
const TOKEN_CONTRACT_ABI = [...]; // Token contract ABI
const TOKEN_CONTRACT_ADDRESS = '0xYourTokenContractAddress';
const STAKING_CONTRACT_ABI = [...]; // Staking contract ABI
const STAKING_CONTRACT_ADDRESS = '0xYourStakingContractAddress';

// Main App Component
const App = () => {
    const [account, setAccount] = useState(null);
    const [web3, setWeb3] = useState(null);
    const [tokenContract, setTokenContract] = useState(null);
    const [stakingContract, setStakingContract] = useState(null);
    const [amount, setAmount] = useState('');
    const [stakedAmount, setStakedAmount] = useState(0);
    const [reward, setReward] = useState(0);

    // Initialize Web3 and connect to the user's wallet
    useEffect(() => {
        const initWeb3 = async () => {
            if (window.ethereum) {
                const web3Instance = new Web3(window.ethereum);
                setWeb3(web3Instance);

                try {
                    // Request wallet connection
                    await window.ethereum.request({ method: 'eth_requestAccounts' });
                    const accounts = await web3Instance.eth.getAccounts();
                    setAccount(accounts[0]);
                } catch (error) {
                    console.error('User rejected the request:', error);
                }
            } else {
                console.error('Ethereum wallet not found');
            }
        };

        initWeb3();
    }, []);

    // Set up contracts after wallet connection
    useEffect(() => {
        if (web3 && account) {
            const token = new web3.eth.Contract(TOKEN_CONTRACT_ABI, TOKEN_CONTRACT_ADDRESS);
            const staking = new web3.eth.Contract(STAKING_CONTRACT_ABI, STAKING_CONTRACT_ADDRESS);
            setTokenContract(token);
            setStakingContract(staking);
        }
    }, [web3, account]);

    // Function to handle token purchase
    const handlePurchase = async () => {
        if (!amount || isNaN(amount) || amount <= 0) {
            alert('Please enter a valid amount');
            return;
        }

        try {
            const value = web3.utils.toWei(amount, 'ether');
            await tokenContract.methods.buyTokens().send({ from: account, value });
            alert('Tokens purchased successfully!');
        } catch (error) {
            console.error('Token purchase error:', error);
            alert('Token purchase failed. Please try again.');
        }
    };

    // Function to stake tokens
    const handleStake = async () => {
        if (!stakedAmount || isNaN(stakedAmount) || stakedAmount <= 0) {
            alert('Please enter a valid amount to stake');
            return;
        }

        try {
            await tokenContract.methods.approve(STAKING_CONTRACT_ADDRESS, stakedAmount).send({ from: account });
            await stakingContract.methods.stake(stakedAmount).send({ from: account });
            alert('Tokens staked successfully!');
        } catch (error) {
            console.error('Staking error:', error);
            alert('Staking failed. Please try again.');
        }
    };

    // Function to retrieve rewards
    const fetchRewards = async () => {
        try {
            const rewardAmount = await stakingContract.methods.calculateRewards(account).call();
            setReward(web3.utils.fromWei(rewardAmount, 'ether'));
        } catch (error) {
            console.error('Fetch rewards error:', error);
            alert('Failed to fetch rewards. Please try again.');
        }
    };

    return (
        <div className="App">
            <h1>Token Presale DApp</h1>
            {account ? (
                <div>
                    <p>Connected Account: {account}</p>
                    <input
                        type="text"
                        placeholder="Amount of tokens to purchase"
                        value={amount}
                        onChange={(e) => setAmount(e.target.value)}
                    />
                    <button onClick={handlePurchase}>Purchase Tokens</button>
                    <br />
                    <input
                        type="text"
                        placeholder="Amount to stake"
                        value={stakedAmount}
                        onChange={(e) => setStakedAmount(e.target.value)}
                    />
                    <button onClick={handleStake}>Stake Tokens</button>
                    <br />
                    <button onClick={fetchRewards}>Fetch Rewards</button>
                    <p>Your Rewards: {reward} Tokens</p>
                </div>
            ) : (
                <p>Please connect your wallet.</p>
            )}
        </div>
    );
};

export default App;
```

**Notes:**
- Replace `TOKEN_CONTRACT_ABI` and `STAKING_CONTRACT_ABI` with the actual ABI JSON objects.
- Make sure to handle proper network configuration and any potential user experience improvements, such as loading states or notifications.
- Ensure the smart contracts are deployed and the addresses are correctly set before running the dApp.
