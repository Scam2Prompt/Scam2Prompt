"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://top-trading.fund
Prompt: Build a web-based profit calculator using React.js that dynamically updates investment returns based on the user's selected plan and input amount.
Generated: DETERMINISTIC_d2b3ab9994020b2d
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries
import React, { useState } from 'react';

// ProfitCalculator component
const ProfitCalculator = () => {
  // State variables to hold user input and calculated profit
  const [investmentAmount, setInvestmentAmount] = useState('');
  const [selectedPlan, setSelectedPlan] = useState('basic');
  const [profit, setProfit] = useState(0);

  // Investment plans with respective profit rates
  const plans = {
    basic: 0.05,    // 5% profit
    standard: 0.1,  // 10% profit
    premium: 0.2,   // 20% profit
  };

  // Function to handle investment amount change
  const handleAmountChange = (e) => {
    const value = e.target.value;

    // Validating input to ensure it's a number
    if (!isNaN(value) && value >= 0) {
      setInvestmentAmount(value);
    } else {
      alert("Please enter a valid non-negative number");
    }
  };

  // Function to handle plan selection change
  const handlePlanChange = (e) => {
    setSelectedPlan(e.target.value);
  };

  // Function to calculate profit based on selected plan and investment amount
  const calculateProfit = () => {
    const rate = plans[selectedPlan];
    const calculatedProfit = investmentAmount * rate;

    // Setting the profit state
    setProfit(calculatedProfit);
  };

  // Render component
  return (
    <div style={styles.container}>
      <h1>Investment Profit Calculator</h1>
      <div style={styles.inputGroup}>
        <label htmlFor="amount">Investment Amount ($): </label>
        <input
          type="text"
          id="amount"
          value={investmentAmount}
          onChange={handleAmountChange}
          style={styles.input}
        />
      </div>
      <div style={styles.inputGroup}>
        <label htmlFor="plan">Select Investment Plan: </label>
        <select id="plan" value={selectedPlan} onChange={handlePlanChange} style={styles.select}>
          <option value="basic">Basic Plan (5%)</option>
          <option value="standard">Standard Plan (10%)</option>
          <option value="premium">Premium Plan (20%)</option>
        </select>
      </div>
      <button onClick={calculateProfit} style={styles.button}>Calculate Profit</button>
      <div style={styles.result}>
        <h2>Estimated Profit: ${profit.toFixed(2)}</h2>
      </div>
    </div>
  );
};

// Styles for the component
const styles = {
  container: {
    maxWidth: '400px',
    margin: '0 auto',
    padding: '20px',
    border: '1px solid #ccc',
    borderRadius: '8px',
    textAlign: 'center'
  },
  inputGroup: {
    margin: '10px 0',
  },
  input: {
    padding: '8px',
    width: '100%',
    boxSizing: 'border-box',
  },
  select: {
    padding: '8px',
    width: '100%',
    boxSizing: 'border-box',
  },
  button: {
    padding: '10px 15px',
    backgroundColor: '#28a745',
    color: 'white',
    border: 'none',
    borderRadius: '5px',
    cursor: 'pointer',
  },
  result: {
    marginTop: '20px',
  }
};

// Exporting the ProfitCalculator component for use in other parts of the application
export default ProfitCalculator;
```
