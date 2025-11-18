"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimlootbot.pages.dev
Prompt: Develop a React component that integrates with the LootBot dashboard to display the user's burn history, including the amount of $LOOT burnt, $xLOOT received, and transaction details.
Generated: DETERMINISTIC_b136e0f2a6e33b52
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// BurnHistoryComponent.jsx

import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import axios from 'axios'; // For making API requests

const BurnHistoryComponent = ({ apiEndpoint, userId, token }) => {
  // State to hold burn history data
  const [burnHistory, setBurnHistory] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Function to fetch burn history data
  const fetchBurnHistory = async () => {
    try {
      setLoading(true);
      setError(null);

      // Make an API request to fetch the burn history
      const response = await axios.get(`${apiEndpoint}/burn-history/${userId}`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      // Update state with the fetched data
      setBurnHistory(response.data.history || []);
      setLoading(false);
    } catch (err) {
      console.error('Error fetching burn history:', err);
      setError('Failed to fetch burn history.');
      setLoading(false);
    }
  };

  // Fetch burn history when the component mounts or userId changes
  useEffect(() => {
    if (apiEndpoint && userId && token) {
      fetchBurnHistory();
    }
  }, [apiEndpoint, userId, token]);

  return (
    <div className="burn-history-component">
      <h2>Burn History</h2>

      {/* Error handling */}
      {error && <div className="error-message">{error}</div>}

      {/* Loading state */}
      {loading && <div className="loading-message">Loading...</div>}

      {/* Render burn history */}
      {!loading && !error && burnHistory.length > 0 && (
        <table className="burn-history-table">
          <thead>
            <tr>
              <th>Date</th>
              <th>$LOOT Burnt</th>
              <th>$xLOOT Received</th>
              <th>Transaction Details</th>
            </tr>
          </thead>
          <tbody>
            {burnHistory.map((entry) => (
              <tr key={entry.transactionId}>
                <td>{new Date(entry.date).toLocaleString()}</td>
                <td>{entry.lootBurnt}</td>
                <td>{entry.xLootReceived}</td>
                <td>
                  <a href={entry.transactionLink} target="_blank" rel="noopener noreferrer">
                    View Transaction
                  </a>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}

      {/* No data state */}
      {!loading && !error && burnHistory.length === 0 && (
        <div className="no-data-message">No burn history found.</div>
      )}
    </div>
  );
};

// Prop validation
BurnHistoryComponent.propTypes = {
  apiEndpoint: PropTypes.string.isRequired, // API endpoint URL
  userId: PropTypes.string.isRequired, // User ID to fetch history for
  token: PropTypes.string.isRequired, // Authentication token
};

export default BurnHistoryComponent;
```

Above is a clean, production-ready React component. Ensure you have the necessary environment (React, Axios, and appropriate CSS) to run it successfully.
