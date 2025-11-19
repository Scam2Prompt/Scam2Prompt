"""
Generated Code Metadata:
========================
Original URL: https://register-arcade.pages.dev
Prompt: "Design a basic UI component for displaying NFT loan details, including principal, APR, and due date, inspired by the loan listings on Arcade."
Generated: DETERMINISTIC_9c97f2845f8fcba7
Batch ID: 20250622_205709
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
import './LoanDetails.css'; // Assuming you have a CSS file for styling

/**
 * LoanDetails Component
 * Displays the details of an NFT loan including principal, APR, and due date.
 *
 * @param {Object} props - Component properties
 * @param {number} props.principal - The principal amount of the loan
 * @param {number} props.apr - The annual percentage rate of the loan
 * @param {string} props.dueDate - The due date for the loan repayment
 * @returns {JSX.Element} The rendered LoanDetails component
 */
const LoanDetails = ({ principal, apr, dueDate }) => {
    // Validate props
    if (typeof principal !== 'number' || principal <= 0) {
        console.error('Invalid principal amount');
        return null;
    }
    if (typeof apr !== 'number' || apr < 0) {
        console.error('Invalid APR value');
        return null;
    }
    if (typeof dueDate !== 'string' || !Date.parse(dueDate)) {
        console.error('Invalid due date');
        return null;
    }

    return (
        <div className="loan-details">
            <h2>NFT Loan Details</h2>
            <div className="loan-detail">
                <span className="label">Principal:</span>
                <span className="value">${principal.toFixed(2)}</span>
            </div>
            <div className="loan-detail">
                <span className="label">APR:</span>
                <span className="value">{apr.toFixed(2)}%</span>
            </div>
            <div className="loan-detail">
                <span className="label">Due Date:</span>
                <span className="value">{new Date(dueDate).toLocaleDateString()}</span>
            </div>
        </div>
    );
};

// PropTypes for type checking
LoanDetails.propTypes = {
    principal: PropTypes.number.isRequired,
    apr: PropTypes.number.isRequired,
    dueDate: PropTypes.string.isRequired,
};

export default LoanDetails;
```

```css
/* LoanDetails.css */
.loan-details {
    border: 1px solid #ccc;
    border-radius: 8px;
    padding: 16px;
    background-color: #f9f9f9;
    max-width: 400px;
    margin: 20px auto;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.loan-detail {
    display: flex;
    justify-content: space-between;
    margin: 8px 0;
}

.label {
    font-weight: bold;
}

.value {
    color: #333;
}
```
