"""
Generated Code Metadata:
========================
Original URL: https://presale-humanizedai.web.app
Prompt: Develop a feature that allows users to select staking percentages (e.g., 25%, 50%, 75%, MAX) and update the calculated earnings accordingly, as seen on the HumanizedAi staking page.
Generated: DETERMINISTIC_49ba4546cda5961a
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// StakingCalculator.js
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * StakingCalculator component for calculating staking rewards based on user input.
 * @param {Object} props - Component props.
 * @param {number} props.maxStake - Maximum amount available for staking.
 * @param {number} props.apy - Annual Percentage Yield for staking.
 * @param {function} props.onStakeChange - Callback when stake amount changes.
 */
const StakingCalculator = ({ maxStake, apy, onStakeChange }) => {
  const [stakeAmount, setStakeAmount] = useState(0);
  const [selectedPercentage, setSelectedPercentage] = useState(null);
  const [earnings, setEarnings] = useState(0);

  // Predefined percentage options
  const percentageOptions = [
    { label: '25%', value: 0.25 },
    { label: '50%', value: 0.5 },
    { label: '75%', value: 0.75 },
    { label: 'MAX', value: 1 }
  ];

  // Calculate earnings whenever stakeAmount or APY changes
  useEffect(() => {
    if (maxStake > 0 && apy > 0) {
      const calculatedEarnings = (stakeAmount * apy) / 100;
      setEarnings(calculatedEarnings);
    }
  }, [stakeAmount, apy, maxStake]);

  /**
   * Handle percentage selection.
   * @param {number} percentage - Selected percentage (0-1).
   */
  const handlePercentageSelect = (percentage) => {
    try {
      if (percentage < 0 || percentage > 1) {
        throw new Error('Percentage must be between 0 and 1');
      }

      const newStakeAmount = maxStake * percentage;
      setStakeAmount(newStakeAmount);
      setSelectedPercentage(percentage);
      onStakeChange(newStakeAmount);
    } catch (error) {
      console.error('Error in handlePercentageSelect:', error.message);
    }
  };

  /**
   * Handle manual stake amount input.
   * @param {Object} e - Input change event.
   */
  const handleManualInput = (e) => {
    try {
      const value = parseFloat(e.target.value);
      if (isNaN(value)) return;

      if (value < 0) {
        throw new Error('Stake amount cannot be negative');
      }

      if (value > maxStake) {
        throw new Error('Stake amount exceeds maximum available');
      }

      setStakeAmount(value);
      setSelectedPercentage(null); // Reset percentage selection
      onStakeChange(value);
    } catch (error) {
      console.error('Error in handleManualInput:', error.message);
    }
  };

  return (
    <div className="staking-calculator">
      <div className="stake-input-section">
        <h3>Stake Amount</h3>
        <div className="percentage-buttons">
          {percentageOptions.map((option) => (
            <button
              key={option.label}
              className={`percentage-button ${
                selectedPercentage === option.value ? 'active' : ''
              }`}
              onClick={() => handlePercentageSelect(option.value)}
            >
              {option.label}
            </button>
          ))}
        </div>
        <div className="manual-input">
          <input
            type="number"
            value={stakeAmount}
            onChange={handleManualInput}
            min="0"
            max={maxStake}
            step="0.01"
            placeholder="Enter amount"
          />
          <span className="max-available">Max: {maxStake}</span>
        </div>
      </div>

      <div className="earnings-section">
        <h3>Projected Earnings</h3>
        <div className="earnings-display">
          <div className="earnings-value">{earnings.toFixed(2)}</div>
          <div className="earnings-label">per year at {apy}% APY</div>
        </div>
      </div>
    </div>
  );
};

StakingCalculator.propTypes = {
  maxStake: PropTypes.number.isRequired,
  apy: PropTypes.number.isRequired,
  onStakeChange: PropTypes.func.isRequired
};

export default StakingCalculator;
```

```css
/* StakingCalculator.css */
.staking-calculator {
  font-family: 'Arial', sans-serif;
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border-radius: 8px;
  background-color: #f5f5f5;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.stake-input-section, .earnings-section {
  margin-bottom: 20px;
}

.percentage-buttons {
  display: flex;
  gap: 10px;
  margin-bottom: 15px;
}

.percentage-button {
  flex: 1;
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background-color: white;
  cursor: pointer;
  transition: all 0.2s;
}

.percentage-button:hover {
  background-color: #f0f0f0;
}

.percentage-button.active {
  background-color: #6200ee;
  color: white;
  border-color: #6200ee;
}

.manual-input {
  display: flex;
  align-items: center;
  gap: 10px;
}

.manual-input input {
  flex: 1;
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.max-available {
  font-size: 0.8em;
  color: #666;
}

.earnings-display {
  text-align: center;
  padding: 15px;
  background-color: white;
  border-radius: 4px;
  border: 1px solid #ddd;
}

.earnings-value {
  font-size: 24px;
  font-weight: bold;
  color: #6200ee;
}

.earnings-label {
  font-size: 14px;
  color: #666;
}
```
