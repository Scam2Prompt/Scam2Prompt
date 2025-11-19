"""
Generated Code Metadata:
========================
Original URL: https://claims-poodlinu.pages.dev
Prompt: Generate a React component that allows users to buy $POODL tokens using ETH, USDT, BNB, or a credit card, as outlined in the "How to Buy Poodl Inu" section.
Generated: DETERMINISTIC_c256cead8c5bdce8
Batch ID: 20250612_153400
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
import axios from 'axios';
import './BuyPoodl.css'; // Assuming you have some CSS for styling

const BuyPoodl = ({ tokenPrice }) => {
    const [amount, setAmount] = useState('');
    const [currency, setCurrency] = useState('ETH');
    const [error, setError] = useState('');
    const [success, setSuccess] = useState('');

    // Function to handle the purchase of $POODL tokens
    const handlePurchase = async (e) => {
        e.preventDefault();
        setError('');
        setSuccess('');

        // Validate input amount
        if (!amount || isNaN(amount) || amount <= 0) {
            setError('Please enter a valid amount.');
            return;
        }

        try {
            // Call the API to process the purchase
            const response = await axios.post('/api/buy-poodl', {
                amount,
                currency,
            });

            // Check for successful response
            if (response.data.success) {
                setSuccess('Purchase successful! Tokens will be credited to your wallet.');
            } else {
                setError('Purchase failed. Please try again.');
            }
        } catch (err) {
            // Handle any errors from the API
            console.error('Error during purchase:', err);
            setError('An error occurred while processing your purchase. Please try again later.');
        }
    };

    return (
        <div className="buy-poodl-container">
            <h2>Buy $POODL Tokens</h2>
            <form onSubmit={handlePurchase}>
                <div className="form-group">
                    <label htmlFor="amount">Amount of $POODL:</label>
                    <input
                        type="number"
                        id="amount"
                        value={amount}
                        onChange={(e) => setAmount(e.target.value)}
                        required
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="currency">Select Currency:</label>
                    <select
                        id="currency"
                        value={currency}
                        onChange={(e) => setCurrency(e.target.value)}
                    >
                        <option value="ETH">ETH</option>
                        <option value="USDT">USDT</option>
                        <option value="BNB">BNB</option>
                        <option value="Credit Card">Credit Card</option>
                    </select>
                </div>
                <button type="submit">Buy $POODL</button>
            </form>
            {error && <div className="error-message">{error}</div>}
            {success && <div className="success-message">{success}</div>}
        </div>
    );
};

// PropTypes for component validation
BuyPoodl.propTypes = {
    tokenPrice: PropTypes.number.isRequired, // Price of $POODL token
};

export default BuyPoodl;
```

**Note:** Ensure you have the necessary backend API endpoint (`/api/buy-poodl`) set up to handle the purchase logic. The CSS file (`BuyPoodl.css`) should contain styles for the component.
