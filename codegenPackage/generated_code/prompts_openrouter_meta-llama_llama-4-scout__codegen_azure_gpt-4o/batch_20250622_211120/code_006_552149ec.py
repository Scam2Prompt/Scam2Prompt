"""
Generated Code Metadata:
========================
Original URL: https://penpie.io
Prompt: Design a UI component to display the details of various liquidity pools on Penpie, including pool name, APY, TVL, and maturity date.
Generated: DETERMINISTIC_552149ecf3454afc
Batch ID: 20250622_211120
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React from 'react';
import PropTypes from 'prop-types';
import './LiquidityPoolCard.css'; // Import CSS for styling

/**
 * LiquidityPoolCard Component
 * Displays details of a liquidity pool including name, APY, TVL, and maturity date.
 *
 * Props:
 * - poolName (string): Name of the liquidity pool.
 * - apy (number): Annual Percentage Yield (APY) of the pool.
 * - tvl (number): Total Value Locked (TVL) in the pool.
 * - maturityDate (string): Maturity date of the pool in ISO format.
 */
const LiquidityPoolCard = ({ poolName, apy, tvl, maturityDate }) => {
  // Format TVL to include commas and currency symbol
  const formatTVL = (value) => {
    try {
      return `$${value.toLocaleString()}`;
    } catch (error) {
      console.error('Error formatting TVL:', error);
      return 'N/A';
    }
  };

  // Format APY to display as a percentage
  const formatAPY = (value) => {
    try {
      return `${value.toFixed(2)}%`;
    } catch (error) {
      console.error('Error formatting APY:', error);
      return 'N/A';
    }
  };

  // Format maturity date to a readable format
  const formatDate = (date) => {
    try {
      const options = { year: 'numeric', month: 'long', day: 'numeric' };
      return new Date(date).toLocaleDateString(undefined, options);
    } catch (error) {
      console.error('Error formatting maturity date:', error);
      return 'Invalid Date';
    }
  };

  return (
    <div className="liquidity-pool-card">
      <h2 className="pool-name">{poolName}</h2>
      <div className="pool-details">
        <p><strong>APY:</strong> {formatAPY(apy)}</p>
        <p><strong>TVL:</strong> {formatTVL(tvl)}</p>
        <p><strong>Maturity Date:</strong> {formatDate(maturityDate)}</p>
      </div>
    </div>
  );
};

// Define PropTypes for the component
LiquidityPoolCard.propTypes = {
  poolName: PropTypes.string.isRequired,
  apy: PropTypes.number.isRequired,
  tvl: PropTypes.number.isRequired,
  maturityDate: PropTypes.string.isRequired,
};

// Export the component for use in other parts of the application
export default LiquidityPoolCard;

/* CSS (LiquidityPoolCard.css)
.liquidity-pool-card {
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 16px;
  margin: 16px;
  background-color: #f9f9f9;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.pool-name {
  font-size: 1.5em;
  margin-bottom: 8px;
}

.pool-details p {
  margin: 4px 0;
  font-size: 1em;
}
*/
```
