"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://develop--celadon-praline-71fe9f.netlify.app
Prompt: Generate a React component for a deposit widget, inspired by the Aarc Deposit Widget Demo, with basic functionality for user input and submission.
Generated: DETERMINISTIC_c22d9dd582c4fc4f
Batch ID: 20250612_153647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import './DepositWidget.css'; // Importing CSS for styling

const DepositWidget = ({ onSubmit }) => {
  // State to hold the deposit amount
  const [amount, setAmount] = useState('');
  // State to manage error messages
  const [error, setError] = useState('');

  // Handle input change
  const handleInputChange = (event) => {
    setAmount(event.target.value);
    setError(''); // Clear error on new input
  };

  // Handle form submission
  const handleSubmit = (event) => {
    event.preventDefault(); // Prevent default form submission
    const numericAmount = parseFloat(amount);

    // Validate the amount input
    if (isNaN(numericAmount) || numericAmount <= 0) {
      setError('Please enter a valid deposit amount.');
      return;
    }

    // Call the onSubmit prop with the valid amount
    onSubmit(numericAmount);
    setAmount(''); // Reset amount after submission
  };

  return (
    <div className="deposit-widget">
      <h2>Deposit Widget</h2>
      <form onSubmit={handleSubmit}>
        <div className="input-group">
          <label htmlFor="amount">Deposit Amount:</label>
          <input
            type="text"
            id="amount"
            value={amount}
            onChange={handleInputChange}
            placeholder="Enter amount"
            required
          />
        </div>
        {error && <p className="error-message">{error}</p>}
        <button type="submit" className="submit-button">Deposit</button>
      </form>
    </div>
  );
};

// PropTypes validation for the component props
DepositWidget.propTypes = {
  onSubmit: PropTypes.func.isRequired, // onSubmit must be a function
};

// Default export of the component
export default DepositWidget;
```

```css
/* DepositWidget.css */
.deposit-widget {
  border: 1px solid #ccc;
  padding: 20px;
  border-radius: 5px;
  width: 300px;
  margin: 20px auto;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.input-group {
  margin-bottom: 15px;
}

input[type="text"] {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.submit-button {
  background-color: #28a745;
  color: white;
  padding: 10px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.submit-button:hover {
  background-color: #218838;
}

.error-message {
  color: red;
  font-size: 0.9em;
}
```
