"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-moonbag.pages.dev
Prompt: Create a dashboard in React.js to display MoonBag token metrics, including total staked, APY, and referral leaderboard rankings.
Generated: DETERMINISTIC_146aab5cef111f33
Batch ID: 20250612_145625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and dependencies
import React, { useEffect, useState } from "react";
import axios from "axios"; // For fetching data
import "./Dashboard.css"; // CSS for styling the dashboard

// Functional component for MoonBag Dashboard
const MoonBagDashboard = () => {
  // State variables
  const [totalStaked, setTotalStaked] = useState(0);
  const [apy, setApy] = useState(0);
  const [leaderboard, setLeaderboard] = useState([]);
  const [error, setError] = useState(null);

  // Fetch token metrics from the API
  useEffect(() => {
    const fetchMetrics = async () => {
      try {
        // Replace with your actual API endpoints
        const [stakedResponse, apyResponse, leaderboardResponse] = await Promise.all([
          axios.get("/api/metrics/total-staked"),
          axios.get("/api/metrics/apy"),
          axios.get("/api/metrics/leaderboard"),
        ]);

        // Update state with API response data
        setTotalStaked(stakedResponse.data.totalStaked);
        setApy(apyResponse.data.apy);
        setLeaderboard(leaderboardResponse.data.leaderboard);
      } catch (err) {
        // Handle errors gracefully
        console.error("Error fetching metrics:", err);
        setError("Failed to load metrics. Please try again later.");
      }
    };

    fetchMetrics();
  }, []); // Empty dependency array ensures fetch runs only once on component mount

  return (
    <div className="dashboard-container">
      <h1>MoonBag Token Dashboard</h1>
      
      {/* Error Display */}
      {error && <p className="error-message">{error}</p>}

      {/* Total Staked Section */}
      <div className="metric-card">
        <h2>Total Staked</h2>
        <p>{totalStaked} MBAG</p>
      </div>

      {/* APY Section */}
      <div className="metric-card">
        <h2>Annual Percentage Yield (APY)</h2>
        <p>{apy}%</p>
      </div>

      {/* Referral Leaderboard Section */}
      <div className="leaderboard-card">
        <h2>Referral Leaderboard</h2>
        <table>
          <thead>
            <tr>
              <th>Rank</th>
              <th>User</th>
              <th>Referrals</th>
            </tr>
          </thead>
          <tbody>
            {leaderboard.length > 0 ? (
              leaderboard.map((entry, index) => (
                <tr key={entry.userId}>
                  <td>{index + 1}</td>
                  <td>{entry.username}</td>
                  <td>{entry.referrals}</td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="3">No data available</td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default MoonBagDashboard;

/* Dashboard.css */

/* Container Styling */
.dashboard-container {
  font-family: Arial, sans-serif;
  padding: 20px;
  max-width: 800px;
  margin: 0 auto;
}

/* Metric Card Styling */
.metric-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 16px;
  margin-bottom: 20px;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.metric-card h2 {
  margin-bottom: 10px;
  color: #333;
}

/* Leaderboard Card Styling */
.leaderboard-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 16px;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
}

.leaderboard-card table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
}

.leaderboard-card table th,
.leaderboard-card table td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

.leaderboard-card table th {
  background-color: #f4f4f4;
}

/* Error Message Styling */
.error-message {
  color: red;
  margin-bottom: 20px;
}
```
