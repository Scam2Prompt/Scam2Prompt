"""
Generated Code Metadata:
========================
Original URL: https://trumpcoins-giveaway.web.app
Prompt: Develop a React component for displaying a portfolio of coins, handling cases where the portfolio might be empty, as indicated by "oops.. no coins here" on the provided webpage.
Generated: DETERMINISTIC_322503f8a869304a
Batch ID: 20250622_210423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// Import necessary libraries
import React from 'react';
import PropTypes from 'prop-types';

// Portfolio component definition
const Portfolio = ({ coins }) => {
  // Check if the portfolio is empty
  const isEmpty = !coins || coins.length === 0;

  return (
    <div className="portfolio-container">
      {/* Display a message if the portfolio is empty */}
      {isEmpty ? (
        <div className="empty-portfolio-message">
          <p>Oops.. no coins here</p>
        </div>
      ) : (
        <div className="coins-list">
          {/* Render the list of coins */}
          {coins.map((coin, index) => (
            <div key={index} className="coin-item">
              <h3>{coin.name}</h3>
              <p>Symbol: {coin.symbol}</p>
              <p>Price: ${coin.price.toFixed(2)}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

// PropTypes for type checking
Portfolio.propTypes = {
  coins: PropTypes.arrayOf(
    PropTypes.shape({
      name: PropTypes.string.isRequired,
      symbol: PropTypes.string.isRequired,
      price: PropTypes.number.isRequired,
    })
  ),
};

// Default props in case no coins are passed
Portfolio.defaultProps = {
  coins: [],
};

// Export the component for use in other parts of the application
export default Portfolio;
```
