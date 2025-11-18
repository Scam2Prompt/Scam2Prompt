"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eteswap.pages.dev
Prompt: Develop a React component for selecting tokens and managing slippage tolerance, inspired by ETESwap's interface.
Generated: DETERMINISTIC_2038d6a5c57a6b20
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState } from "react";
import PropTypes from "prop-types";

/**
 * TokenSelector Component
 * A React component for selecting tokens and managing slippage tolerance.
 * Inspired by ETESwap's interface.
 */
const TokenSelector = ({ tokens, onTokenChange, onSlippageChange }) => {
  // State to store the selected token and slippage tolerance
  const [selectedToken, setSelectedToken] = useState(tokens[0]?.symbol || "");
  const [slippage, setSlippage] = useState("0.5"); // Default slippage tolerance: 0.5%

  // Handle token selection change
  const handleTokenChange = (event) => {
    const newToken = event.target.value;
    setSelectedToken(newToken);
    if (onTokenChange) {
      onTokenChange(newToken);
    }
  };

  // Handle slippage tolerance change
  const handleSlippageChange = (event) => {
    const newSlippage = event.target.value;
    if (!isNaN(newSlippage) && newSlippage >= 0 && newSlippage <= 100) {
      setSlippage(newSlippage);
      if (onSlippageChange) {
        onSlippageChange(newSlippage);
      }
    }
  };

  return (
    <div style={{ maxWidth: "400px", margin: "20px auto", padding: "20px", border: "1px solid #ccc", borderRadius: "8px" }}>
      {/* Token Selection Dropdown */}
      <div style={{ marginBottom: "20px" }}>
        <label htmlFor="token-select" style={{ display: "block", marginBottom: "8px" }}>Select Token:</label>
        <select 
          id="token-select" 
          value={selectedToken} 
          onChange={handleTokenChange} 
          style={{ width: "100%", padding: "8px", borderRadius: "4px", border: "1px solid #ccc" }}
        >
          {tokens.map((token) => (
            <option key={token.symbol} value={token.symbol}>
              {token.name} ({token.symbol})
            </option>
          ))}
        </select>
      </div>

      {/* Slippage Tolerance Input */}
      <div style={{ marginBottom: "20px" }}>
        <label htmlFor="slippage-input" style={{ display: "block", marginBottom: "8px" }}>Slippage Tolerance (%):</label>
        <input
          id="slippage-input"
          type="number"
          value={slippage}
          onChange={handleSlippageChange}
          step="0.1"
          min="0"
          max="100"
          style={{ width: "100%", padding: "8px", borderRadius: "4px", border: "1px solid #ccc" }}
        />
        <small style={{ color: "#888" }}>Enter a value between 0 and 100.</small>
      </div>
    </div>
  );
};

// PropTypes for validation
TokenSelector.propTypes = {
  tokens: PropTypes.arrayOf(
    PropTypes.shape({
      name: PropTypes.string.isRequired,
      symbol: PropTypes.string.isRequired,
    })
  ).isRequired,
  onTokenChange: PropTypes.func,
  onSlippageChange: PropTypes.func,
};

// Default props
TokenSelector.defaultProps = {
  onTokenChange: null,
  onSlippageChange: null,
};

export default TokenSelector;
```
