"""
Generated Code Metadata:
========================
Original URL: https://diamond-7n0.pages.dev
Prompt: Develop a front-end application using React.js that integrates with the Diamond Coin smart contract to allow users to stake tokens, view their rewards, and swap cryptocurrencies.
Generated: DETERMINISTIC_304a14fe57e67caa
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// src/App.js
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import DiamondCoinABI from './abis/DiamondCoin.json';
import StakingABI from './abis/Staking.json';
import SwapABI from './abis/Swap.json';
import './App.css';

const App = () => {
  const [provider, setProvider] = useState(null);
  const [account, setAccount] = useState('');
  const [diamondCoinContract, setDiamondCoinContract] = useState(null);
  const [stakingContract, setStakingContract] = useState(null);
  const [swapContract, setSwapContract] = useState(null);
  const [balance, setBalance] = useState('0');
  const [stakedAmount, setStakedAmount] = useState('0');
  const [rewards, setRewards] = useState('0');
  const [stakeAmount, setStakeAmount] = useState('');
  const [unstakeAmount, setUnstakeAmount] = useState('');
  const [swapFromAmount, setSwapFromAmount] = useState('');
  const [swapToToken, setSwapToToken] = useState('ETH');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');

  // Contract addresses (replace with actual addresses)
  const DIAMOND_COIN_ADDRESS = '0x...';
  const STAKING_ADDRESS = '0x...';
  const SWAP_ADDRESS = '0x...';

  // Initialize provider and contracts
  useEffect(() => {
    const init = async () => {
      try {
        if (window.ethereum) {
          const provider = new ethers.providers.Web3Provider(window.ethereum);
          setProvider(provider);

          const signer = provider.getSigner();
          const diamondCoinContract = new ethers.Contract(
            DIAMOND_COIN_ADDRESS,
            DiamondCoinABI,
            signer
          );
          const stakingContract = new ethers.Contract(
            STAKING_ADDRESS,
            StakingABI,
            signer
          );
          const swapContract = new ethers.Contract(
            SWAP_ADDRESS,
            SwapABI,
            signer
          );

          setDiamondCoinContract(diamondCoinContract);
          setStakingContract(stakingContract);
          setSwapContract(swapContract);

          window.ethereum.on('accountsChanged', (accounts) => {
            setAccount(accounts[0]);
            loadData(accounts[0]);
          });

          const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
          setAccount(accounts[0]);
          loadData(accounts[0]);
        } else {
          setError('Please install MetaMask to use this application');
        }
      } catch (err) {
        setError(err.message);
      }
    };

    init();
  }, []);

  // Load user data
  const loadData = async (account) => {
    try {
      setIsLoading(true);
      const balance = await diamondCoinContract.balanceOf(account);
      const staked = await stakingContract.stakedBalance(account);
      const rewards = await stakingContract.calculateRewards(account);

      setBalance(ethers.utils.formatEther(balance));
      setStakedAmount(ethers.utils.formatEther(staked));
      setRewards(ethers.utils.formatEther(rewards));
      setIsLoading(false);
    } catch (err) {
      setError(err.message);
      setIsLoading(false);
    }
  };

  // Stake tokens
  const handleStake = async () => {
    try {
      if (!stakeAmount || isNaN(stakeAmount)) {
        setError('Please enter a valid amount');
        return;
      }

      setIsLoading(true);
      const amount = ethers.utils.parseEther(stakeAmount);
      
      // Approve staking contract to spend tokens
      const approveTx = await diamondCoinContract.approve(STAKING_ADDRESS, amount);
      await approveTx.wait();

      // Stake tokens
      const stakeTx = await stakingContract.stake(amount);
      await stakeTx.wait();

      await loadData(account);
      setStakeAmount('');
      setIsLoading(false);
    } catch (err) {
      setError(err.message);
      setIsLoading(false);
    }
  };

  // Unstake tokens
  const handleUnstake = async () => {
    try {
      if (!unstakeAmount || isNaN(unstakeAmount)) {
        setError('Please enter a valid amount');
        return;
      }

      setIsLoading(true);
      const amount = ethers.utils.parseEther(unstakeAmount);
      const tx = await stakingContract.unstake(amount);
      await tx.wait();

      await loadData(account);
      setUnstakeAmount('');
      setIsLoading(false);
    } catch (err) {
      setError(err.message);
      setIsLoading(false);
    }
  };

  // Claim rewards
  const handleClaimRewards = async () => {
    try {
      setIsLoading(true);
      const tx = await stakingContract.claimRewards();
      await tx.wait();

      await loadData(account);
      setIsLoading(false);
    } catch (err) {
      setError(err.message);
      setIsLoading(false);
    }
  };

  // Swap tokens
  const handleSwap = async () => {
    try {
      if (!swapFromAmount || isNaN(swapFromAmount)) {
        setError('Please enter a valid amount');
        return;
      }

      setIsLoading(true);
      const amount = ethers.utils.parseEther(swapFromAmount);
      
      if (swapToToken === 'ETH') {
        // Swap Diamond Coin to ETH
        const tx = await swapContract.swapToETH(amount);
        await tx.wait();
      } else {
        // Swap ETH to Diamond Coin
        const tx = await swapContract.swapFromETH({
          value: amount
        });
        await tx.wait();
      }

      await loadData(account);
      setSwapFromAmount('');
      setIsLoading(false);
    } catch (err) {
      setError(err.message);
      setIsLoading(false);
    }
  };

  return (
    <div className="app">
      <header className="header">
        <h1>Diamond Coin Staking & Swap</h1>
        {account && <p>Connected: {account.substring(0, 6)}...{account.substring(38)}</p>}
      </header>

      {error && <div className="error">{error}</div>}

      <div className="dashboard">
        <div className="card">
          <h2>Wallet Balance</h2>
          <p>{balance} DMD</p>
        </div>

        <div className="card">
          <h2>Staked Amount</h2>
          <p>{stakedAmount} DMD</p>
        </div>

        <div className="card">
          <h2>Rewards</h2>
          <p>{rewards} DMD</p>
          <button onClick={handleClaimRewards} disabled={isLoading || rewards === '0.0'}>
            {isLoading ? 'Processing...' : 'Claim Rewards'}
          </button>
        </div>
      </div>

      <div className="actions">
        <div className="action-card">
          <h2>Stake Tokens</h2>
          <input
            type="text"
            value={stakeAmount}
            onChange={(e) => setStakeAmount(e.target.value)}
            placeholder="Amount to stake"
          />
          <button onClick={handleStake} disabled={isLoading}>
            {isLoading ? 'Processing...' : 'Stake'}
          </button>
        </div>

        <div className="action-card">
          <h2>Unstake Tokens</h2>
          <input
            type="text"
            value={unstakeAmount}
            onChange={(e) => setUnstakeAmount(e.target.value)}
            placeholder="Amount to unstake"
          />
          <button onClick={handleUnstake} disabled={isLoading}>
            {isLoading ? 'Processing...' : 'Unstake'}
          </button>
        </div>

        <div className="action-card">
          <h2>Swap Tokens</h2>
          <input
            type="text"
            value={swapFromAmount}
            onChange={(e) => setSwapFromAmount(e.target.value)}
            placeholder="Amount"
          />
          <select value={swapToToken} onChange={(e) => setSwapToToken(e.target.value)}>
            <option value="ETH">DMD to ETH</option>
            <option value="DMD">ETH to DMD</option>
          </select>
          <button onClick={handleSwap} disabled={isLoading}>
            {isLoading ? 'Processing...' : 'Swap'}
          </button>
        </div>
      </div>
    </div>
  );
};

export default App;
```

```javascript
// src/abis/DiamondCoin.json
{
  "abi": [
    {
      "inputs": [],
      "stateMutability": "nonpayable",
      "type": "constructor"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internal
