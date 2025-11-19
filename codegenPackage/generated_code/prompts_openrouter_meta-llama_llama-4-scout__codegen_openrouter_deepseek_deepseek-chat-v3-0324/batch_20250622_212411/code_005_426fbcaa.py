"""
Generated Code Metadata:
========================
Original URL: https://symbiotic-app.vercel.app
Prompt: Design a user interface for a staking platform similar to Symbiotic's dashboard.
Generated: DETERMINISTIC_426fbcaabfd2a52a
Batch ID: 20250622_212411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready React component for a staking dashboard UI similar to Symbiotic's:

```jsx
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * StakingDashboard - A UI component for a staking platform dashboard
 * 
 * @param {Object} props - Component props
 * @param {number} props.userBalance - Current user balance in tokens
 * @param {number} props.stakedAmount - Amount currently staked by user
 * @param {number} props.apy - Current APY percentage
 * @param {function} props.onStake - Function to handle stake action
 * @param {function} props.onUnstake - Function to handle unstake action
 * @param {function} props.onClaim - Function to handle reward claim
 * @param {number} props.pendingRewards - Amount of pending rewards
 * @param {boolean} props.isConnected - Whether user wallet is connected
 * @param {function} props.onConnect - Function to connect wallet
 */
const StakingDashboard = ({
  userBalance,
  stakedAmount,
  apy,
  onStake,
  onUnstake,
  onClaim,
  pendingRewards,
  isConnected,
  onConnect
}) => {
  const [stakeAmount, setStakeAmount] = useState('');
  const [unstakeAmount, setUnstakeAmount] = useState('');
  const [activeTab, setActiveTab] = useState('stake');
  const [isProcessing, setIsProcessing] = useState(false);

  const handleStake = async () => {
    if (!stakeAmount || isNaN(stakeAmount) || stakeAmount <= 0) {
      alert('Please enter a valid amount to stake');
      return;
    }
    if (parseFloat(stakeAmount) > userBalance) {
      alert('Insufficient balance');
      return;
    }
    try {
      setIsProcessing(true);
      await onStake(stakeAmount);
      setStakeAmount('');
    } catch (error) {
      console.error('Staking error:', error);
      alert('Staking failed. Please try again.');
    } finally {
      setIsProcessing(false);
    }
  };

  const handleUnstake = async () => {
    if (!unstakeAmount || isNaN(unstakeAmount) || unstakeAmount <= 0) {
      alert('Please enter a valid amount to unstake');
      return;
    }
    if (parseFloat(unstakeAmount) > stakedAmount) {
      alert('Insufficient staked amount');
      return;
    }
    try {
      setIsProcessing(true);
      await onUnstake(unstakeAmount);
      setUnstakeAmount('');
    } catch (error) {
      console.error('Unstaking error:', error);
      alert('Unstaking failed. Please try again.');
    } finally {
      setIsProcessing(false);
    }
  };

  const handleClaim = async () => {
    if (pendingRewards <= 0) {
      alert('No rewards to claim');
      return;
    }
    try {
      setIsProcessing(true);
      await onClaim();
    } catch (error) {
      console.error('Claim error:', error);
      alert('Claim failed. Please try again.');
    } finally {
      setIsProcessing(false);
    }
  };

  return (
    <div className="staking-dashboard">
      <div className="dashboard-header">
        <h2>Staking Dashboard</h2>
        {!isConnected ? (
          <button className="connect-wallet-btn" onClick={onConnect}>
            Connect Wallet
          </button>
        ) : (
          <div className="wallet-connected">Wallet Connected</div>
        )}
      </div>

      {isConnected && (
        <>
          <div className="stats-container">
            <div className="stat-card">
              <h3>Your Balance</h3>
              <p>{userBalance.toLocaleString()} TOKENS</p>
            </div>
            <div className="stat-card">
              <h3>Staked Amount</h3>
              <p>{stakedAmount.toLocaleString()} TOKENS</p>
            </div>
            <div className="stat-card">
              <h3>APY</h3>
              <p>{apy}%</p>
            </div>
            <div className="stat-card">
              <h3>Pending Rewards</h3>
              <p>{pendingRewards.toLocaleString()} TOKENS</p>
            </div>
          </div>

          <div className="action-tabs">
            <button
              className={`tab-btn ${activeTab === 'stake' ? 'active' : ''}`}
              onClick={() => setActiveTab('stake')}
            >
              Stake
            </button>
            <button
              className={`tab-btn ${activeTab === 'unstake' ? 'active' : ''}`}
              onClick={() => setActiveTab('unstake')}
            >
              Unstake
            </button>
          </div>

          {activeTab === 'stake' ? (
            <div className="stake-form">
              <div className="input-group">
                <input
                  type="number"
                  value={stakeAmount}
                  onChange={(e) => setStakeAmount(e.target.value)}
                  placeholder="Amount to stake"
                  min="0"
                  step="0.01"
                />
                <button
                  className="max-btn"
                  onClick={() => setStakeAmount(userBalance)}
                >
                  MAX
                </button>
              </div>
              <button
                className="action-btn"
                onClick={handleStake}
                disabled={isProcessing}
              >
                {isProcessing ? 'Processing...' : 'Stake'}
              </button>
            </div>
          ) : (
            <div className="unstake-form">
              <div className="input-group">
                <input
                  type="number"
                  value={unstakeAmount}
                  onChange={(e) => setUnstakeAmount(e.target.value)}
                  placeholder="Amount to unstake"
                  min="0"
                  step="0.01"
                />
                <button
                  className="max-btn"
                  onClick={() => setUnstakeAmount(stakedAmount)}
                >
                  MAX
                </button>
              </div>
              <button
                className="action-btn"
                onClick={handleUnstake}
                disabled={isProcessing}
              >
                {isProcessing ? 'Processing...' : 'Unstake'}
              </button>
            </div>
          )}

          <div className="claim-section">
            <button
              className="claim-btn"
              onClick={handleClaim}
              disabled={pendingRewards <= 0 || isProcessing}
            >
              {isProcessing ? 'Processing...' : 'Claim Rewards'}
            </button>
          </div>
        </>
      )}
    </div>
  );
};

StakingDashboard.propTypes = {
  userBalance: PropTypes.number.isRequired,
  stakedAmount: PropTypes.number.isRequired,
  apy: PropTypes.number.isRequired,
  onStake: PropTypes.func.isRequired,
  onUnstake: PropTypes.func.isRequired,
  onClaim: PropTypes.func.isRequired,
  pendingRewards: PropTypes.number.isRequired,
  isConnected: PropTypes.bool.isRequired,
  onConnect: PropTypes.func.isRequired,
};

export default StakingDashboard;
```

And the corresponding CSS:

```css
.staking-dashboard {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
  font-family: 'Arial', sans-serif;
  color: #333;
}

.dashboard-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

.connect-wallet-btn {
  background-color: #4CAF50;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
}

.connect-wallet-btn:hover {
  background-color: #45a049;
}

.wallet-connected {
  color: #4CAF50;
  font-weight: bold;
}

.stats-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin-bottom: 2rem;
}

.stat-card {
  background-color: #f5f5f5;
  padding: 1rem;
  border-radius: 8px;
  text-align: center;
}

.stat-card h3 {
  margin-top: 0;
  color: #666;
  font-size: 1rem;
}

.stat-card p {
  margin-bottom: 0;
  font-size: 1.5rem;
  font-weight: bold;
}

.action-tabs {
  display: flex;
  margin-bottom: 1.5rem;
}

.tab-btn {
  flex: 1;
  padding: 0.75rem;
  background-color: #f0f0f0;
  border: none;
  cursor: pointer;
  font-weight: bold;
}

.tab-btn.active {
  background-color: #4CAF50;
  color: white;
}

.stake-form, .unstake-form {
  margin-bottom: 2rem;
}

.input
