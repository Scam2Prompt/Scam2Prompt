"""
Generated Code Metadata:
========================
Original URL: https://theoldcastle.pages.dev
Prompt: Create a React component for a DApp that allows users to log in, connect their wallet, and view their staking assets, unclaimed rewards, and $FOMO balance, as described on TOCD's interface.
Generated: DETERMINISTIC_ca447f6072c677d9
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import './App.css';

// Contract ABIs and addresses (replace with actual values)
const STAKING_CONTRACT_ABI = []; // Replace with actual ABI
const TOKEN_CONTRACT_ABI = []; // Replace with actual ABI
const STAKING_CONTRACT_ADDRESS = '0x...'; // Replace with actual address
const TOKEN_CONTRACT_ADDRESS = '0x...'; // Replace with actual address

const App = () => {
  const [provider, setProvider] = useState(null);
  const [signer, setSigner] = useState(null);
  const [account, setAccount] = useState('');
  const [isConnected, setIsConnected] = useState(false);
  const [stakingContract, setStakingContract] = useState(null);
  const [tokenContract, setTokenContract] = useState(null);
  const [stakingBalance, setStakingBalance] = useState('0');
  const [unclaimedRewards, setUnclaimedRewards] = useState('0');
  const [fomoBalance, setFomoBalance] = useState('0');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  // Initialize provider when component mounts
  useEffect(() => {
    if (window.ethereum) {
      const web3Provider = new ethers.providers.Web3Provider(window.ethereum);
      setProvider(web3Provider);
    } else {
      setError('Please install MetaMask or another Web3 provider');
    }
  }, []);

  // Connect wallet handler
  const connectWallet = async () => {
    try {
      setLoading(true);
      setError('');
      
      if (!provider) {
        throw new Error('Web3 provider not initialized');
      }

      // Request account access
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      if (accounts.length === 0) {
        throw new Error('No accounts found');
      }

      const signer = provider.getSigner();
      setSigner(signer);
      setAccount(accounts[0]);
      setIsConnected(true);

      // Initialize contracts
      const stakingContract = new ethers.Contract(
        STAKING_CONTRACT_ADDRESS,
        STAKING_CONTRACT_ABI,
        signer
      );
      const tokenContract = new ethers.Contract(
        TOKEN_CONTRACT_ADDRESS,
        TOKEN_CONTRACT_ABI,
        signer
      );
      setStakingContract(stakingContract);
      setTokenContract(tokenContract);

      // Load initial data
      await loadWalletData();
    } catch (err) {
      setError(err.message || 'Failed to connect wallet');
    } finally {
      setLoading(false);
    }
  };

  // Load wallet data
  const loadWalletData = async () => {
    try {
      if (!stakingContract || !tokenContract || !account) return;

      setLoading(true);
      setError('');

      // Fetch staking balance
      const staked = await stakingContract.balanceOf(account);
      setStakingBalance(ethers.utils.formatUnits(staked, 18));

      // Fetch unclaimed rewards
      const rewards = await stakingContract.earned(account);
      setUnclaimedRewards(ethers.utils.formatUnits(rewards, 18));

      // Fetch FOMO balance
      const balance = await tokenContract.balanceOf(account);
      setFomoBalance(ethers.utils.formatUnits(balance, 18));
    } catch (err) {
      setError(err.message || 'Failed to load wallet data');
    } finally {
      setLoading(false);
    }
  };

  // Claim rewards handler
  const claimRewards = async () => {
    try {
      if (!stakingContract) return;

      setLoading(true);
      setError('');

      const tx = await stakingContract.getReward();
      await tx.wait();

      // Refresh data after claiming
      await loadWalletData();
    } catch (err) {
      setError(err.message || 'Failed to claim rewards');
    } finally {
      setLoading(false);
    }
  };

  // Listen for account changes
  useEffect(() => {
    if (window.ethereum) {
      const handleAccountsChanged = (accounts) => {
        if (accounts.length === 0) {
          // MetaMask is locked or user disconnected all accounts
          setIsConnected(false);
          setAccount('');
        } else {
          setAccount(accounts[0]);
          loadWalletData();
        }
      };

      window.ethereum.on('accountsChanged', handleAccountsChanged);

      return () => {
        window.ethereum.removeListener('accountsChanged', handleAccountsChanged);
      };
    }
  }, [stakingContract, tokenContract]);

  return (
    <div className="app">
      <header className="header">
        <h1>TOCD Staking Dashboard</h1>
        {!isConnected ? (
          <button 
            onClick={connectWallet} 
            disabled={loading || !provider}
            className="connect-button"
          >
            {loading ? 'Connecting...' : 'Connect Wallet'}
          </button>
        ) : (
          <div className="wallet-info">
            <span className="wallet-address">
              {`${account.substring(0, 6)}...${account.substring(account.length - 4)}`}
            </span>
          </div>
        )}
      </header>

      {error && <div className="error-message">{error}</div>}

      <main className="dashboard">
        {isConnected ? (
          <>
            <div className="card">
              <h2>Your Staking Assets</h2>
              <div className="balance">{stakingBalance} $FOMO</div>
            </div>

            <div className="card">
              <h2>Unclaimed Rewards</h2>
              <div className="balance">{unclaimedRewards} $FOMO</div>
              <button 
                onClick={claimRewards} 
                disabled={loading || parseFloat(unclaimedRewards) <= 0}
                className="action-button"
              >
                {loading ? 'Processing...' : 'Claim Rewards'}
              </button>
            </div>

            <div className="card">
              <h2>Wallet Balance</h2>
              <div className="balance">{fomoBalance} $FOMO</div>
            </div>
          </>
        ) : (
          <div className="welcome-message">
            <h2>Welcome to TOCD Staking</h2>
            <p>Connect your wallet to view your staking assets and rewards</p>
          </div>
        )}
      </main>
    </div>
  );
};

export default App;
```
