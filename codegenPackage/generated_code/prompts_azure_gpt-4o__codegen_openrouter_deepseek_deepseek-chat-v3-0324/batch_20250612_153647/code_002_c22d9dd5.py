"""
Generated Code Metadata:
========================
Original URL: https://develop--celadon-praline-71fe9f.netlify.app
Prompt: Generate a React component for a deposit widget, inspired by the Aarc Deposit Widget Demo, with basic functionality for user input and submission.
Generated: DETERMINISTIC_c22d9dd582c4fc4f
Batch ID: 20250612_153647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState } from 'react';
import PropTypes from 'prop-types';

/**
 * DepositWidget - A component for handling deposit transactions.
 * 
 * @param {Object} props - Component props
 * @param {Function} props.onDeposit - Callback function triggered on deposit submission
 * @param {string} [props.defaultToken='ETH'] - Default token symbol
 * @param {number} [props.defaultAmount=0] - Default deposit amount
 * @returns {JSX.Element} DepositWidget component
 */
const DepositWidget = ({ onDeposit, defaultToken = 'ETH', defaultAmount = 0 }) => {
  const [amount, setAmount] = useState(defaultAmount);
  const [token, setToken] = useState(defaultToken);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleAmountChange = (e) => {
    const value = parseFloat(e.target.value);
    if (!isNaN(value)) {
      setAmount(value);
      setError(null);
    }
  };

  const handleTokenChange = (e) => {
    setToken(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (amount <= 0) {
      setError('Amount must be greater than 0');
      return;
    }

    setIsLoading(true);
    setError(null);

    try {
      await onDeposit({ amount, token });
      setAmount(0);
    } catch (err) {
      setError(err.message || 'Deposit failed. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="deposit-widget">
      <h2>Deposit Funds</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="amount">Amount</label>
          <input
            type="number"
            id="amount"
            value={amount}
            onChange={handleAmountChange}
            step="0.0001"
            min="0"
            placeholder="Enter amount"
            required
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="token">Token</label>
          <select id="token" value={token} onChange={handleTokenChange}>
            <option value="ETH">ETH</option>
            <option value="USDC">USDC</option>
            <option value="DAI">DAI</option>
            <option value="WBTC">WBTC</option>
          </select>
        </div>
        
        {error && <div className="error-message">{error}</div>}
        
        <button type="submit" disabled={isLoading}>
          {isLoading ? 'Processing...' : 'Deposit'}
        </button>
      </form>
    </div>
  );
};

DepositWidget.propTypes = {
  onDeposit: PropTypes.func.isRequired,
  defaultToken: PropTypes.string,
  defaultAmount: PropTypes.number
};

export default DepositWidget;
```
