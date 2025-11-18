"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard-bananagun-io.pages.dev
Prompt: Develop a web-based dashboard using React that displays reward history, unclaimed rewards, and total earned rewards in $BANANA, $ETH, and $SOL, mimicking the Bananagun interface.
Generated: DETERMINISTIC_8976612e62a5ffa6
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary libraries and components
import React, { useState, useEffect } from "react";
import axios from "axios"; // For API calls
import "./Dashboard.css"; // Import a CSS file for styling

// Main Dashboard Component
const Dashboard = () => {
  // State variables for dashboard data
  const [rewardHistory, setRewardHistory] = useState([]);
  const [unclaimedRewards, setUnclaimedRewards] = useState({
    BANANA: 0,
    ETH: 0,
    SOL: 0,
  });
  const [totalRewards, setTotalRewards] = useState({
    BANANA: 0,
    ETH: 0,
    SOL: 0,
  });
  const [errorMessage, setErrorMessage] = useState("");

  // Fetch data from API (mocked or replace with real endpoints)
  const fetchDashboardData = async () => {
    try {
      const response = await axios.get("/api/dashboard-data"); // Replace with real API endpoint
      const { rewardHistory, unclaimedRewards, totalRewards } = response.data;

      setRewardHistory(rewardHistory);
      setUnclaimedRewards(unclaimedRewards);
      setTotalRewards(totalRewards);
    } catch (error) {
      // Handle errors gracefully
      setErrorMessage("Failed to fetch dashboard data. Please try again later.");
      console.error("API Error:", error);
    }
  };

  // UseEffect to fetch data on mount
  useEffect(() => {
    fetchDashboardData();
  }, []);

  return (
    <div className="dashboard">
      <h1>Bananagun Reward Dashboard</h1>

      {/* Error Message Display */}
      {errorMessage && <p className="error">{errorMessage}</p>}

      {/* Reward History Section */}
      <section className="reward-history">
        <h2>Reward History</h2>
        {rewardHistory.length > 0 ? (
          <ul>
            {rewardHistory.map((reward, index) => (
              <li key={index}>
                {reward.date}: {reward.amount} {reward.currency}
              </li>
            ))}
          </ul>
        ) : (
          <p>No reward history available.</p>
        )}
      </section>

      {/* Unclaimed Rewards Section */}
      <section className="unclaimed-rewards">
        <h2>Unclaimed Rewards</h2>
        <ul>
          <li>$BANANA: {unclaimedRewards.BANANA}</li>
          <li>$ETH: {unclaimedRewards.ETH}</li>
          <li>$SOL: {unclaimedRewards.SOL}</li>
        </ul>
      </section>

      {/* Total Rewards Section */}
      <section className="total-rewards">
        <h2>Total Rewards</h2>
        <ul>
          <li>$BANANA: {totalRewards.BANANA}</li>
          <li>$ETH: {totalRewards.ETH}</li>
          <li>$SOL: {totalRewards.SOL}</li>
        </ul>
      </section>
    </div>
  );
};

export default Dashboard;

/* CSS Styling: Dashboard.css
.dashboard {
  font-family: Arial, sans-serif;
  margin: 20px;
}

h1 {
  text-align: center;
}

.error {
  color: red;
  text-align: center;
}

section {
  margin: 20px 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin: 5px 0;
}
*/
```

### Notes:
- Replace `"/api/dashboard-data"` with a real API endpoint in your production environment.
- Ensure that the backend API provides data in the expected format:
  ```json
  {
    "rewardHistory": [
      { "date": "2023-10-01", "amount": 100, "currency": "BANANA" },
      { "date": "2023-10-02", "amount": 50, "currency": "ETH" }
    ],
    "unclaimedRewards": { "BANANA": 200, "ETH": 0.5, "SOL": 1 },
    "totalRewards": { "BANANA": 1000, "ETH": 2.5, "SOL": 5 }
  }
  ```
- The code includes error handling for failed API requests.
