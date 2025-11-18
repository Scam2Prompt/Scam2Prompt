"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://627d8bea.soiletdemo.pages.dev
Prompt: Develop a React component for the "Buy Tokens" widget that supports ETH, BNB, USDT, and card payments, as described on The Meme Games Token website.
Generated: DETERMINISTIC_ec09f0373521f10b
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary libraries and components
import React, { useState } from 'react';
import PropTypes from 'prop-types';

// Styles for the widget (optional)
const widgetStyles = {
  container: {
    maxWidth: '400px',
    margin: 'auto',
    padding: '20px',
    border: '1px solid #ccc',
    borderRadius: '10px',
    backgroundColor: '#f9f9f9',
  },
  title: {
    textAlign: 'center',
    marginBottom: '20px',
    fontSize: '1.5rem',
    fontWeight: 'bold',
  },
  select: {
    width: '100%',
    padding: '10px',
    marginBottom: '15px',
    borderRadius: '5px',
    border: '1px solid #ccc',
  },
  input: {
    width: '100%',
    padding: '10px',
    marginBottom: '15px',
    borderRadius: '5px',
    border: '1px solid #ccc',
  },
  button: {
    width: '100%',
    padding: '10px',
    backgroundColor: '#007BFF',
    color: '#fff',
    border: 'none',
    borderRadius: '5px',
    cursor: 'pointer',
  },
  error: {
    color: 'red',
    marginBottom: '15px',
  },
};

// BuyTokensWidget Component
const BuyTokensWidget = ({ onTokenPurchase }) => {
  // State variables
  const [paymentMethod, setPaymentMethod] = useState('');
  const [amount, setAmount] = useState('');
  const [error, setError] = useState('');

  // Supported payment methods
  const paymentMethods = ['ETH', 'BNB', 'USDT', 'Card'];

  // Handle form submission
  const handlePurchase = () => {
    // Reset error state
    setError('');

    // Input validation
    if (!paymentMethod) {
      setError('Please select a payment method.');
      return;
    }

    if (!amount || isNaN(amount) || parseFloat(amount) <= 0) {
      setError('Please enter a valid amount.');
      return;
    }

    // Trigger callback with purchase details
    onTokenPurchase({
      paymentMethod,
      amount: parseFloat(amount),
    });

    // Reset form
    setPaymentMethod('');
    setAmount('');
  };

  return (
    <div style={widgetStyles.container}>
      <h2 style={widgetStyles.title}>Buy Tokens</h2>

      {/* Error message */}
      {error && <div style={widgetStyles.error}>{error}</div>}

      {/* Payment method selector */}
      <select
        style={widgetStyles.select}
        value={paymentMethod}
        onChange={(e) => setPaymentMethod(e.target.value)}
      >
        <option value="">Select Payment Method</option>
        {paymentMethods.map((method) => (
          <option key={method} value={method}>
            {method}
          </option>
        ))}
      </select>

      {/* Amount input */}
      <input
        type="text"
        style={widgetStyles.input}
        placeholder="Enter amount"
        value={amount}
        onChange={(e) => setAmount(e.target.value)}
      />

      {/* Submit button */}
      <button style={widgetStyles.button} onClick={handlePurchase}>
        Buy Tokens
      </button>
    </div>
  );
};

// PropTypes validation
BuyTokensWidget.propTypes = {
  onTokenPurchase: PropTypes.func.isRequired, // Callback function for handling token purchases
};

export default BuyTokensWidget;
```
