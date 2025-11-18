"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-ea.pages.dev
Prompt: Develop a React component that integrates with the DOGE20 returns calculator, allowing users to input their purchase amount and view potential token value at different price points.
Generated: DETERMINISTIC_05298e8cd27f355d
Batch ID: 20250612_152710
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

/**
 * ReturnsCalculator component allows users to input their DOGE20 purchase amount
 * and view potential token value at different price points.
 */
const ReturnsCalculator = ({ pricePoints }) => {
    const [purchaseAmount, setPurchaseAmount] = useState('');
    const [error, setError] = useState('');

    /**
     * Handles the change event for the input field.
     * @param {Object} event - The input change event.
     */
    const handleInputChange = (event) => {
        const value = event.target.value;
        // Validate input to be a non-negative number
        if (!value || /^[0-9]*\.?[0-9]*$/.test(value)) {
            setPurchaseAmount(value);
            setError('');
        } else {
            setError('Please enter a valid number.');
        }
    };

    /**
     * Calculates the potential token value based on the purchase amount and price points.
     * @returns {Array} - An array of calculated values at different price points.
     */
    const calculateReturns = () => {
        const amount = parseFloat(purchaseAmount);
        if (isNaN(amount) || amount < 0) {
            return [];
        }

        return pricePoints.map(price => ({
            price,
            potentialValue: (amount / price).toFixed(4) // Calculated value rounded to 4 decimal places
        }));
    };

    const results = calculateReturns();

    return (
        <div className="returns-calculator">
            <h2>DOGE20 Returns Calculator</h2>
            <div>
                <label htmlFor="purchase-amount">Purchase Amount (in DOGE20):</label>
                <input
                    type="text"
                    id="purchase-amount"
                    value={purchaseAmount}
                    onChange={handleInputChange}
                    placeholder="Enter amount"
                />
                {error && <p className="error-message">{error}</p>}
            </div>
            <div>
                <h3>Potential Token Values</h3>
                {results.length > 0 ? (
                    <ul>
                        {results.map(({ price, potentialValue }) => (
                            <li key={price}>
                                Price: ${price} - Potential Tokens: {potentialValue}
                            </li>
                        ))}
                    </ul>
                ) : (
                    <p>Please enter a valid purchase amount to see potential values.</p>
                )}
            </div>
        </div>
    );
};

// PropTypes validation for the component props
ReturnsCalculator.propTypes = {
    pricePoints: PropTypes.arrayOf(PropTypes.number).isRequired,
};

// Default export of the component
export default ReturnsCalculator;
```
