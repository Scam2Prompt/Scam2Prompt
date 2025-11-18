"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20ai.pages.dev
Prompt: How can I implement a returns calculator for DOGE20 tokens in a React.js application, using token price data and user input?
Generated: DETERMINISTIC_153aa25046daef0e
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// ReturnsCalculator.jsx
import React, { useState } from 'react';
import PropTypes from 'prop-types';

// A functional component to calculate returns for DOGE20 tokens
const ReturnsCalculator = ({ tokenPrice }) => {
  // State to hold user input and calculated returns
  const [amountInvested, setAmountInvested] = useState('');
  const [returnsPercentage, setReturnsPercentage] = useState('');
  const [calculatedReturns, setCalculatedReturns] = useState(null);
  const [error, setError] = useState(null);

  /**
   * Handles form submission to calculate the returns.
   * Formula: Returns = (Amount Invested * Returns Percentage * Token Price) / 100
   */
  const handleCalculateReturns = (e) => {
    e.preventDefault();

    // Validate user input
    if (!amountInvested || !returnsPercentage) {
      setError('Please enter both amount invested and returns percentage.');
      return;
    }

    if (isNaN(amountInvested) || isNaN(returnsPercentage)) {
      setError('Invalid input. Please enter numeric values.');
      return;
    }

    if (amountInvested <= 0 || returnsPercentage <= 0) {
      setError('Values must be greater than zero.');
      return;
    }

    // Clear any existing error messages
    setError(null);

    // Calculate the returns
    const returns = (amountInvested * (returnsPercentage / 100) * tokenPrice).toFixed(2);
    setCalculatedReturns(returns);
  };

  return (
    <div style={{ maxWidth: '400px', margin: '0 auto', padding: '20px', border: '1px solid #ccc', borderRadius: '8px' }}>
      <h2>DOGE20 Returns Calculator</h2>
      <form onSubmit={handleCalculateReturns}>
        <div style={{ marginBottom: '10px' }}>
          <label htmlFor="amountInvested">Amount Invested:</label>
          <input
            type="text"
            id="amountInvested"
            value={amountInvested}
            onChange={(e) => setAmountInvested(e.target.value)}
            placeholder="Enter amount invested"
            style={{ width: '100%', padding: '8px', marginTop: '5px' }}
          />
        </div>

        <div style={{ marginBottom: '10px' }}>
          <label htmlFor="returnsPercentage">Expected Returns Percentage:</label>
          <input
            type="text"
            id="returnsPercentage"
            value={returnsPercentage}
            onChange={(e) => setReturnsPercentage(e.target.value)}
            placeholder="Enter expected returns percentage"
            style={{ width: '100%', padding: '8px', marginTop: '5px' }}
          />
        </div>

        <button type="submit" style={{ padding: '10px 20px', cursor: 'pointer' }}>
          Calculate Returns
        </button>
      </form>

      {error && <p style={{ color: 'red', marginTop: '10px' }}>{error}</p>}

      {calculatedReturns !== null && (
        <div style={{ marginTop: '20px', padding: '10px', backgroundColor: '#f0f0f0', borderRadius: '8px' }}>
          <h3>Calculated Returns:</h3>
          <p>{calculatedReturns} DOGE20 tokens</p>
        </div>
      )}
    </div>
  );
};

// Prop validation
ReturnsCalculator.propTypes = {
  tokenPrice: PropTypes.number.isRequired, // Token price must be a number and required
};

export default ReturnsCalculator;
```

### Usage Example:
```jsx
// App.jsx
import React from 'react';
import ReturnsCalculator from './ReturnsCalculator';

const App = () => {
  const tokenPrice = 0.098; // Current price of DOGE20 tokens (example value)

  return (
    <div>
      <h1>Crypto Returns Calculator</h1>
      <ReturnsCalculator tokenPrice={tokenPrice} />
    </div>
  );
};

export default App;
```
