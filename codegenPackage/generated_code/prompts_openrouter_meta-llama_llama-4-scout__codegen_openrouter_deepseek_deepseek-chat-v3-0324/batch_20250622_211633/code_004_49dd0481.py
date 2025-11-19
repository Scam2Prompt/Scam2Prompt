"""
Generated Code Metadata:
========================
Original URL: https://widget-builder-cihe26ic7-superfluid-finance.vercel.app
Prompt: "Generate a demo for a Web3 subscription service with a checkout builder that supports real-time payments and easy export of the checkout component."
Generated: DETERMINISTIC_49dd048122909caa
Batch ID: 20250622_211633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Web3SubscriptionDemo.js
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import './Web3SubscriptionDemo.css';

/**
 * Web3 Subscription Service Demo
 * Features:
 * - Checkout builder with real-time payments
 * - Easy export of checkout component
 * - Supports Ethereum mainnet and testnets
 */

// Mock subscription plans
const subscriptionPlans = [
  {
    id: 'basic',
    name: 'Basic Plan',
    price: ethers.utils.parseEther('0.01'),
    features: ['Feature 1', 'Feature 2'],
    duration: 30 // days
  },
  {
    id: 'pro',
    name: 'Pro Plan',
    price: ethers.utils.parseEther('0.05'),
    features: ['Feature 1', 'Feature 2', 'Feature 3'],
    duration: 30 // days
  },
  {
    id: 'enterprise',
    name: 'Enterprise Plan',
    price: ethers.utils.parseEther('0.1'),
    features: ['All Features', 'Priority Support'],
    duration: 30 // days
  }
];

// Checkout component
const Checkout = ({ plan, onPaymentComplete, onCancel }) => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handlePayment = async () => {
    try {
      setLoading(true);
      setError(null);
      
      if (!window.ethereum) {
        throw new Error('MetaMask not detected');
      }

      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const signer = provider.getSigner();
      const address = await signer.getAddress();

      // In a real app, you would call your smart contract here
      // This is a mock implementation
      await new Promise(resolve => setTimeout(resolve, 2000));
      
      onPaymentComplete({
        txHash: '0x' + Math.random().toString(16).substr(2, 64),
        planId: plan.id,
        address
      });
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="checkout-container">
      <h3>Checkout</h3>
      <div className="plan-details">
        <h4>{plan.name}</h4>
        <p>Price: {ethers.utils.formatEther(plan.price)} ETH</p>
        <ul>
          {plan.features.map((feature, i) => (
            <li key={i}>{feature}</li>
          ))}
        </ul>
      </div>
      
      {error && <div className="error">{error}</div>}
      
      <div className="checkout-actions">
        <button onClick={onCancel}>Cancel</button>
        <button 
          onClick={handlePayment} 
          disabled={loading}
        >
          {loading ? 'Processing...' : 'Pay with MetaMask'}
        </button>
      </div>
    </div>
  );
};

// Main component
const Web3SubscriptionDemo = () => {
  const [selectedPlan, setSelectedPlan] = useState(null);
  const [paymentComplete, setPaymentComplete] = useState(false);
  const [exportCode, setExportCode] = useState('');

  const handlePlanSelect = (plan) => {
    setSelectedPlan(plan);
    setPaymentComplete(false);
  };

  const handlePaymentComplete = (receipt) => {
    console.log('Payment complete:', receipt);
    setPaymentComplete(true);
  };

  const handleCancel = () => {
    setSelectedPlan(null);
  };

  const generateExportCode = () => {
    const code = `import Checkout from './Checkout';

const MyCheckout = () => (
  <Checkout 
    plan={${JSON.stringify(selectedPlan, null, 2)}}
    onPaymentComplete={(receipt) => console.log('Payment complete:', receipt)}
    onCancel={() => console.log('Checkout cancelled')}
  />
);

export default MyCheckout;`;

    setExportCode(code);
  };

  return (
    <div className="app-container">
      <h1>Web3 Subscription Service</h1>
      
      {!selectedPlan ? (
        <div className="plans-container">
          <h2>Select a Plan</h2>
          <div className="plan-cards">
            {subscriptionPlans.map(plan => (
              <div key={plan.id} className="plan-card">
                <h3>{plan.name}</h3>
                <p>{ethers.utils.formatEther(plan.price)} ETH/month</p>
                <ul>
                  {plan.features.map((feature, i) => (
                    <li key={i}>{feature}</li>
                  ))}
                </ul>
                <button onClick={() => handlePlanSelect(plan)}>Select</button>
              </div>
            ))}
          </div>
        </div>
      ) : paymentComplete ? (
        <div className="success-container">
          <h2>Payment Successful!</h2>
          <p>Thank you for subscribing to {selectedPlan.name}.</p>
          <button onClick={() => setSelectedPlan(null)}>Back to Plans</button>
          
          <div className="export-section">
            <h3>Export Checkout Component</h3>
            <button onClick={generateExportCode}>Generate Export Code</button>
            {exportCode && (
              <pre className="export-code">
                <code>{exportCode}</code>
              </pre>
            )}
          </div>
        </div>
      ) : (
        <Checkout 
          plan={selectedPlan} 
          onPaymentComplete={handlePaymentComplete}
          onCancel={handleCancel}
        />
      )}
    </div>
  );
};

export default Web3SubscriptionDemo;

// Web3SubscriptionDemo.css
.app-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
  font-family: Arial, sans-serif;
}

.plans-container {
  text-align: center;
}

.plan-cards {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
  margin-top: 2rem;
}

.plan-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 1.5rem;
  width: 300px;
  text-align: left;
}

.plan-card h3 {
  margin-top: 0;
}

.plan-card button {
  margin-top: 1rem;
  padding: 0.5rem 1rem;
  background: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.checkout-container {
  max-width: 500px;
  margin: 0 auto;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 1.5rem;
}

.checkout-actions {
  display: flex;
  justify-content: space-between;
  margin-top: 1.5rem;
}

.checkout-actions button {
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.checkout-actions button:first-child {
  background: #6c757d;
  color: white;
}

.checkout-actions button:last-child {
  background: #28a745;
  color: white;
}

.error {
  color: #dc3545;
  margin: 1rem 0;
}

.success-container {
  text-align: center;
  max-width: 600px;
  margin: 0 auto;
}

.success-container button {
  padding: 0.5rem 1rem;
  background: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-top: 1rem;
}

.export-section {
  margin-top: 2rem;
  text-align: left;
  border-top: 1px solid #ddd;
  padding-top: 1rem;
}

.export-section button {
  background: #17a2b8;
}

.export-code {
  background: #f8f9fa;
  padding: 1rem;
  border-radius: 4px;
  overflow-x: auto;
  margin-top: 1rem;
}
```
