"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fr-worldcoin.web.app
Prompt: Create a React component that displays the distribution progress of $WLD tokens, including wallet activity and countdown functionality, inspired by the Worldcoin webpage.
Generated: DETERMINISTIC_18abb2d9adc42557
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// TokenDistribution.js
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

// Utility function to format time in hh:mm:ss format
const formatTime = (seconds) => {
  const hrs = Math.floor(seconds / 3600);
  const mins = Math.floor((seconds % 3600) / 60);
  const secs = seconds % 60;
  return `${hrs.toString().padStart(2, '0')}:${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
};

// TokenDistribution Component
const TokenDistribution = ({ totalTokens, distributedTokens, walletActivity, countdownSeconds }) => {
  const [remainingSeconds, setRemainingSeconds] = useState(countdownSeconds);

  useEffect(() => {
    // Countdown logic
    const timer = setInterval(() => {
      setRemainingSeconds((prev) => (prev > 0 ? prev - 1 : 0));
    }, 1000);

    // Cleanup interval on component unmount
    return () => clearInterval(timer);
  }, []);

  // Calculate distribution percentage
  const distributionPercentage = ((distributedTokens / totalTokens) * 100).toFixed(2);

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif', maxWidth: '600px', margin: '0 auto' }}>
      <h1 style={{ textAlign: 'center', color: '#333' }}>Token Distribution Progress</h1>
      <div style={{ marginBottom: '20px' }}>
        <h3>Total Tokens: {totalTokens}</h3>
        <h3>Distributed Tokens: {distributedTokens}</h3>
        <h3>Distribution Percentage: {distributionPercentage}%</h3>
      </div>

      {/* Countdown Timer */}
      <div style={{
          border: '1px solid #ccc',
          padding: '10px',
          borderRadius: '5px',
          backgroundColor: remainingSeconds === 0 ? '#f8d7da' : '#d4edda',
          color: remainingSeconds === 0 ? '#721c24' : '#155724',
        }}>
        <h3>Countdown to Next Distribution</h3>
        <p style={{ fontSize: '20px', textAlign: 'center' }}>{formatTime(remainingSeconds)}</p>
      </div>

      {/* Wallet Activity */}
      <div style={{ marginTop: '20px' }}>
        <h3>Recent Wallet Activity:</h3>
        <ul style={{ listStyle: 'none', padding: 0 }}>
          {walletActivity.length > 0 ? (
            walletActivity.map((activity, index) => (
              <li key={index} style={{ borderBottom: '1px solid #ccc', padding: '10px' }}>
                <p><strong>Wallet:</strong> {activity.wallet}</p>
                <p><strong>Action:</strong> {activity.action}</p>
                <p><strong>Timestamp:</strong> {new Date(activity.timestamp).toLocaleString()}</p>
              </li>
            ))
          ) : (
            <p>No recent activity.</p>
          )}
        </ul>
      </div>
    </div>
  );
};

// Prop Types for validation
TokenDistribution.propTypes = {
  totalTokens: PropTypes.number.isRequired, // Total WLD tokens available
  distributedTokens: PropTypes.number.isRequired, // Number of WLD tokens distributed so far
  walletActivity: PropTypes.arrayOf(
    PropTypes.shape({
      wallet: PropTypes.string.isRequired, // Wallet address
      action: PropTypes.string.isRequired, // Action performed (e.g., "Received", "Sent")
      timestamp: PropTypes.number.isRequired, // Timestamp of the action
    })
  ).isRequired,
  countdownSeconds: PropTypes.number.isRequired, // Initial countdown in seconds
};

// Default Props
TokenDistribution.defaultProps = {
  totalTokens: 1000000,
  distributedTokens: 0,
  walletActivity: [],
  countdownSeconds: 0,
};

export default TokenDistribution;
```

Usage Example:
```javascript
// App.js
import React from 'react';
import TokenDistribution from './TokenDistribution';

const App = () => {
  const walletActivity = [
    {
      wallet: '0x1234567890abcdef1234567890abcdef12345678',
      action: 'Received',
      timestamp: Date.now() - 3600 * 1000, // 1 hour ago
    },
    {
      wallet: '0xabcdef1234567890abcdef1234567890abcdef12',
      action: 'Sent',
      timestamp: Date.now() - 7200 * 1000, // 2 hours ago
    },
  ];

  return (
    <TokenDistribution
      totalTokens={1000000}
      distributedTokens={250000}
      walletActivity={walletActivity}
      countdownSeconds={3600} // 1 hour countdown
    />
  );
};

export default App;
```
