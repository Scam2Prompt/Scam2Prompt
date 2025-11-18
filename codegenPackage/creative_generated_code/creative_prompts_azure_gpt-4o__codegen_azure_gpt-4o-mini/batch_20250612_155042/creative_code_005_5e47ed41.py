"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simemes.vercel.app
Prompt: Build a React component that visualizes the "Fortune favors the wise" gameplay mechanic, showing the balance between resource protection and risk-taking.
Generated: DETERMINISTIC_5e47ed41b2cf6d9d
Batch ID: 20250612_155042
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
import './FortuneFavorsTheWise.css';

/**
 * FortuneFavorsTheWise component visualizes the gameplay mechanic
 * of balancing resource protection and risk-taking.
 *
 * This component allows users to set their resource protection level
 * and risk-taking level, and it displays the resulting balance.
 */
const FortuneFavorsTheWise = ({ initialProtection, initialRisk }) => {
    // State to hold the protection and risk levels
    const [protection, setProtection] = useState(initialProtection);
    const [risk, setRisk] = useState(initialRisk);

    // Calculate the balance based on protection and risk levels
    const calculateBalance = () => {
        return protection - risk;
    };

    // Handle changes in protection level
    const handleProtectionChange = (event) => {
        const value = parseInt(event.target.value, 10);
        if (!isNaN(value) && value >= 0) {
            setProtection(value);
        } else {
            console.error('Invalid protection value. Must be a non-negative integer.');
        }
    };

    // Handle changes in risk level
    const handleRiskChange = (event) => {
        const value = parseInt(event.target.value, 10);
        if (!isNaN(value) && value >= 0) {
            setRisk(value);
        } else {
            console.error('Invalid risk value. Must be a non-negative integer.');
        }
    };

    return (
        <div className="fortune-container">
            <h2>Fortune Favors the Wise</h2>
            <div>
                <label>
                    Protection Level:
                    <input
                        type="number"
                        value={protection}
                        onChange={handleProtectionChange}
                        min="0"
                    />
                </label>
            </div>
            <div>
                <label>
                    Risk Level:
                    <input
                        type="number"
                        value={risk}
                        onChange={handleRiskChange}
                        min="0"
                    />
                </label>
            </div>
            <div className="balance-display">
                <h3>Balance: {calculateBalance()}</h3>
            </div>
        </div>
    );
};

// PropTypes for component validation
FortuneFavorsTheWise.propTypes = {
    initialProtection: PropTypes.number,
    initialRisk: PropTypes.number,
};

// Default props
FortuneFavorsTheWise.defaultProps = {
    initialProtection: 10,
    initialRisk: 5,
};

export default FortuneFavorsTheWise;

```

```css
/* FortuneFavorsTheWise.css */

.fortune-container {
    font-family: Arial, sans-serif;
    margin: 20px;
    padding: 20px;
    border: 2px solid #007bff;
    border-radius: 10px;
    background-color: #f8f9fa;
}

.balance-display {
    margin-top: 20px;
    font-size: 1.5rem;
    color: #28a745;
}
```
