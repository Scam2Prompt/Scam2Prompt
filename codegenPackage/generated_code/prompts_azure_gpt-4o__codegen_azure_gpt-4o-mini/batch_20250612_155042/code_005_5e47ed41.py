"""
Generated Code Metadata:
========================
Original URL: https://simemes.vercel.app
Prompt: Build a React component that visualizes the "Fortune favors the wise" gameplay mechanic, showing the balance between resource protection and risk-taking.
Generated: DETERMINISTIC_5e47ed41b2cf6d9d
Batch ID: 20250612_155042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import './FortuneFavorsTheWise.css'; // Importing CSS for styling

/**
 * FortuneFavorsTheWise component visualizes the balance between resource protection and risk-taking.
 * It allows users to adjust their resource protection and risk levels, displaying the resulting balance.
 */
const FortuneFavorsTheWise = ({ initialProtection, initialRisk }) => {
    // State variables for resource protection and risk levels
    const [protection, setProtection] = useState(initialProtection);
    const [risk, setRisk] = useState(initialRisk);

    // Function to handle protection level change
    const handleProtectionChange = (event) => {
        const value = parseInt(event.target.value, 10);
        if (!isNaN(value) && value >= 0) {
            setProtection(value);
        } else {
            console.error('Invalid protection value');
        }
    };

    // Function to handle risk level change
    const handleRiskChange = (event) => {
        const value = parseInt(event.target.value, 10);
        if (!isNaN(value) && value >= 0) {
            setRisk(value);
        } else {
            console.error('Invalid risk value');
        }
    };

    // Calculate the balance based on protection and risk levels
    const calculateBalance = () => {
        return protection - risk;
    };

    return (
        <div className="fortune-favors-the-wise">
            <h1>Fortune Favors the Wise</h1>
            <div className="controls">
                <label>
                    Resource Protection:
                    <input
                        type="number"
                        value={protection}
                        onChange={handleProtectionChange}
                        min="0"
                    />
                </label>
                <label>
                    Risk Taking:
                    <input
                        type="number"
                        value={risk}
                        onChange={handleRiskChange}
                        min="0"
                    />
                </label>
            </div>
            <div className="balance">
                <h2>Balance: {calculateBalance()}</h2>
                <p>{calculateBalance() >= 0 ? 'You are in a safe zone!' : 'You are at risk!'}</p>
            </div>
        </div>
    );
};

// PropTypes for type checking
FortuneFavorsTheWise.propTypes = {
    initialProtection: PropTypes.number.isRequired,
    initialRisk: PropTypes.number.isRequired,
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
.fortune-favors-the-wise {
    font-family: Arial, sans-serif;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    max-width: 400px;
    margin: auto;
    text-align: center;
}

.controls {
    margin-bottom: 20px;
}

label {
    display: block;
    margin: 10px 0;
}

input {
    width: 100%;
    padding: 8px;
    margin-top: 5px;
}

.balance {
    font-weight: bold;
}
```
