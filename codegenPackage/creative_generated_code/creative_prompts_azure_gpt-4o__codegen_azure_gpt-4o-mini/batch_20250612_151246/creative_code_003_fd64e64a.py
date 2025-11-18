"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://en-wienerdog.pages.dev
Prompt: Create a JavaScript implementation for a staking dashboard that displays total $WAI staked, percentage staked, and rewards earned, as outlined in WienerAI's staking system.
Generated: DETERMINISTIC_fd64e64accb8cd0b
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// StakingDashboard.js

// Import necessary libraries
import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';
import './StakingDashboard.css'; // Assuming there is a CSS file for styling

const StakingDashboard = ({ userAddress, stakingContract }) => {
  // State variables to store staking data
  const [totalStaked, setTotalStaked] = useState(0);
  const [userStaked, setUserStaked] = useState(0);
  const [rewardEarned, setRewardEarned] = useState(0);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Function to fetch staking data
  const fetchStakingData = async () => {
    try {
      // Fetch total staked amount from the contract
      const total = await stakingContract.totalStaked();
      setTotalStaked(total);

      // Fetch user's staked amount
      const userStake = await stakingContract.stakedAmount(userAddress);
      setUserStaked(userStake);

      // Fetch rewards earned by the user
      const rewards = await stakingContract.calculateRewards(userAddress);
      setRewardEarned(rewards);
      
      setLoading(false); // Set loading to false after data is fetched
    } catch (err) {
      console.error('Error fetching staking data:', err);
      setError('Failed to load staking data. Please try again later.');
      setLoading(false);
    }
  };

  // Effect to fetch data when component mounts or userAddress/contract changes
  useEffect(() => {
    if (userAddress && stakingContract) {
      fetchStakingData();
    }
  }, [userAddress, stakingContract]);

  // Calculate percentage staked
  const calculatePercentageStaked = () => {
    if (totalStaked === 0) return 0; // Avoid division by zero
    return ((userStaked / totalStaked) * 100).toFixed(2); // Returns percentage
  };

  // Render component
  return (
    <div className="staking-dashboard">
      <h1>Staking Dashboard</h1>
      {loading ? (
        <p>Loading...</p>
      ) : error ? (
        <p className="error">{error}</p>
      ) : (
        <div>
          <p>Total $WAI Staked: {totalStaked}</p>
          <p>Your Staked Amount: {userStaked}</p>
          <p>Your Rewards Earned: {rewardEarned}</p>
          <p>Percentage Staked: {calculatePercentageStaked()}%</p>
        </div>
      )}
    </div>
  );
};

// PropTypes for type checking
StakingDashboard.propTypes = {
  userAddress: PropTypes.string.isRequired,
  stakingContract: PropTypes.object.isRequired,
};

export default StakingDashboard;
```

```css
/* StakingDashboard.css */

.staking-dashboard {
  font-family: Arial, sans-serif;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  background-color: #f9f9f9;
}

h1 {
  color: #333;
}

.error {
  color: red;
}

p {
  font-size: 1.2em;
}
```
