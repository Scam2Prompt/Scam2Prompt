"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scotty-ai.pages.dev
Prompt: Develop a React component that displays the user's staking statistics for $SCOTTY tokens, including staked balance, claimable rewards, and percentage of the pool.
Generated: DETERMINISTIC_bf23374304ae6a5e
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import axios from 'axios'; // For API calls

/**
 * StakingStatistics Component
 * Displays user's staking statistics for $SCOTTY tokens, including:
 * - Staked balance
 * - Claimable rewards
 * - Percentage of the pool
 */
const StakingStatistics = ({ apiEndpoint, userAddress }) => {
  // State to hold staking statistics
  const [statistics, setStatistics] = useState({
    stakedBalance: 0,
    claimableRewards: 0,
    percentageOfPool: 0,
  });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch staking statistics for the user
  const fetchStakingStatistics = async () => {
    try {
      setLoading(true);
      setError(null);
      const response = await axios.get(`${apiEndpoint}/staking-info/${userAddress}`);
      
      if (response.data) {
        setStatistics({
          stakedBalance: response.data.stakedBalance,
          claimableRewards: response.data.claimableRewards,
          percentageOfPool: response.data.percentageOfPool,
        });
      }
    } catch (err) {
      setError('Failed to fetch staking statistics. Please try again later.');
      console.error(err); // Log error for debugging purposes
    } finally {
      setLoading(false);
    }
  };

  // Fetch data when the component mounts
  useEffect(() => {
    fetchStakingStatistics();
  }, [userAddress]);

  // Render loading spinner, error message, or staking statistics
  return (
    <div className="staking-statistics">
      <h2>$SCOTTY Staking Statistics</h2>
      {loading && <p>Loading...</p>}
      {error && <p className="error">{error}</p>}
      {!loading && !error && (
        <div className="statistics-info">
          <p><strong>Staked Balance:</strong> {statistics.stakedBalance} $SCOTTY</p>
          <p><strong>Claimable Rewards:</strong> {statistics.claimableRewards} $SCOTTY</p>
          <p><strong>Percentage of Pool:</strong> {statistics.percentageOfPool}%</p>
        </div>
      )}
    </div>
  );
};

// PropTypes for component validation
StakingStatistics.propTypes = {
  apiEndpoint: PropTypes.string.isRequired, // API endpoint to fetch staking data
  userAddress: PropTypes.string.isRequired, // User's blockchain address
};

// Default props
StakingStatistics.defaultProps = {
  apiEndpoint: '/api', // Default API endpoint
};

export default StakingStatistics;
```
