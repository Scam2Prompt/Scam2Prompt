"""
Generated Code Metadata:
========================
Original URL: https://steep-zebra-teeny.on-fleek.app
Prompt: Design a basic UI component in React for a cryptocurrency swap feature that displays the swap amount, token prices, and estimated gas fees, similar to Zeedex's swap interface.
Generated: DETERMINISTIC_8b5ea7c07942c13c
Batch ID: 20250622_205030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * CryptocurrencySwapUI - A React component for displaying a cryptocurrency swap interface.
 * 
 * @param {Object} props - Component props
 * @param {string} props.defaultFromToken - Default 'from' token symbol
 * @param {string} props.defaultToToken - Default 'to' token symbol
 * @param {Array} props.availableTokens - List of available tokens for swap
 * @param {function} props.onSwap - Callback function when swap is initiated
 * @returns {JSX.Element} Swap UI component
 */
const CryptocurrencySwapUI = ({
  defaultFromToken = 'ETH',
  defaultToToken = 'USDT',
  availableTokens = ['ETH', 'USDT', 'BTC', 'DAI'],
  onSwap
}) => {
  const [fromToken, setFromToken] = useState(defaultFromToken);
  const [toToken, setToToken] = useState(defaultToToken);
  const [fromAmount, setFromAmount] = useState('');
  const [toAmount, setToAmount] = useState('');
  const [exchangeRate, setExchangeRate] = useState(0);
  const [gasFee, setGasFee] = useState(0);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  // Simulate fetching exchange rate and gas fee
  useEffect(() => {
    const fetchRates = async () => {
      if (!fromToken || !toToken || !fromAmount) return;
      
      try {
        setIsLoading(true);
        // In a real app, this would be an API call
        await new Promise(resolve => setTimeout(resolve, 500));
        
        // Mock data
        const mockRate = Math.random() * 10;
        const mockGasFee = Math.random() * 0.01;
        
        setExchangeRate(mockRate);
        setGasFee(mockGasFee);
        setToAmount((parseFloat(fromAmount) * mockRate).toFixed(6));
        setError(null);
      } catch (err) {
        setError('Failed to fetch exchange rates');
        console.error('Error fetching rates:', err);
      } finally {
        setIsLoading(false);
      }
    };

    fetchRates();
  }, [fromToken, toToken, fromAmount]);

  const handleFromAmountChange = (e) => {
    const value = e.target.value;
    if (value === '' || /^[0-9]*\.?[0-9]*$/.test(value)) {
      setFromAmount(value);
    }
  };

  const handleTokenChange = (token, isFromToken) => {
    if (isFromToken) {
      setFromToken(token);
    } else {
      setToToken(token);
    }
  };

  const handleSwapTokens = () => {
    setFromToken(toToken);
    setToToken(fromToken);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!fromAmount || parseFloat(fromAmount) <= 0) {
      setError('Please enter a valid amount');
      return;
    }
    if (onSwap) {
      onSwap({
        fromToken,
        toToken,
        fromAmount,
        toAmount,
        exchangeRate,
        gasFee
      });
    }
  };

  return (
    <div className="swap-container">
      <h2>Swap Tokens</h2>
      
      {error && <div className="error-message">{error}</div>}
      
      <form onSubmit={handleSubmit}>
        <div className="token-input">
          <label>From</label>
          <div className="input-group">
            <input
              type="text"
              value={fromAmount}
              onChange={handleFromAmountChange}
              placeholder="0.0"
              disabled={isLoading}
            />
            <TokenSelector
              selectedToken={fromToken}
              tokens={availableTokens}
              onChange={(token) => handleTokenChange(token, true)}
              disabled={isLoading}
            />
          </div>
        </div>
        
        <div className="swap-arrow" onClick={handleSwapTokens}>
          ↓
        </div>
        
        <div className="token-input">
          <label>To</label>
          <div className="input-group">
            <input
              type="text"
              value={toAmount}
              readOnly
              placeholder="0.0"
            />
            <TokenSelector
              selectedToken={toToken}
              tokens={availableTokens}
              onChange={(token) => handleTokenChange(token, false)}
              disabled={isLoading}
            />
          </div>
        </div>
        
        <div className="swap-details">
          <div className="detail-row">
            <span>Exchange Rate</span>
            <span>1 {fromToken} = {exchangeRate.toFixed(6)} {toToken}</span>
          </div>
          <div className="detail-row">
            <span>Estimated Gas Fee</span>
            <span>{gasFee.toFixed(6)} ETH</span>
          </div>
        </div>
        
        <button
          type="submit"
          className="swap-button"
          disabled={isLoading || !fromAmount || parseFloat(fromAmount) <= 0}
        >
          {isLoading ? 'Swapping...' : 'Swap'}
        </button>
      </form>
    </div>
  );
};

/**
 * TokenSelector - A dropdown component for selecting tokens.
 * 
 * @param {Object} props - Component props
 * @param {string} props.selectedToken - Currently selected token
 * @param {Array} props.tokens - Available tokens
 * @param {function} props.onChange - Callback when token is changed
 * @param {boolean} props.disabled - Whether the selector is disabled
 * @returns {JSX.Element} Token selector component
 */
const TokenSelector = ({ selectedToken, tokens, onChange, disabled }) => {
  return (
    <select
      value={selectedToken}
      onChange={(e) => onChange(e.target.value)}
      disabled={disabled}
    >
      {tokens.map((token) => (
        <option key={token} value={token}>
          {token}
        </option>
      ))}
    </select>
  );
};

TokenSelector.propTypes = {
  selectedToken: PropTypes.string.isRequired,
  tokens: PropTypes.arrayOf(PropTypes.string).isRequired,
  onChange: PropTypes.func.isRequired,
  disabled: PropTypes.bool
};

CryptocurrencySwapUI.propTypes = {
  defaultFromToken: PropTypes.string,
  defaultToToken: PropTypes.string,
  availableTokens: PropTypes.arrayOf(PropTypes.string),
  onSwap: PropTypes.func
};

export default CryptocurrencySwapUI;
```
