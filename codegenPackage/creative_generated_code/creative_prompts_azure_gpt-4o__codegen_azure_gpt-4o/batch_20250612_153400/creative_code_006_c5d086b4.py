"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-greenbitcoin-xyz.pages.dev
Prompt: Develop a React component for a Green Bitcoin staking dashboard that displays total staked tokens, percentage staked, and rewards earned in real-time.
Generated: DETERMINISTIC_c5d086b4ce56903e
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary libraries and hooks
import React, { useState, useEffect } from "react";
import PropTypes from "prop-types";
import "./StakingDashboard.css"; // Import custom CSS for styling

/**
 * StakingDashboard Component
 * Displays real-time information about Green Bitcoin staking:
 * Total staked tokens, percentage staked, and rewards earned.
 */
const StakingDashboard = ({ fetchData }) => {
  // State variables for staking data
  const [totalStaked, setTotalStaked] = useState(0);
  const [percentageStaked, setPercentageStaked] = useState(0);
  const [rewardsEarned, setRewardsEarned] = useState(0);
  const [error, setError] = useState(null); // State for error handling

  /**
   * Fetch staking data from the provided fetchData function.
   * Updates state variables with the latest data.
   */
  const updateStakingData = async () => {
    try {
      const data = await fetchData(); // Fetch data from API or server
      setTotalStaked(data.totalStaked);
      setPercentageStaked(data.percentageStaked);
      setRewardsEarned(data.rewardsEarned);
    } catch (err) {
      console.error("Error fetching staking data:", err);
      setError("Failed to fetch staking data. Please try again later.");
    }
  };

  // useEffect hook to fetch data on component mount and at regular intervals
  useEffect(() => {
    updateStakingData(); // Initial fetch
    const interval = setInterval(updateStakingData, 30000); // Refresh data every 30 seconds
    return () => clearInterval(interval); // Cleanup interval on unmount
  }, []);

  return (
    <div className="staking-dashboard">
      <h1>Green Bitcoin Staking Dashboard</h1>
      {error ? (
        <p className="error-message">{error}</p> // Display error message if there's an error
      ) : (
        <div className="staking-data">
          <div className="data-item">
            <h2>Total Staked</h2>
            <p>{totalStaked} GBTC</p>
          </div>
          <div className="data-item">
            <h2>Percentage Staked</h2>
            <p>{percentageStaked}%</p>
          </div>
          <div className="data-item">
            <h2>Rewards Earned</h2>
            <p>{rewardsEarned} GBTC</p>
          </div>
        </div>
      )}
    </div>
  );
};

// Prop validation to ensure fetchData is a function
StakingDashboard.propTypes = {
  fetchData: PropTypes.func.isRequired
};

export default StakingDashboard;

/*
 * Example CSS in `StakingDashboard.css`:
 * 
 * .staking-dashboard {
 *   font-family: Arial, sans-serif;
 *   padding: 20px;
 *   background-color: #f4f4f4;
 *   border-radius: 8px;
 *   width: 400px;
 *   margin: auto;
 * }
 *
 * .data-item {
 *   margin-bottom: 20px;
 * }
 *
 * .error-message {
 *   color: red;
 * }
 */
```
