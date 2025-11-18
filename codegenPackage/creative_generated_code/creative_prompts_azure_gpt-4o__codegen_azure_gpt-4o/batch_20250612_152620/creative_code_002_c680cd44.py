"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-humanizedai.web.app
Prompt: Develop a web application interface using React that mimics the HumanizedAi staking platform, including features like HMZ balance display, lock duration selection, and calculated earnings preview.
Generated: DETERMINISTIC_c680cd44f0df60ec
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// HumanizedAi Staking Platform Interface
// File: App.js

import React, { useState } from 'react';
import './App.css'; // Importing custom CSS for styling

// Utility function to calculate earnings
const calculateEarnings = (balance, lockDuration) => {
  // Assuming a simple earnings calculation: 10% annual rate
  const annualRate = 0.10;
  const earnings = (balance * annualRate * lockDuration) / 12; // Prorated for months
  return earnings.toFixed(2); // Return with two decimal precision
};

const App = () => {
  // State to hold user's HMZ balance
  const [balance, setBalance] = useState('');
  // State to hold selected lock duration
  const [lockDuration, setLockDuration] = useState('');
  // State to display calculated earnings
  const [earnings, setEarnings] = useState(0);

  // Event handler for balance input change
  const handleBalanceChange = (e) => {
    const inputBalance = e.target.value;
    if (!isNaN(inputBalance)) {
      setBalance(inputBalance); // Update state if input is valid
    }
  };

  // Event handler for lock duration selection
  const handleLockDurationChange = (e) => {
    setLockDuration(e.target.value); // Update selected lock duration
  };

  // Event handler to calculate earnings
  const handleCalculateEarnings = () => {
    if (!balance || !lockDuration) {
      alert('Please fill in both HMZ balance and lock duration.');
      return;
    }
    const calculatedEarnings = calculateEarnings(parseFloat(balance), parseInt(lockDuration));
    setEarnings(calculatedEarnings); // Update earnings state
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>HumanizedAi Staking Platform</h1>
      </header>
      <main className="App-main">
        {/* HMZ Balance Input */}
        <div className="form-group">
          <label htmlFor="balance">HMZ Balance:</label>
          <input
            type="text"
            id="balance"
            value={balance}
            onChange={handleBalanceChange}
            placeholder="Enter your HMZ balance"
            className="form-control"
          />
        </div>

        {/* Lock Duration Selection */}
        <div className="form-group">
          <label htmlFor="lockDuration">Lock Duration (months):</label>
          <select
            id="lockDuration"
            value={lockDuration}
            onChange={handleLockDurationChange}
            className="form-control"
          >
            <option value="">Select</option>
            <option value="1">1 month</option>
            <option value="3">3 months</option>
            <option value="6">6 months</option>
            <option value="12">12 months</option>
          </select>
        </div>

        {/* Calculate Earnings Button */}
        <button onClick={handleCalculateEarnings} className="calculate-btn">
          Calculate Earnings
        </button>

        {/* Earnings Preview */}
        <div className="earnings-preview">
          <h2>Estimated Earnings: {earnings} HMZ</h2>
        </div>
      </main>
    </div>
  );
};

export default App;

/*
File: App.css
Basic CSS for styling the application
*/

.App {
  text-align: center;
  font-family: Arial, sans-serif;
}

.App-header {
  background-color: #282c34;
  padding: 20px;
  color: white;
}

.App-main {
  margin: 20px;
}

.form-group {
  margin-bottom: 15px;
}

.form-control {
  width: 300px;
  padding: 8px;
  margin: 5px 0;
}

.calculate-btn {
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.calculate-btn:hover {
  background-color: #0056b3;
}

.earnings-preview {
  margin-top: 20px;
  font-size: 1.2em;
  color: #333;
}

/*
File: index.js
Entry point of the React application
*/

import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

/*
File: index.css
Basic global styles
*/

body {
  margin: 0;
  padding: 0;
  background-color: #f5f5f5;
  color: #333;
}
```
