"""
Generated Code Metadata:
========================
Original URL: https://en-wienerdog.pages.dev
Prompt: Create a JavaScript implementation for a staking dashboard that displays total $WAI staked, percentage staked, and rewards earned, as outlined in WienerAI's staking system.
Generated: DETERMINISTIC_fd64e64accb8cd0b
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// StakingDashboard.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { ethers } from 'ethers';

/**
 * Staking Dashboard Component
 * Displays staking statistics for WienerAI token ($WAI)
 */
const StakingDashboard = ({ contractAddress, abi }) => {
  // State variables
  const [totalStaked, setTotalStaked] = useState('0');
  const [percentageStaked, setPercentageStaked] = useState('0');
  const [rewardsEarned, setRewardsEarned] = useState('0');
  const [userStaked, setUserStaked] = useState('0');
  const [totalSupply, setTotalSupply] = useState('0');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [account, setAccount] = useState(null);

  // Initialize provider and contract
  const provider = new ethers.providers.Web3Provider(window.ethereum);
  const contract = new ethers.Contract(contractAddress, abi, provider);

  /**
   * Fetch staking data from contract
   */
  const fetchStakingData = async () => {
    try {
      setLoading(true);
      
      // Get total supply
      const supply = await contract.totalSupply();
      setTotalSupply(ethers.utils.formatUnits(supply, 18));
      
      // Get total staked
      const staked = await contract.totalStaked();
      setTotalStaked(ethers.utils.formatUnits(staked, 18));
      
      // Calculate percentage staked
      const percentage = (staked.mul(10000).div(supply)).toNumber() / 100;
      setPercentageStaked(percentage.toFixed(2));
      
      // Get user rewards if wallet connected
      if (account) {
        const rewards = await contract.pendingRewards(account);
        setRewardsEarned(ethers.utils.formatUnits(rewards, 18));
        
        const userStake = await contract.stakedBalance(account);
        setUserStaked(ethers.utils.formatUnits(userStake, 18));
      }
      
      setLoading(false);
    } catch (err) {
      console.error('Error fetching staking data:', err);
      setError('Failed to load staking data');
      setLoading(false);
    }
  };

  /**
   * Connect wallet handler
   */
  const connectWallet = async () => {
    try {
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      setAccount(accounts[0]);
    } catch (err) {
      console.error('Error connecting wallet:', err);
      setError('Failed to connect wallet');
    }
  };

  // Effect to load data on mount and account change
  useEffect(() => {
    if (window.ethereum) {
      fetchStakingData();
      
      // Listen for account changes
      window.ethereum.on('accountsChanged', (accounts) => {
        setAccount(accounts[0] || null);
      });
      
      // Cleanup
      return () => {
        window.ethereum.removeListener('accountsChanged', () => {});
      };
    } else {
      setError('Ethereum wallet not detected');
    }
  }, [account]);

  // Format large numbers
  const formatNumber = (num) => {
    return Number(num).toLocaleString('en-US', {
      minimumFractionDigits: 2,
      maximumFractionDigits: 2
    });
  };

  return (
    <div className="staking-dashboard">
      <h2>WienerAI Staking Dashboard</h2>
      
      {error && <div className="error-message">{error}</div>}
      
      {loading ? (
        <div className="loading">Loading staking data...</div>
      ) : (
        <div className="stats-container">
          <div className="stat-card">
            <h3>Total $WAI Staked</h3>
            <p>{formatNumber(totalStaked)}</p>
          </div>
          
          <div className="stat-card">
            <h3>Percentage Staked</h3>
            <p>{percentageStaked}%</p>
          </div>
          
          {account && (
            <>
              <div className="stat-card">
                <h3>Your Staked $WAI</h3>
                <p>{formatNumber(userStaked)}</p>
              </div>
              
              <div className="stat-card">
                <h3>Your Rewards</h3>
                <p>{formatNumber(rewardsEarned)} $WAI</p>
              </div>
            </>
          )}
        </div>
      )}
      
      {!account && (
        <button className="connect-wallet" onClick={connectWallet}>
          Connect Wallet
        </button>
      )}
    </div>
  );
};

export default StakingDashboard;

// Example usage:
// <StakingDashboard 
//   contractAddress="0x123...abc" 
//   abi={stakingContractABI} 
// />
```
