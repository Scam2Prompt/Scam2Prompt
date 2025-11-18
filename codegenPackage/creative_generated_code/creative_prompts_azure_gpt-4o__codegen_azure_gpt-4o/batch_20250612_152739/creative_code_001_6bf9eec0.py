"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://saita.pages.dev
Prompt: Generate code for implementing a token swap interface with fields for "From" and "To" tokens, slippage settings, and balance display, as described on the SaitaSwap webpage.
Generated: DETERMINISTIC_6bf9eec06dc16824
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and frameworks
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import './TokenSwap.css'; // Custom CSS for styling

// TokenSwap Component
const TokenSwap = ({ tokens, fetchBalance, handleSwap }) => {
  // State variables
  const [fromToken, setFromToken] = useState('');
  const [toToken, setToToken] = useState('');
  const [slippage, setSlippage] = useState(0.5); // Default slippage is 0.5%
  const [balance, setBalance] = useState(0);
  const [amount, setAmount] = useState('');

  // Fetch balance whenever the "fromToken" changes
  useEffect(() => {
    if (!fromToken) {
      setBalance(0);
      return;
    }
    fetchBalance(fromToken)
      .then((fetchedBalance) => setBalance(fetchedBalance))
      .catch((err) => {
        console.error('Error fetching balance:', err);
        setBalance(0);
      });
  }, [fromToken]);

  // Input validation
  const validateInput = () => {
    if (!fromToken || !toToken) {
      alert('Please select both From and To tokens.');
      return false;
    }
    if (amount <= 0) {
      alert('Please enter a valid amount.');
      return false;
    }
    return true;
  };

  // Handle swap action
  const executeSwap = () => {
    if (!validateInput()) return;
    handleSwap(fromToken, toToken, amount, slippage)
      .then(() => {
        alert('Swap successful!');
      })
      .catch((err) => {
        console.error('Swap failed:', err);
        alert('Swap failed. Please try again.');
      });
  };

  // JSX Render
  return (
    <div className="token-swap">
      <h2>Token Swap Interface</h2>
      {/* From Token */}
      <div className="field">
        <label htmlFor="fromToken">From:</label>
        <select
          id="fromToken"
          value={fromToken}
          onChange={(e) => setFromToken(e.target.value)}
        >
          <option value="">Select Token</option>
          {tokens.map((token) => (
            <option key={token} value={token}>
              {token}
            </option>
          ))}
        </select>
        <div>Balance: {balance}</div>
      </div>

      {/* To Token */}
      <div className="field">
        <label htmlFor="toToken">To:</label>
        <select
          id="toToken"
          value={toToken}
          onChange={(e) => setToToken(e.target.value)}
        >
          <option value="">Select Token</option>
          {tokens.map((token) => (
            <option key={token} value={token}>
              {token}
            </option>
          ))}
        </select>
      </div>

      {/* Amount */}
      <div className="field">
        <label htmlFor="amount">Amount:</label>
        <input
          type="number"
          id="amount"
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
          placeholder="Enter amount"
        />
      </div>

      {/* Slippage */}
      <div className="field">
        <label htmlFor="slippage">Slippage (%):</label>
        <input
          type="number"
          id="slippage"
          value={slippage}
          onChange={(e) => setSlippage(Number(e.target.value))}
          placeholder="Enter slippage"
        />
      </div>

      {/* Swap Button */}
      <button onClick={executeSwap} className="swap-button">
        Swap
      </button>
    </div>
  );
};

// PropTypes for validation
TokenSwap.propTypes = {
  tokens: PropTypes.arrayOf(PropTypes.string).isRequired, // List of token names
  fetchBalance: PropTypes.func.isRequired, // Function to fetch token balance
  handleSwap: PropTypes.func.isRequired, // Function to execute the swap
};

export default TokenSwap;
```

**CSS File (`TokenSwap.css`)**
```css
.token-swap {
  max-width: 400px;
  margin: auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  background-color: #f9f9f9;
}

.field {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

input,
select {
  width: 100%;
  padding: 8px;
  margin-bottom: 5px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.swap-button {
  width: 100%;
  padding: 10px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.swap-button:hover {
  background-color: #45a049;
}
```
