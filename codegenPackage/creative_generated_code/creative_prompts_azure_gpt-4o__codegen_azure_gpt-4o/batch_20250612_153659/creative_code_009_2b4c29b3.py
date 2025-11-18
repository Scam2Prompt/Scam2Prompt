"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assetdash-staking.vercel.app
Prompt: Generate a Next.js page that allows users to stake Vanta tokens and view their staking progress and rewards.
Generated: DETERMINISTIC_2b4c29b3e5e7a385
Batch ID: 20250612_153659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// pages/stake.js

import { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import styles from '../styles/Stake.module.css';

// Replace with your Vanta token and staking contract addresses
const TOKEN_ADDRESS = '0xYourTokenAddress';
const STAKING_CONTRACT_ADDRESS = '0xYourStakingContractAddress';

// Replace with your staking contract ABI
const STAKING_CONTRACT_ABI = [
  // Add your contract's ABI here
];

export default function Stake() {
  const [account, setAccount] = useState(null);
  const [provider, setProvider] = useState(null);
  const [stakingContract, setStakingContract] = useState(null);
  const [stakeAmount, setStakeAmount] = useState('');
  const [stakingInfo, setStakingInfo] = useState({ staked: 0, rewards: 0 });
  const [loading, setLoading] = useState(false);

  // Connect to wallet
  const connectWallet = async () => {
    if (typeof window.ethereum === 'undefined') {
      alert('MetaMask is required. Please install MetaMask and try again.');
      return;
    }

    try {
      const accounts = await ethereum.request({ method: 'eth_requestAccounts' });
      const providerInstance = new ethers.providers.Web3Provider(window.ethereum);
      const contractInstance = new ethers.Contract(
        STAKING_CONTRACT_ADDRESS,
        STAKING_CONTRACT_ABI,
        providerInstance.getSigner()
      );

      setAccount(accounts[0]);
      setProvider(providerInstance);
      setStakingContract(contractInstance);
    } catch (error) {
      console.error('Error connecting wallet:', error);
      alert('Failed to connect wallet. Please try again.');
    }
  };

  // Fetch staking progress and rewards
  const fetchStakingInfo = async () => {
    if (!stakingContract || !account) return;

    try {
      const staked = await stakingContract.getStakedTokens(account);
      const rewards = await stakingContract.getRewards(account);

      setStakingInfo({
        staked: ethers.utils.formatEther(staked),
        rewards: ethers.utils.formatEther(rewards),
      });
    } catch (error) {
      console.error('Error fetching staking info:', error);
      alert('Failed to fetch staking info. Please try again.');
    }
  };

  // Stake tokens
  const handleStake = async () => {
    if (!stakingContract || !account) {
      alert('Please connect your wallet first.');
      return;
    }

    if (!stakeAmount || isNaN(stakeAmount) || Number(stakeAmount) <= 0) {
      alert('Please enter a valid staking amount.');
      return;
    }

    setLoading(true);

    try {
      const stakeValue = ethers.utils.parseEther(stakeAmount);
      const tx = await stakingContract.stakeTokens(stakeValue);
      await tx.wait();

      alert('Tokens staked successfully!');
      setStakeAmount('');
      fetchStakingInfo();
    } catch (error) {
      console.error('Error during staking:', error);
      alert('Failed to stake tokens. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (stakingContract && account) {
      fetchStakingInfo();
    }
  }, [stakingContract, account]);

  return (
    <div className={styles.container}>
      <h1>Vanta Token Staking</h1>

      {!account ? (
        <button className={styles.connectButton} onClick={connectWallet}>
          Connect Wallet
        </button>
      ) : (
        <>
          <p>Connected Account: {account}</p>

          <div className={styles.stakingInfo}>
            <h2>Staking Progress</h2>
            <p>Staked Tokens: {stakingInfo.staked}</p>
            <p>Rewards: {stakingInfo.rewards}</p>
          </div>

          <div className={styles.stakeForm}>
            <h2>Stake Tokens</h2>
            <input
              type="number"
              placeholder="Amount to stake"
              value={stakeAmount}
              onChange={(e) => setStakeAmount(e.target.value)}
              className={styles.input}
            />
            <button
              className={styles.stakeButton}
              onClick={handleStake}
              disabled={loading}
            >
              {loading ? 'Staking...' : 'Stake'}
            </button>
          </div>
        </>
      )}
    </div>
  );
}

// CSS module (styles/Stake.module.css)
/*
.container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}

.connectButton,
.stakeButton {
  background-color: #0070f3;
  color: white;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
  border-radius: 5px;
}

.connectButton:hover,
.stakeButton:hover {
  background-color: #005bb5;
}

.stakingInfo,
.stakeForm {
  margin-top: 20px;
}

.input {
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
*/
```
