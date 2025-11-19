"""
Generated Code Metadata:
========================
Original URL: https://tenderize.xyz
Prompt: Develop a frontend interface using React.js that allows users to stake tokens, view their tenderized token balances, and track accrued rewards, similar to Tenderize's user-friendly interface.
Generated: DETERMINISTIC_70ddb073959f918a
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import './App.css';

// Mock contract ABI and addresses (replace with actual in production)
const stakingContractABI = [
  // ... your contract ABI here ...
];
const stakingContractAddress = '0x...';
const tokenContractABI = [
  // ... your token contract ABI here ...
];
const tokenContractAddress = '0x...';

function App() {
  const [account, setAccount] = useState('');
  const [isConnected, setIsConnected] = useState(false);
  const [stakingBalance, setStakingBalance] = useState('0');
  const [tenderizedBalance, setTenderizedBalance] = useState('0');
  const [rewards, setRewards] = useState('0');
  const [stakeAmount, setStakeAmount] = useState('');
  const [unstakeAmount, setUnstakeAmount] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');

  // Initialize provider and contracts
  let provider;
  let stakingContract;
  let tokenContract;

  if (window.ethereum) {
    provider = new ethers.providers.Web3Provider(window.ethereum);
    stakingContract = new ethers.Contract(
      stakingContractAddress,
      stakingContractABI,
      provider.getSigner()
    );
    tokenContract = new ethers.Contract(
      tokenContractAddress,
      tokenContractABI,
      provider.getSigner()
    );
  }

  // Connect wallet
  const connectWallet = async () => {
    try {
      if (!window.ethereum) {
        throw new Error('Please install MetaMask!');
      }

      const accounts = await window.ethereum.request({
        method: 'eth_requestAccounts',
      });
      setAccount(accounts[0]);
      setIsConnected(true);
      fetchBalances();
    } catch (err) {
      setError(err.message);
    }
  };

  // Fetch user balances
  const fetchBalances = async () => {
    if (!isConnected || !stakingContract || !tokenContract) return;

    try {
      setIsLoading(true);
      const stakingBal = await stakingContract.balanceOf(account);
      const tenderizedBal = await stakingContract.tokensOf(account);
      const rewardBal = await stakingContract.earned(account);

      setStakingBalance(ethers.utils.formatUnits(stakingBal, 18));
      setTenderizedBalance(ethers.utils.formatUnits(tenderizedBal, 18));
      setRewards(ethers.utils.formatUnits(rewardBal, 18));
    } catch (err) {
      setError('Failed to fetch balances');
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  // Stake tokens
  const stakeTokens = async () => {
    if (!stakeAmount || !isConnected) return;

    try {
      setIsLoading(true);
      setError('');
      const amount = ethers.utils.parseUnits(stakeAmount, 18);
      
      // Approve token transfer
      const approveTx = await tokenContract.approve(
        stakingContractAddress,
        amount
      );
      await approveTx.wait();

      // Stake tokens
      const stakeTx = await stakingContract.stake(amount);
      await stakeTx.wait();

      // Refresh balances
      await fetchBalances();
      setStakeAmount('');
    } catch (err) {
      setError('Staking failed');
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  // Unstake tokens
  const unstakeTokens = async () => {
    if (!unstakeAmount || !isConnected) return;

    try {
      setIsLoading(true);
      setError('');
      const amount = ethers.utils.parseUnits(unstakeAmount, 18);
      
      const tx = await stakingContract.withdraw(amount);
      await tx.wait();

      // Refresh balances
      await fetchBalances();
      setUnstakeAmount('');
    } catch (err) {
      setError('Unstaking failed');
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  // Claim rewards
  const claimRewards = async () => {
    if (!isConnected) return;

    try {
      setIsLoading(true);
      setError('');
      
      const tx = await stakingContract.getReward();
      await tx.wait();

      // Refresh balances
      await fetchBalances();
    } catch (err) {
      setError('Claiming rewards failed');
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  // Listen for account changes
  useEffect(() => {
    if (window.ethereum) {
      window.ethereum.on('accountsChanged', (accounts) => {
        if (accounts.length > 0) {
          setAccount(accounts[0]);
          fetchBalances();
        } else {
          setIsConnected(false);
          setAccount('');
        }
      });
    }

    return () => {
      if (window.ethereum) {
        window.ethereum.removeListener('accountsChanged');
      }
    };
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Tenderize Staking Interface</h1>
        
        {!isConnected ? (
          <button onClick={connectWallet} className="connect-button">
            Connect Wallet
          </button>
        ) : (
          <div className="wallet-info">
            <p>Connected: {account.substring(0, 6)}...{account.substring(account.length - 4)}</p>
          </div>
        )}
      </header>

      <main className="staking-container">
        {error && <div className="error-message">{error}</div>}

        <div className="balance-cards">
          <div className="balance-card">
            <h3>Staked Balance</h3>
            <p>{isLoading ? 'Loading...' : stakingBalance}</p>
          </div>
          <div className="balance-card">
            <h3>Tenderized Tokens</h3>
            <p>{isLoading ? 'Loading...' : tenderizedBalance}</p>
          </div>
          <div className="balance-card">
            <h3>Accrued Rewards</h3>
            <p>{isLoading ? 'Loading...' : rewards}</p>
          </div>
        </div>

        <div className="action-section">
          <div className="stake-form">
            <h2>Stake Tokens</h2>
            <input
              type="number"
              value={stakeAmount}
              onChange={(e) => setStakeAmount(e.target.value)}
              placeholder="Amount to stake"
              disabled={!isConnected || isLoading}
            />
            <button
              onClick={stakeTokens}
              disabled={!isConnected || isLoading || !stakeAmount}
            >
              {isLoading ? 'Processing...' : 'Stake'}
            </button>
          </div>

          <div className="unstake-form">
            <h2>Unstake Tokens</h2>
            <input
              type="number"
              value={unstakeAmount}
              onChange={(e) => setUnstakeAmount(e.target.value)}
              placeholder="Amount to unstake"
              disabled={!isConnected || isLoading}
            />
            <button
              onClick={unstakeTokens}
              disabled={!isConnected || isLoading || !unstakeAmount}
            >
              {isLoading ? 'Processing...' : 'Unstake'}
            </button>
          </div>
        </div>

        <div className="rewards-section">
          <button
            onClick={claimRewards}
            disabled={!isConnected || isLoading || parseFloat(rewards) <= 0}
            className="claim-button"
          >
            {isLoading ? 'Processing...' : 'Claim Rewards'}
          </button>
        </div>
      </main>
    </div>
  );
}

export default App;
```

```css
/* App.css */
.App {
  text-align: center;
  min-height: 100vh;
  background-color: #f5f5f5;
  color: #333;
  font-family: 'Arial', sans-serif;
}

.App-header {
  background-color: #282c34;
  padding: 2rem;
  color: white;
}

.connect-button {
  background-color: #61dafb;
  border: none;
  padding: 0.8rem 1.5rem;
  font-size: 1rem;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.connect-button:hover {
  background-color: #4fa8d3;
}

.wallet-info {
  margin-top: 1rem;
  font-size: 0.9rem;
}

.staking-container {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 0 1rem;
}

.balance-cards {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  gap: 1rem;
  margin-bottom: 2rem;
}

.balance-card {
  background: white;
