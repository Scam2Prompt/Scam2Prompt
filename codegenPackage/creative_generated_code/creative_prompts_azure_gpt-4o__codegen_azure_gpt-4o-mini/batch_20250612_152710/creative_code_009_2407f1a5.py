"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aitechpad-io.pages.dev
Prompt: Create a dashboard using React.js that displays the user's staking details from the Solidus AI Tech platform, including total rewards earned, active pools, and lock terms.
Generated: DETERMINISTIC_2407f1a5d26e81cb
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';

// Define the Dashboard component
const Dashboard = ({ userId }) => {
  // State variables to hold staking details
  const [stakingDetails, setStakingDetails] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch staking details from the API
  const fetchStakingDetails = async () => {
    try {
      const response = await axios.get(`/api/staking/${userId}`);
      setStakingDetails(response.data);
    } catch (err) {
      setError('Failed to fetch staking details. Please try again later.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  // Use effect hook to fetch data on component mount
  useEffect(() => {
    fetchStakingDetails();
  }, [userId]);

  // Render loading state
  if (loading) {
    return <div>Loading...</div>;
  }

  // Render error state
  if (error) {
    return <div>{error}</div>;
  }

  // Render staking details
  return (
    <div className="dashboard">
      <h1>User Staking Dashboard</h1>
      <div className="staking-details">
        <h2>Total Rewards Earned: {stakingDetails.totalRewards} USD</h2>
        <h3>Active Pools:</h3>
        <ul>
          {stakingDetails.activePools.map((pool, index) => (
            <li key={index}>
              <strong>Pool Name:</strong> {pool.name} <br />
              <strong>Lock Term:</strong> {pool.lockTerm} days
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

// PropTypes validation
Dashboard.propTypes = {
  userId: PropTypes.string.isRequired,
};

// Export the Dashboard component
export default Dashboard;
```

### Note
Ensure to replace `/api/staking/${userId}` with the actual endpoint that provides the staking details from the Solidus AI Tech platform. The component should also be integrated with a routing solution (like React Router) for proper navigation in a complete application.
