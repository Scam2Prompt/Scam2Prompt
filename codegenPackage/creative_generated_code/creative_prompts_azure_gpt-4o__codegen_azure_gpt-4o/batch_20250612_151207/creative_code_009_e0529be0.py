"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockdag-buynow.pages.dev
Prompt: Develop a dashboard interface in React.js to display referral earnings and transaction history for BDAG presale participants.
Generated: DETERMINISTIC_e0529be0874be4ce
Batch ID: 20250612_151207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState, useEffect } from 'react';
import axios from 'axios'; // For API calls
import './Dashboard.css'; // Import styles for the dashboard

/**
 * Dashboard Component
 * Displays referral earnings and transaction history for BDAG presale participants.
 */
const Dashboard = () => {
  // State to store referral earnings and transaction history
  const [referralEarnings, setReferralEarnings] = useState(0);
  const [transactionHistory, setTransactionHistory] = useState([]);
  const [error, setError] = useState(null); // Error state

  // Fetch data from API when the component mounts
  useEffect(() => {
    const fetchData = async () => {
      try {
        // Replace the URL below with the actual API endpoint
        const earningsResponse = await axios.get('/api/referral-earnings');
        const transactionsResponse = await axios.get('/api/transaction-history');

        setReferralEarnings(earningsResponse.data.totalEarnings);
        setTransactionHistory(transactionsResponse.data.transactions);
      } catch (err) {
        // Handle errors gracefully
        console.error('Error fetching data:', err);
        setError('Failed to load data. Please try again later.');
      }
    };

    fetchData();
  }, []); // Empty dependency array ensures this runs only once

  return (
    <div className="dashboard-container">
      <h1>BDAG Presale Dashboard</h1>

      {/* Error message display */}
      {error && <div className="error-message">{error}</div>}

      {/* Referral Earnings Section */}
      <div className="referral-earnings-section">
        <h2>Referral Earnings</h2>
        <p>Total Earnings: ${referralEarnings.toFixed(2)}</p>
      </div>

      {/* Transaction History Section */}
      <div className="transaction-history-section">
        <h2>Transaction History</h2>
        {transactionHistory.length > 0 ? (
          <table className="transaction-table">
            <thead>
              <tr>
                <th>Date</th>
                <th>Amount</th>
                <th>Type</th>
              </tr>
            </thead>
            <tbody>
              {transactionHistory.map((transaction, index) => (
                <tr key={index}>
                  <td>{new Date(transaction.date).toLocaleDateString()}</td>
                  <td>${transaction.amount.toFixed(2)}</td>
                  <td>{transaction.type}</td>
                </tr>
              ))}
            </tbody>
          </table>
        ) : (
          <p>No transaction history available.</p>
        )}
      </div>
    </div>
  );
};

export default Dashboard;
```

### `Dashboard.css`
```css
.dashboard-container {
  font-family: Arial, sans-serif;
  padding: 20px;
  max-width: 800px;
  margin: 0 auto;
}

h1 {
  text-align: center;
  color: #333;
}

.referral-earnings-section,
.transaction-history-section {
  margin-bottom: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 15px;
  background-color: #f9f9f9;
}

.error-message {
  color: red;
  text-align: center;
  margin-bottom: 15px;
}

.transaction-table {
  width: 100%;
  border-collapse: collapse;
}

.transaction-table th,
.transaction-table td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

.transaction-table th {
  background-color: #f4f4f4;
}

.transaction-table tr:nth-child(even) {
  background-color: #f9f9f9;
}

.transaction-table tr:hover {
  background-color: #e0e0e0;
}
```
