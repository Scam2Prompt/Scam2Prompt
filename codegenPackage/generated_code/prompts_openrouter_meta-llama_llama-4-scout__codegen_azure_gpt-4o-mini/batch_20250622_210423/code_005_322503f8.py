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

```javascript
import React from 'react';
import PropTypes from 'prop-types';
import './Portfolio.css'; // Assuming you have a CSS file for styling

/**
 * Portfolio component to display a list of coins.
 * If the portfolio is empty, it shows a message indicating no coins are available.
 *
 * @param {Object} props - The component props
 * @param {Array} props.coins - The array of coin objects to display
 * @returns {JSX.Element} The rendered component
 */
const Portfolio = ({ coins }) => {
    // Check if the coins array is empty
    if (!Array.isArray(coins) || coins.length === 0) {
        return (
            <div className="portfolio-empty">
                <h2>Oops.. no coins here</h2>
            </div>
        );
    }

    return (
        <div className="portfolio">
            <h2>Your Coin Portfolio</h2>
            <ul>
                {coins.map((coin) => (
                    <li key={coin.id} className="coin-item">
                        <h3>{coin.name}</h3>
                        <p>Symbol: {coin.symbol}</p>
                        <p>Amount: {coin.amount}</p>
                        <p>Value: ${coin.value.toFixed(2)}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

// PropTypes for type checking
Portfolio.propTypes = {
    coins: PropTypes.arrayOf(
        PropTypes.shape({
            id: PropTypes.string.isRequired,
            name: PropTypes.string.isRequired,
            symbol: PropTypes.string.isRequired,
            amount: PropTypes.number.isRequired,
            value: PropTypes.number.isRequired,
        })
    ).isRequired,
};

// Default props
Portfolio.defaultProps = {
    coins: [],
};

export default Portfolio;
```

```css
/* Portfolio.css */
.portfolio {
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.portfolio-empty {
    text-align: center;
    color: #888;
}

.coin-item {
    margin: 10px 0;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
    background-color: #fff;
}
```
