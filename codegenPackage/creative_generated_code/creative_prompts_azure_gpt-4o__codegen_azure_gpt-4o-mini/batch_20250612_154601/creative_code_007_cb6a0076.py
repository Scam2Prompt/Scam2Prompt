"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okx-web3-usdt-trc20-payfor-00000017.pages.dev
Prompt: Create a user interface component in React for entering USDT amounts, including a keypad and balance display, inspired by the OKX payment page.
Generated: DETERMINISTIC_cb6a0076afa86a9d
Batch ID: 20250612_154601
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
import './USDTInput.css'; // Importing CSS for styling

const USDTInput = ({ balance }) => {
    const [amount, setAmount] = useState(''); // State to hold the entered amount

    // Updates the input amount when a number is pressed
    const handleKeyPress = (value) => {
        if (!isNaN(value)) {
            setAmount((prev) => prev + value);
        }
    };

    // Clears the input amount
    const handleClear = () => {
        setAmount('');
    };

    // Removes the last character from the input amount
    const handleBackspace = () => {
        setAmount((prev) => prev.slice(0, -1));
    };

    // Renders the keypad buttons
    const renderKeypad = () => {
        const keypadButtons = [...Array(10).keys()].map((num) => (
            <button key={num} onClick={() => handleKeyPress(num.toString())}>
                {num}
            </button>
        ));
        
        return (
            <div className="keypad">
                {keypadButtons}
                <button onClick={handleBackspace}>⌫</button>
                <button onClick={handleClear}>C</button>
            </div>
        );
    };

    return (
        <div className="usdt-input">
            <h2>Enter USDT Amount</h2>
            <div className="balance-display">
                <p>Balance: {balance} USDT</p>
            </div>
            <input 
                type="text" 
                value={amount} 
                readOnly 
                className="amount-input" 
                placeholder="0.00" 
            />
            {renderKeypad()}
        </div>
    );
};

// PropTypes for type checking
USDTInput.propTypes = {
    balance: PropTypes.number.isRequired,
};

export default USDTInput;

```

```css
/* USDTInput.css */

.usdt-input {
    width: 300px;
    margin: 0 auto;
    text-align: center;
}

.balance-display {
    margin-bottom: 15px;
    font-size: 1.2em;
    color: #333;
}

.amount-input {
    width: 100%;
    padding: 10px;
    font-size: 1.5em;
    border: 1px solid #ccc;
    border-radius: 5px;
    margin-bottom: 15px;
}

.keypad {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
}

.keypad button {
    padding: 15px;
    font-size: 1.5em;
    border: none;
    border-radius: 5px;
    background-color: #007bff;
    color: white;
    cursor: pointer;
}

.keypad button:hover {
    background-color: #0056b3;
}
```
