"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poodlinu-com.pages.dev
Prompt: Create a React component that displays the user's staked $POODL balance, estimated rewards, and allows them to claim rewards, based on the Poodl Inu staking system.
Generated: DETERMINISTIC_72a7827c250f9774
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';
import { fetchStakedBalance, fetchEstimatedRewards, claimRewards } from './api'; // Assume these API functions are defined in api.js

const PoodlStaking = ({ userAddress }) => {
  // State to store user's staked balance and estimated rewards
  const [stakedBalance, setStakedBalance] = useState(0);
  const [estimatedRewards, setEstimatedRewards] = useState(0);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch user's staked balance and estimated rewards on component mount
  useEffect(() => {
    const fetchStakingData = async () => {
      try {
        setLoading(true);
        
        // Fetch staked balance
        const balance = await fetchStakedBalance(userAddress);
        setStakedBalance(balance);

        // Fetch estimated rewards
        const rewards = await fetchEstimatedRewards(userAddress);
        setEstimatedRewards(rewards);

      } catch (err) {
        setError('Failed to fetch staking data. Please try again later.');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    if (userAddress) {
      fetchStakingData();
    }
  }, [userAddress]);

  // Function to handle claiming rewards
  const handleClaimRewards = async () => {
    try {
      setLoading(true);
      await claimRewards(userAddress);
      // Re-fetching the estimated rewards after claiming
      const newRewards = await fetchEstimatedRewards(userAddress);
      setEstimatedRewards(newRewards);
      alert("Rewards claimed successfully!");
    } catch (err) {
      setError('Failed to claim rewards. Please try again later.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  // Render loading state, error message or the staking data
  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div className="error">{error}</div>;
  }

  return (
    <div className="poodl-staking">
      <h2>Poodl Inu Staking</h2>
      <p><strong>Staked Balance:</strong> {stakedBalance} $POODL</p>
      <p><strong>Estimated Rewards:</strong> {estimatedRewards} $POODL</p>
      <button onClick={handleClaimRewards} disabled={estimatedRewards <= 0}>
        Claim Rewards
      </button>
    </div>
  );
};

// PropTypes validation for the component's props
PoodlStaking.propTypes = {
  userAddress: PropTypes.string.isRequired,
};

export default PoodlStaking;
```

Make sure to implement the `fetchStakedBalance`, `fetchEstimatedRewards`, and `claimRewards` functions in the `api.js` file to interact with your backend or blockchain as needed.
