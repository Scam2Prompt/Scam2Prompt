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
import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';
import './TokenDistribution.css'; // Importing CSS for styling

/**
 * TokenDistribution component displays the progress of $WLD token distribution.
 *
 * @param {Object} props - The component props.
 * @param {number} props.totalTokens - The total number of $WLD tokens available for distribution.
 * @param {number} props.tokensDistributed - The number of $WLD tokens already distributed.
 * @param {Date} props.endDate - The end date for the distribution.
 */
const TokenDistribution = ({ totalTokens, tokensDistributed, endDate }) => {
  const [timeRemaining, setTimeRemaining] = useState(calculateTimeRemaining(endDate));
  const [progress, setProgress] = useState(calculateProgress(totalTokens, tokensDistributed));

  // Calculate time remaining until distribution end date
  function calculateTimeRemaining(endDate) {
    const now = new Date();
    const timeLeft = endDate - now;
    return timeLeft > 0 ? Math.floor(timeLeft / 1000) : 0; // Return seconds
  }

  // Calculate distribution progress percentage
  function calculateProgress(total, distributed) {
    return total > 0 ? (distributed / total) * 100 : 0;
  }

  // Update countdown every second
  useEffect(() => {
    const timer = setInterval(() => {
      const newTimeRemaining = calculateTimeRemaining(endDate);
      if (newTimeRemaining <= 0) {
        clearInterval(timer);
      }
      setTimeRemaining(newTimeRemaining);
      setProgress(calculateProgress(totalTokens, tokensDistributed));
    }, 1000);

    // Cleanup on unmount
    return () => clearInterval(timer);
  }, [endDate, tokensDistributed, totalTokens]);

  return (
    <div className="token-distribution">
      <h2>$WLD Token Distribution Progress</h2>
      <div className="progress-container">
        <div className="progress-bar" style={{ width: `${progress}%` }}>
          {`${Math.round(progress)}% Distributed`}
        </div>
      </div>
      <p>{`Tokens Distributed: ${tokensDistributed}`}</p>
      <p>{`Total Tokens: ${totalTokens}`}</p>
      <p>{`Time Remaining: ${timeRemaining} seconds`}</p>
    </div>
  );
};

TokenDistribution.propTypes = {
  totalTokens: PropTypes.number.isRequired,
  tokensDistributed: PropTypes.number.isRequired,
  endDate: PropTypes.instanceOf(Date).isRequired,
};

export default TokenDistribution;
```

```css
/* TokenDistribution.css */
.token-distribution {
  font-family: Arial, sans-serif;
  text-align: center;
  margin: 20px;
}

.progress-container {
  background-color: #e0e0e0;
  border-radius: 25px;
  overflow: hidden;
  height: 30px;
  margin: 20px 0;
}

.progress-bar {
  background-color: #76c7c0;
  height: 100%;
  text-align: center;
  line-height: 30px; /* Center text vertically */
  color: white;
  transition: width 0.5s ease-in-out;
}
```
