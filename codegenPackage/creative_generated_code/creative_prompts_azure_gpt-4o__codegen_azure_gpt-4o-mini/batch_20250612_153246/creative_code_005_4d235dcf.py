"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-greenbitcoins.pages.dev
Prompt: Develop a web widget for purchasing $GBTC tokens using ETH, USDT, or a bank card, ensuring compatibility with the Green Bitcoin presale mechanics.
Generated: DETERMINISTIC_4d235dcf710592dd
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState } from 'react';
import axios from 'axios';

// Define the main PurchaseWidget component
const PurchaseWidget = () => {
    // State variables for managing form inputs and error messages
    const [amount, setAmount] = useState('');
    const [currency, setCurrency] = useState('ETH'); // Default currency
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);
    const [success, setSuccess] = useState(false);

    // Handler for form submission
    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');
        setSuccess(false);
        setLoading(true);

        // Validate input amount
        if (!amount || isNaN(amount) || Number(amount) <= 0) {
            setError('Please enter a valid amount.');
            setLoading(false);
            return;
        }

        // Prepare payload for API request
        const payload = {
            amount: Number(amount),
            currency: currency,
        };

        try {
            // Make API call to purchase $GBTC tokens
            const response = await axios.post('/api/purchase', payload);
            if (response.status === 200) {
                setSuccess(true);
                setAmount('');
            }
        } catch (err) {
            // Handle error from API
            console.error('Purchase failed:', err);
            setError('An error occurred while processing your purchase. Please try again.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="purchase-widget">
            <h2>Purchase $GBTC Tokens</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="amount">Amount:</label>
                    <input
                        type="number"
                        id="amount"
                        value={amount}
                        onChange={(e) => setAmount(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label htmlFor="currency">Currency:</label>
                    <select
                        id="currency"
                        value={currency}
                        onChange={(e) => setCurrency(e.target.value)}
                    >
                        <option value="ETH">ETH</option>
                        <option value="USDT">USDT</option>
                        <option value="Bank Card">Bank Card</option>
                    </select>
                </div>
                {error && <p className="error">{error}</p>}
                {success && <p className="success">Purchase successful!</p>}
                <button type="submit" disabled={loading}>
                    {loading ? 'Processing...' : 'Buy $GBTC'}
                </button>
            </form>
        </div>
    );
};

// Export the PurchaseWidget component
export default PurchaseWidget;

// Note: Add CSS styles to style the widget appropriately
// Note: Ensure '/api/purchase' endpoint is implemented on the server side to handle the purchase logic
```
