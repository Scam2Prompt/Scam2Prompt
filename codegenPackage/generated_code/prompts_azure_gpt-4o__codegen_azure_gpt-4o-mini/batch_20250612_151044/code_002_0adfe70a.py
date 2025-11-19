"""
Generated Code Metadata:
========================
Original URL: https://exchange24h.com
Prompt: Generate code in JavaScript to create a responsive user interface for slot deposit transactions, incorporating features like "promo khusus" and "modal kecil" as described on the site.
Generated: DETERMINISTIC_0adfe70af8688527
Batch ID: 20250612_151044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SlotDepositUI.js

// Import necessary libraries
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import './SlotDepositUI.css'; // Importing CSS for styling

// SlotDepositUI Component
const SlotDepositUI = ({ onDeposit }) => {
    // State variables for managing input and modal visibility
    const [amount, setAmount] = useState('');
    const [promoCode, setPromoCode] = useState('');
    const [showModal, setShowModal] = useState(false);
    const [error, setError] = useState('');

    // Handle amount change
    const handleAmountChange = (e) => {
        setAmount(e.target.value);
    };

    // Handle promo code change
    const handlePromoCodeChange = (e) => {
        setPromoCode(e.target.value);
    };

    // Handle deposit submission
    const handleDeposit = (e) => {
        e.preventDefault();
        // Basic validation
        if (!amount || isNaN(amount) || amount <= 0) {
            setError('Please enter a valid deposit amount.');
            return;
        }
        if (promoCode && promoCode.length < 5) {
            setError('Promo code must be at least 5 characters long.');
            return;
        }
        setError('');
        // Call the onDeposit function passed as a prop
        onDeposit({ amount, promoCode });
        // Reset fields after submission
        setAmount('');
        setPromoCode('');
        setShowModal(false);
    };

    // Toggle modal visibility
    const toggleModal = () => {
        setShowModal(!showModal);
    };

    return (
        <div className="slot-deposit-ui">
            <button className="btn-open-modal" onClick={toggleModal}>
                Open Deposit Modal
            </button>

            {showModal && (
                <div className="modal">
                    <div className="modal-content">
                        <span className="close" onClick={toggleModal}>&times;</span>
                        <h2>Deposit Slot</h2>
                        <form onSubmit={handleDeposit}>
                            <div>
                                <label htmlFor="amount">Deposit Amount:</label>
                                <input
                                    type="number"
                                    id="amount"
                                    value={amount}
                                    onChange={handleAmountChange}
                                    required
                                />
                            </div>
                            <div>
                                <label htmlFor="promoCode">Promo Khusus:</label>
                                <input
                                    type="text"
                                    id="promoCode"
                                    value={promoCode}
                                    onChange={handlePromoCodeChange}
                                />
                            </div>
                            {error && <p className="error">{error}</p>}
                            <button type="submit" className="btn-submit">Submit</button>
                        </form>
                    </div>
                </div>
            )}
        </div>
    );
};

// PropTypes for type checking
SlotDepositUI.propTypes = {
    onDeposit: PropTypes.func.isRequired,
};

export default SlotDepositUI;
```

```css
/* SlotDepositUI.css */

/* Basic styling for the slot deposit UI */
.slot-deposit-ui {
    text-align: center;
    margin: 20px;
}

.btn-open-modal {
    padding: 10px 20px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

.modal {
    display: flex;
    justify-content: center;
    align-items: center;
    position: fixed;
    z-index: 1;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgba(0, 0, 0, 0.5);
}

.modal-content {
    background-color: #fefefe;
    margin: 15% auto;
    padding: 20px;
    border: 1px solid #888;
    width: 300px;
    border-radius: 10px;
}

.close {
    color: #aaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
}

.close:hover,
.close:focus {
    color: black;
    text-decoration: none;
    cursor: pointer;
}

.error {
    color: red;
    font-size: 14px;
}

.btn-submit {
    padding: 10px 20px;
    background-color: #008CBA;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}
```
