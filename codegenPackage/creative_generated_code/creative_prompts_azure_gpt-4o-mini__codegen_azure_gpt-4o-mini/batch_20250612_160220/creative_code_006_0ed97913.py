"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://affinityprimetrade.com
Prompt: Create a user interface in React that displays the various trading account types offered by Affinity Prime Trade, including their minimum and maximum investment amounts.
Generated: DETERMINISTIC_0ed9791355e1997f
Batch ID: 20250612_160220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React from 'react';
import PropTypes from 'prop-types';
import './TradingAccountTypes.css'; // CSS for styling

// Sample data representing trading account types
const accountTypes = [
  {
    id: 1,
    name: 'Standard Account',
    minInvestment: 1000,
    maxInvestment: 100000,
  },
  {
    id: 2,
    name: 'Premium Account',
    minInvestment: 5000,
    maxInvestment: 500000,
  },
  {
    id: 3,
    name: 'VIP Account',
    minInvestment: 10000,
    maxInvestment: 1000000,
  },
];

// TradingAccountTypes component to display account information
const TradingAccountTypes = () => {
  return (
    <div className="trading-account-types">
      <h1>Affinity Prime Trade - Trading Account Types</h1>
      <ul>
        {accountTypes.map((account) => (
          <li key={account.id} className="account-item">
            <h2>{account.name}</h2>
            <p>Minimum Investment: ${account.minInvestment.toLocaleString()}</p>
            <p>Maximum Investment: ${account.maxInvestment.toLocaleString()}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

// PropTypes for future extensibility and validation
TradingAccountTypes.propTypes = {
  accountTypes: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.number.isRequired,
      name: PropTypes.string.isRequired,
      minInvestment: PropTypes.number.isRequired,
      maxInvestment: PropTypes.number.isRequired,
    })
  ),
};

// Export the component for use in other parts of the application
export default TradingAccountTypes;
```

```css
/* TradingAccountTypes.css */
/* Basic styling for the trading account types component */

.trading-account-types {
  font-family: Arial, sans-serif;
  padding: 20px;
}

h1 {
  color: #333;
  font-size: 24px;
}

.account-item {
  border: 1px solid #ccc;
  border-radius: 5px;
  margin: 10px 0;
  padding: 15px;
  background-color: #f9f9f9;
}

.account-item h2 {
  font-size: 20px;
  margin: 0;
}

.account-item p {
  margin: 5px 0;
  font-size: 16px;
}
```
