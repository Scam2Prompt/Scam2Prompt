"""
Generated Code Metadata:
========================
Original URL: https://qubeticstoken-live.web.app
Prompt: Create a React component for the Qubetics "How to Buy" page that dynamically displays payment options and guides users through the token purchase process.
Generated: DETERMINISTIC_27678ac48e8dec0c
Batch ID: 20250612_154236
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
 * PaymentOption component for displaying individual payment method details
 */
const PaymentOption = ({ method, icon, steps, isSelected, onSelect }) => {
  return (
    <div 
      className={`payment-option ${isSelected ? 'selected' : ''}`}
      onClick={() => onSelect(method)}
    >
      <div className="payment-header">
        <img src={icon} alt={`${method} icon`} className="payment-icon" />
        <h3>{method}</h3>
      </div>
      {isSelected && (
        <div className="payment-steps">
          {steps.map((step, index) => (
            <div key={index} className="step">
              <span className="step-number">{index + 1}</span>
              <p>{step}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

PaymentOption.propTypes = {
  method: PropTypes.string.isRequired,
  icon: PropTypes.string.isRequired,
  steps: PropTypes.arrayOf(PropTypes.string).isRequired,
  isSelected: PropTypes.bool.isRequired,
  onSelect: PropTypes.func.isRequired
};

/**
 * HowToBuy component - Main component for the Qubetics "How to Buy" page
 */
const HowToBuy = () => {
  const [selectedMethod, setSelectedMethod] = useState(null);
  const [paymentMethods, setPaymentMethods] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchPaymentMethods = async () => {
      try {
        // In a real app, this would be an API call
        const mockPaymentMethods = [
          {
            method: 'Credit Card',
            icon: '/icons/credit-card.svg',
            steps: [
              'Enter your card details',
              'Verify your identity',
              'Confirm the transaction',
              'Receive your QUBE tokens'
            ]
          },
          {
            method: 'Bank Transfer',
            icon: '/icons/bank-transfer.svg',
            steps: [
              'Select bank transfer option',
              'Send funds to provided account',
              'Wait for confirmation (1-3 business days)',
              'Receive your QUBE tokens'
            ]
          },
          {
            method: 'Crypto Swap',
            icon: '/icons/crypto-swap.svg',
            steps: [
              'Connect your wallet',
              'Select token to swap',
              'Confirm swap transaction',
              'Receive QUBE tokens instantly'
            ]
          }
        ];

        setPaymentMethods(mockPaymentMethods);
        setLoading(false);
      } catch (err) {
        setError('Failed to load payment methods. Please try again later.');
        setLoading(false);
        console.error('Error fetching payment methods:', err);
      }
    };

    fetchPaymentMethods();
  }, []);

  const handleMethodSelect = (method) => {
    setSelectedMethod(method === selectedMethod ? null : method);
  };

  if (loading) {
    return <div className="loading">Loading payment options...</div>;
  }

  if (error) {
    return <div className="error">{error}</div>;
  }

  return (
    <div className="how-to-buy-container">
      <h1>How to Buy QUBE Tokens</h1>
      <p className="subtitle">Select your preferred payment method below</p>
      
      <div className="payment-options">
        {paymentMethods.map((option) => (
          <PaymentOption
            key={option.method}
            method={option.method}
            icon={option.icon}
            steps={option.steps}
            isSelected={selectedMethod === option.method}
            onSelect={handleMethodSelect}
          />
        ))}
      </div>

      {selectedMethod && (
        <div className="disclaimer">
          <p>
            <strong>Important:</strong> Always verify transaction details before completing your purchase.
            Qubetics is not responsible for incorrect transactions.
          </p>
        </div>
      )}
    </div>
  );
};

export default HowToBuy;
```
